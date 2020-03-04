"""
Tuple: imutable : Means read-only, we can't change.
"""

mytuple = ('HAL', 'BEL', 'BHEL', 'ISRO')
print(mytuple)

#try to modify , It will not be allowed "tuple object does not support item assignment"
#mytuple[0] = "DRDO"
print(mytuple)


#Note: Rest of the operations is similar to List

#empty tuple

temptuple = ()
#or
temptuple = tuple()
