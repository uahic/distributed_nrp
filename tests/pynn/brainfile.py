import pyNN.nest as sim
import numpy
import nest
__population_views = {}


pop1 = sim.Population(10, sim.IF_cond_alpha())
__population_views['pop1'] = pop1


nest_source = nest.Create('poisson_generator')
nest.SetStatus(nest_source, {'rate': 10000.0})
nest.Connect(nest_source, map(int, pop1.all_cells), 'all_to_all')

print "Network loaded"


