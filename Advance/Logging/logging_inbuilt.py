"""
Python logging level:

INFO: Lowest priority
DEBUG:
WARNING:
ERROR:
CRITICAL: highest priority

By defult logging level is  WARNING.
Above WARNING is supported. INFO and DEBUG is not supported by default.
"""

import logging
#No logging file is creted , by defult it will printout on console
logging.basicConfig(level=logging.DEBUG) #we are setting logging level to DEBUG, bydefault it's warrning

#This one cretes logging file and dumps into log file which we created.
logging.basicConfig(filename='simplelog.txt', level=logging.DEBUG,
					format='%(asctime)s:%(levelname)s')


def add(x, y):
	return x+y

def sub(x, y):
	return x-y

def mult(x, y):
	return x*y

def div(x, y):
	return x/y

m = 5
n = 3

a = add(m,n)
logging.warrning("{} + {} = {}".format(m, n, a)) 

b= sub(m, n)
logging.warrning("{} - {} = {}".format(m, n, b))

c= mul(m, n)
logging.warrning("{} * {} = {}".format(m, n, c))

