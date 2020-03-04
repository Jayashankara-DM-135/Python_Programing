"""
test module to text employee module:

Note: 
1> Test cases will run in random order.
2> setUp() and tearDown() will get called for each test cases.
3> setUpClass() and tearDownClass() will get called before any test case execution and once all the test cases execution is done, 
   It is not per test case. 

4> Test driven coding: Means prepare the test case before writting the software/code. 
"""

import unittest
from unittest.mock import patch
from employee import Employee 

class TestEmployee(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		print("setUpClass")

	@classmethod
	def tearDownClass(cls):
		print("tearDownClass")
	
	#This is getting called before each test case, Name of method should be setUp
	def setUp(self):
		print("setUp")
		self.emp1 = Employee('Jayashnakara', 'DM', 100)
		self.emp2 = Employee('John', 'Candi', 2000)
			
	#This is getting called after each text case
	def tearDown(self):
		print("tearDown")
		#Not used here, you can use it close the file or data base ext.
		pass

	def test_email(self):
		print("Test_email")
		self.assertEqual(self.emp1.fullname, 'Jayashnakara DM')
		self.assertEqual(self.emp2.fullname, 'John Candi')

		self.emp1.fname = 'abc'
		self.emp2.lname = 'abc'

		self.assertEqual(self.emp1.emailid, 'abc.DM@gmail.com')
		self.assertEqual(self.emp2.emailid, 'John.abc@gmail.com')
	
	def test_fullname(self):
		print("Test_fullname")
		self.emp1.fname = 'XYZ'

		self.assertEqual(self.emp1.fullname, 'XYZ DM')

	
	def test_apply_raise(self):
		print("Test apply raise")
		self.emp1.apply_raise()
		self.assertEqual(self.emp1.pay, 100)
	
	#uses mock , when we don't have control over it
	#I mean "Let say we called some API, Which is get some data from some website
	#In this if website it'self is down then we can not do anything. In such senario we have write test case
	# Just to validate whether we request right URL, URL format and not worried about website is return success response
	# or failure response"	
	def test_monthly_schedule(self):
		with patch('emplyoee.requests.get') as mocked_get:
			mocked_get.return_value.ok = True
			mocked_get.return_value.text = 'Success'
			
			schedule = self.emp1.monthly_schedule('May')
			mocked_get.assert_called_with('http://company.com/DM/May')
			self.assertEqual(schedule, 'Success')	

if __name__ == '__main__':
	unittest.main()

