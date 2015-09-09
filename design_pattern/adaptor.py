### Adaptor Pattern --> We can adapt a certain class to create another class to get similar kind of data
class Korean(object):
	""" Korean Speaker """
	def __init__(self):
		self.name = "Korean"

	def speak_korean(self):
		return "Korean"

class British(object):
	""" English Speaker """
	def __init__(self):
		self.name = "British"
	def speak_english(self):
		return "English"

class Adaptor(object):
	"""This changes the method to individual names as per need """
	def __init__(self,object, **adapted_method):
		self._object = object	

		self.__dict__.update(adapted_method)

	def __getattr__(self, attr):
		""" Simply return the rest of attributes """
		return getattr(self._object, attr)	

objects = []

korean = Korean()

british = British()

objects.append(Adaptor(korean,speak=korean.speak_korean))
objects.append(Adaptor(british,speak=british.speak_english))


for obj in objects:
	print "'{}' says '{}' \n".format(obj.name,obj.speak())
