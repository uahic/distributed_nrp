import sys
import nest
from music_wizard.common.Interfaces import Port

if sys.version_info.major > 2:
    from past.builtins import xrange

class ContOutputPort(Port):

    def __init__(self, port_name, record_from=["V_m"], interval=0.1, **kwargs):
        self.port = nest.Create('music_cont_out_proxy')
        nest.SetStatus(self.port, {'port_name':port_name,
                                   'record_from': record_from,
                                   'interval': interval})
        self.port_name = port_name
        self.record_from = record_from
        self.interval = interval

    def connect(self, global_ids):
        if nest.GetStatus(self.port, 'published'):
            raise Exception("The NEST implementation of continuous output \
                            port does not support connect() after the \
                            simulation has been started!")

        nest.SetStatus(self.port, {'target_gids': global_ids})

class ContInputPort(Port):

    def __init__(self, port_name, accLatency=0.01, **kwargs):
        self.port = nest.Create('music_cont_in_proxy')
        self.port_name = port_name
        nest.SetStatus(self.port, {'port_name':self.port_name})
        nest.SetAcceptableLatency(port_name, accLatency)

    def connect(self, global_ids):
        pass


class EventOutputPort(Port):

    def __init__(self, port_name, width, use_parrots=True, **kwargs):
        self.width = width
        self.parrots = None
        self.port = nest.Create('music_event_out_proxy')
        nest.SetStatus(self.port, 'port_name', port_name)
        self.port_name = port_name

        if use_parrots:
            self.parrots = nest.Create('parrot_neuron', width)
            for i in xrange(self.width):
                nest.Connect([self.parrots[i]], self.port, 'one_to_one',
                             {'music_channel': i})

    def connect(self, global_ids):
        if not args:
            args = ['one_to_one']
        if self.parrots:
            nest.Connect(global_ids, self.parrots, *args, **params)
        else:
            for i in global_ids:
                nest.Connect([i], self.port, 'one_to_one',
                             {'music_channel': i})


class EventInputPort(Port):

    def __init__(self, port_name, width, use_parrots=True, accLatency=0.01, **kwargs):
        self.width = width
        self.ports = nest.Create('music_event_in_proxy', width)
        self.port_name = port_name
        self.parrots = None
        nest.SetStatus(self.ports,
                {'port_name': "{}".format(self.port_name)})
        nest.SetAcceptableLatency(port_name, accLatency)

        for i in xrange(self.width):
            nest.SetStatus([self.ports[i]], {'music_channel': i})
        if use_parrots:
            self.parrots = nest.Create('parrot_neuron', width)
            nest.Connect(self.ports, self.parrots, 'one_to_one')

    def connect(self, global_ids, *args, **params):
        if not args:
            args = ['one_to_one']
            if len(global_ids) != self.width:
                raise Exception('The number of target GIDs must either match\
                                the width of the EventInputPort or pass the \
                                connection rule "all_to_all" as argument.')
        if self.parrots:
            nest.Connect(self.parrots, global_ids, *args, **params)
        else:
            nest.Connect(self.ports, global_ids, *args, **params)

