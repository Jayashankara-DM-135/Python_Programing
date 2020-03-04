"""
Dictionary : 
1> Key-value pair, But key should be immutable, Where as value is mutable
2> Key can be any type but immutable.
3> We can add new key , value pair to existing dictionary.
"""

student = {} #creating empty dictonary
student = {'Name':'Jayashnakara', 'age':28, 'courses':['Math', 'Computer', 'Electronics']}
print(student)

print(student['Name'])
print(student['courses'])
#print(student['Courses']) Not allowed , case sensitive.

student = {1:'Jayashankara', 2:29, 3:['Math', 'Computer', 'Electronics']}
print(student[1])

#in above example if key is not found then we will get error during compliltion.

print("--------------------------------------------------------------")
#otherway of accesing dictionary is using get() method

print(student.get(1)) #if key does not found then , It will return 'None'
print(student.get(10))
print(student.get(10, 'Not found')) # we can also add message to be printed it does not fimd it.
print(student.get(1, 'Not Found'))

print("----------------------------------------------------------------")
#change the value of dictionary
student[1] = 'Poornima'
print(student[1])

student['Addres'] = 'HAL II'
print(student)


#Update mutiple values at once
student.update({1:'Jeevan', 2:27, 'Email':'jayashankara.dm@wdc.com'})
print(student)


print("-----------------------------------------------------------------")
print(student)
del student['Email'] # Remove key 2  and it's value
print(student)
#Remove the key 3 along with it's value
student.pop(1)
print(student)


print("------------------------------------------------------------------")
print(student)
print(len(student))
print(student.keys())
print(student.values())

#both keys and values

print(student.items())

print("--------------------------------------------------------------------")
#Looping through dictinary

for key in student:
	print(key)
print("\n")
for key, value in student.items():
	print(key, value)
print("\n")

for key in student.keys():
	print(key)

for value in student.values():
	print(value)

	

