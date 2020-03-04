import sys;

print("difference between == and is")

# ==: will compare the value of object
# is : will compare the two object are refereing same memory location or not

l1 =[1,2,3,4,5]
l2 = [1, 2, 3, 4, 5]

if l1 == l2:
    print("==: Both l1 and l2 are equal")
else:
    print("==: Both l1 and l2 are not equal")

k1 = [1, 2, 3, 4, 5]
k2 = [1, 3, 4, 5]

if k1 == k2:
    print("==: Both k1 and k2 are equal")
else:
    print("==: Both k1 and k2 are not equal")


l1 =[1,2,3,4,5]
l2 = [1, 2, 3, 4, 5]
l3 = l1

if l1 is l2:
    print("True")
else:
    print("false")

if l3 is l1 :
    print("True")
else:
    print("False")


print("Memory address of object")
print(id(l1))
print(id(l2))
print(id(l3))

l1[3] = 20
print(l1)
print(l2)
print(l3)



