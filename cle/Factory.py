from music_nest.common.DeviceInterfaces import Device
import music_nest.common.Factory as CommonFactory 
import DeviceProxy
import functools
import numpy as np

def create_setter_from_xml(music_setup, device, port_name, xml_elem):
    port_type = xml_elem.type
    property_name = xml_elem.property_
    annotated_port_name = "{}_{}".format(port_name, property_name)
    if port_type == "Cont":
        buf = np.array([0.0], dtype=np.float)
        port = ContOutputPort(music_setup, annotated_port_name, buf, -1)
        setattr(device, property_name, buf)
    else:
        raise Exception("Invalid setter type for device with port name '{}'".format(port_name))


def create_observer_from_xml(music_setup, device, port_name, xml_elem):
    port_type = xml_elem.type
    property_name = xml_elem.property_
    annotated_port_name = "{}_{}".format(port_name, property_name)
    if port_type == "Cont":
        buf = np.array([0.0], dtype=np.float)
        port = ContInputPort(music_setup, annotated_port_name, buf, 0.0, -1)
        setattr(device, property_name, buf)
    else:
        raise Exception("Invalid observer type for device with port name '{}'".format(port_name))

def create_device_proxy(music_setup, xml_element):
    port_name = xml_element.portname 
    assert port_name is not None
    # Validation of type_name is done by pyXB
    type_name = xml_element.type
    xml_observers = xml_element.observer
    xml_setters = xml_element.setter
    device_cls = Device[type_name]
    device = device_cls(port_name)

    if xml_observers:
        try:
            xml_observers = iter(xml_observers)
        except TypeError:
            xml_observers = [xml_observers]
        for xml_observer in xml_observers:
            create_observer_from_xml(music_setup, device, port_name, xml_observer)

    if xml_setters:
        try:
            xml_setters = iter(xml_setters)
        except TypeError:
            xml_setters = [xml_setters]
        for xml_setter in xml_setters:
            create_setter_from_xml(music_setup, device, port_name, xml_setter)

    return device

def create_devices_from_xml(xml_text, music_setup):
    device_factory = functools.partial(create_device_proxy, music_setup)
    device_dict = CommonFactory.create_devices_from_xml(xml_text, device_factory=device_factory)
    return device_dict
