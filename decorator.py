import functools

def now():
	print('2015-3-25')

f = now
f()

print(now.__name__)
print(f.__name__)

def log(text):
	def deco(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('{1} {0}: '.format(func.__name__, text))
			return func(*args, **kw)
		return wrapper
	return deco

def sayHi(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('Hi, {0}'.format(func.__name__))
		return func(*args, **kw)
	return wrapper
	
@log('execute')
def now():
	print('2015-3-25')

now()