import pyNN.nest as sim
import music
from music_nest.simulator_backend.__populations import population_register
from music_nest.simulator_backend.music_setup import setup as music_setup
from music_nest.simulator_backend.music_setup import default_parameters as music_defaults
from operator import itemgetter
from music_nest.common.Ports import ContOutputPort, ContInputPort
from music_nest.simulator_backend.Ports import RPCPort
from music_nest.simulator_backend.Mixins import RPCMixin, RemoteConnectableMixin, RemoteUpdatableMixin
from music_nest.common.DeviceInterfaces import ICurrentSource, ICurrentSink
from music_nest.simulator_backend.Factories import create_setter
import nest
import numpy as np
import abc
import sys

class ContinuousRecorder(ICurrentSink):

    def __init__(self, port_name, target_population=None, recordables=["V_m"], interval=0.1, *args, **params):
        super(ContinuousRecorder, self).__init__(*args, **kwargs)
        self._recorder = None
        self.port_name = port_name
        self.target_population = target_population
        self.recordables = recordables
        self.interval = interval

    def _create_device(self):
        self._recorder = nest.Create('music_cont_out_proxy')
        self.connect(self.target_population)

    def connect_via_ids(self, id_list):
        nest.SetStatus(self._recorder, {'port_name': self.port_name, 'record_from': self.recordables, 'interval': self.interval, 'target_gids': id_list})

    def connect(self, population_label, selector=None):
        target_pop = population_register[population_label]
        if selector:
            target_pop = sim.PopulationView(target_pop, selector)
        global_ids = map(int, target_pop.all_cells)
        self.connect_via_ids(global_ids)

