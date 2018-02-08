class Person(object):
	def __init__(self, name):
		self.name = name

	def say_hi(self):
		print('Helo , my name is',self.name)


P = Person('Pizisuan')
P.say_hi()
