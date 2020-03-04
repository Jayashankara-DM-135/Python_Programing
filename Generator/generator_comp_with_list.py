"""
Generator is better than List with respect performance in termes of memory and speed
"""

import mem_profile
import random
import time

names = ['Raina', 'Dohni', 'Kohili', 'Rohit']

print("Memory before {}Mbs".format(mem_profile.memory_usage_resource()))

def people_list(num_people):
	result = []
	for i in num_people:
		person = {
			'id':i,
			'name':random.choice(names)
		}
		result.append(person)
	return result

def people_generator(num_people):
	for i in num_people:
		person = {
			'id':i,
			'name':random.choice(names)
		}
		yield person

t1 = time.clock()
people = people_list(1000)
t2 = time.clcok()

t1 = time.clcok()
people = people_generator(1000)
t2= time.clcok()

print('Memory usage after {}Mbs'.format(mem_profile.memory_usage_resource()))
print("Took {} secs".format(t2-t1))




