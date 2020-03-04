"""
Sorting :
"""
print("************************ List sorting ***********************")
li = [9,7, 3, 8, 5, 6, 2, 1]

#in-place sorting with acescending order
li.sort()
print(li)

del li

#in-place sorting with descending order
li = [9,7, 3, 8, 5, 6, 2, 1]
li.sort(reverse=True)
print(li)
print("================Key========")

li = [-9, -3, 4, 5]
li.sort(key=abs)
print(li)
print("======== End ================")

#sorting accesnding order
li = [9,7, 3, 8, 5, 6, 2, 1]
temp_li = sorted(li)
print(temp_li)

#sorted with descending order
li = [9,7, 3, 8, 5, 6, 2, 1]
temp_li = sorted(li, reverse=True)
print(temp_li)

#sort based on absolute values
li = [-6, 3, 0, -7, 8, 2]
temp_li = sorted(li, key=abs)
print(temp_li)
li.sort(key=abs)
print(li)



print("********************** Tuple Sorting *******************************")

ti = (7, 3, 8, 2, -1, 1 ,0)
print(ti)
#ti.sort() in-place sorting is not supported , Since tuple is immutable.
#print(ti)

temp_ti = sorted(ti)
print(temp_ti)

temp_ti = sorted(ti, reverse=True)
print(temp_ti)
temp_ti = sorted(ti, reverse=True, key=abs)
print(temp_ti)

print("********************* Dictionary sorting *****************************")

dic = {'Name':'Jayashankara', 'Job':'Software', 'age':28, 'DOB':'1990-June-02'}
print(dic)
#dic.sort(), In-place sorting is not supported
#print(dic)

temp_dic = sorted(dic) #sorts only Keys
print(temp_dic)


print("********************** Object sorting ************************************")

#How to sort objects of the same class
"""
Three way of doing this:
1> Defining your own custom lambda function
2> Using lambda function
3> Using operator attrgetter()
"""

class Empolyee:
	def __init__(self, first, last, salary):
		self.first = first
		self.last = last
		self.salary = salary

	def __repr__(self):
		return ("({} {}, ${})".format(self.first, self.last, self.salary))

E1 = Empolyee("Jayashankara", "DM", "11000")
E2 = Empolyee("Savitha", "DM", "1000")
E3 = Empolyee("Poornima", "C", "10000")

emp_list = [E1, E2, E3]

#emp_list.sort(key=salary)  This key will not work , Hence we need to write our own key function for sorting based on that

#custom key function

#Using our own lambda function
def emp_sort(emp):
	return emp.first

temp_emp_list = sorted(emp_list, key=emp_sort)
print(emp_list)
print(temp_emp_list)


#try sorting based on salary, This function is called as lambda function.

def emp_sort_salary(emp):
	return emp.salary

temp_emp_list = sorted(emp_list, key=emp_sort_salary, reverse=True)
print(temp_emp_list)

print("----------------------------------------")
# Using lambda function
temp_elist = sorted(emp_list, key=lambda emp:emp.first)
print(temp_elist)
temp_elist = sorted(emp_list, key=lambda emp:emp.last, reverse=True)

print("--------------------------------------")
#Using operator attrgetter()
from operator import attrgetter
temp_elist = sorted(emp_list, key=attrgetter('salary'))
print(temp_elist)
