import port_xml_reader
import unittest
from collections import defaultdict

class ACSource(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self._prop1 = None

    @property
    def prop1(self):
        return self._prop1

    @property.setter
    def prop1(self, value):
        self._prop1 = value 

class PropertyFactory(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

class MusicXmlParserTest(unittest.TestCase):

    def __init__(self):
        self.port_fac_map = {'ACSource': ACSource}
        self.propery_port_fac_map = defaultdict(PropertyFactory)
        self.xml_file = 'test.xml'

    def test_parsing(self):
        port_handler = port_xml_reader.parse_music_xml(self.xml_file, self.port_fac_map, self.propery_port_fac_map)
        port = port_handler.ports.pop()
        property_ports = port_handler.property_ports

  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
    unittest.main()


port_map = {}
source_factory = port_xml_reader.ElementTreeNodeFactory("source", 
