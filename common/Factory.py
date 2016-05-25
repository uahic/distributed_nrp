from music_nest.common.xml_config import music_xml
from collections import OrderedDict
from collections import namedtuple



def create_devices_from_xml(xml_text, application_name, device_factory):
    root = music_xml.CreateFromDocument(xml_text)
    xml_devices = root.Device 
    devices = OrderedDict()
    for xml_device in xml_devices:
        device = device_factory(xml_device, application_name)
        if device:
            devices[xml_device.portname] = device

    return devices

def extract_device_kwargs(xml_parameter_list):
    if not xml_parameter_list:
        return {}
    kwargs = {} 
    for elem in xml_parameter_list.orderedContent():
        kwargs[elem.value.name] = elem.value.content()
    return kwargs
