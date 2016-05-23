from music_nest.common.DeviceInterfaces import ICurrentSink, ICurrentSource, ISpikeSink, ISpikeSource
from music_nest.common.Ports import RPCOutPort, ContOutputPort, ContInputPort, EventInputPort, EventOutputPort
from music_nest.common.Messages import encode_message, decode_message
from music_nest.cle.Mixins import RemoteUpdatableMixin, RemoteConnectableMixin
from music_nest.cle.__music_setup import accLatency, music_setup, default_parameters
import numpy as np

class PopulationRate(ICurrentSource):

    def __init__(self, port_name, *args, **kwargs):
        super(PopulationRate, self).__init__(port_name, *args, **kwargs)
        self._port_name = port_name
        self.rate = np.array([0.0], dtype=np.double)
        self._cont_rate_port = ContInputPort(music_setup, port_name, self.rate, accLatency, maxBuffered=1)

class SpikeRecorder(ISpikeSink):

    def __init__(self, port_name, *args, **kwargs):
        super(SpikeRecorder, self).__init__(port_name, *args, **kwargs)
        self._port_name = port_name
        self._event_in_port = EventInputPort(music_setup, port_name, self._callback, accLatency, **kwargs)
        self.callback = lambda d, i, t: self._callback(d,i,t)

    def _callback(self,d, i, t):
        self.callback(d,i,t)
        


