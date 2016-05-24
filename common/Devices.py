from music_wizard.common.Interfaces import AbstractDevice
from music_wizard.pymusic.Mixins import RPCConnectMixin, RPCUpdateMixin

class SimpleDevice(AbstractDevice):

    def __init__(self, rpc_connector_cls, port, target, *args, **kwargs):
        super(SimpleDevice, self).__init__(*args, **kwargs)
        self.port = port  
        self.connector = rpc_connector_cls(self.port, target)

class SpikeRecorder(SimpleDevice):

    def __init__(self, rpc_connector_cls, event_port, target, *args, **kwargs):
        super(SpikeRecorder, self).__init__(rpc_connector_cls, port, target, *args, **kwargs)

class PopulationRate(SimpleDevice):

    def __init__(self, rpc_connector_cls, current_port, target, *args, **kwargs):
        super(PopulationRate, self).__init__(rpc_connector_cls, current_port, target, *args, **kwargs)


class SpikeSource(SimpleDevice):

    def __init__(self, rpc_connector_cls, event_port, target, *args, **kwargs):
        super(SpikeSource, self).__init__(rpc_connector_cls, event_port, target, *args, **kwargs)

class ACSource(SpikeSource):

    def __init__(self, rpc_connector_cls, event_port, target, *args, **kwargs):
        super(ACSource, self).__init__(rpc_connector_cls, event_port, target, *args, **kwargs)

class DCSource(SpikeSource):

    def __init__(self, rpc_connector_cls, event_port, target, *args, **kwargs):
        super(DCSource, self).__init__(rpc_connector_cls, event_port, target, *args, **kwargs)

class NCSource(SpikeSource):

    def __init__(self, rpc_connector_cls, event_port, target, *args, **kwargs):
        super(NCSource, self).__init__(rpc_connector_cls, event_port, target, *args, **kwargs)

class Poisson(SpikeSource):

    def __init__(self, rpc_connector_cls, event_port, target, *args, **kwargs):
        super(Poisson, self).__init__(rpc_connector_cls, event_port, target, *args, **kwargs)



        
