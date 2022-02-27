#!/usr/bin/env python3

import env_sim

simulation = Simulation()

# add a new species
simulation.add_species(name="Name", eats=["list", "of", "things", "it", "eats"])

# get the current frame of the simulation
res, width, height = simulation.get_frame()
# res will be a list of strings, which will either be the name of the species or None, if no species is there.

# remove a species
simulation.remove_species("species_name")
# Will remove the species if it exists, and if it doesn't, does nothing

# Move the simulation forward.
simulation.advance()
