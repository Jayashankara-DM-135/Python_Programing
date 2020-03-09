"""
Loops and iterators:
"""

num = [10, 20, 30, 40, 50]

for i in num:
	print(i)

print("-----------------enumarate--------------")


# for ind, val  in enumerte(num):
# 	print("index :{} value:{}".format(ind, val))

for ind, val in enumerate(num):
	print("{} {}".format(ind, val))

for i in num:
	if(i == 3):
		print("Found")
		break
	else:
		print(i)

print("--------------------------------")

for i in num:
	if(i == 3):
		print("Found")
		continue
	else:
		print(i)
print("----------------------------------")

for i in num:
	for letter in 'abc':
		print(i, letter)

print("-----------------------------------")

#range(start, end, step)
#when only one input is provided, then it's consider as start from 0 to specified value

for i in range(10):
	print(i)

print("-------------------------------------")

for i in range(5, 10, 2):
	print(i)

print("--------------------------------------")
#while loop

x = 0
while x < 10:
	if x == 6:
		break
	print(x)
	x = x+2

