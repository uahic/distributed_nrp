from collections import namedtuple
from collections import deque
import msgpack

apply_fmt = namedtuple("rpc_msg", ['func_name', 'args', 'kwargs'])

typecode_method_map = {
        0: 'connect',
        1: 'connect_via_ids'
        }

revd = dict([reversed(i) for i in typecode_method_map.items()])
typecode_method_map.update(revd)

def encode_message(func_name, *args, **kwargs):
    #typecode = typecode_method_map[func_name]
    return msgpack.packb(apply_fmt(func_name, args, kwargs))

def decode_message(encoded_msg):
    msg = msgpack.unpackb(encoded_msg)
    return apply_fmt(*msg)

class MessageQueue(deque):
    pass
