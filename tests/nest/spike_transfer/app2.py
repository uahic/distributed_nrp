#!/usr/bin/env python

import nest
import numpy as np
import faulthandler
from music_wizard.nest._Setup import music_setup
from music_wizard.common.Factory import create_connections_from_xml
from music_wizard.nest.Factories import NestPortFactory, NestConnectorFactory
import pyNN.nest as sim
faulthandler.enable()

def callback(t, msg):
    print (t, msg)

xml = music_setup.config('xml')

# Sim.setup must be called before any pyNN and NEST calls!
sim.setup()
proxy_synapse_mdl = nest.CopyModel("static_synapse", "proxy_synapse", {'weight': 1.0, "delay": 0.1})
detector = nest.Create('spike_detector')

# Load and execute brain file
import brainfile

def connector_callback(port, pop_name, rule, selector):
    if not pop_name:
	return
    pop_view = brainfile.__population_views[pop_name]
    if selector:
        pop_view = sim.PopulationView(pop_view, selector)
    gids = map(int, pop_view.all_cells)
    port.connect(gids, rule)
    for gid in gids:
        nest.Connect([int(gid)], detector, 'one_to_one', syn_spec="proxy_synapse")

port_factory = NestPortFactory(music_setup)  # def __init__(self, music_setup, acc_latency=10.0, max_buffered=1, use_parrots=True):
connector_factory = NestConnectorFactory(connector_callback, port_factory) # def __init__(self, connector_callback, port_factory):

with open(xml, 'r') as xml_text:
    connections = create_connections_from_xml(xml_text.read(), "app2",
                                              connector_factory, port_factory)

i = 0.0
while i < 200.0:
    sim.run(20.0)
    print "App2 detector ", nest.GetStatus(detector, 'events')
        #spike_recorder.connect(runtime.time(), 'pop1')
        #poi_rpc.apply(runtime.time(), 'connect', 'pop1')
    i += 0.01
sim.end()

