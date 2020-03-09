"""
Varible scope:

LEGB : Local, Enclosing, Global, Built-in

Python will check the scope of varible below order:
1> Local
2> Enclosing
3> Global
4> Built-In

"""

#Example 1

x = "Global X"
def test():
	x="Local x"
	y="Local y"
	print(x) #prints Local x
	print(y) #prints Local y

test()
print(x) # prints Global X
#print(y) It's Not defined , Since y inside test() is no more exist

print("-----------------------------------")
#Now i want to change Global X with whatever test() updates on Local X

x = "Global X"
def test():
	global x  #Now Global X is also used here
	x="Local x" #Now this changes is also applicable to globle X, since we used "global x" statemnets
	y="Local y"
	print(x) #prints Local x
	print(y) #prints Local y

test()
print(x) # prints Local X

print("-----------------------------------")
#Now i am not defining X in globally
def test():
	global x  #Now X is used as a global after this method
	x="Local x" #Now this changes is also applicable to globle X, since we used "global x" statemnets
	y="Local y"
	print(x) #prints Local x
	print(y) #prints Local y

test()
print(x) # prints Local X



print("-----------------------------------")
#Now i am not defining X in globally
def test():
	#global x  #Now X is used as a global after this method
	x="Local x" #Now this changes is also applicable to globle X, since we used "global x" statemnets
	y="Local y"
	print(x) #prints Local x
	print(y) #prints Local y

test()
print(x) # Accessing X is error, Since we commented out


print("-----------------------------------")

def text(z):
	print(z)

text("Hi Hello")
#print(z) Similar to C language , Function parameter are local to that function


print("---------------------Builtin--------------")
import builtins
print(dir(builtins))

#It will throw error, Since we overwriting inbuilt min() method, overide will not take any parameter
#Where as builtin take some arguments.
"""
def min():
	pass
"""
m = min([1,4,7,2])

print(m)

print("------------------------Enclosing 1-----------")


def outer():
	x = "outer x"
	def inner():
		x="Inner X"
		print(x)
	inner()
	print(x)

outer()

print("------------------------Enclosing 2-----------")


def outer():
	x = "outer x"
	def inner():
		#x="Inner X"
		print(x)
	inner()
	print(x)

outer()


print("------------------------Enclosing 3-----------")

#If we run this alone we will get the error, Since print(x) at *** is not defined.
def outer():
	#x = "outer x"
	def inner():
		x="Inner X"
		print(x)
	inner()
	print(x) #***

outer()


print("------------------------Enclosing 4-----------")


def outer():
	x = "outer x"
	def inner():
		nonlocal x # similar to global keyword, But here it's outer loop x is used in inner loop.
		x="Inner X"
		print(x)
	inner()
	print(x)

outer()

print("------------------------Enclosing 5-----------")

x="Global X"
def outer():
	x = "outer x"
	def inner():
		x="Inner X"
		print(x)
	inner()
	print(x)

outer()
print(x)
