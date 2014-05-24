import unittest

from finances.base import _Base

class TestBase(unittest.TestCase):
	def test_positive_annual(self):
		"""Check positive annual value is normalised correctly.
		
		This test shows the frequency breakdown is correct."""
		obj = _Base('test', 52, 'annual')
		self.assertEqual(obj.name, 'test')
		self.assertEqual(obj.annual, 52.0)
		self.assertEqual(obj.monthly, 52.0/12)
		self.assertEqual(obj.weekly, 1.0)

	def test_negative_annual(self):
		"""Check negative annual value is converted to positive."""
		obj = _Base('test', -52, 'annual')
		self.assertEqual(obj.weekly, 1.0)

	def test_positive_monthly(self):
		"""Check positive monthly value is correct."""
		obj = _Base('test', 12, 'monthly')
		self.assertAlmostEqual(obj.weekly, 2.77, 2)

	def test_negative_weekly(self):
		"""Check a negative weekly value is correct."""
		obj = _Base('test', -2, 'weekly')
		self.assertAlmostEqual(obj.monthly, 8.67, 2)

if __name__ == '__main__':
	unittest.main()
