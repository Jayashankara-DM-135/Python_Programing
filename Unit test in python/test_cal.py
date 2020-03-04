"""
Test utility to test cal.py module
"""

import unittest
import cal

class TestCalc(unittest.TestCase):
	def test_add(self): #method name should be start with 'test_'
		self.assertEqual(cal.add(10,5), 15)
		self.assertEqual(cal.add(-1, 1), 0)
		self.assertEqual(cal.add(-1, -1), -2)
		self.assertEqual(cal.add(-1, 0), -1)

	def test_sub(self):
		self.assertEqual(cal.sub(10,5), 5)
		self.assertEqual(cal.sub(-1, 1), -2)
		self.assertEqual(cal.sub(-1, -1), 0)
		self.assertEqual(cal.sub(-1, 0), -1)
	
	def test_mult(self):
		self.assertEqual(cal.mult(10,5), 50)
		self.assertEqual(cal.mult(-1, 1), -1)
		self.assertEqual(cal.mult(-1, -1), 1)
		self.assertEqual(cal.mult(-1, 0), 0)
	
	def test_div(self):
		self.assertEqual(cal.div(10,5), 2)
		self.assertEqual(cal.div(-1, 1), -1)
		self.assertEqual(cal.div(-1, -1), 1)
		self.assertEqual(cal.div(5, 2), 2.5)
		#How to check divisible by zero
		#1st way of doing
		#self.assertRaises(ValueError, cal.div, 10, 0)

		#2nd way using context manager:
		#It is best of way of doing it 
		with self.assertRaises(ValueError):
			cal.div(10, 0)
		


if __name__ == '__main__':
	unittest.main()

