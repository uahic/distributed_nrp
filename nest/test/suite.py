import unittest

#suite = unittest.TestSuite()
suits = []
# unittests
import factory
suits.append(factory.get_suite())


import brainloader
suits.append(brainloader.get_suite())


import property_modifier
suits.append(property_modifier.get_suite())

import interfaces
suits.append(interfaces.get_suite())

for suite in suits:
    unittest.TextTestRunner().run(suite)
