"""The grid in which the game happens"""

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

	def dump(self):
		return "width: %s, height: %s, x: %s, y: %s" % (self.width, self.height, self.x, self.y)
		
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