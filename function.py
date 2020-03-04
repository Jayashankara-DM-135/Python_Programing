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

#args and kwargs allowing us to accept the orbitory number of postional or keyword value arguments
def student_info(*args, **kwargs):
	print(args)
	print(kwargs)

student_info("Math", "Computer", name='Jayashankara', age=28)
student_info("Hello", 1, 3, age=19, DOB='1990-02-06')
"""
Here , Math and Computer are positinal arguments
Where as name and age are Keyword values arguments

*args ==> gives all positinal arguments ==> like list
**kwargs ==> Gives all keyword values argumenst ==> like dictionary

Note:
1> args and kwargs are convestinal name , We can still use anyother name inplace of them
2> The grammar of the language specifies that positional arguments appear before keyword or starred arguments in calls:
"""
print("--------------------------------")
course = ["Math", "CS", "EC"]
info = {'name':'Jayashnakara', 'age':28}
student_info(course, info) # Here studen_info consider both course and info as positinal argumnets
print("++++++++++++++++++++++++++++++++++")
#so we have to pass like this
student_info(*course, **info)


