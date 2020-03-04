"""
decorator: Decorator is just a function take a another function and adds the functionality to other function
           without modifying exiting other function.

Note: first 3 examples are function decorator.
"""
#One way of using decorator

def decorator_fun(orginal_func):
	def wrapper_fun():
		print("Wrapper executed this before \"{}\" function".format(orginal_func.__name__))
		return orginal_func()
	return wrapper_fun

def display():
	print("The display method is called")

dec_func1 = decorator_fun(display)

dec_func1()
print("*"*40)
print("------------- why decorator ---------------------")
# we can add extra functionality , without modifying the existing function


#Second way of using decorator
"""
def my_decotor_func(original_func):
	def wrapper_fun():
		print("Wrapper function is executed before original {} function".format(original_func.__name__))
		return original_func()
	return wrapper_fun

@my_decotor_func
def display():
	print("The display function ran")

display()
display()
display()
"""

"""
1>
@my_decotor_func
def display():
	-----
	and
2>
display = my_decotor_func(display)

Both are same
"""

print("-------- Example 3--------------------")
"""
def my_decorator_func(orginal_func):
	def wrapper_fun(*args, **kwargs):
		print("Wrapper function executed before orginal \"{}\" function".format(orginal_func.__name__))
		return orginal_func(*args, **kwargs)
	return wrapper_fun

@my_decorator_func
def display():
	print("display function without parameter is called")

@my_decorator_func
def display_parameter(name, age):
	print("Display function with parameter name:{0} age={1}".format(name, age))

display()
display_parameter("Jayashnakara", 28)
"""
print("------------------------ Class decorator------------------------")
#Exapmple 1
"""
class my_decorator_class(object):
	def __init__(self, original_func):
		self.original_func = original_func

	def __call__(self, *args, **kwargs):
		print("Call routine is excuted before calling orginal \"{0}\" function".format(self.original_func.__name__))
		return self.original_func(*args, **kwargs)

@my_decorator_class
def display():
	print("Display routine without parameter is called")

@my_decorator_class
def display_info(name, age):
	print("Dispay fun is called with parameter name:{0} age:{1}".format(name, age))


display_info("Jayashankara", 28)

display()
"""

print("--------------- Practical example of decorator-------------------")
"""
def my_logger(orginal_func):
	import logging
	logging.basicConfig(filename='{}.log'.format(orginal_func.__name__), level=logging.INFO)
	def wrapper(*args, **kwargs):
		logging.info("Ran with args:{}, kwargs:{}".format(*args, **kwagrs))
		return orginal_func(*args, **kwargs)
	return wrapper

@my_logger
def display(name, age):
	print("display is called with name:{} and age:{}".format(name, age))

display("Jayashnakara", 28)

"""

print("------------- Practical example 2 -----------------")
"""
import time
def my_timer(orginal_func):
	import time
	def wrapper(*args, **kwargs):
		t1 = time.time()
		result = orginal_func(*args, **kwargs)
		t2 = time.time()- t1
		print("{} tooks {} sec to complete".format(orginal_func.__name__, t2))
	return wrapper

@my_timer
def display(name, age):
	time.sleep(1)
	print("display is called with name:{} and age:{}".format(name, age))


display("Jayashankara", 28)
"""

print("------------ using mutiple decorator-------------------------")

from functools import wraps #wraps all the decorator
def my_logger(orginal_func):
	import logging
	logging.basicConfig(filename='{}.log'.format(orginal_func.__name__), level=logging.INFO)

	@wraps
	# if it is not done here, then orginal_func name is "wrapper" which is output of my_timer(display),
	# By adding this we wraped that and orginal_func name here is "display"
	def wrapper(*args, **kwargs):
		logging.info("Ran with args:{}, kwargs:{}".format(*args, **kwagrs))
		return orginal_func(*args, **kwargs)
	return wrapper

import time
def my_timer(orginal_func):
	import time

	@wraps
	def wrapper(*args, **kwargs):
		t1 = time.time()
		result = orginal_func(*args, **kwargs)
		t2 = time.time()- t1
		print("{} tooks {} sec to complete".format(orginal_func.__name__, t2))
	return wrapper

@my_logger
@my_timer
def display(name, age):
	time.sleep(1)
	print("display is called with name:{} and gae:{}".format(name, age))
"""
Above call will become:

display = my_logger(my_timer(display))

for my_logger() : my_timer wrapper function is become orginal function.

"""

display("Jayashankara", 28)

