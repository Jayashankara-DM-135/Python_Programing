"""
first class function.py

First class funcation: "A programing language is said to have a first class function if it treat function as a
                        first-class citizen(first class object)".

First class citizen/object: "A first class citizen(some time called as first class object) in programing language is a
                             entity which support all the operations generally avilable to other entities.
                             These operations typically
                             include beging passed as a argument, return from a function and assigned to a varible"

Basically means : function can be treated as other object.
                   1> funcation can be assigned to other varible.
                   2> Pass function as argument to another function
                   3> Function can return from another function similarly how other object being return from function.
"""


#Example

def squre(x):
	return x*x

f = squre(5)
print(squre)
print(f)

print("--------- 1> Function can be assigned----------------------")

def squre_x(x):
	return x*x

m = squre_x; # Here we are assiging function to varible and m()is used as  squre_x() function later
print(m)
print(squre_x)
print(m(5))

print("---------- 2> Function can passed to other function---------")

def my_squre_func(x):
	return x*x

def squre_list(func, my_list):
	result = []
	for ind in my_list:
		result.append(func(ind))
	return result

tmp_list = [1, 2, 3, 4, 5]
res = squre_list(my_squre_func, tmp_list)
print(res)

print("------------------ 3> return function from another function---------")

def my_tag(tag):
	def my_body(msg):
		return"<{0}> {1} <\{0}>".format(tag,msg)
	return my_body

tmpfunc = my_tag('h1')
print(tmpfunc("Hello, world"))
print(tmpfunc("Welcome to python progriming"))

tmpfunc = my_tag('p')
print(tmpfunc('This is scripting languge'))
print(tmpfunc('It supports function assigning, passing and returning'))





