#!/usr/bin/env python

import nest
import numpy as np
import faulthandler
from music_wizard.nest._Setup import music_setup
from music_wizard.common.Factory import create_connections_from_xml
from music_wizard.nest.Factories import NestPortFactory, NestConnectorFactory

xml = music_setup.config('xml')

spike_detector = nest.Create('spike_detector')

def connector_callback(port, pop_name, rule, selector):
    if selector:
        print "Ignoring selector ", selector
    port.connect(spike_detector, 'all_to_all')

port_factory = NestPortFactory(music_setup)  # def __init__(self, music_setup, acc_latency=10.0, max_buffered=1, use_parrots=True):
connector_factory = NestConnectorFactory(connector_callback, port_factory) # def __init__(self, connector_callback, port_factory):

with open(xml, 'r') as xml_text:
    connections = create_connections_from_xml(xml_text.read(), "app1",
                                              connector_factory, port_factory)

connected = False
import math
i = 0.0

for i in xrange(10):
    nest.Simulate(20)
    print nest.GetStatus(spike_detector, 'events')

