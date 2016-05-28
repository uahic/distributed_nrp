from music_wizard.common.Interfaces import AbstractConnector
from music_wizard.nest.__populations import population_register

class StaticConnector(AbstractConnector):

    def __init__(self, connector_fcn):
        self.connector_fcn = connector_fcn

    def connect(self, port, pop_name):
        self.connector_fcn(port, pop_name)

    def set_connector_fcn(self, connector_fcn):
        self.connector_fcn = connector_fcn


