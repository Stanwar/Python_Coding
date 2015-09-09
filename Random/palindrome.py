## Palindrome 
class string_manipulation:
	""" This is a string manipulation class """
	def __init__(self,string_name):
		self.string_name = string_name

	def palindrome(self):
		#for (int i=0;i<self.string_name.length/2;i++):
		s = len(self.string_name)

		for i in range(0,s):
			if self.string_name[i] != self.string_name[s -i - 1]:
				return False
		return True

var = string_manipulation("")

result = var.palindrome()
print result
