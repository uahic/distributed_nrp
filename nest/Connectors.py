from music_wizard.common.Interfaces import AbstractConnector
from music_wizard.nest.__populations import population_register

def connect_to_pynn_population(port, pop_name):
    pop_view = population_register[pop_name]
    gids = map(int, pop_view.all_cells)
    port.connect(gids)

class StaticConnector(AbstractConnector):

    def __init__(self):
        self.connector_fcn = connect_to_pynn_population

    def connect(self, port, pop_name):
        self.connector_fcn(port, pop_name)

    def set_connector_fcn(self, connector_fcn):
        self.connector_fcn = connector_fcn


