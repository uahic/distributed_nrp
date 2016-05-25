from music_wizard.common.Interfaces import AbstractConnector
from music_wizard.pymusic.Ports import RPCInPort, RPCOutPort 
from music_wizard.nest.__populations import population_register

def connect_to_pynn_population(port, pop_name):
    pop_view = population_register[pop_name]
    gids = map(int, pop_view.all_cells)
    port.connect(gids)

class RPCInConnector(AbstractConnector):

    def __init__(self, rpc_port_name, music_setup, accLatency, maxBuffered=1, *args, **kwargs):
        self.rpc_port = RPCInPort(music_setup, rpc_port_name, accLatency, maxBuffered=maxBuffered, *args, **kwargs)
        self.ports = []
        self.rpc_port.register_callback('connect', self.connect)

    def add_ports(self, ports):
        self.ports.extend(ports)

    def connect(self, pop_name):
        for port in self.ports:
            connect_to_pynn_population(port, pop_name)
        
class RPCOutConnector(AbstractConnector):

    def __init__(self, rpc_port_name, music_setup, maxBuffered=1, *args, **kwargs):
        self.rpc_port = RPCOutPort(music_setup, rpc_port_name, maxBuffered, *args, **kwargs)
        self.music_setup = music_setup
        self.ports = []

    def connect(self, time_stamp, pop_name):
        self.rpc_port.apply(self.music_setup, time_stamp, 'connect', pop_name)

