from music_wizard.common.Interfaces import AbstractDevice

class SimpleDevice(AbstractDevice):

    def __init__(self, connector, port,  *args, **kwargs):
        super(SimpleDevice, self).__init__(*args, **kwargs)
        self.port = port  
        self.connector = connector
        self.connector.add_ports(list(self.port))

class SpikeRecorder(SimpleDevice):
    port_spec = ['Event']

    def __init__(self, connector, port,  *args, **kwargs):
        super(SpikeRecorder, self).__init__(connector, port,  *args, **kwargs)

class PopulationRate(SimpleDevice):
    port_spec = ['Continuous']

    def __init__(self, connector, port,  *args, **kwargs):
        super(PopulationRate, self).__init__(connector, port,  *args, **kwargs)

class SpikeSource(SimpleDevice):
    port_spec = ['Event']

    def __init__(self, connector, port,  *args, **kwargs):
        super(SpikeSource, self).__init__(connector, port,  *args, **kwargs)

class ACSource(SpikeSource):
    port_spec = ['Event']

    def __init__(self, connector, port, *args, **kwargs):
        super(ACSource, self).__init__(connector, port,  *args, **kwargs)

class DCSource(SpikeSource):
    port_spec = ['Event']

    def __init__(self, connector, port,  *args, **kwargs):
        super(DCSource, self).__init__(connector, port,  *args, **kwargs)

class NCSource(SpikeSource):
    port_spec = ['Event']

    def __init__(self, connector, port,  *args, **kwargs):
        super(NCSource, self).__init__(connector, port,  *args, **kwargs)

class Poisson(SpikeSource):
    port_spec = ['Event']

    def __init__(self, connector, port,  *args, **kwargs):
        super(Poisson, self).__init__(connector, port,  *args, **kwargs)



        
