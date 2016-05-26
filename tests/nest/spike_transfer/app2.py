#!/usr/bin/env python

import numpy as np
import faulthandler
from music_wizard.nest._Setup import music_setup
from music_wizard.nest.Factories import create_connections_from_xml
faulthandler.enable()

def callback(t, msg):
    print (t, msg)


xml = music_setup.config('xml')

connections = create_connections_from_xml(xml, "app2")

connected = False
import math
i = 0.0

while i < 2000.0:
    nest.Simulate(20)
        #spike_recorder.connect(runtime.time(), 'pop1')
        #poi_rpc.apply(runtime.time(), 'connect', 'pop1')
    i += 0.01

