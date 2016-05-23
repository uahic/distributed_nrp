
import sys
import os
import numpy as np 
import unittest
import mock
from music_nest.simulator_backend.Brainloader import load_py_brain

from music_nest.common import Interfaces

class BrainLoaderTests(unittest.TestCase):

    def test_load_py_brain(self):
        pop_dict = load_py_brain('brainfiles/simple_1.py')
        self.assertTrue(pop_dict['pop1'])
        self.assertTrue(pop_dict['circuit'])

def get_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(BrainLoaderTests))
    return suite 

if __name__ == '__main__':
    unittest.main()
