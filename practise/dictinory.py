student = {}
print(student)
#print(help(student))
student.update({1:"Hi", 2:"Hello", 3:"ABCD"})
print(student)
student[1] = "WoW"
print(student)
items = dict()
print(items)


print("+++++++++")
print(student.get(1))
print(student.get(2))
print(student.get(3))
print(student.get(4))
print(student.get(5, "Not found"))
print(student.get(5))

#print(help(items))

del student[1]

student.update({'courses':['CSE', 'EC', 'EEE']})
#del student
item = dict(student)
print(student)
print(item)

if id(student) == id(item):
    print("Both are refereing same")
else:
    print("Both are different entires")

print(id(student))
print(id(item))


print(student)

for key in student.keys():
    print(key)

print()
print(student.keys())
print(student.values())
print(student.items())

for value in student.values():
    print(value)


for key, value in student.items():
    print("{0}->{1}".format(key, value))



print(student)
#print(student.pop('courses'))
print(student)
#print(student.pop(2))
print(student)

#print(dir(item))
print("+++++++++")
print(student.popitem())
print(student)
print(student.popitem())
print(student)
print(student.popitem())
print(student)


