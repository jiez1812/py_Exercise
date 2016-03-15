class Student(object):

	def __init__(self, name, score):
		self.__name = name
		self.__score = score
	
	def get_name(self):
		return self.__name
		
	def get_score(self):
		return self.__score
		
	def set_name(self, name):
		self.__name = name
		
	def set_score(self, score):
		self.__score = score
	
	def print_score(self):
		print('{0}: {1}'.format(self.__name, self.__score))
		
bart = Student('Bart Simpson', 56)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
bart.set_score(68)
bart.set_name('Bart Warner')
bart.print_score()
print(lisa.get_name())