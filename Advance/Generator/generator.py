"""
Generator => Which will not create any object on memory untill you ask for next.
             Where as list will have memory for all the object it holds.
"""

#Lets return squre of list of given number using List
def list_squre(nums):
	result = []
	for num in nums:
		result.append(num*num)
	return result

res = list_squre([1,2,3,4,5])
print(res)

print("-------------- Generator------------------")
#Now try above program with generator

def generator_squre(nums):
	for num in nums:
		yield(num*num)

res = generator_squre([1,2 ,3,4, 5])

#It does not hold all the result in memory, It will wait for ask for next value. Hence it's prints only object information
print(res)

print("---- Ask to print next values----------")
"""
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
"""
#if we try to access outside of the scope , will get stopIterartion error.
#print(next(res)) 
print("------------- Iterate the generator----------")

for num in res:
	print(num)


print("==============List compression for above generator funcation ====================")
"""
List compresion for above gererator funcation

def generator_squre(nums):
	for num in nums:
		yield(num*num)

res = generator_squre([1,2 ,3,4, 5])

This above code is equivalent to below line of code using list compresion.
"""


res =[x*x for x in [1, 2, 3, 4, 5]]
#This is list, Which means it holds memory for all the results
#prints all the results.
print(res)

# Below is code for above list comprestion (In single line of code for generator)
res =(x*x for x in [1,2,3,4,5])
#It prints only generator object info
print(res)

#ask for next value , which will creates the memory and holds result in it.
for i in res:
	print(i)

#in case if want to print out all all values of generator without iterating/next,then convert the generator into list.
res =(x*x for x in [1,2,3,4,5])
print(list(res)) # this performance penalty




