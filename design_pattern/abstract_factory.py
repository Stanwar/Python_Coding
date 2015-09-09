class Dog:

	def speak(self):
		return "Woof!"

	def __str__(self):
		return "Dog"


class DogFactory:
	"""Concrete Factory"""
	def get_pet(self):
		"""Returns a Dog Object"""
		return Dog()

	def get_food(self):
		"""Returns a Dog Food Object"""
		return "Dog Food"

class Cat:
	def speak(self):
		return "Meow!"

	def __str__(self):
		return "Cat"

class CatFactory:
	"""docstring for CatFactory"""
	def get_pet(self):
		return Cat()
	def get_food(self):
		return "Cat Food"
		

class PetStore:
	def __init__(self,pet_factory=None):
		""" pet_factory is the abstract factory """ 
		self._pet_factory = pet_factory

	def show_pet(self):

		""" Utility method to display the details of the objects returned by the DogFactory """

		pet = self._pet_factory.get_pet()
		pet_food = self._pet_factory.get_food()

		print("Our Pet is '{}'!".format(pet))
		print("Our Pet says hello by '{}'".format(pet.speak()))
		print("Its food is '{}'!".format(pet_food))

### Creating a Concrete Factory
factory = DogFactory()

### Create a pet store housing our abtract factory 
shop = PetStore(factory)

### Invoke the utility method to show the details of our pet 
shop.show_pet()

factory = CatFactory()
shop = PetStore(factory)

shop.show_pet()