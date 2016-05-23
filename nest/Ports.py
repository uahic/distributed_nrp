import nest
from music_nest.common.Interfaces import Port

class ContOutputPort(object):

    def __init__(self, port_name, record_from, interval):
        self.port = nest.Create('music_cont_out_proxy')    
        self.port_name = port_name
        self.record_from = record_from
        self.interval = interval

    def connect(self, global_ids):
        nest.SetStatus(self.port, { 'port_name': self.port_name, 'record_from': self.record_from,
                    'interval': self.interval,
                    'target_gids': global_ids })

class EventOutputPort(object):
    
    def __init__(self, port_name):
        self.port = nest.Create('music_event_out_proxy')
        self.port_name = port_name

    def connect(self, global_ids):
        nest.SetStatus(self.port,
                {'port_name': "{}".format(self.port_name)})

        for i, g_id in enumerate(global_ids):
            nest.Connect([g_id], list(self.port), 'one_to_one', {'music_channel': i})

