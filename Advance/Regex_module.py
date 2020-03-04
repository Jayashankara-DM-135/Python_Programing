"""
Regular expression:
"""

import re

#Raw string will not interrupt the special charcter like \n \t.
#It just treat that as a part of the string

print('\tTab')
print(r'\tTab') #raw string

text_to_search = '''
ab bc cdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa HaHa Ha
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
bat
mat
mat
'''


sentence = 'Star a sentence and then bring it to an end'


print("------ Simple text serch using re(Regular expression) module-----------")
#case-sensitive
print("====Example1====")
pattern = re.compile(r'abc')
matches = pattern.finditer(text_to_search)

for match in matches:
	print(match)
#print(text_to_search[1:4])


print("======== Example2=====")

pattern = re.compile(r'\.')
matches = pattern.finditer(text_to_search)

for match in matches:
	print(match)

print("====Example 3 : serach for email id===========")
pattern = re.compile(r'coreyms\.com')

matches = pattern.finditer(text_to_search)

for match in matches:
	print(match)


print("=====ex4: search for digits ===========")
pattern = re.compile(r'\d')
matches = pattern.finditer(sentence)
for match in matches:
	print(match)


print("===========ex5: ==============")
string = "oen two three"

pattern1 =re.compile(r'\btwo\b')
matches1 = pattern1.finditer(string)
for math1 in matches1:
	print(math1)

# we can also serach like below
x= re.search(r'\btwo\b', string)
print(x)


print("======== Ex6: search beging of the string===========")
mysetence = "H Hello world program"

pattern = re.compile(r'^\bHello\b')
matches = pattern.finditer(mysetence)

for match in matches:
	print(match)

print("=======================================================")
pattern = re.compile(r'^a')
matches = pattern.finditer(sentence)

for match in matches:
	print(match)

print("========= Search at the end of string ==============")
mystring = "Hello world program"
pattern = re.compile(r'program$')
matches = pattern.finditer(mystring)

for match in matches:
	print(match)

print("===== Find out phone nuber =====")
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
matches = pattern.finditer(text_to_search)

for match in matches:
	print(match)

print("======== Seach in file ========")
with open('regex_input_data.txt', 'r') as fr:
	contents = fr.read()

	matches = pattern.finditer(contents)
	for match in matches:
		print(match)

print("========== Character set ============")
#using character set we can specify which character we want to match
#in above exampple .(period) will macth all the charcter execept \n.
#We want only . and - to be accepted as part of phone number , but not other character.

#charcter set will match either .(period) or -(dash) but not both
# means only one charcter in character set
pattern = re.compile(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d')

matches = pattern.finditer(text_to_search)

for match in matches:
	print(match)


print("====== find phone number start with 800 or 900 ============")
pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
matches = pattern.finditer(text_to_search)

for match in matches:
	print(match)



print("=========== Specifying range in chacter set ===============")
#find number having digit 1 to 5
pattern = re.compile(r'[1-5]')
matches = pattern.finditer(text_to_search)

for match in matches:
	print(match)


#find word which is having a to z character (lower case)
pattern = re.compile(r'[a-z]')
matches = pattern.finditer(text_to_search)

for match in matches:
	print(match)


pattern = re.compile(r'[1-5a-zA-Z]')
matches = pattern.finditer(text_to_search)

for match in matches:
	print(match)



print("======= Negate the character set ======")

#find number start with 1 to 5
pattern = re.compile(r'[^1-5]') # find number/charcter but not 1 to 5
matches = pattern.finditer(text_to_search)

for match in matches:
	print(match)

"""
Note :
1> pattern = re.compile(r'[^1-5]') ==> It is negate the chacter set, means find the charcter aprt form 1 to 5
2> pattern = re.compile(r'^[1-5]') ==> find the charcter/word which starts with any of the charter lies between 1 to 5
"""

print("============ Diff negating charcter set and beging ==================")
pattern = re.compile(r'[^1-9]') # find number/charcter but not 1 to 5
matches = pattern.finditer(text_to_search)

for match in matches:
	print(match)


mystring = "412 wdjd fkekfe"
pattern = re.compile(r'^[1-3]') # find number/charcter at the begining with contains 1-9
matches = pattern.finditer(mystring)
print("++++++++++++")
for match in matches:
	print(match)


print("========== simple patter serach ====================")
pattern = re.compile(r'[^bB]at') # find string ends with at and does not statrt with b or B
matches = pattern.finditer(text_to_search)

for match in matches:
	print(match)


print("=============== Quantifier ============================")

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') # find number/charcter but not 1 to 5
matches = pattern.finditer(text_to_search)

for match in matches:
	print(match)

print("==Ex: re-write above one using Quantifiers=======")

pattern = re.compile(r'\d{3}.\d{3}.\d{4}') # find number/charcter but not 1 to 5
matches = pattern.finditer(text_to_search)

for match in matches:
	print(match)

print("======== Find a patter which matches the Mr==============")
"""
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
"""
# I wnat to print names Which starts with Mr. or Mr
# Here ? marks say "Charcter before to ? , here period(.) will appers zero or more times"
pattern = re.compile(r'Mr\.?\s[A-Z]')
matches = pattern.finditer(text_to_search)

for match in matches:
	print(match)
