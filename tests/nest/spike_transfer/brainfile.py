import pyNN.nest as sim
import numpy
__population_views = {}


pop1 = sim.Population(10, sim.IF_cond_alpha())
__population_views['pop1'] = pop1

source = sim.Population(1, sim.SpikeSourcePoisson(rate=1000000.0))

sim.Projection(source, pop1, sim.AllToAllConnector())
print "Network loaded"
#pop1.sample(10).record('v')





