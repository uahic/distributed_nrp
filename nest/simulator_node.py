import sys
import music
import nest
import pyNN.nest as sim
from . import Brainloader 
from . import Factories
from . import Observers
from . import Setters
from . import TypeRegistry
from music_nest.common import Interfaces
from music_nest.common import Ports as CommonPorts 
from music_nest.simulator_backend import Ports as SimulatorPorts
from .__populations import population_register
from . music_setup import setup as music_setup
from . music_setup import accLatency as global_accLatency

# Populations
_population_dict = {}

def create_system_rpc_port(port_name):
    system_rpc_port = SimulatorPorts.RPCInPort(music_setup, "{}_rpc".format(port_name), global_accLatency)
    return system_rpc_port

def create_error_port(port_name):
    error_port = CommonPorts.MsgOutputPort(music_setup, port_name, global_accLatency)
    return error_port

def load_devices(music_xml_path):
    with open(music_xml_path, 'r') as f:
        xml_file = f.read()
    devices = Factories.create_devices_from_xml(xml_file)
    return devices

def load_brain(brain_file_path):
    population_view_dict = Brainloader.load_py_brain(brain_file_path)
    return population_view_dict

def dirty_fixes_before_simulation():
    # This raises the min and max_delay to 1.0
    # to ensure that connecting devices via RPC messages 
    # will not cause Seg.Faults. Seg.Faults can occur if 
    # nest.Connect() tries to change the min/max-delay after
    # the first simulation steps have been done.
    #nest.SetDefaults("static_synapse", {"min_delay": 0.1, "max_delay":1.0})

    # This dummy neuron ensures that at least one static_synapse has been created before the simulation starts
    dummy = nest.Create('iaf_neuron')
    nest.Connect(dummy, dummy)

def simulator_setup():
    sim.setup(min_delay=0.1, max_delay=1.0)
    dirty_fixes_before_simulation()

def loop():
    for device_instance in Interfaces.DeviceMeta._instances:
        device_instance._create_device()
    print "Entered loop"
    i = 0
    
    while(True):
        sim.run(20.0)
        Observers.Observer.notify()
        Setters.Setter.notify()
        SimulatorPorts.RPCPort.execute()
        for pop_view in population_register.values():
            pass
            #print pop_view.meanSpikeCount()
            #print 'amplitude', pop_view.get_data().segments[0].filter(name='v')
            #print nest.GetStatus(map(int, [pop_view.all_cells[0]]), 'V_m')

        i += 1
    sim.end()

def main(brain_file_path, music_xml_path):
    simulator_setup()
    _population_dict = load_brain(brain_file_path)
    population_register.update(_population_dict)
    devices = load_devices(music_xml_path)
    error_port = create_error_port("error_port")
    system_rpc_port = create_system_rpc_port("nest")
    loop()

if __name__ == '__main__':
    brain_file_path = music_setup.config("brain_file")
    music_xml_path = music_setup.config("port_config_file")
    main(brain_file_path, music_xml_path)
