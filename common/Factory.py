import abc
from collections import OrderedDict
from collections import namedtuple
from music_wizard.common.xml_config import music_xml
from music_wizard.common.Interfaces import AbstractConnection

class Connection(AbstractConnection):
    def __init__(self, port, connector):
        self.port = port
        self.connector = connector

class BasePortFactory(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, in_port_map, out_port_map):
        self.in_port_map = in_port_map
        self.out_port_map = out_port_map 

    @abc.abstractmethod
    def create_port(self, port_name, port_type, width, is_output):
        pass

class BaseConnectorFactory(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create_connector(self, connector_type, port, port_name, synapses, \
                     is_output):
        pass


def extract_kwargs(xml_parameter_list):
    if not xml_parameter_list:
        return {}
    kwargs = {}
    for elem in xml_parameter_list.orderedContent():
        kwargs[elem.value.name] = elem.value.content()
    return kwargs

def create_selector(selector_type, values):
    if selector_type == 'slice':
        return slice(values.start, values.stop, values.step)
    elif selector_type == 'indice':
        return [x for x in values]
    else:
        raise Exception('Unknown selector type {}'.format(selector_type))

def create_connection(xml_connection, connector_factory, port_factory, peer, is_output):
    port_name = xml_connection.portname
    port_type = xml_connection.type
    width = xml_connection.width
    connector_type = xml_connection.connector
    kwargs = extract_kwargs(peer.parameters)

    port = port_factory.create_port(port_name, port_type, width, is_output)
    synapses = getattr(peer, 'synapse', None)
    connectors = []
    if synapses:
        for synapse in synapses:
            selector = getattr(synapse, 'selector', None)
            if selector:
                selector = create_selector(selector.name, selector.value)
            connector = connector_factory.create_connector(connector_type, port, port_name, synapse, selector, is_output)
            connectors.append(connector)
    return Connection(port, connectors)


def assemble_connection(xml_connection, application_name, connector_factory, port_factory):
    sender = xml_connection.sender
    receiver_list = xml_connection.receiver

    if sender.name == application_name:
        return create_connection(xml_connection, connector_factory, port_factory, sender, True)
    else:
        for receiver in list(receiver_list):
            if receiver.name == application_name:
                return create_connection(xml_connection, connector_factory, port_factory, receiver, False)
    return None

def create_connections_from_xml(xml_text, application_name, connector_factory, port_factory):
    root = music_xml.CreateFromDocument(xml_text)
    xml_connections = root.Connection
    connections = OrderedDict()
    for xml_connection in xml_connections:
        connection = assemble_connection(xml_connection, application_name, connector_factory, port_factory)
        if connection:
            connections[xml_connection.portname] = connection

    return connections

