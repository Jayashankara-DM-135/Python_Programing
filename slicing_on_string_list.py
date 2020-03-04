"""
Slicing on string and list
"""

#list
my_list = [0, 1, 2, 3, 4, 5]

print(my_list[0])
print(my_list[4])
print(my_list[-2]) #prints form back end of the list
print(my_list[-0]) # Since there is no negative zero it is tread as zero

#negative index is -5 to -1 in above example

#list[start:end:step]
# end is not included

mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(mylist[0:10:2])
print(mylist[2:10:1])
print(mylist[-10:-1:2])
print(mylist[0:-2])

print(mylist[0::-1])
print(mylist[:-1:3])
print(mylist)

print(mylist[::-1])

print("**********************************Slicing *******************************************")

#string slicing

url = "www.google.com"
print(url)
revurl = url[::-1]
print(revurl)
print(url[::-1])

print (url[-4:])
