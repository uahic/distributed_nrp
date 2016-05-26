from music_wizard.common.Interfaces import AbstractConnector

class RPCInConnector(AbstractConnector):

    def __init__(self, static_connector, data_ports, rpc_port, *args, **kwargs):
        self.rpc_port = rpc_port
        self.ports = data_ports
        self.rpc_port.register_callback('connect', self.connect)
        self.static_connector = static_connector

    def connect(self, pop_name):
        for port in self.ports:
            self.static_connector(port, target)
        
class RPCOutConnector(AbstractConnector):

    def __init__(self, rpc_port, *args, **kwargs):
        self.rpc_port = rpc_port

    def connect(self, time_stamp, target):
        self.rpc_port.apply(time_stamp, 'connect', target)



