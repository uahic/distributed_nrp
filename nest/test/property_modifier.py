import sys
import os
import numpy as np 
import unittest
import mock
from music_nest.common.Interfaces import Device
from music_nest.simulator_backend.Observers import Observer, CallbackObserver
from music_nest.simulator_backend.Setters import Setter, PropertySetter
from music_nest.simulator_backend.Setters import instances as setter_instances
from music_nest.simulator_backend.Observers import instances as observer_instances 
from stubs import DeviceStub


class ObserverTest(unittest.TestCase):

    def setUp(self):
        self.callback_called = False

    def tearDown(self):
        observer_instances = []

    def test_callback_observer(self):
        def callback():
            self.callback_called = True
        callback_observer = CallbackObserver(callback)
        Observer.notify()
        self.assertEqual(self.callback_called, True)

class SetterTest(unittest.TestCase):

    def setUp(self):
        self.callback_called = False

    def tearDown(self):
        setter_instances = []

    def test_property_setter(self):
        def callback():
            print "YO"
            self.callback_called = True
        property_setter = PropertySetter(callback)
        Setter.notify()
        self.assertEqual(self.callback_called, True)

def get_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ObserverTest))
    suite.addTest(unittest.makeSuite(SetterTest))
    return suite 

if __name__ == '__main__':
    unittest.main()


