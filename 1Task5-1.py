def do_twice(f):
	"""Calls the following function twice"""
	f()
	f()

def print_spam():
	print('spam')

do_twice(print_spam)
