"""
itertools module: Iterator funcation for efficent looping
"""

import itertools

print("================ itertools.count() demo=============")
#By default itertool.count() starts from zero to infinity
counts = itertools.count()
print(counts)
print(next(counts))
print(next(counts))

#We can specify the start and step as well
counts = itertools.count(start=-5, step=-2)
print(next(counts))
print(next(counts))
print(next(counts))

#we can traverse back and we can use flot value as well

counts = itertools.count(start=100, step=2.5)
print(next(counts))
print(next(counts))


#Real time example is provide index to some list

fruits = ['applez', 'orange', 'mango']
counts = itertools.count()

#zip will consider the shortest iterable
output = list(zip(itertools.count(), fruits))
print(output)


#itertools.zip_longest will iterable till longest iterable
#for remaing entries in shortest iterable will be filled with 'None'
output = list(itertools.zip_longest(range(10), fruits))
print(output)



print("====================== itertools.cycle() demo==========================")

nums = [1, 2, 3]

counts = itertools.cycle(nums)

print(next(counts))
print(next(counts))
print(next(counts))

print(next(counts))
print(next(counts))
print(next(counts))

#if we use for loop for loop over, It will never get terminated and it will leads overflow.

counts = itertools.cycle(('on', 'off'))
print(next(counts))
print(next(counts))
print(next(counts))
print(next(counts))
print(next(counts))
print(next(counts))


print("===================== itertools.repeat() demo ==============")
nums = [10, 20, 30]
counts = itertools.repeat(nums) #will always repaet the same value/list/tuple/dictionary
print(next(counts))
print(next(counts))
print(next(counts))
print(next(counts))
print(next(counts))
print(next(counts))

counts = itertools.repeat(2)
print(next(counts))
print(next(counts))
print(next(counts))
print(next(counts))
print(next(counts))
print(next(counts))

print('-------')
# after 'times' times it will through StopIteration exception
counts = itertools.repeat(2, times=2)
print(next(counts))
print(next(counts))
#print(next(counts))
#print(next(counts))
#print(next(counts))
#print(next(counts))


print("===== List out first 10 numbers squre uisng map ===========")


squeres = map(pow, range(10), itertools.repeat(2))
print(list(squeres))

squeres = map(pow, range(10), itertools.cycle([1, 2]))
print(list(squeres))

squeres = map(pow, range(10), itertools.count(start=1))
print(list(squeres))

print("========= itertools.starmap() demo=============")
#starmap will take the tuples as arguments instead iterators

#prints fist 3 numbers squre
squeres = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2)])
print(list(squeres))



print("=========== Permutation and Commbination demo================")
#combinations : Order matters
#Permutation: Order does not matters

alpha = ['a', 'b', 'c', 'c']
comb = itertools.combinations(alpha, 2) # group of two letters
print(list(comb))

perm = itertools.permutations(alpha, 2)
print(list(perm))


print("=================== itertools.product() demo ================")
nums = [0, 1, 2, 3]
#Gives out arangement of nums
res = itertools.product(nums, repeat=4)

for i in res:
	print (i)


print("============ Combination with replacement==================")
nums = [0, 1, 2, 3]
res = itertools.combinations_with_replacement(nums, 4)

for i in res:
	print(i)



print("============== Iterat over mutiple collections ==================")
nums = [1, 2, 3, 4]
alpha = ['a', 'b', 'c']
names = ["Jai", "Raina", "Dravid"]

# This is bad way of doing, Since it consumes lots of memory to combine.
combined = nums + alpha + names

for i in combined:
	print(i)

print("===== Use itertools.chain()=============")

combined = itertools.chain(nums, alpha, names)

#first nums, alpha and the names, depends on order in which specifed in chain()
for i in combined:
	print(i)


print("============= Iterator slicing ===============")
#When we want get the part of list/tuple/dict/sets

#only end is specified : 5
res = itertools.islice(range(10), 5)

for i in res:
	print(i)

#both start and end 1 and 5 respectively, if no start then second arguments is considered as end.
res = itertools.islice(range(10), 1, 5)

for i in res:
	print(i)


# start, end and step is specified
res = itertools.islice(range(10), 1, 5, 2)
for i in res:
	print(i)

"""
list slicing vs i-slicing:

i-slicing is very helpfully when we want perform slicing on logs file, Which we don't want to
store in list and then do slicing. 
"""

#file are iterator: when we call next on file it move to next line.
with open('logs.txt', 'r') as fr:
	res = itertools.islice(fr, 3) #read first 3 lines

	for line in res:
		print(line, end='')

print("================== itertools.compress()=====================")
"""
copmpress v/s in-build 'filter':

filter will use method to determine true or flase, Where as compress take those values as a pameters.
"""

#compress example
nums = [0, 1, 2, 3, 4]

selector = [True, False, True, False, True]

#It will select only True entries
res = itertools.compress(nums, selector)
for i in res:
	print(i)

#Now how fliter works

def check_even(num):
	if num%2 == 0:
		return True
	return False

nums = [0, 1, 2, 3, 4]

print('====')	
res = filter(check_even, nums)
for i in res:
	print(i)

#use itertool.filter
print('===')
res = itertools.filterfalse(check_even, nums)
for i in res:
	print(i)

print("================= dropwhile() demo============")


nums = [0, 1, 2, 3, 4, 5, 6]

def even_check(num):
	if num%2 == 0:
		return True
	return False


#drops till it gets False 
res = itertools.dropwhile(even_check, nums)
for i in res:
	print(i)

print('------')
#takes it till it gets first False
res = itertools.takewhile(even_check, nums)
for i in res:
	print(i)


print("================== accumalate() demo==============")

nums = [1, 2, 3, 5, 6, 9]
#adds it's previous sum to it's value.
res = itertools.accumulate(nums)
for i in res:
	print(i)

#Lets say i want take mutiplication but not sum.
import operator
nums = [1, 2, 3, 5, 6]
res = itertools.accumulate(nums, operator.mul)
for i in res:
	print(i)

nums = [1, 2, 3, 5, 6]
res = itertools.accumulate(nums, operator.sub)
for i in res:
	print(i)


print("======= Groupby() demo ============")

"""
Groupby needs list to be sorted , I mean all state 'NY' in below example should be in sequence.
"""
people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]


def getkey(person):
	return person['state']

result = itertools.groupby(people, getkey)

#Group based on state
for key, group in result:
	print(key)
	for per in group:
		print(per)
#count number of people in each group
result = itertools.groupby(people, getkey)
for key, group in result:
	print(key, len(list(group)))


print("==============tee demo ====================")
#replicate the iterators using tee()

copy1, copy2 = itertools.tee(person)

#Now copy1 and copy2 are copy of person .after tee() we will not able to use orginal person iterator.










