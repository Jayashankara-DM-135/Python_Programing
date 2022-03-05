"""
SETS: 
   1> unordered list.
   2> Duplicates are not allowed 
   3> Sets it self is mutable, But value inside SET are imutable. 
      Example: 
          myset = set() # #empty set
          myset.add(10) # We add new , means set is mutable
          myset.update([20, 30]) # Now add many elements sets.
          myset2 = {40, 50}
          myset.update(myset2) # Now set got updated few more elements.
          print(myset)  # 10, 20, 40, 30, 50 , We can see here order is not guranted.
          
          But,
          print(myset[0]) # TypeError: 'set' object is not subscriptable
          myset[0] = 100  # TypeError: 'set' object is not subscriptable
      
   
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




