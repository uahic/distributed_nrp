#!/usr/bin/env python

import nest
import pyNN.nest as sim
import music
import numpy as np
import random
from itertools import takewhile

print(" IAM CLE DUMMY ")
setup = music.Setup()
buff = np.array([0.0], dtype=np.float)


ac_rate_out = setup.publishContInput("ac1_amplitude")
ac_rate_out.map(buff)
def test_callback(time, msg):
    print time, msg
##msg_port.map(test_callback, accLatency=accLatency, maxBuffered=maxBuffered)
#ac_rpc = setup.publishMessageInput("ac1_rpc")
#ac_rpc.map(test_callback)
msg_port = nest.Create('music_message_in_proxy')
nest.SetStatus(msg_port,
        {'port_name': "ac1_rpc"})


#runtime = setup.runtime(0.01)
#times = takewhile(lambda x: True, runtime)
while True:
    #print buff
    #buff[:] =  np.random.rand(1)*1000.0
    #runtime.tick()
    nest.Simulate(20.0)
    print nest.GetStatus(msg_port)
