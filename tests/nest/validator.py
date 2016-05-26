from lxml import etree, objectify
from lxml.etree import XMLSyntaxError

def xml_validator(some_xml_string, xsd_file='/path/to/my_schema_file.xsd'):
    try:
        schema = etree.XMLSchema(file=xsd_file)
        parser = objectify.makeparser(schema=schema)
        objectify.fromstring(some_xml_string, parser)
        print "YEAH!, my xml file has validated"
    except XMLSyntaxError:
        #handle exception here
        print "Oh NO!, my xml file does not validate"
        pass

xml_file = open('music.xml', 'r')
xml_string = xml_file.read()
xml_file.close()

xml_validator(xml_string, '/home/packages/music_wizard/common/xml_config/music.xsd')
