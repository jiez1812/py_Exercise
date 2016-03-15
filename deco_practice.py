import functools

def log(text):
	if isinstance(text,(str, int, float)):
		def deco(func):
			@functools.wraps(func)
			def wrapper(*args, **kw):
				print('Begin Call, {0} {1}'.format(text,func.__name__))
				func(*args, **kw)
				print('End Call')
				return func
			return wrapper
		return deco
	else:
		func = text
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('Begin Call')
			func(*args, **kw)
			print('End Call')
			return func
		return wrapper

@log
def f():
	print ('  {0}'.format('this function'))

f()