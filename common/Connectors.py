from music_wizard.common.Interfaces import AbstractConnector

class RPCInConnector(AbstractConnector):

    def __init__(self, data_ports, rpc_port, *args, **kwargs):
        self.rpc_port = rpc_port
        self.ports = data_ports
        self.rpc_port.register_callback('connect', self.connect)
        self.connector_fcn = None

    def connect(self, pop_name):
        for port in self.ports:
            self.connector_fcn(port, target)

    def set_connector_fcn(self, connector_fcn):
        self.connector_fcn = connector_fcn

class RPCOutConnector(AbstractConnector):

    def __init__(self, rpc_port, *args, **kwargs):
        self.rpc_port = rpc_port
        self.connector_fcn = None

    def connect(self, time_stamp, target):
        self.rpc_port.apply(time_stamp, 'connect', target)

    def set_connector_fcn(self, connector_fcn):
        self.connector_fcn = connector_fcn



