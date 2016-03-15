class Animal(object):
	def run(self):
		print('Animal is running...')

class Dog(Animal):
	def run(self):
		print('Dog is running...')
	
	def eat(self):
		print('Eating meat...')

class Cat(Animal):
	def run(self):
		print('Cat is running...')
		
class Tortoise(Animal):
	def run(self):
		print('Turtoise is running slowly...')

class Timer(object):
	def run(self):
		print('Start...')

def run_twice(animal):
	for x in range(0,2):
		animal.run()

dog = Dog()
dog.run()

cat = Cat()
cat.run()

run_twice(Tortoise())
run_twice(Timer())