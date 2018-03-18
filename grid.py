"""The grid in which the game happens"""

from room import Wall
from action import *

class Grid:
	"""Represents the 2D grid"""
	
	def __init__(self, width, height):
		"""
		2 argument constructor.
		
		width: the width if the grid
		height: the height of the grid
		"""
		self.width = width
		self.height = height
		self.x = 0
		self.y = 0
		
		self.col = []
		
		for c in range(self.width):
		
			row = []
			
			for r in range(self.height):
			
					row.append(Wall())
					
			self.col.append(row)

	def dump(self):
		return "width: %s, height: %s, x: %s, y: %s\n grid: \n%s" % (self.width, self.height, self.x, self.y, self.dumpGrid())
		
	def dumpGrid(self):
		"""Visual representation of a grid"""
		result = ""
		for r in range(self.height):
			
			for c in range(self.width):
					
					text = self.col[c][r].locationType()
					if c == self.x and r == self.y:
						text = text.lower()
					result += " %s" % text
					
			result += '\n'
		
		return result

	def canUp(self):
		"""Can we go up the grid"""
		return self.y > 0 and self.col[self.x][self.y - 1].locationType() != "WALL"

	def canDown(self):
		"""Can we go down the grid"""
		return self.y < self.height - 1 and self.col[self.x][self.y + 1].locationType() != "WALL"

	def canLeft(self):
		"""Can we go left on the grid"""
		return self.x > 0 and self.col[self.x - 1][self.y].locationType() != "WALL"

	def canRight(self):
		"""Can we go right on the grid"""
		return self.x < self.width - 1 and self.col[self.x + 1][self.y].locationType() != "WALL"

	def up(self):
		"""Move up the grid"""
		result = False
		if self.y > 0:
			self.y -= 1
			result = True
		return result
		
	def down(self):
		"""Move up the grid"""
		result = False
		if self.y < self.height - 1:
			self.y += 1
			result = True
		return result

	def left(self):
		"""Move left on the grid"""
		result = False
		if self.x > 0:
			self.x -= 1
			result = True
		return result

	def right(self):
		"""Move right on the grid"""
		result = False
		if self.x < self.width - 1:
			self.x += 1
			result = True
		return result

	def getActions(self):
		"""Provide actions at current location"""
		location = self.col[self.x][self.y]
		actions = location.getActions()
		
		if self.canUp():
			actions.append(Action("N", "Head North", self.up))

		if self.canRight():
			actions.append(Action("E", "Head East", self.right))			

		if self.canDown():
			actions.append(Action("S", "Head South", self.down))

		if self.canLeft():
			actions.append(Action("W", "Head West", self.left))

		return actions