from music_nest.common.Interfaces import Connectable, Updateable
from music_nest.simulator_backend.Ports import RPCPort
from music_nest.cle.__music_setup import music_setup 
from music_nest.cle.__music_setup import accLatency as global_acc_latency 

class RPCInPortMixin(object):

    def __init__(self, port_name, *args, **kwargs):
        super(RPCMixin, self).__init__(*args, **kwargs)
        self._rpc_port = RPCPort(music_setup, "{}_rpc".format(port_name), global_acc_latency, 1)

class RemoteConnectableMixin(RPCMixin):

    def __init__(self, port_name, *args, **kwargs):
        super(RemoteConnectableMixin, self).__init__(port_name, *args, **kwargs)
        self._rpc_port.register_callback('connect', self.connect)
        self._rpc_port.register_callback('connect_via_ids', self.connect_via_ids)

class RemoteUpdatableMixin(RPCMixin):

    def __init__(self, port_name, *args, **kwargs):
        super(RemoteUpdatableMixin, self).__init__(port_name, *args, **kwargs)
        self._rpc_port.register_callback('update', self.update)
