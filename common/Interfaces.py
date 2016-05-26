import abc

class AbstractConnection(object):
    pass

class AbstractConnector(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def connect(self, target, *args, **kwargs):
        pass

class Port(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        super(Port, self).__init__(*args, **kwargs)

    @abc.abstractmethod
    def connect(self, target):
        pass


class DeviceMeta(abc.ABCMeta):
    _instances = []
    _device_classes = {}

    def __new__(cls, clsname, bases, attrs):
        newclass = type.__new__(cls, clsname, bases, attrs)
        if clsname in DeviceMeta._device_classes:
            raise TypeError("Device {} has already been defined.".format(clsname))
        DeviceMeta._device_classes[clsname] = newclass 
        return newclass

    def __call__(self, *args, **kwargs):
        obj = super(DeviceMeta, self).__call__(*args, **kwargs)
        DeviceMeta._instances.append(obj)
        return obj

    def __getitem__(self, clsname):
        try:
            return DeviceMeta._device_classes[clsname]
        except KeyError:
            raise KeyError("Class {} has not been registered yet.".format(clsname))

    def __setitem__(self, clsname, cls):
        DeviceMeta._device_classes[clsname] = cls

class AbstractDevice(object):
    __metaclass__ = DeviceMeta

    def __init__(self, *args, **kwargs):
        super(AbstractDevice, self).__init__(*args, **kwargs)

    @abc.abstractmethod
    def _create_device(self):
        pass

