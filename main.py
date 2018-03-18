"""
Entry point for the application
"""

from grid import *
from grid_builder import *
from action import *

def leave():
	global goon
	goon = False
	
def nextAction(grid):
	print grid.dump()
	actionList = grid.getActions()
	actionList.append(leaveAction)
	for action in actionList:
		print action.getDescription()
	option = raw_input("? ").upper()
	for action in actionList:
		if action.getOption() == option:
			#print "matched"
			action.run()
		else:
			#print "not matched [%s] [%s]" % (action.getOption(), option)
			pass

grid = Grid(5, 7)
GridBuilder().build(grid)

goon = True

leaveAction = Action("X", "Exit the dungeon", leave)

while goon:
	nextAction(grid)
