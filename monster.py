"""
Monsters may be found through the game map.
"""

from random import *

class Monster(object):
	"""A generic type of monster"""
	
	health = 0
	
	def __init__(self):
		"""Constructor will provide random health 5-10"""
		self.health = randint(5,10)
		
	def attack(self, points):
		""" recieve an attack """
		self.health -= points
		return isAlive()
		
	def isAlive(self):
		"""The monster is alive if it has any health left"""
		return self.health > 0