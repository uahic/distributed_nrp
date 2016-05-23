import abc

instances = []

class ObserverMeta(abc.ABCMeta):

    def __call__(cls, *args, **kwds):
        obj = abc.ABCMeta.__call__(cls, *args, **kwds)
        instances.append(obj)
        return obj


class Observer(object):
    __metaclass__ = ObserverMeta

    @classmethod
    def notify(cls):
        for instance in instances:
            instance.update()

    @abc.abstractmethod
    def update(self):
        pass

class CallbackObserver(Observer):

    def __init__(self, callback):
        self.callback = callback
        
    def update(self):
        self.callback()


            
        
        

