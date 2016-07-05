#!/usr/bin/env python

import faulthandler
from music_wizard.pynn import XmlFactory, Factory
import music
import pyNN.nest as sim

sim.setup()
music_setup = music.Setup()
xml = music_setup.config('xml')

model_factory = Factory.PyNNProxyFactory(sim, music_setup, acc_latency=10.0)
connector_factory = Factory.PyNNConnectorFactory(sim)

##########
# Load and execute brain file
import brainfile
##########

population_dict = brainfile.__population_views
proxy_factory = XmlFactory.ProxyFactory("app2", connector_factory, model_factory, population_dict)

with open(xml, 'r') as xml_stream:
    proxys = proxy_factory.create_proxys(xml_stream.read())

for i in xrange(20):
    sim.run(20.0)
