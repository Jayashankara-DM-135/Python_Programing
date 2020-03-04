"""
List comprehension:
"""

print('-------- copy list ----------------')

nums = [1, 2, 3, 4, 5]
mylist = []

for num in nums:
	mylist.append(num)

print(mylist)

#Now try above thing using list compreshion

nums = [10, 20, 30, 40, 50]
mylist2 = [n for n in nums]
print(mylist2)


print('-------------- Get squre of nums into mylist --------')

mylist3 = [n*n for n in nums]
print(mylist3)

print('---- using lamabda and map ---------------')
mylist4 = map(lambda n: n*n, nums)
print(mylist4)

for i in mylist4:
	print(i)

print('-----i want n for each n in nums if n is even --------')

nums = [1, 2, 3, 4, 5]
mylist=[]
for n in nums:
	if (n%2 == 0):
		mylist.append(n)
print(mylist)

mylist5 = [n for n in nums if n%2 == 0]
print(mylist5)

print('---- Filter and lambda function -------')
mylist6 = filter(lambda n: n%2 == 0, nums)
print(nums)
print(list(mylist6))

print('---------need (letter, num) pari for each letter in "abcd"  and each num in muber "0123"-----')

mylist7 = []
for let in 'abcd':
	for n in range(4):
		mylist7.append({let, n})
print(mylist7)

mylist8 = [{let, n} for let in 'abcd' for n in range(4)]
print(mylist8)

print("=================== End of List comprehension================")


print('----------- Dictionary comprehension -------------------------')

names = ['Raina', 'Dohni', 'Virat', 'Dinesh K']
teams = ['CSK', 'CSK', 'RCB']

print(zip(names, teams))

mydictionary = {}
for name, team in zip(names, teams):
	mydictionary[name] = team

print(mydictionary)


my_dict = {name:team for name, team in zip(names, teams)}
print(my_dict)

#Let say i don't RCB player then

my_dict = {name:team for name, team in zip(names, teams) if team!='RCB'}
print(my_dict)


print("--------------- End of dictionary comprehension -----------------")


print("------------------ SETS comprehension ----------------------")
#Set unordered list, Means dupicates is not allowed.

nums = [1, 2, 3, 1, 2, 4, 5, 2]
#print(nums)
#Now convert this list into sets

my_sets = set()
for i in nums:
	my_sets.add(i) #append is not supported
print(my_sets)

mysets = {n for n in nums}
print(mysets)



print('---- Generator expression -------')
#Note: Generator expression is simillor to List comprehension

nums = [1, 2, 3, 4, 5]
# i want N*N for each N in nums using generator


def list_squre(nums):
	mylist = []
	for n in nums:
		mylist.append(n*n)
	return mylist
listtmp = list_squre(nums)
print(listtmp)

#Now use generator

def generator_squre(nums):
	for n in nums:
		yield(n*n)

listtmp2 = generator_squre(nums)
print(listtmp2)
#print(next(listtmp2))
for n in listtmp2:
	print(n)

#Note : use brace not braket
my_gen = (n*n for n in nums)
for n in my_gen:
	print(n)
