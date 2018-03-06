"""The grid in which the game happens"""

from room import Room

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
			
					row.append(Room())
					
			self.col.append(row)

	def dump(self):
		return "width: %s, height: %s, x: %s, y: %s\n grid: \n%s" % (self.width, self.height, self.x, self.y, self.dumpGrid())
		
	def dumpGrid(self):
		"""Visual representation of a grid"""
		result = ""
		for r in range(self.height):
			
			for c in range(self.width):

					result += " %s" % self.col[c][r].locationType()
					
			result += '\n'
		
		return result
		
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
		if self.y < self.width:
			self.y += 1
			result = True
		return result
