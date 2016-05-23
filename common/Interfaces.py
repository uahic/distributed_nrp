import abc

class Port(object):
    __metaclass__ = abc.ABCMeta
    _port_prefix = None

    def __init__(self):
        super(Port, self).__init__()


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

class Device(object):
    __metaclass__ = DeviceMeta
    _port_prefix = None

    def __init__(self, *args, **kwargs):
        super(Device, self).__init__(*args, **kwargs)

    @abc.abstractmethod
    def _init_model(self):
        pass

class Connectable(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        super(Connectable, self).__init__()

    @abc.abstractmethod
    def connect(self, target_pop):
        pass

    @abc.abstractmethod
    def connect_via_ids(self, id_list):
        pass

class Updateable(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        super(Updateable, self).__init__()

    @abc.abstractmethod
    def update(self, *args, **kwargs):
        pass
