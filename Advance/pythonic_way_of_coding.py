"""
Duck typing and EAFP(Easier to Ask Forgiveness then Permission):

These are the some of rules for coding python : if we follow this rules then it's called as pythonic , otherwise non-pythonic.
"""
#1> Duck typing: Means we don't care what is type of the object, we only care whether it perform action which we asked to do.
#2> EAFP : try fisrt accessing without checking for persmission if it's failed take care of that.
# see below example.

class Duck:
	def quack(self):
		print("Quack, quack!")
	
	def fly(self):
		print("Flap, flap!")

class Person:
	def quack(self):
		print("I am quack like duck")
	
	def fly(self):
		print("I am flapping my arams")

print("----- Non Duck typing --------")
def quck_and_fly_one(thing):
	#Not duck-typed (Means non-pythonic)
	# Here we are cheking object type is Duck or not . Hence it's Non Duck-typing.
	# We should not care about it's type if it's capble of quack() and fly().
	if isinstance(thing, Duck):
		thing.quack()
		thing.fly()
		print("\n")
	else:
		print("This has to be Duck")

d = Duck()
p = Person()

quck_and_fly_one(d)
quck_and_fly_one(p)


print("-------- Duck typing, But not pythonic (since we are using LBYL) ---------")

def quck_and_fly_two(thing):
	#LBYL(Look Before You Leave) : Non-pythonic styple
	if hasattr(thing, 'quack'):
		if callable(thing.quack):
			thing.quack()

	if hasattr(thing, 'fly'):
		if callable(thing.fly):
			thing.fly()
	print("\n")
	

d = Duck()
p = Person()

quck_and_fly_two(d)
quck_and_fly_two(p)
	 

print("---------------- Pythonic way(both duck typing and EAFP)-------------")               
            

def quck_and_fly_three(thing):
	try:
		thing.quack()
		thing.fly()
		thing.wrong()
	except AttributeError as e:
		print(e)


d = Duck()
p = Person()

quck_and_fly_three(d)
quck_and_fly_three(p)


print("------------- One more example---------------------")

#mydict = {'name':'JAI', 'age':28, 'emailid':'jayashankara.dm@gmail.com'}
mydict = {'name':'JAI','emailid':'jayashankara.dm@gmail.com'}
#Non-Pythonic style , Since we are LBYL
if 'name' in mydict and 'age' in mydict and 'emailid' in mydict:
	print("name:{0} age:{1} emaild:{2}".format(mydict['name'], mydict['age'], mydict['emailid']))
else:
	print("Keys are not present")


#pythonic style 

try:
	print("name:{0} age:{1} emaild:{2}".format(mydict['name'], mydict['age'], mydict['emailid']))
except KeyError as k:
	print("Key {} is missing".format(k))

print("------------ List example------------")
#mylist = [1,2,3,4,5,6,7]
mylist = [1,2,3,4]

#Non-pythonic style
if len(mylist) >= 6:
	print(mylist[5])
else:
	print("IndexError found")

#pythonic --> EAFP
try:
	print(mylist[5])
except IndexError as ind:
	print("Index error:{}".format(ind))






