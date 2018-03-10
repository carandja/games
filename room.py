"""
A room within the game map.
"""

class Location(object):
	"""A location on the map."""
	
	def __init__(self):
		"""Constructor"""

	def locationType():
		"""Return the type of location as a 4-char string"""
		return "LOCA"
	
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

	def __init__(self):
		"""Constructor"""
		super(Exit, self).__init__()
		
	def locationType(self):
		"""Return the type of location as a 4-char string"""
		return "EXIT"
	
class Room(Location):
	"""The Room class"""

	def __init__(self):
		"""Constructor"""
		super(Room, self).__init__()

	def locationType(self):
		"""Return the type of location as a 4-char string"""
		return "ROOM"

	def getActions(self):
		"""Return a list of user Actions"""

