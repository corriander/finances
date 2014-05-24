class IncomeTax(object):
	def __init__(self, personal_allowance, thresholds):
		self.personal_allowance = personal_allowance
		self.bands = thresholds

	@property
	def personal_allowance(self):
		"""Personal allowance for people born after 1948-04-05."""
		return self._personal_allowance
	@personal_allowance.setter
	def personal_allowance(self, value):
		self._personal_allowance = value

	@property
	def bands(self):
		"""Current (2013-) tax rates are 20%, 40% and 45%.
		
		Income Tax bands are set by providing the thresholds for the
		basic and higher rates as a 2-tuple.

		NOTE: This doesn't consider the 10% savings rate.

		"""
		return self._bands
	@bands.setter
	def bands(self, thresholds):
		rates = 0.2, 0.4, 0.45		
		real_thresholds = (self.personal_allowance,) + thresholds
		self._bands = zip(real_thresholds, rates)

	@staticmethod
	def adjusted_pa(personal_allowance, salary):
		"""Adjust personal allowance based on salary."""
		lo, hi = 100000, 120000
		if salary <= lo:
			return personal_allowance
		elif salary >= hi:
			return 0
		else:
			return (salary - 100000) / 2


class NationalInsurance(object):
	"""National Insurance contributions for employees."""
	rates = (0.12, 0.02)

	def __init__(self, pthresh, upperlim):
		self._primary_threshold = pthresh
		self._upper_earning_limit = upperlim

	@property
	def primary_threshold(self):
		"""Weekly primary threshold."""
		return self._primary_threshold
	
	@property
	def upper_earning_limit(self):
		"""Weekly upper earnings limit, primary Class 1."""
		return self._upper_earning_limit

	@property
	def bands(self):
		"""National Insurance contribution bands."""
		return zip((self.primary_threshold, self.upper_earning_limit),
				   self.rates)

class CouncilTax(dict):
	def __init__(self, values):
		dict.__init__(self, zip('ABCDEFGH', values))
# --------------------------------------------------------------------
# Data
# --------------------------------------------------------------------
# Source: http://www.hmrc.gov.uk/rates/it.htm
income_tax = {'2013-14' : IncomeTax(9440, (9440+32010, 150000)),
			  '2014-15' : IncomeTax(10000, (10000+31865, 150000))}

# Source: http://www.hmrc.gov.uk/rates/nic.htm
national_insurance  = {'2013-14' : NationalInsurance(149, 797),
					   '2014-15' : NationalInsurance(153, 805)}

fiscal_year = '2014-15'
IT = income_tax[fiscal_year].bands
NI = national_insurance[fiscal_year].bands
