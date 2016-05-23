import sys
import os
import numpy as np 
import unittest
import mock
from music_nest.common.Interfaces import Device, DeviceMeta 
from music_nest.simulator_backend.TypeRegistry import __devices

class DummyDevice(Device):

    def __init__(self, port_name):
        self.port_name = port_name

class InterfaceTests(unittest.TestCase):

    def test_register(self):
        self.assertIn('DummyDevice', DeviceMeta._device_classes)

def get_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(DummyDevice))
    return suite

if __name__ == '__main__':
    unittest.main()
