"""
test_module.py

Note: for imported modules python will serach print(sys.path)
Looks for :
1> Current directory
2> Python Enviornmnet path
3> Python library path
4> Third party packges
"""
print("------------------ First way of importing")

#before importing module add this , so that path of our module is present in sys.path
import sys
sys.path.append("/user/jaydm/Desktop/my_module")

import module as mm
course = ['Math', 'CS', 'EC']
index = mm.find_pattern(course, 'Eaaa')
print(index)
print(mm.text)

print("------------- Other way of importing---------------")

from module import find_pattern
course =['Math', 'CS', 'EC']
index = find_pattern(course, 'EC')
print(index)
#print(text) is not allowed since we have imported only find_pattern

print("----------------------- import text as well-------------------")

from module import find_pattern, text
course =['Math', 'CS', 'EC']
index = find_pattern(course, 'EC')
print(index)
print(text)

print("------------------------- Import as --------------------------")
from module import find_pattern as fp, text as txt
course = ["Math", "EC", "CS"]
index= fp(course,'EC')
print(index)
print(txt)
print("------------------- Import all --------------------")
from module import *
course =['Math', 'CS', 'EC']
index = find_pattern(course, 'EC')
print(index)
print(text)

print("------------------------sys.path--------------------")
import sys
print(sys.path)

print("----------------------importing standard lib-----------")
import random
import math

mylist = ['CS', 'EC', 'EE', 'IS']

rd = random.choice(mylist)
print(rd)
print(random.choice(mylist))

radn = math.radians(90)
print(math.sin(radn))


print("------------------------datetime calnder----------------")
import datetime
import calendar

today = datetime.date.today()
print(today)

print(calendar.isleap(2017))


print("------------------------- OS module ----------------")
import os

print(os.getcwd())

#path where os libary we can find
print(os.__file__)
print(datetime.__file__)



print