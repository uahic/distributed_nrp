#!/usr/bin/env python

import numpy as np

from music_nest.cle.DeviceProxy import PopulationRate, SpikeRecorder
from music_nest.cle.__music_setup import music_setup as setup

print(" IAM CLE DUMMY ")
import faulthandler
faulthandler.enable()
def callback(t, msg):
    print (t, msg)
error_port = setup.publishMessageInput("error_port")
error_port.map(callback, accLatency=0.01, pickled=False)

sys_rpc_port = setup.publishMessageOutput("nest_rpc")
sys_rpc_port.map(pickled=False)


print PopulationRate.mro()
pop_rate_obj = PopulationRate("pop_rate")
spike_recorder = SpikeRecorder("spike_detector")

msg = "hallo"
print "Before setup", pop_rate_obj
runtime = setup.runtime(0.010)

connected = False
import math
i = 0.0
while i < 2000.0:
    runtime.tick()
    if not connected:
        pop_rate_obj.connect(runtime.time(), 'pop1')
        #spike_recorder.connect(runtime.time(), 'pop1')
        #poi_rpc.apply(runtime.time(), 'connect', 'pop1')
        connected = True
        print "Connected"
    print pop_rate_obj.rate 
    print "loop"

    i += 0.01

