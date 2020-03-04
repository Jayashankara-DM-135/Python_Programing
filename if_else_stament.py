"""
If else stament:

Note: There is no switch statements in python
"""

if True:
	print("Condition is true")

language = 'python'

if language == 'python':
	print("Yes, It's Python")
else:
	print("Not a pyhton")

var = 20

if var == 10:
	print("10")
elif var == 20:
	print("20")
else:
	print("30")


print("******************************************************")
#usig logical operator

name = "DM"
age = 29

if name == 'DM' and age == 28:
	print("Jayashankara")
else:
    print("It is not jayashnakar")


if name == 'DM' or age == 28:
	print("Jayashankara ")
else:
	print("No....")

if not(name=='DM'):
	print("No")
else:
	print('Jayashankara DM ')



print("************************************************************")
#Now check for object identity using 'is'

a = [1, 2, 3]
b = [1, 2, 3]
c = [1, 2, 3, 4]
print(a==b)
print(a==c)

print(id(a)) #prints memory location of a
print(id(b))
print(a is b) #check both are at same memory location or not

d = a #Both are pointing to same memory location
print(d is a)
print(a is d)

print("******************************************************************")
"""
Which are evaluates to False in python:
 1> False
 2> None
 3> Zero of any numeric type
 4> Any empty sequence, example: '', (), []
 5> Any empty mapping, Exmple: {}

"""

if False:
	print("Yes, It's false")
else:
	print("No, It's not False")


if None:
	print("Yes, It is None")
else:
	print("No , It's not None")

var = 0

if var:
	print("Yes, It's True")
else:
	print("No, It is not false")

mylist = []

if mylist:
	print("List is not empty")
else:
	print("List is empty")

mytuple = ()

if mytuple:
	print("Tuple is empty")
else:
	print("Tuple is not empty")

temp =''

if temp:
	print("String is not empty")
else:
	print("string is empty")



my_dict = {}

if my_dict:
	print("Dictionary is not empty")
else:
	print("Dictionary is empty")

