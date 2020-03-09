"""
SETS: unordered list , Means duplicates are not allowed and it's immutable(Non allowed to change)
"""

# Duplicates removed silientely
mysets = {"Math", "Histroy", "Computer", "Graph", "Math", "DS"}
print(mysets)

mysets1 = {"Math", "Electronics", "DS"}

print(mysets1)

# Check which are comman item
print(mysets.intersection(mysets1))

# Check union of two SETS
print(mysets.union(mysets1))

# Check set1 is how different from set2
print(mysets.difference(mysets1))


# Crete empty set
tempset = set()

# Don't use below option, that is for dictonary
tempset = {} #It will became a dict




