"""
module.py
"""

print("Module is inserted !!!")

text = "My Module programing"

def find_pattern(to_serach, pattern):
	for ind, value in enumerate(to_serach):
		if (value == pattern):
			return ind
		
	return -1

