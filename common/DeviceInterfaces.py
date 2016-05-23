from Interfaces import Device, Connectable, Updateable

class ICurrentSource(Device, Connectable):
    def __init__(self, *args, **kwargs):
        super(ICurrentSource, self).__init__()

class ICurrentSink(Device, Connectable):
    def __init__(self, *args, **kwargs):
        super(ICurrentSink, self).__init__()

class ISpikeSource(Device, Connectable):
    def __init__(self, *args, **kwargs):
        super(ISpikeSource, self).__init__()

class ISpikeSink(Device, Connectable):
    def __init__(self, *args, **kwargs):
        super(ISpikeSink, self).__init__()



