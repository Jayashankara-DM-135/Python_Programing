"""
Formating string,Dictionary, List, Number and Dates
"""
#1 string formating
msg = "Hello"
msg2 = "World"
print(msg + msg2)
print(msg+" "+msg2)

msg3 = msg+" "+msg2
print(msg3)

print("{} {}".format(msg, msg2))
print("{0} {1}".format(msg, msg2))
print("{1} {0}".format(msg, msg2))

fname = "Jayashankara"
lname = "DM"
age = 28

print("My name is {0} {1}, age is {2} and my email id is {0}.{1}@gmail.com".format(fname, lname, age))

tag = "h1"
text = "Wel come to Python programing"

print("<{0}>{1}</{0}>".format(tag, text))
print("*****************************************************************************************")
#dictonary

person = {"Name":"Jayashankara  DM", "age":28}

print("My name is {0} and age is {1}".format(person["Name"], person["age"]))

print("My name is {0[Name]} and age is {0[age]}".format(person))

#also we can unpack the dictory

print("Name is {Name} and age is {age}".format(**person))
print("****************************************************************************************")
#class

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

p1 = Person("Jayashankara", 29)

print("My name is {0.name} and age is {0.age}".format(p1))

#keyword

print("Name is {name} and age is {age}".format(name="Jayashankara", age=29))

print("*********************************************************************************")

#Number formating
for i in range(1, 11):
	print("The vale is {}".format(i))

#print in three digit format

#prefix the zero to make to three digit number
for i in range(1, 11):
	print("The value is {:012}".format(i))

for i in range(1, 11):
	print("The value is {:12}".format(i))

for i in range(1, 11):
	print("The value is {:13}".format(i*100))

pi = 3.13159265
print("Pi value is {}".format(pi))
print("Pi value is {:.2f}".format(pi))
#print("Pi value is {:04f}".format(pi))

#add comma separted values
print("The long value is {:,}".format(1000**2))


print("The value is {:,.2f}".format(1000**2))

print("*********************************************************************************")

#date formating
import datetime

my_date = datetime.datetime(2019, 3, 29, 12,30, 45)

print(my_date)

#format like this : March 29, 2019
"""
%B ==> Month  ==> March
%b ==> Month ==> Mar

%D ==> date : 03/29/19
%d ==> date of the month : 29

%Y ==> Year ==> 2019
%y ==> Yaer ==> 19

%A ==> Day of the Week
%j ==> Date of the year
"""

print("{:%b %D, %y}".format(my_date))

#format the like this : "March 29, 2019 fell on Monday and was the 061 day of the year"

print("{0:%b %d, %y} fell on {0:%A} and was the {0:%j} day of the year".format(my_date))






