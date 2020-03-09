"""
Which are evaluates to False in python:
 1> False
 2> None
 3> Zero of any numeric type
 4> Any empty sequence, example: '', (), []
 5> Any empty mapping, Exmple: {}

"""
print ('-------- True -------')
if True:
    print("A")
else:
    print*("B")

print ('------ Flase -------')
if False:
    print("A")
else:
    print("B")

print ("-------- None ---------")
if None:
    print("A")
else:
    print("B")

print ("------ Numeric varible with value zero -----")

var = 0
if var:
    print("A")
else:
    print("B")

print("------ Empty List  ------")
mylist = []
if mylist:
    print("List is not empty")
else:
    print("List is empty")

print("----- Empty Tuple ------")
mytuple = ()
if mytuple:
    print("A")
else:
    print("B")


print("----- Empty String ------")
temp =''
if temp:
    print("A")
else:
    print("B")


print("------- Empty Dictionary --------")
my_dict = {}
if my_dict:
    print("A")
else:
    print("B")
