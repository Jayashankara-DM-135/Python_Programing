"""
special funcations in python:
__init__ => Get called when class initance is created
__str__ => meant to print in the human undersnatbale format, Does not care about unambigus : Used for debug purpose
__repr__ ==> meant to print the content in unambigus way, Means prints in programing language format, so that output of __repr__ can be used
             directely in program : Used for programer
"""

import datetime
import pytz

a = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

b = str(a)


print ("str(a): {}".format(str(a)))
print ("str(b): {}".format(str(b)))


print ("repr(a): {}".format(repr(a)))
print ("repr(b): {}".format(repr(b)))


