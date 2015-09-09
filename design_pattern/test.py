## Design Patterns in Python
class Dog:
	def __init__(self,name):
		self._name = name

	def speak(self):
		return "woof!"

## Design Patterns in Python
class Cat:
	def __init__(self,name):
		self._name = name

	def speak(self):
		return "Meow!"

def get_pet(pet="dog"):

	""""The factory method"""
	pets = dict(dog=Dog("Hope"),cat=Cat("Kitty"))

	return pets[pet]


d = get_pet("dog")

c = get_pet("cat")

print d.speak()

print c.speak() 