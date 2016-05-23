
import abc

instances = []

class SetterMeta(abc.ABCMeta):

    def __call__(cls, *args, **kwds):
        obj = abc.ABCMeta.__call__(cls, *args, **kwds)
        instances.append(obj)
        return obj

class Setter(object):
    __metaclass__ = SetterMeta 

    @classmethod
    def notify(cls):
        for instance in instances:
            instance.update()

    @abc.abstractmethod
    def update(self):
        pass

class PropertySetter(Setter):

    def __init__(self, callback, buf):
        self.callback = callback 
        self._buffer = buf

    def update(self):
        self.callback(self._buffer)



            
        
        

