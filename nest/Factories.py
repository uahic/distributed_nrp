from music_wizard.nest.Ports
from music_wizard.common.Interfaces import AbstractDevice, DeviceMeta
from music_wizard.nest._Setup import music_setup
from music_wizard.nest._Setup import default_parameters as music_defaults 
from music_wizard.nest._Setup import accLatency 
from music_wizard.nest.Ports import EventInputPort, EventOutputPort, ContOutputPort
from music_wizard.pymusic.Ports import RPCInPort, RPCOutPort, MsgInputPort, MsgOutputPort
import music_wizard.common.Factory as CommonFactory 
import collections
import numpy as np


#def create_observer(device, port_name, port_type, property_name, maxBuffered=1):
#    if port_type == "Cont":
#        buf = np.array([0.0], dtype=np.float)
#        port = ContOutputPort(music_setup, port_name, buf, maxBuffered)
#        def callback():
#            buf[0] = getattr(device, property_name)
#        observer = CallbackObserver(callback)
#    elif port_type == "Msg":
#        raise NotImplementedError("TODO ... ")
#    else:
#        raise Exception("Invalid Observer type for device with port name '{}'".format(port_name))
#    return observer
#
#def create_observer_from_xml(device, port_prefix, xml_observer_obj):
#    port_type = xml_observer_obj.type
#    property_name = xml_observer_obj.property_
#    port_name = "{}_{}".format(port_prefix, property_name)
#    return create_observer(device, port_name, port_type, property_name)
#
#def create_setter(port_name, port_type, property_setter, accLatency=global_acc_latency, maxBuffered=1):
#
#    if port_type == "Cont":
#        buf = np.array([0.0], dtype=np.float)
#        port = ContInputPort(music_setup, port_name, buf, accLatency, maxBuffered=maxBuffered)
#        setter = PropertySetter(property_setter, buf)
#    elif port_type == "Msg":
#        raise NotImplementedError("TODO ... ")
#    else:
#        raise Exception("Invalid Observer type for device with port name '{}'".format(port_name))
#    return setter 
#
#def create_setter_from_xml(device, port_prefix, xml_setter_obj):
#    port_type = xml_setter_obj.type
#    property_name = xml_setter_obj.property_
#    device_property = getattr(device, property_name)
#    property_setter = device_property
#    port_name = "{}_{}".format(port_prefix, property_name)
#    return create_setter(port_name, port_type, property_setter, accLatency=global_acc_latency)

output_port_map = {'Event': EventOutputPort, 'Continuous': ContOutputPort, 'Message': MsgOutputPort, 'RPC': RPCOutPort}
input_port_map = {'Event': EventInputPort, 'Continuous': None, 'Message': MsgInputPort, 'RPC': RPCInPort}


def create_port(port_name, port_type_name, width, is_output_device):
    if is_output_device:
        if port_type_name == 'Event':
            return EventOutputPort(port_name, width)
            return port_cls 
    
    

def create_connector(xml_connector, port_name, is_output_device):
    pass

def create_device(port_name, width, device_type_name, device_kwargs, xml_connector, is_output_device):
    connector = create_connector(xml_connector, port_name, is_output_device)
    device_cls = Device[device_type_name]
    ports = create_ports(port_name, device_cls.port_spec, width, is_output_device)

    device = device_cls(connector, ports, **device_kwargs)


def nest_device_factory(xml_device, application_name):
    port_name = xml_device.portname 
    assert port_name is not None
    # Validation of type_name is done by pyXB
    device_type_name = xml_device.type
    connector_type_name = xml_device.connector
    device = None

    if xml_device.from.name == application_name:

        device_kwargs = CommonFactory.extract_device_kwargs(xml_device.from.parameters)
        device = create_device(port_name, xml_device.width, device_type_name, device_kwargs, xml_device.connector, True)
    else:
        for to_section_entity in list(xml_device.to):
            if to_section_entity.name == application_name:
                device_kwargs = CommonFactory.extract_device_kwargs(to_section_entity.parameters)
                device = create_device(port_name, xml_device.width, device_type_name, device_kwargs, xml_device.connector, False)
                break
    return device

def create_devices_from_xml(xml_text):
    device_dict = CommonFactory.create_devices_from_xml(xml_text, device_factory=nest_device_factory)
    return device_dict.values()


