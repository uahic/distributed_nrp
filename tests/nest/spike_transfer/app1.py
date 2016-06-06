#!/usr/bin/env python

import nest
import numpy as np
import faulthandler
from music_wizard.nest._Setup import music_setup
from music_wizard.common.Factory import create_connections_from_xml
from music_wizard.nest.Factories import NestPortFactory, NestConnectorFactory
faulthandler.enable()

def callback(t, msg):
    print (t, msg)


xml = music_setup.config('xml')

def connector_callback(port, pop_name, rule, selector):
    print "Request", port, pop_name, rule, selector
    raise

port_factory = NestPortFactory(music_setup)  # def __init__(self, music_setup, acc_latency=10.0, max_buffered=1, use_parrots=True):
connector_factory = NestConnectorFactory(connector_callback, port_factory) # def __init__(self, connector_callback, port_factory):

with open(xml, 'r') as xml_text:
    connections = create_connections_from_xml(xml_text.read(), "app1",
                                              connector_factory, port_factory)

connected = False
import math
i = 0.0

while i < 2000.0:
    nest.Simulate(20)

        #spike_recorder.connect(runtime.time(), 'pop1')
        #poi_rpc.apply(runtime.time(), 'connect', 'pop1')
    i += 0.01

