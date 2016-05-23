import sys
import os
import numpy as np 
import unittest
import mock
from music_nest.simulator_backend.Factories import create_devices_from_xml
from music_nest.common.Interfaces import Device 
from music_nest.simulator_backend.Setters import instances as setter_instances
from music_nest.simulator_backend.Observers import instances as observer_instances 
from stubs import DeviceStub


class FactoryTests(unittest.TestCase):

    def tearDown(self):
        setter_instances = []
        observer_instances = []

    @mock.patch.dict('music_nest.simulator_backend.Factories.DeviceMeta._device_classes', values={'ACSource': DeviceStub})
    def test_multi_devices(self):
        with open("xmlfiles/source_stub.xml", 'r') as f:
            xml_file = f.read()
        devices = create_devices_from_xml(xml_file) 
        print "devices:" ,devices
        self.assertEqual(devices[0].port_prefix, 'Port1')
        self.assertEqual(devices[1].port_prefix, 'Port2')

    @mock.patch('music_nest.simulator_backend.Factories.ContInputPort', autospec=True)
    @mock.patch.dict('music_nest.simulator_backend.Factories.DeviceMeta._device_classes', values={'ACSource': DeviceStub})
    @mock.patch('music_nest.simulator_backend.Factories.music_setup', autospec=True)
    def test_cont_setter(self, mock_music_setup, mock_ContInputPort):
        with open("xmlfiles/setter.xml", 'r') as f:
            xml_file = f.read()
        devices = create_devices_from_xml(xml_file) 
        self.assertEqual(devices[0].port_prefix, 'Port1')
        mock_ContInputPort.assert_has_calls([mock.call(mock_music_setup, 'Port1_rate', [0.0], 0.0, -1)])
        
    @mock.patch('music_nest.simulator_backend.Factories.ContInputPort', autospec=True)
    @mock.patch.dict('music_nest.simulator_backend.Factories.DeviceMeta._device_classes', values={'ACSource': DeviceStub})
    @mock.patch('music_nest.simulator_backend.Factories.music_setup', autospec=True)
    def test_multi_cont_setter(self, mock_music_setup, mock_ContInputPort):
        with open("xmlfiles/multi_setter.xml", 'r') as f:
            xml_file = f.read()
        devices = create_devices_from_xml(xml_file) 
        self.assertEqual(devices[0].port_prefix, 'Port1')
        mock_ContInputPort.assert_has_calls([mock.call(mock_music_setup, 'Port1_rate', [0.0], 0.0, -1)])
        mock_ContInputPort.assert_has_calls([mock.call(mock_music_setup, 'Port1_offset', [0.0], 0.0, -1)])


    @mock.patch('music_nest.simulator_backend.Factories.ContOutputPort', autospec=True)
    @mock.patch.dict('music_nest.simulator_backend.Factories.DeviceMeta._device_classes', values={'ACSource': DeviceStub})
    @mock.patch('music_nest.simulator_backend.Factories.music_setup', autospec=True)
    def test_cont_getter(self, mock_music_setup, mock_ContOutputPort):
        with open("xmlfiles/getter.xml", 'r') as f:
            xml_file = f.read()
        devices = create_devices_from_xml(xml_file) 
        self.assertEqual(devices[0].port_prefix, 'Port1')
        port_prefix, buffer = mock_ContOutputPort.call_args[0]
        mock_ContOutputPort.assert_has_calls([mock.call(mock_music_setup, 'Port1_rate', [0.0], -1)])

    @mock.patch('music_nest.simulator_backend.Factories.ContOutputPort', autospec=True)
    @mock.patch.dict('music_nest.simulator_backend.Factories.DeviceMeta._device_classes', values={'ACSource': DeviceStub})
    @mock.patch('music_nest.simulator_backend.Factories.music_setup', autospec=True)
    def test_cont_getter(self, mock_music_setup, mock_ContOutputPort):
        with open("xmlfiles/multi_getter.xml", 'r') as f:
            xml_file = f.read()
        devices = create_devices_from_xml(xml_file) 
        self.assertEqual(devices[0].port_prefix, 'Port1')
        mock_ContOutputPort.assert_has_calls([mock.call(mock_music_setup, 'Port1_rate', [0.0], -1)])
        mock_ContOutputPort.assert_has_calls([mock.call(mock_music_setup, 'Port1_offset', [0.0], -1)])

def get_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(FactoryTests))
    return suite

if __name__ == '__main__':
    unittest.main()
