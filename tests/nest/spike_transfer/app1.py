#!/usr/bin/env python

import nest
import numpy as np
import faulthandler
from music_wizard.nest._Setup import music_setup
from music_wizard.nest.Factories import create_connections_from_xml
faulthandler.enable()

def callback(t, msg):
    print (t, msg)


xml = music_setup.config('xml')

def connect_to_pynn_population(port, pop_name):
    pass

with open(xml, 'r') as xml_text:
    connections = create_connections_from_xml(xml_text.read(), "app1",
                                              connect_to_pynn_population)

connected = False
import math
i = 0.0

while i < 2000.0:
    nest.Simulate(20)

    if i > 0.02:
        connections.connector
        #spike_recorder.connect(runtime.time(), 'pop1')
        #poi_rpc.apply(runtime.time(), 'connect', 'pop1')
    i += 0.01

