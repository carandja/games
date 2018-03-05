"""
A room within the game map.
"""

class Location(object):
	"""A location on the map."""
	
	def __init__(self):
		"""Constructor"""
		print "New Location"

	def locationType():
		"""Return the type of location as a 4-char string"""
		return "LOCA"
	
class Wall(Location):
	"""The Room class"""

	def __init__(self):
		"""Constructor"""
		super(Wall, self).__init__()
		print "New Room"

	def locationType(self):
		"""Return the type of location as a 4-char string"""
		return "WALL"
	
class Room(Location):
	"""The Room class"""

	def __init__(self):
		"""Constructor"""
		super(Room, self).__init__()
		print "New Room"

	def locationType(self):
		"""Return the type of location as a 4-char string"""
		return "ROOM"

	def getActions(self):
		"""Return a list of user Actions"""

