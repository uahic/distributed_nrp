#!/usr/bin/env python

import nest
import numpy as np
import faulthandler
from music_wizard.nest._Setup import music_setup
from music_wizard.nest.Factories import create_connections_from_xml
from music_wizard.nest.Factory import static_connector
import brainfile
faulthandler.enable()

def callback(t, msg):
    print (t, msg)

xml = music_setup.config('xml')

def connect_to_pynn_population(port, pop_name):
    pop_view = brainfile.__population_views[pop_name]
    gids = map(int, pop_view.all_cells)
    port.connect(gids)

static_connector.set_connector_fcn(connect_to_pynn_population)

with open(xml, 'r') as xml_text:
    connections = create_connections_from_xml(xml_text.read(), "app2")

connected = False
import math
i = 0.0

while i < 2000.0:
    nest.Simulate(20)
        #spike_recorder.connect(runtime.time(), 'pop1')
        #poi_rpc.apply(runtime.time(), 'connect', 'pop1')
    i += 0.01

