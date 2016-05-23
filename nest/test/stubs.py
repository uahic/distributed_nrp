import sys
import os
from music_nest.common.Interfaces import Device

class DeviceStub(object):

    def __init__(self, port_prefix):
        self.port_prefix = port_prefix
        self._rate = None
        self._offset = None

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value

    @property
    def offset(self):
        return self._offset

    @offset.setter
    def rate(self, value):
        self._offset = value

    def _init_model(self):
        pass
