"""
Iterators: One which knows it's state by it's self.
           Object which supports next() will be called as iterator since with help of next() method
           object can gets it's next state.
	   Once it reached the end , further call to next() will throw StopIteration exception.
	   Note: 
	    --> We can use for loop for iterator as well.
	    --> Only once we can acccess the element, we can repeatlty access the Iterator object, It will through StopIteration exception.
	   
Iterable:  Object which can be loop through is called iterable.
           I mean object which is having __iter__()(special method) is called iterable.
	   next() will not work on iterable, Sicne it does not keep the current state.
	   We can access the element as many time as possible , No restictation on that since it does not know the current state.
"""

#Note: Iterator is object which knows it's state while iterating.
#List is iterable , but not iterator
num = [1, 2, 3]
print(dir(num))

#List is not Iterators, Hence next() will not work on list
print(next(num))  #TypeError: 'list' object is not an iterator

#List is iterable since it has special method called __iter__
for i in num:
	print(i)

print("===== Make List is iterator=====")

# Get iterator object, Which will have __iter__ and __next__ special methods
i_num = iter(num)

#Now i can i_num as iterator
print(next(i_num))
print(next(i_num))
print(next(i_num))

print("====== Loop through ================")
#Here we already reached the end of the list since we used next(i_num) just above , Hence it will not print anything.
for i in i_num:
	print(i)

#if we want to print from begining, get iterator object again
print("===== Loop through again==========")
i_num = iter(num) # Here we got iterator object which is having next() method and iter() method as well
for i in i_num:
	print(i)


"""
Note: When we use next() to iterate the object, We should be carefull about end of the object, Otherwise it will throw
      StopIteration exception.
"""
#Here also exception thrown, since for loop will internally use next() to get the next value. At the end of the for loop we have
#     already reached the end of the object.
#print(next(i_num))

#This will not print anything since we alredy reached end of the iterator object. But it want show any exception beacuse internal
# implemenation of for loop will cacth the StopIterar exception.
for i in i_num:
	print(i)


print("==== Now let see how for loop is implemented internally ==========")

i_num = iter(num)
while True:
	try:
		print(next(i_num))
	except StopIteration:
		break

print("========== Let see how make class is iteratable==================")

"""
Implement the rang(1, 10) method and support iterator for the same.

To implement our own iterator, We need to implemet __iter__ and __next__ method
"""

class MyRange:
	def __init__(self, start, end):
		self.value = start
		self.end = end

	def __iter__(self):
		return self  #Just return we don't want to with it iter()

	def __next__(self):
		if self.value >= self.end:
			raise StopIteration
		current_val = self.value
		self.value += 1
		return current_val

nums = MyRange(1,5)

#Using for loop
for num in nums:
	print(num)

#using next()
nums = MyRange(1,5)
print(next(nums))


print("======================== Generator =====================")
"""
Generator are iterator and iteratable , So we no need add our own __next__ and __iter__ methods
"""

def my_range(start, end):
	current = start
	while current <= end:
		yield current
		current += 1

nums = my_range(1, 10)

#using for loop
for num in nums:
	print(num)


#using next()
nums = my_range(1, 10)
print(next(nums))
print(next(nums))


