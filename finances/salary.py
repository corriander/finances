from finances.base import Income
from finances.tax import IncomeTax
from finances.tax import IT as ITax
from finances.tax import NI as NIns

class Salary(Income):
	"""Model an effective annual salary.
	
	Model includes Income Tax, National Insurance and Student Loan
	repayments.
	
	"""
	def __init__(self, pretax_salary, student_loan=False):
		# Create a pre-tax Income instance for reference.
		self.pretax = Income('Pretax salary', pretax_salary)
		self.student_loan = student_loan # Include student loan?
		Income.__init__(self, 'Take-home salary', 
						self.effective_salary())

	def effective_salary(self):
		"""Calculate effective salary."""
		return (self.pretax.annual - 
				self.income_tax - 
				self.nat_ins - 
				self.student_loan)

	@property
	def income_tax(self):
		"""Income Tax, evaluated from bands and pre-tax salary."""
		try:
			return self._income_tax
		except AttributeError:
			# Calculate income tax
			remaining = salary = self.pretax.annual
			bands = filter(lambda band: band[0] < salary, ITax)

			# Modify the personal allowance for salary > 100,000
			if bands:
				pa, rate = bands[0]
				bands[0] = (IncomeTax.adjusted_pa(pa, salary), rate)

			# Calculate the tax for salary lying in each band, total
			income_tax = []
			for threshold, rate in reversed(bands):
				income_tax.append((remaining - threshold) * rate)
				remaining = threshold
			self._income_tax = sum(income_tax)
			return self._income_tax

	@property
	def nat_ins(self):
		"""National Insurance contributions evaluated from salary."""
		try:
			return self._nat_ins
		except AttributeError:
			# Calculate national insurance contributions
			remaining = salary = self.pretax.weekly
			bands = filter(lambda band: band[0] < salary, NIns)

			# Calculate the NI contributions for each band, total
			ni_contrib = []
			for threshold, rate in reversed(bands):
				ni_contrib.append((remaining - threshold) * rate)
				remaining = threshold
			self._nat_ins = sum(ni_contrib) * 52
			return self._nat_ins

	@property
	def student_loan(self):
		"""A crude estimate of student loan repayments."""
		return self._student_loan
	@student_loan.setter
	def student_loan(self, exists):
		self._student_loan = 0
		if exists:
			# http://www.moneysavingexpert.com/students/student-loans-repay
			threshold, rate = 16910, 0.09
			pretax = self.pretax.annual
			if pretax > threshold:
				self._student_loan = (pretax - threshold) *	rate
