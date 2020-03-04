""" Difference between map and filter:
    Map: Will inovke specifed routine for each item in list and contrsuct a new map object which contins all the return value of all the invoke.
    Filter: Will invoke specified routine for each ithem in the list and construct a new filtter object whic contins all the elements item in list which
            are evaluated as a true.
"""

def squre(n):
    return n* n

num1 = [1, 2, 3, 4]
res1 = map(squre, num1)

print(res1)
print(list(res1))
#for i in res1:
#    print(i)

res2 = filter(squre, num1)
print(res2)
print(list(res2))


def evennumber(n):
    return n%2 == 0

num2 = [1, 2, 3, 4]

res3 = map(evennumber, num2)
res4 = filter(evennumber, num2)
print(list(res3))
print(list(res4))
num3 = {2,8, 9, 11, 12, 13}
res5 = map(evennumber, num3)
res6 = filter(evennumber, num3)
print(list(res5))
print(list(res6))

