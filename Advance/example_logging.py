"""
Looging example
"""
import logging
#print(logging.__file__)
logging.basicConfig(filename='closure_logging.txt', level=logging.INFO)


def logger(func):
	def log_func(*args):
		logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
		print(func(*args))
	return log_func

def my_add(x, y):
	return x+y

def my_sub(x, y):
	return x-y

add_logger = logger(my_add)
sub_logger = logger(my_sub)

print(add_logger(5,4))
print(sub_logger(5,3))

