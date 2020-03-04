# It take zero or more argumnets
def fun1(*args):
    for arg in args:
        print(arg)

fun1('one')
print("="*10)
fun1('one', 'two')
print("="*10)
fun1()
print("+"*40)

# It takes one or more arguments
def fun2(arg1, *args):
    print(arg1)
    for arg in args:
        print(arg)


fun2('one')
print("="*10)
fun2('One', 'two')
print("="*10)
fun2('One', 'two', 'three')
print("="*10)
#fun2() ==> missing 1 required positional argument: 'arg1'
print("="*10)

print("+"*40)

""" This will at least two parameter and max can be anytrhing"""
def fun3(arg1, arg2, *args):
    pass

print("+"*40)


""" Kwargs: Key word args, It will take name of the arg and it's value"""
# Double ** here is to represent the dictonory
def fun4(**kwargs):
    for key, value in kwargs.items():
        print("{} == {}".format(key, value))
        print("%s == %s" %(key, value))  #another way of printing

    print("Done")

fun4(arg1="Hello", arg2="Surya", arg3="Welcome")
fun4(arg1=1, arg2=2, arg3=3)
fun4()

print("*"*10)
""" One fixed args and any number key wors args"""
def fun6(arg1, **kwargs):
    print("arg1: {}".format(arg1))
    for key, value in kwargs.items():
        print("{} == {}".format(key, value))
    print("Done fun6")

fun6("heloo", name="Sury", lastname="DM")

""" Combination of *args and **kwargs :
This will first take varible number of unnmaed arguments followed by any number of named argumntes
"""

def fun7(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print("{} == {}".format(key, value))

    print("Done with -{}".format(fun7.__name__))


print("+"*40)
fun7()
fun7('1', '2', '3', arg4='one', arg5='two', arg6='three')


""" Way of passing mutiple args to function """
# This fun takes exactely 3 args
def fun8(arg1, arg2, arg3):
    print("arg1 = {}".format(arg1))
    print("arg2 = {}".format(arg2))
    print("arg3 = {}".format(arg3))

fun8(1, 2, 3)

args = (1, 2, 3)
fun8(*args) # This will expanded before calling . It looks like fun8(1, 2, 3)

kwargs = {'arg1' : 'one', 'arg2': 'two', 'arg3': 'three'}
fun8(**kwargs) # This will expanded to fun8(one, two, three)

fun8(*kwargs) # This will expanded to fun8(arg1, arg2, arg3)

