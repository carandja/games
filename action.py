"""
Actions describe what a player can do to progress the game
"""
class Action(object):
	"""An action available to the player"""
	
	def __init__(self, option, text, invoke):
		"""Constructor"""
		self.option = option
		self.text = text
		self.invoke = invoke
		
	def run(self):
		"""Invoke the associated action"""
		self.invoke()
		
	def getOption(self):
		"""Get the option - a single character key"""
		return self.option
		
	def getText(self):
		"""Get the text - descriptive text about what the action will do"""
		return self.text
		
	def getDescription(self):
		"""Get a description including option and text"""
		return "%s: %s" % (self.option, self.text)
		