from pyNN import nest as sim



def load_cell_types(simulator_name):
    cell_type_dict = {}

    if simulator_name == "NEST":
        music_event_out_proxy = sim.native_cell_type('music_event_out_proxy')
        music_event_in_proxy = sim.native_cell_type('music_event_in_proxy')
        parrot_neuron_type = sim.native_cell_type('parrot_neuron')
        model_list = [music_event_out_proxy, music_event_in_proxy, parrot_neuron_type]
        for model in model_list:
            model.default_initial_values = {}
            model.default_parameters = {}
        cell_type_dict['out'] = {'Event': music_event_out_proxy}
        cell_type_dict['in'] = {'Event': music_event_in_proxy}
        cell_type_dict['parrot'] = parrot_neuron_type
    else:
        raise Exception("Implementation for {} not found"
                        .format(simulator_name))
    return cell_type_dict
