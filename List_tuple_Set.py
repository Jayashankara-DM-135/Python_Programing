"""
List : Mutable , Menas we can change the value of list. Hence list is mutable.
"""
#List

#emptylist
templist = []
#or
templist = list()

print("********************************************")

mylist = ["CS", "EC", "EE", "IS"]
mylist2 = ['apple', 'Mango', 'Orange']


print(mylist)
print(mylist2)
print(mylist[1])
print(mylist[0:3])
print(mylist[-2:0])
print(len(mylist))
mylist.append("Kannada")


print(mylist)
mylist.remove("Kannada")

print(mylist)

mylist.insert(0, "Kannada")
print(mylist)

mylist.insert(3, "English")
print(mylist)


mylist2 = ['Tamil', 'Telugu']
mylist.insert(0, mylist2)
print(mylist)
print(mylist[0])

mylist3 =  ["Bengali", "Hindi"]
mylist.extend(mylist3)
print(mylist)

# remove from list using remove and pop
print(mylist)
mylist[0].remove("Tamil")
print(mylist)

mylist.remove("Bengali")
print(mylist)

#pop() will remove last element by default, Otherwise specified index
mylist.pop()
print(mylist)
mylist.pop(2)
print(mylist)
#Need to check why string sorting is not possible
#mylist.sort()
print(mylist)

numlist = [9, 7, 10, 2, 6]
print(numlist)
numlist.sort()
print(numlist)

numlist = [19, 20, 1, 82, 7]
print(numlist)
numlist.sort(reverse=True)
print(numlist)

"""
 diff between sort and sorted is:
 sort is inplace sorting ==> means modifiy the same list
 sorted will give the sorted list , Keeping the orginal as it's.
"""

numlist = [78, 99, 56, 23, 98]

numtemp = sorted(numlist)
print(numlist)
print(numtemp)



#min and max in list

print(min(numlist))
print(max(numlist))

#checking index of value
print(numlist)
print(numlist.index(99))
print(mylist.index("EC"))

#check for existance
print("EC" in mylist)


#printing list one by one
for language in mylist:
	print(language)

print("============================")
for index, language in enumerate(mylist):
	print(index, language)
print("==============================")
#start say index should be start from that number
for index, language in enumerate(mylist, start=1):
	print(index, language)


mylist = ['AB', 'CD', 'EF', 'XY']

#convert list into comma separated string
print(mylist)
tempstr = ','.join(mylist)
print(tempstr)

#Create llist from string
templist = tempstr.split(',')
print(templist)
