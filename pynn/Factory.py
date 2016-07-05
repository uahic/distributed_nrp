from music_wizard.pynn import CellTypes


def create_proxy_with_native_cell_types(pynn_sim, width, cell_type, port_name,
                                        proxy_type, acc_latency, is_output):
    import nest
    kwargs = {'port_name': port_name}
    proxy = pynn_sim.Population(width, cell_type, {})
    ids = map(int, proxy.all_cells)
    nest.SetStatus(ids, kwargs)
    # Acc. latency actually only matters for input ports
    if not is_output:
        nest.SetAcceptableLatency(port_name, acc_latency)
    if proxy_type == "Event" and not is_output:
        for i, proxy_id in enumerate(ids):
            nest.SetStatus([proxy_id], 'music_channel', i)
    return proxy


def projection(simulator_name, presynaptic, postsynaptic, *args, **kwargs):
    if not simulator_name == "NEST":
        raise Exception("Only Nest is currently supported.")
    import nest
    presynaptic_ids = map(int, presynaptic.all_cells)
    postsynaptic_ids = map(int, postsynaptic.all_cells)
    nest.Connect(presynaptic_ids, postsynaptic_ids, *args, **kwargs)


def out_projection(simulator_name, presynaptic, postsynaptic):
    if not simulator_name == "NEST":
        raise Exception("Only Nest is currently supported.")
    import nest
    presynaptic_ids = map(int, presynaptic.all_cells)
    postsynaptic_ids = map(int, postsynaptic.all_cells)
    for i, (pre_id, post_id) in enumerate(zip(presynaptic_ids, postsynaptic_ids)):
        nest.Connect([pre_id], [post_id], 'one_to_one', {'music_channel': i})


class PyNNProxyFactory(object):

    def __init__(self, pynn_simulator, music_setup, acc_latency=10.0, max_buffered=1):
        self.acc_latency = acc_latency
        self.max_buffered = max_buffered
        self.pynn_simulator = pynn_simulator
        self.cell_type_dict = CellTypes.load_cell_types(pynn_simulator.
                                                        simulator.name)

    def create_proxy(self, port_name, proxy_type, width, is_output):
        simulator_name = self.pynn_simulator.simulator.name
        if proxy_type == 'RPC':
            raise Exception('Currently not supported for PyNN.')

        if is_output:
            cell_type = self.cell_type_dict['out'][proxy_type]
        else:
            cell_type = self.cell_type_dict['in'][proxy_type]

        # Currently NEST specific, will be replaced by a MUSIC branch of PyNN
        proxy = create_proxy_with_native_cell_types(self.pynn_simulator, width,
                                                    cell_type, port_name,
                                                    proxy_type, self.acc_latency, is_output)

        if proxy_type == 'Event':
            parrots = self.pynn_simulator.Population(width, self.cell_type_dict['parrot'], {})
            if is_output:
                out_projection(simulator_name, parrots, proxy)
            else:
                projection(simulator_name, proxy, parrots, 'one_to_one')
            return parrots
        return proxy


class PyNNConnectorFactory(object):

    def __init__(self, pynn_simulator):
        self.pynn_simulator = pynn_simulator

    def create_and_connect_synapse(self, proxy, port_name, xml_synapse, selector, target_pop, is_output):
        if selector:
            target_pop = self.pynn_simulator.PopulationView(target_pop, selector)
        if is_output:
            self.pynn_simulator.Projection(target_pop, proxy, self.pynn_simulator.OneToOneConnector())
            #out_projection(self.pynn_simulator.simulator.name, target_pop, proxy)
        else:
            self.pynn_simulator.Projection(proxy, target_pop, self.pynn_simulator.OneToOneConnector())
            #projection(simulator_name, proxy, target_pop, 'one_to_one')

 

