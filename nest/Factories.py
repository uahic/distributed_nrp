from .Observers import CallbackObserver
from .Setters import PropertySetter 
from music_nest.common.Ports import ContOutputPort, ContInputPort
from music_nest.common.Interfaces import Device, DeviceMeta
from .music_setup import setup as music_setup
from .music_setup import default_parameters as music_defaults 
from .music_setup import accLatency as global_acc_latency
import music_nest.common.Factory as CommonFactory 
import collections
import numpy as np


def create_observer(device, port_name, port_type, property_name, maxBuffered=1):
    if port_type == "Cont":
        buf = np.array([0.0], dtype=np.float)
        port = ContOutputPort(music_setup, port_name, buf, maxBuffered)
        def callback():
            buf[0] = getattr(device, property_name)
        observer = CallbackObserver(callback)
    elif port_type == "Msg":
        raise NotImplementedError("TODO ... ")
    else:
        raise Exception("Invalid Observer type for device with port name '{}'".format(port_name))
    return observer

def create_observer_from_xml(device, port_prefix, xml_observer_obj):
    port_type = xml_observer_obj.type
    property_name = xml_observer_obj.property_
    port_name = "{}_{}".format(port_prefix, property_name)
    return create_observer(device, port_name, port_type, property_name)

def create_setter(port_name, port_type, property_setter, accLatency=global_acc_latency, maxBuffered=1):

    if port_type == "Cont":
        buf = np.array([0.0], dtype=np.float)
        port = ContInputPort(music_setup, port_name, buf, accLatency, maxBuffered=maxBuffered)
        setter = PropertySetter(property_setter, buf)
    elif port_type == "Msg":
        raise NotImplementedError("TODO ... ")
    else:
        raise Exception("Invalid Observer type for device with port name '{}'".format(port_name))
    return setter 

def create_setter_from_xml(device, port_prefix, xml_setter_obj):
    port_type = xml_setter_obj.type
    property_name = xml_setter_obj.property_
    device_property = getattr(device, property_name)
    property_setter = device_property
    port_name = "{}_{}".format(port_prefix, property_name)
    return create_setter(port_name, port_type, property_setter, accLatency=global_acc_latency)


def create_device(xml_autogen_device_obj):
    port_name = xml_autogen_device_obj.portname 
    assert port_name is not None
    # Validation of type_name is done by pyXB
    type_name = xml_autogen_device_obj.type
    xml_observers = xml_autogen_device_obj.observer
    xml_setters = xml_autogen_device_obj.setter
    xml_parameter_list = xml_autogen_device_obj.parameters
    device_kwargs = CommonFactory.extract_device_kwargs(xml_parameter_list)

    device_cls = Device[type_name]
    device = device_cls(port_name, **device_kwargs)

    if xml_observers:
        try:
            xml_observers = iter(xml_observers)
        except TypeError:
            xml_observers = [xml_observers]
        for xml_observer in xml_observers:
            create_observer_from_xml(device, port_name, xml_observer)

    if xml_setters:
        try:
            xml_setters = iter(xml_setters)
        except TypeError:
            xml_setters = [xml_setters]
        for xml_setter in xml_setters:
            create_setter_from_xml(device, port_name, xml_setter)

    return device

def create_devices_from_xml(xml_text):
    device_dict = CommonFactory.create_devices_from_xml(xml_text, device_factory=create_device)
    return device_dict.values()


