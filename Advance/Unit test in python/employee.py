"""
class employee
"""

import requests

class Employee:
	raise_ammount = 1.0

	def __init__(self, fname, lname, pay):
		self.fname = fname
		self.lname = lname
		self.pay = pay

	@property
	def fullname(self):
		return '{} {}'.format(self.fname, self.lname)
	
	@property
	def emailid(self):
		return '{}.{}@gmail.com'.format(self.fname, self.lname)
	
	def apply_raise(self):
		self.pay = (self.pay*self.raise_ammount)
	
	def monthly_schdule(self, month):
		response = requests.get(f'http://company.com/{self.lname}/{month}')
		if response.ok:
			return response.text
		else:
			return 'Bad Response!'


	

	