# Example of a class. Classifying pets. 

class Pet (object):
	def __init__ (self, name, species):
		self.name = name
		self.species = species

	def GetName(self):
		return self.name

	def GetSpecies(self):
		return self.species

	def __str__(self):
		return "%s is a %s" % (self.name, self.species)