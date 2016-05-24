from music_wizard.common.Interfaces import Port
from music_wizard.common.Messages import MessageQueue, decode_message, encode_message
import music

class PyMusicPort(Port):

    def __init__(self, *args, **kwargs):
        super(PyMusicPort, self).__init__(*args, **kwargs)

    def connect(self, target):
        pass

class MsgInputPort(PyMusicPort):

    def __init__(self, music_setup, port_name, callback, accLatency, maxBuffered=-1, pickled=False, *args, **kwargs):
        super(MsgInputPort, self).__init__(*args, **kwargs)
        self._port = music_setup.publishMessageInput(port_name)
        self._port.map(callback, accLatency=accLatency, maxBuffered=maxBuffered, pickled=pickled)


class MsgOutputPort(PyMusicPort):

    def __init__(self, music_setup, port_name, maxBuffered=-1, pickled=False, *args, **kwargs):
        super(MsgOutputPort, self).__init__(*args, **kwargs)
        self._port = music_setup.publishMessageOutput(port_name)
        self._port.map(maxBuffered=maxBuffered, pickled=pickled)

    def insertMessage(self, time, msg):
        self._port.insertMessage(time, msg)

class RPCInPort(PyMusicPort):

    _instances = []
    @classmethod
    def execute(cls):
        for instance in cls._instances:
            instance.apply_messages()

    def __init__(self, music_setup, port_name, accLatency, maxBuffered=-1, *args, **kwargs):
        super(RPCPort, self).__init__(*args, **kwargs)
        self._callbacks = {}
        self._queue = MessageQueue()

        def music_callback(time, encoded_msg):
            msg = decode_message(encoded_msg)
            self._queue.append(msg)

        self._rpc_msg_port = MsgInputPort(music_setup, port_name, music_callback, accLatency, maxBuffered)
        self._instances.append(self)


    def register_callback(self, name, func):
        self._callbacks[name] = func

    def apply_messages(self):
        for msg in self._queue:
            func = self._callbacks[msg.func_name]
            func(*msg.args, **msg.kwargs)
        self._queue.clear()


class RPCOutPort(PyMusicPort):

    def __init__(self, music_setup, port_name, maxBuffered, *args, **kwargs):
        super(RPCOutPort, self).__init__(*args, **kwargs)
        self._music_setup = music_setup
        self._music_runtime = None
        self.port = MsgOutputPort(music_setup, port_name, maxBuffered=maxBuffered)

    def apply(self, time_stamp, func_name, *args, **kwargs):
        msg = encode_message(func_name, *args, **kwargs)
        self.port.insertMessage(time_stamp, msg)

class ContOutputPort(PyMusicPort):

    def __init__(self, music_setup, port_name, buffer_obj, maxBuffered=-1, *args, **kwargs):
        super(ContOutputPort, self).__init__(*args, **kwargs)
        self._buffer = buffer_obj
        self._port = music_setup.publishContOutput(port_name)
        self._port.map(self._buffer, maxBuffered=maxBuffered)

class ContInputPort(PyMusicPort):

    def __init__(self, music_setup, port_name, buffer_obj, accLatency, maxBuffered=-1, *args, **kwargs):
        super(ContInputPort, self).__init__(*args, **kwargs)
        self._buffer = buffer_obj
        self._port = music_setup.publishContInput(port_name)
        self._port.map(self._buffer, delay=accLatency, maxBuffered=maxBuffered)

class EventInputPort(PyMusicPort):

    def __init__(self, music_setup, port_name, callback, accLatency, music_index_type=music.Index.GLOBAL, maxBuffered=-1, perm=None, base=-1, size=-1, *args, **kwargs):
        super(EventInputPort, self).__init__(*args, **kwargs)
        self._port = music_setup.publishEventInput(port_name)
        self._port.map(callback, music_index_type, accLatency, maxBuffered=maxBuffered, perm=perm, base=base, size=size)

class EventOutputPort(PyMusicPort):

    def __init__(self, music_setup, port_name, accLatency, music_index_type=music.Index.GLOBAL, maxBuffered=-1, perm=None, base=-1, size=-1, *args, **kwargs):
        super(EventOutputPort, self).__init__(*args, **kwargs)
        self.music_index_type = music_index_type
        self._port = music_setup.publishEventOutput(port_name)
        self._port.map(music_index_type, maxBuffered=maxBuffered, perm=perm, base=base, size=size)

    def insertEvent(self, time, index, music_index_type=music.Index.GLOBAL):
        self._port.insertEvent(time, index, music_index_type)

