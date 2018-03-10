"""
Main entry point for the system
"""

from room import *

r = Room()
print r

from action import *
a = Action()
print a

from grid import *
g = Grid(5, 7)
print g.dump()

from grid_builder import *
gb = GridBuilder()
gb.build(g)

print g.dump()
