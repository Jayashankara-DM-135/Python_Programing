"""
Function :
"""

def fun():
	pass #Incomplete funcation, But it wan't throw any error

print(fun())

print("----------------------------")

def fun():
	print("My first function")

fun()
print(fun())

print("-------------------------------")

def fun():
	print("Hello world")
	return 10
print(fun())
fun()

print("-------------------------------")

def fun():
	return "Hello world"

tmp = fun()
print(tmp)
print(fun())
#print(fun().upper())

print("--------------------------------")


def fun(greeting):
	return "{} funcation".format(greeting)

print(fun("Hi"))
print(fun("Hello"))

print("----------------------------------")


def fun(greeting, name='You'):
	return "Hi {}, {}".format(name, greeting)

print(fun("welcome", "Jayashnakar"))

print("-----------------------------------")



