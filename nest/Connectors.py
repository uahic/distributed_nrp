from music_wizard.common.Interfaces import AbstractConnector
from music_wizard.nest.__populations import population_register

class StaticConnector(AbstractConnector):

    def __init__(self, connector_fcn, connection_rule, selector):
        self.connector_fcn = connector_fcn
        self.connection_rule = connection_rule
        self.selector = selector

    def connect(self, port, pop_name):
        self.connector_fcn(port, pop_name, self.connection_rule, self.selector)

    def set_connector_fcn(self):
        raise Exception('Use the constructor to set all properties.')



