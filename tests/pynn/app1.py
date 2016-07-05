#!/usr/bin/env python

import faulthandler
from music_wizard.pynn import XmlFactory, Factory
import music
import pyNN.nest as sim

sim.setup()
music_setup = music.Setup()
xml = music_setup.config('xml')

detector = sim.Population(1, sim.native_cell_type('spike_detector'), {})
population_dict={'detector': detector}
model_factory = Factory.PyNNProxyFactory(sim, music_setup, acc_latency=10.0)
connector_factory = Factory.PyNNConnectorFactory(sim)
proxy_factory = XmlFactory.ProxyFactory("app1", connector_factory, model_factory, population_dict)

with open(xml, 'r') as xml_stream:
    proxys = proxy_factory.create_proxys(xml_stream.read())

for i in xrange(20):
    sim.run(20.0)
    print nest.GetStatus(detector, 'events')

