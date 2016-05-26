import pyNN.nest as sim
import numpy
__population_views = {}


pop1 = sim.Population(10, sim.IF_cond_alpha())
__population_views['pop1'] = pop1

source = sim.StepCurrentSource(times=[0.1], amplitudes=[.8])

source.inject_into(pop1)
print "Network loaded"
#pop1.sample(10).record('v')





