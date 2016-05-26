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
static_connector = StaticConnector()


def create_rpc_port(port_name, is_output_device):
    if is_output_device:
        rpc_port = RPCOutPort(music_setup, port_name, maxBuffered=1)
    else:
        rpc_port = RPCInPort(music_setup, port_name, accLatency, maxBuffered=1)

    return rpc_port

def create_port(port_name, port_type_name, width, is_output_device, **params):

    if is_output_device:
        port_cls = output_port_map[port_type_name]
    else:
        port_cls = input_port_map[port_type_name]

    if port_type_name == 'Event':
        port = port_cls(port_name, width)
    else:
        port = port_cls(port_name, **params)
    return port

def create_connector(connector_type_name, port, port_name, target, \
                     is_output_device):
    if connector_type_name == 'RPC':
        if is_output_device:
            rpc_port = create_rpc_port(port_name, is_output_device)
            connector = RPCOutConnector(rpc_port)
            connector.set_connector_fcn(static_connector.connect)
        else:
            rpc_port = create_rpc_port(port_name, is_output_device)
            connector = RPCInConnector(port, rpc_port)
            connector.set_connector_fcn(static_connector.connect)
    else:
        connector = StaticConnector()
        connector.set_connector_fcn(static_connector.connect)
        if target:
            connector.connect(port, target)
    return connector


def create_connections_from_xml(xml_text, application_name, connector_fcn):
    static_connector.set_connector_fcn(connector_fcn)
    connection_dict = Factory.create_connections_from_xml(xml_text, application_name,\
                                                  create_connector, \
                                                  create_port)
    return connection_dict.values()

