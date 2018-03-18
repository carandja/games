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
	print grid.getDescription()
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

print "Welcome"
grid = Grid(5, 7)
goon = True

leaveAction = Action("Q", "Quit the game", leave)
exitAction =	Action("X", "Escape from the dungeon", leave)
GridBuilder().build(grid, exitAction)


while goon:
	nextAction(grid)
