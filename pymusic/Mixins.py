from music_nest.pymusic.Ports import RPCInPort, RPCOutPort

class RPCInPortMixin(object):

    def __init__(self, port_name, music_setup, accLatency, maxBuffered, *args, **kwargs):
        super(RPCInPortMixin, self).__init__(*args, **kwargs)
        self.rpc_port = RPCInPort(music_setup, "{}_rpc".format(port_name), accLatency, maxBuffered=maxBuffered)

class RPCOutPortMixin(object):

    def __init__(self, port_name, music_setup, maxBuffered, *args, **kwargs):
        super(RPCOutPortMixin, self).__init__(*args, **kwargs)
        self.rpc_port = RPCOutPort(music_setup, "{}_rpc".format(port_name), accLatency, maxBuffered)

class RPCConnectMixin(RPCOutPortMixin):

    def __init__(self, port_name, music_setup, accLatency, maxBuffered, *args, **kwargs):
        super(RPCConnectMixin, self).__init__(port_name, music_setup, accLatency, maxBuffered *args, **kwargs)
        self.rpc_port.register_callback('connect', self.connect)

class RPCUpdateMixin(RPCOutPortMixin):

    def __init__(self, port_name, music_setup, accLatency, maxBuffered, *args, **kwargs):
        super(RPCUpdateMixin, self).__init__(port_name, music_setup, accLatency, maxBuffered, *args, **kwargs)
        self.rpc_port.register_callback('update', self.update)
