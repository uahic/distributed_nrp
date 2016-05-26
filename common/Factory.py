from music_wizard.common.xml_config import music_xml
from collections import OrderedDict
from collections import namedtuple
from music_wizard.common.Interfaces import AbstractConnection

class Connection(AbstractConnection):
    def __init__(self, port, connector):
        self.port = port
        self.connector = connector

def extract_kwargs(xml_parameter_list):
    if not xml_parameter_list:
        return {}
    kwargs = {} 
    for elem in xml_parameter_list.orderedContent():
        kwargs[elem.value.name] = elem.value.content()
    return kwargs

def make_connection(xml_connection, application_name, connector_factory, port_factory):
    port_name = xml_connection.portname 
    # Validation of type_name is done by pyXB
    port_type = xml_connection.type
    width = xml_connection.width
    connector_type = xml_connection.connector
    sender = xml_connection.sender
    receiver_list = xml_connection.receiver

    if sender.name == application_name:
        kwargs = extract_kwargs(sender.parameters)
        port = port_factory(port_name, port_type, width, True)
        connector = connector_factory(connector_type, port, port_name, sender.target, True)
        return Connection(port, connector)
    else:
        for receiver in list(receiver):
            if receiver.name == application_name:
                kwargs = extract_kwargs(receiver.parameters)
                port = port_factory(port_name, port_type, width, False)
                connector = connector_factory(connector_type, port, port_name, receiver.target, False)
                return Connection(port, connector)
    return None 

def create_connections_from_xml(xml_text, application_name, connector_factory, port_factory):
    root = music_xml.CreateFromDocument(xml_text)
    xml_connections = root.Connection
    connections = OrderedDict()
    for xml_connection in xml_connections:
        connection = make_connection(xml_connection, application_name, connector_factory, port_factory)
        if connection:
            connections[xml_connection.portname] = connection 

    return connections 

    port = create_port(port_name, port_type_name, width, is_output_device)
    connector = create_connector(xml_connector, port, port_name, is_output_device)
    connection = Connection(port, connector)
