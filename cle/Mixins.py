from music_nest.common.Interfaces import Connectable, Updateable
from music_nest.cle.__music_setup import music_setup
from music_nest.cle.__music_setup import accLatency as global_acc_latency 
from music_nest.common.Ports import RPCOutPort

class RPCMixin(object):

    def __init__(self, port_name, *args, **params):
        super(RPCMixin, self).__init__(*args, **params)
        self._rpc_port = RPCOutPort(music_setup, "{}_rpc".format(port_name), 1)

class RemoteConnectableMixin(RPCMixin, Connectable):

    def __init__(self, port_name, *args, **params):
        super(RemoteConnectableMixin, self).__init__(port_name, *args, **params)

    def connect(self, time_stamp, pop_name):
        self._rpc_port.apply(time_stamp, 'connect', pop_name)

    def connect_via_ids(self, time_stamp, gid_list):
        self._rpc_port.apply(time_stamp, 'connect_via_ids', gid_list)


class RemoteUpdatableMixin(RPCMixin, Updateable):

    def __init__(self, port_name, *args, **params):
        super(RemoteUpdatableMixin, self).__init__(port_name, *args, **params)

    def update(self, time_stamp, **params):
        self._rpc_port.apply(time_stamp, 'update', **params)
