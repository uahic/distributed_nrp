import sys
import nest
from music_wizard.common.Interfaces import Port

if sys.version_info.major > 2:
    from past.builtins import xrange

class ContOutputPort(Port):

    def __init__(self, port_name, record_from=["V_m"], interval=0.1):
        self.port = nest.Create('music_cont_out_proxy')    
        self.port_name = port_name
        self.record_from = record_from
        self.interval = interval

    def connect(self, global_ids):
        nest.SetStatus(self.port, { 'port_name': self.port_name, 'record_from': self.record_from,
                    'interval': self.interval,
                    'target_gids': global_ids })

class ContInputPort(Port):

    def __init__(self, port_name, **params):
        self.port = nest.Create('music_cont_in_proxy')
        self.port_name = port_name
        nest.SetStatus(self.port, {'port_name':self.port_name})

    def connect(self, global_ids):
        raise Exception("The music_cont_in_proxy model can not be connected to other neurons. 
                The value must be read out via the dictionary.")


class EventOutputPort(Port):
    
    def __init__(self, port_name, width):
        self.port = nest.Create('music_event_out_proxy')
        self.port_name = port_name

    def connect(self, global_ids):
        nest.SetStatus(self.port,
                {'port_name': "{}".format(self.port_name)})

        for i, g_id in enumerate(global_ids):
            nest.Connect([g_id], list(self.port), 'one_to_one', {'music_channel': i})

class EventInputPort(Port):

    def __init__(self, port_name, width):
        self.width = width
        self.ports = nest.Create('music_event_in_proxy', width)
        self.parrots = nest.Create('parrot_neuron', width)
        self.port_name = port_name
        nest.SetStatus(self.ports, 
                {'port_name': "{}".format(self.port_name)})
        for i in xrange(self.width):
            nest.SetStatus(parrots[i], {'music_channel': i})
        nest.Connect(self.ports, self.parrots, 'one_to_one')

    def connect(self, global_ids, *args, **params):
        if not args:
            args = ['one_to_one']
        nest.Connect(self.parrots, global_ids, *args, **params)

            

