"""
SETS:unordered list , Means duplicate is not allowed and it's immutable
"""

#Duplicates removed silientely
mysets = {"Math", "Histroy", "Computer", "Graph", "Math", "DS"}
print(mysets)

mysets1 = {"Math", "Electronics", "DS"}

print(mysets1)

#check which are comman item
print(mysets.intersection(mysets1))

#check union of two SETS
print(mysets.union(mysets1))

#check set1 is how different from set2
print(mysets.difference(mysets1))


#Crete empty set
tempset = set()

#don't use below option, that is for dictonary
tempset = {} #It will became a dict




