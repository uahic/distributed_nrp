import pyNN.nest as sim
import music
from music_nest.simulator_backend.devices.AbstractDevice import AbstractBrainDevice
from music_nest.simulator_backend.__populations import population_register
from music_nest.simulator_backend.music_setup import setup as music_setup
from music_nest.simulator_backend.music_setup import accLatency
from music_nest.simulator_backend.music_setup import default_parameters as music_defaults
from operator import itemgetter
from music_nest.common.Ports import ContOutputPort, ContInputPort, EventInputPort, EventOutputPort
from music_nest.simulator_backend.Ports import create_nest_cont_out_port, RPCPort
from music_nest.simulator_backend.Observers import CallbackObserver
from music_nest.simulator_backend.Mixins import RPCMixin, RemoteConnectableMixin, RemoteUpdatableMixin
from music_nest.common.DeviceInterfaces import ISpikeSource, ISpikeSink, ICurrentSink
from music_nest.simulator_backend.Factories import create_setter
from collections import OrderedDict
from scipy.integrate import simps
import numpy as np
import abc
import sys
import nest

class SpikeRecorder(AbstractBrainDevice, ISpikeSink):

    def __init__(self, port_name, target_population_label=None, *args, **params):
        assert target_population_label is not None
        super(SpikeRecorder, self).__init__(*args, **params)
        self._recorder = None
        self.port_name = port_name
        self.target_population_label = target_population_label[0]

    def _create_device(self):
        self._recorder = nest.Create('music_event_out_proxy') 
        nest.SetStatus(self._recorder, {'port_name': self.port_name})
        self.connect(self.target_population_label)

    def connect_via_ids(self, id_list):
        assert self._recorder is not None
        index_map_size = len(nest.GetStatus(self._recorder))
        for i, neuron_id in enumerate(id_list):
            nest.Connect([neuron_id], self._recorder, 'one_to_one', {'music_channel': i + index_map_size})

    def connect(self, population_label, selector=None):
        assert self._recorder is not None
        target_pop = population_register[population_label]
        if selector:
            target_pop = sim.PopulationView(target_pop, selector)
        self.connect_via_ids(map(int, target_pop.all_cells))

class SpikeInput(AbstractBrainDevice, ISpikeSource):

    def __init__(self, port_name, music_channel = 0, *args, **kwargs):
        super(SpikeDetector, self).__init__(*args, **kwargs)
        self._detector = None
        self.port_name = port_name
        self.music_channel =  music_channel
    
    def _create_device(self):
        self._detector = nest.Create('music_event_in_proxy')
        nest.SetStatus(self._detector, {'port_name': self.port_name})
        nest.SetStatus(self._detector, {'music_channel': self.music_channel})
        
    def connect_via_ids(self, id_list):
        assert self._detector is not None
        nest.Connect(self._detector, id_list)

    def connect(self, population_label, selector=None):
        assert self._recorder is not None
        target_pop = population_register[population_label]
        if selector:
            target_pop = sim.PopulationView(target_pop, selector)
        self.connect_via_ids(map(int, target_pop.all_cells))


class PopulationRate(RemoteConnectableMixin, RemoteUpdatableMixin, AbstractBrainDevice, ICurrentSink):

    default_parameters = {
        'tau_fall': 20.0,
        'tau_rise': 10.0
    }

    fixed_parameters = {
        'v_thresh': float('inf'),
        'cm': 1.0,
        'v_rest': 0.0
    }

    def __init__(self, port_name, *args, **params):
        super(PopulationRate, self).__init__(port_name, *args, **params)

        self._cell = None
        #port_name = "{}_{}".format(self._port_name, self._target_property)
        #self._rate_observer = CallbackObserver(lambda: self.__generator.set('rate', self._rate_buffer[0]))
        self._cell = None
        self._weight = None
        self._rate = None
        self._port_name = port_name

        self._rate_cont_out_port = None

    def update(self, **params):
        super(PopulationRate, self)._update_parameters(params)
        self._parameters["tau_rise"], self._parameters["tau_fall"] = \
            sorted(self.get_parameters("tau_rise", "tau_fall").values())
        #print nest.GetStatus(map(int, self._cell.all_cells))
        #if self._target:
        #    print nest.GetStatus([map(int, self._target.local_cells)[0]])

    def _create_device(self):
        """
        Creates a LIF neuron with decaying-exponential post-synaptic currents
        and current-based synapses.
        """

        # IF_curr_exp
        self._cell = sim.Population(1, sim.IF_curr_exp(**self.get_parameters(("tau_m", "tau_fall"),
                                                        ("tau_syn_E", "tau_rise"),
                                                        "v_thresh",
                                                        "cm",
                                                        "v_rest")))
        self._cell.initialize(v=self._cell[0].v_rest)
        self._calculate_weight()
        self._rate_cont_out_port = create_nest_cont_out_port(self._cell, self._port_name, ["V_m"], 0.1)

    def _calculate_weight(self):
        """
        Calculates the weight of a neuron from the population to the device
        such that the area below the resulting PSP is 1. The exact shape of a
        PSP can be found e.g. in Bytschok, I., Diploma thesis.
        """
        tau_c = (1. / self._cell[0].tau_syn_E - 1. / self._cell[0].tau_m) ** -1
        t_end = -np.log(1e-10) * self._cell[0].tau_m
        x_new = np.arange(0., t_end, 0.1)
        y_new = tau_c / self._cell[0].cm * (np.exp(
            -x_new / self._cell[0].tau_m) - np.exp(
            -x_new / self._cell[0].tau_syn_E))
        self._weight = 1.0 / simps(y_new, dx=sim.state.dt)


    # No connection parameters necessary for this device
    # pylint: disable=W0613
    def _connect(self, neurons):
        """
        Connects the neurons specified by "neurons" to the
        device.

        :param neurons: must be a Population, PopulationView or
            Assembly object
        """
        self._target = neurons
        connector = sim.AllToAllConnector()
        synapse = sim.StaticSynapse(delay=sim.state.dt, weight=self._weight * 1000)
        sim.Projection(neurons, self._cell, connector, synapse_type=synapse, receptor_type='excitatory')

    def connect_via_ids(self, id_list):
        raise Exception("Not implemented yet")

    def connect(self, population_label, selector=None):
        target_pop = population_register[population_label]
        if selector:
            target_pop = sim.PopulationView(target_pop, selector)
        self._connect(target_pop)


class Poisson(SpikeInput):
    def __init__(self, port_name, *args, **params):
        super(Poisson, self).__init__(port_name, *args, **params)

class ACSource(SpikeInput):
    def __init__(self, port_name, *args, **params):
        super(ACSource, self).__init__(port_name, *args, **params)

class DCSource(SpikeInput):
    def __init__(self, port_name, *args, **params):
        super(DCSource, self).__init__(port_name, *args, **params)

class FixedFrequency(SpikeInput):
    def __init__(self, port_name, *args, **params):
        super(FixedFrequency, self).__init__(port_name, *args, **params)

class NCSource(SpikeInput):
    def __init__(self, port_name, *args, **params):
        super(NCSource, self).__init__(port_name, *args, **params)



