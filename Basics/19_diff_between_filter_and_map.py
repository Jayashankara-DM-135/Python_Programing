"""
map: Calls funcation for all the object in list and returns list of return values of each call
filter: Calls funcation for all the object in list and
       create a new list with all objects that return True in that function
"""

def squre(n):
    return n*n

nums =[1, 2, 3, 4]
newlist = map(squre, nums)

print(nums)
print(newlist)
#print(next(newlist))
#print(next(newlist))
print(id(nums))
print(id(newlist))
print(list(newlist))

nums2 = [1, 2, 3, 4]
newlist2 = filter(squre, nums)

print(nums)
print(newlist2)
print(list(newlist2))

"""
Above function is evalutes to below form for filter()

def squre(n)
    return n*n !=0  // return n for n*n is not equal to zero

"""


print("==================================")

def evennum(n):
    return n%2 == 0

num = [1, 2, 3, 4]
newlist3 = map(evennum, num)
print(num)
print(list(newlist3))

newlist4 = filter(evennum, num)
print(num)
print(list(newlist4))


print(dir(newlist2))
print(dir(newlist))

