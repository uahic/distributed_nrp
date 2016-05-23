import sys
import os
import numpy as np 
import unittest
import mock
from music_nest.common.Ports import ContOutputPort, ContInputPort, RPCPort, create_nest_event_out_port, create_nest_msg_in_port, create_nest_cont_out_port


class MusicPorts(unittest.TestCase):

    def setUp(self):
        self.buffer = np.array([0.0], dtype=np.float)
        self.callback_func = None
        self.rpc_port_name = None
        self.callback_msg_args = None
        self.music_setup = mock.MagicMock()

    def test_cont_out(self):
        cont_out = ContOutputPort(self.music_setup, "Port1", self.buffer)
        self.assertEqual(cont_out._buffer, self.buffer)
        self.music_setup.publishContOutput.assert_has_calls([mock.call("Port1")])

    def test_cont_out(self):
        cont_in = ContInputPort(self.music_setup, "Port1", self.buffer)
        self.assertEqual(cont_in._buffer, self.buffer)
        self.music_setup.publishContInput.assert_has_calls([mock.call("Port1")])

    @mock.patch('music_nest.common.Ports.create_nest_msg_in_port', autospec=True)
    def test_rpc_port(self, mock_create_nest_message_port):
        # This stores the internal callback that would have been passed to the music port (called whenever new messages arrive)
        def side_effect(music_setup, name, func, acc_latency=-1.0, max_buffered=-1):
            self.callback_func = func
            self.rpc_port_name = name
            self.acc_latency = acc_latency
            self.max_buffered = max_buffered
        mock_create_nest_message_port.side_effect = lambda music_setup, name, func, acc_latency, max_buffered: side_effect(music_setup, name, func, acc_latency, max_buffered)

        # This is the user-defined callback, we want just check here if it ever gets called and the message passed
        def callback(*args, **kwargs):
            self.callback_msg_args = args 
        rpc_port = RPCPort(self.music_setup, "Port1", 2.0, 2)
        rpc_port.register_callback("callback1", callback)
        self.assertEqual(self.rpc_port_name, "Port1_rpc")
        self.assertGreater(self.acc_latency, 0.0)
        self.assertGreater(self.max_buffered, 1)

        # Trying to send a message (thus simulating the message in port)
        class Message(object):
            def __init__(self):
                self.func_name = 'callback1'
                self.args = ['my message']
                self.kwargs = {}
        self.callback_func(0.0, Message())
        self.assertEqual(self.callback_msg_args, ('my message',))

def get_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(MusicPorts))
    return suite 

if __name__ == '__main__':
    unittest.main()
