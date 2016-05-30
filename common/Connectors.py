from music_wizard.common.Interfaces import AbstractConnector

class RPCInConnector(AbstractConnector):

    def __init__(self, data_ports, rpc_port, *args, **kwargs):
        self.rpc_port = rpc_port
        self.ports = data_ports
        self.rpc_port.register_callback('connect', self.connect)
        self.connector_fcn = None

    def connect(self, pop_name, connection_rule='all_to_all', selector=None):
        for port in self.ports:
            self.connector_fcn(port, target, connection_rule, selector)

    def set_connector_fcn(self, connector_fcn):
        self.connector_fcn = connector_fcn

class RPCOutConnector(AbstractConnector):

    def __init__(self, rpc_port, *args, **kwargs):
        self.rpc_port = rpc_port
        self.connector_fcn = None

    def connect(self, time_stamp, target, connection_rule='all_to_all', selector=None):
        self.rpc_port.apply(time_stamp, 'connect', target, connection_rule=connection_rule, selector=selector)

    def set_connector_fcn(self, connector_fcn):
        pass



