"""
A room within the game map.
"""

from random import *
from monster import *
from action import *

class Location(object):
	"""A location on the map."""
	
	def __init__(self):
		"""Constructor"""

	def locationType():
		"""Return the type of location as a 4-char string"""
		return "LOCA"

	def getActions(self):
		"""Return a list of user Actions"""
		return []
		
	def getDescription(self):
		return "You are - somewhere..."
	
class Wall(Location):
	"""The Wall class"""

	def __init__(self):
		"""Constructor"""
		super(Wall, self).__init__()
		
	def locationType(self):
		"""Return the type of location as a 4-char string"""
		return "WALL"
	
class Entrance(Location):
	"""The Entrance class"""

	def __init__(self):
		"""Constructor"""
		super(Entrance, self).__init__()
		
	def locationType(self):
		"""Return the type of location as a 4-char string"""
		return "ENTR"
	
class Exit(Location):
	"""The Entrance class"""

	def __init__(self, exitAction):
		"""Constructor"""
		super(Exit, self).__init__()
		self.action = exitAction

	def locationType(self):
		"""Return the type of location as a 4-char string"""
		return "EXIT"
		
	def getDescription(self):
		return "There's light you can see the way out!'"


	def getActions(self):
		"""Return a list of user Actions"""
		return [self.action]

	
class Room(Location):
	"""The Room class"""
	
	def __init__(self, context):
		"""Constructor"""
		super(Room, self).__init__()
		self.context = context
		
		self.wall_colour = choice(['Red', 'Green', 'Blue', 'Purple', 'Yellow', 'Orange', 'Black', 'White', 'Grey', 'Indigo'])
		self.wall_material = choice(['Wooden', 'Stone', 'Brick', 'Plaster', 'Iron', 'Marble'])
		self.treasure = randint(0,100)
		self.monsters = []
		for m in range(3):
			# randomly allocate a monsters
			if randint(1,10) > 4:
				self.monsters.append(Monster())
		

	def locationType(self):
		"""Return the type of location as a 4-char string"""
		return "ROOM"
		
	def getDescription(self):
		result = "You are in a room with %s %s walls." % (self.wall_colour.lower(), self.wall_material.lower())
		if len(self.monsters) > 1:
			result += "\nThere are %d monsters here" % len(self.monsters)
		elif len(self.monsters) == 1:
			result += "\nThere's a monster here"
		return result

	def getActions(self):
		"""Return a list of user Actions"""
		actions = []
		if len(self.monsters) > 0:
			actions.append(Action("F", "Fight", self.context.fight))
		return actions
		
	def fight(self):
		"""Fight a monster"""
		points = self.monsters[0].attack()
		if (points == 0):
			self.context.setMessage("You missed.")
		else:
			self.context.setMessage("You did %d points of damage." % points)
		if (not self.monsters[0].isAlive()):
			self.monsters.pop(0)
			self.context.setMessage("You killed a monster.")