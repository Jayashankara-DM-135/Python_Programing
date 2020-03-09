"""
Mutable vs Immutable
Mutable : Chanable 
Im-mutable : Not chanable

Mutbale Example: List
Immutable Example: String, Tuple, Dict
"""

# 1st tmp is here two different object
tmp = "Hello"
print(tmp)
print("Address of tmp is {0}".format(id(tmp)))

tmp = "Jayashnakara"
print("Address of temp is {0}".format(id(tmp)))

# 2nd Now modifiy tmp
print(tmp)
tmp[0]='S' # Not supported , since string is immutable 
print(tmp)

