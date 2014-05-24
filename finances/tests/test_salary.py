import unittest
from finances.salary import Salary

class TestSalary(unittest.TestCase):
	"""Test the Salary class.

	The class possesses the following attributes:

	  - Pretax salary
	  - Income attributes (annual, monthly, weekly)
	  - Income tax property
	  - National insurance property
	  - Student loan property

	All these need testing and verifying for sample salaries. I'm not
	about to end up above the basic tax rate so these tests should be
	valid for salaries up to ~41,000 GBP/yr

	"""
	def test_nontaxable_salary(self):
		salary = Salary(9600)
		self.assertEqual(salary.pretax.monthly, 800.0)
		self.assertEqual(salary.income_tax, 0)
		self.assertEqual(salary.student_loan, 0)
		self.assertAlmostEqual(salary.nat_ins, 197.28, 2)

	def test_basic_rate_no_loan(self):
		"""Test a basic tax band salary with no student loan."""
		salary = Salary(19200)
		self.assertEqual(salary.pretax.monthly, 1600.0)
		self.assertEqual(salary.income_tax, 1840.0)
		self.assertEqual(salary.student_loan, 0.0)
		self.assertAlmostEqual(salary.nat_ins, 1349.28, 2)
		self.assertAlmostEqual(salary.annual, 16010.72, 2)

	def test_basic_rate_below_sl_threshold(self):
		"""Test a basic tax band salary with loan, under threshold."""
		salary = Salary(15000, student_loan=True)
		# We've tested the pretax above.
		self.assertEqual(salary.income_tax, 1000.0)
		self.assertEqual(salary.student_loan, 0)
		self.assertAlmostEqual(salary.nat_ins, 845.28, 2)
		self.assertAlmostEqual(salary.annual, 13154.72, 2)


	def test_basic_rate_with_loan(self):
		salary = Salary(19200, student_loan=True)
		# We've tested the pretax above.
		self.assertEqual(salary.income_tax, 1840.0)
		self.assertAlmostEqual(salary.student_loan, 206.1, 1)
		self.assertAlmostEqual(salary.nat_ins, 1349.28, 2)
		self.assertAlmostEqual(salary.annual, 15804.62, 2)

	def test_high_basic_rate(self):
		salary = Salary(36000, student_loan=True)
		# We've tested the pretax above.
		self.assertEqual(salary.income_tax, 5200.0)
		self.assertAlmostEqual(salary.student_loan, 1718.1, 1)
		self.assertAlmostEqual(salary.nat_ins, 3365.28, 2)
		self.assertAlmostEqual(salary.annual, 25716.62, 2)


if __name__ == '__main__':
	unittest.main()
