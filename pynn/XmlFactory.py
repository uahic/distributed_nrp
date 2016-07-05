
import abc
from collections import OrderedDict
from collections import namedtuple
from music_wizard.common.xml_config import music_xml
from music_wizard.common.Interfaces import AbstractConnection


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



class ProxyFactory(object):

    def __init__(self, application_name, connector_factory, proxy_factory, population_dict):
        self.application_name = application_name
        self.connector_factory = connector_factory
        self.proxy_factory = proxy_factory
        self.population_dict = population_dict

    def _create_selector(self, selector_type, values):
        if selector_type == 'slice':
            return slice(values.start, values.stop, values.step)
        elif selector_type == 'indice':
            return [x for x in values]
        else:
            raise Exception('Unknown selector type {}'.format(selector_type))

    def _create_and_connect_proxy(self, xml_connection, peer, is_output):
        port_name = xml_connection.portname
        port_type = xml_connection.type
        width = int(xml_connection.width)
        #connector_type = xml_connection.connector
        kwargs = extract_kwargs(peer.parameters)

        proxy = self.proxy_factory.create_proxy(port_name, port_type, width, is_output)
        xml_synapses = getattr(peer, 'synapse', None)
        if xml_synapses:
            for xml_synapse in xml_synapses:
                xml_selector = getattr(xml_synapse, 'selector', None)
                if xml_selector:
                    selector = self._create_selector(xml_selector.name, xml_selector.value)
                else:
                    selector = None
                target_name = getattr(xml_synapse, 'target')
                try:
                    target_pop = self.population_dict[target_name]
                except:
                    raise Exception("Population with name (key) {} was not found.".format(target_name))
                self.connector_factory.create_and_connect_synapse(proxy, port_name, xml_synapse, selector, target_pop, is_output)
        return proxy

    def _assemble_proxy(self, xml_connection):
        sender = xml_connection.sender
        receiver_list = xml_connection.receiver

        if sender.name == self.application_name:
            return self._create_and_connect_proxy(xml_connection, sender, True)
        else:
            for receiver in list(receiver_list):
                if receiver.name == self.application_name:
                    return self._create_and_connect_proxy(xml_connection, receiver, False)

    def create_proxys(self, xml_text):
        root = music_xml.CreateFromDocument(xml_text)
        xml_connections = root.Connection
        proxy_dict = OrderedDict()
        for xml_connection in xml_connections:
            proxy = self._assemble_proxy(xml_connection)
            proxy_dict[xml_connection.portname] = proxy
        return proxy_dict


