"""A Builder for grids"""

from random import randint
from room import *

class GridBuilder:
	""" The grid building class"""
	
	def __init__(self):
		"""Constructor"""
		
	def build(self, grid):
		"""Build a grid"""
		grid.x = randint(0, grid.width - 1)
		grid.y = randint(0, grid.height - 1)
		grid.col[grid.x][grid.y] = Entrance()
		
		# save coordinates of entrance for later
		runx = grid.x
		runy = grid.y
		
		target = max(grid.width, grid.height)
		length = 1
		
		direction = {
			1: grid.up,
			2: grid.right,
			3: grid.down,
			4: grid.left
		}
		while length < target:
			dir = randint(1, 4)
			if direction[dir]() and grid.col[grid.x][grid.y].locationType() == "WALL":
				length += 1
				grid.col[grid.x][grid.y] = Room()
				
		grid.col[grid.x][grid.y] = Exit()
		
		grid.x = runx
		grid.y = runy
