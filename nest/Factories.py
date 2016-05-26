from music_wizard.nest.Ports
from music_wizard.nest._Setup import music_setup
from music_wizard.nest._Setup import default_parameters as music_defaults 
from music_wizard.nest._Setup import accLatency 
from music_wizard.nest.Connectors import StaticConnector
from music_wizard.nest.Ports import EventInputPort, EventOutputPort, ContOutputPort
from music_wizard.pymusic.Ports import RPCInPort, RPCOutPort, MsgInputPort, MsgOutputPort
from music_wizard.common.Connectors import RPCInConnector, RPCOutConnector
import music_wizard.common.Factory as CommonFactory 
import collections
import numpy as np


output_port_map = {'Event': EventOutputPort, 'Continuous': ContOutputPort }
input_port_map = {'Event': EventInputPort, 'Continuous': None}
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

def create_connector(connector_type_name, port, port_name, target, is_output_device):
    if connector_type_name == 'RPC':
        if is_output_device:
            rpc_port = create_rpc_port(port_name, is_output_device)
            connector = RPCOutConnector(rpc_port)
        else:
            rpc_port = create_rpc_port(port_name, is_output_device)
            connector = RPCInConnector(static_connector, port, rpc_port)
    else:
        connector = StaticConnector()
    return connector


def create_connections_from_xml(xml_text, application_name):
    connection_dict = CommonFactory.create_connections_from_xml(xml_text, application_name, connection_factory)
    return device_dict.values()

