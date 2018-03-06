"""
Main entry point for the system
"""

from room import *

r = Room()
print r
#print r.description()

from action import *
a = Action()
print a

from grid import *
g = Grid(5, 7)
print g.dump()
g.down()
g.down()
g.down()
print g.dump()
g.up()
g.up()
print g.dump()