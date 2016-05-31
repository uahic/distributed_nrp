import collections
import numpy as np
from music_wizard.nest._Setup import music_setup
from music_wizard.nest._Setup import accLatency
from music_wizard.nest.Connectors import StaticConnector
from music_wizard.nest.Ports import EventInputPort, EventOutputPort, ContOutputPort, ContInputPort
from music_wizard.pymusic.Ports import RPCInPort, RPCOutPort, MsgInputPort, MsgOutputPort
from music_wizard.common.Connectors import RPCInConnector, RPCOutConnector
from music_wizard.common import Factory


output_port_map = {'Event': EventOutputPort, 'Continuous': ContOutputPort }
input_port_map = {'Event': EventInputPort, 'Continuous': ContInputPort}
port_connector_blacklist = {'RPC': [ContInputPort, ContOutputPort]}
default_connector_fcn = None


class NestPortFactory(Factory.BasePortFactory):

    def __init__(self, music_setup, acc_latency=10.0, max_buffered=1, use_parrots=True):
        super(NestPortFactory, self).__init__(input_port_map, output_port_map)
        self.acc_latency = acc_latency
        self.max_buffered = max_buffered
        self.use_parrots = use_parrots

    def create_rpc_port(self, port_name, is_output):
        if is_output:
            rpc_port = RPCOutPort(self.music_setup, port_name, self.max_buffered=1)
        else:
            rpc_port = RPCInPort(self.music_setup, port_name, self.acc_latency, self.max_buffered=1)
        return rpc_port

    def create_port(self, port_name, port_type, width, is_output):
        if port_type == 'RPC':
            port = self.create_rpc_port(port_name, is_output)

        if is_output:
            port_cls = self.out_port_map[port_type]
        else:
            port_cls = self.in_port_map[port_type]

        if port_type == 'Event':
            port = port_cls(port_name, width, accLatency=self.acc_latency, maxBuffered=self.max_buffered, **params)
        else:
            port = port_cls(port_name, accLatency=self.acc_latency, maxBuffered=self.max_buffered, **params)
        return port

def check_connector_port_validity(connector_type_name, port):
    class Dummy(object):
        pass
    bool_list = map(lambda cls: isinstance(port, cls), port_connector_blacklist.get(connector_type_name, [Dummy]))
    if any(bool_list):
        raise Exception('Connector type {} is not supported for the Port type\
                        {} in NEST'.format(connector_type_name, type(port)))


class NestConnectorFactory(Factory.BaseConnectorFactory):

    def __init__(self, connector_callback, port_factory):
        self.connector_callback = connector_callback
        self.port_factory = port_factory

    def create_connector(self, connector_type, port, port_name, synapses, \
                     is_output):

        #check_connector_port_validity(connector_type_name, port)
        if connector_type == 'RPC':
            rpc_port = self.port_factory.create_port(port_name, 'RPC', None, is_output)
            if is_output:
                connector = RPCOutConnector(port, rpc_port)
            else:
                connector = RPCInConnector(port, rpc_port)
            connector.set_connector_fcn(self.connector_callback)
        elif connector_type =='Static':
            connector = StaticConnector(self.connector_callback)
            selector = Factory.create_selector()
            if synapses:
                for synapse in synapses:
                    selector = getattr(synapse, 'selector', None)
                    if selector:
                        selector = Factory.create_selector(selector.name, selector.value)
                    if hasattr(synapse, 'target'):
                        connector.connect(port, synapse.target, synapse.rule, selector)
        else:
            raise Exception('Unknown connector type {}'.format(connector_type))

        return connector

