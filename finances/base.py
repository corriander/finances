class _Base(object):
	"""Base class for everything.

	Takes an id/name, value and frequency as an input and normalises
	this into weekly/monthly/annual values via properties.

	"""
	def __init__(self, name, value, frequency):
		self.name = name
		annualise = {'weekly' : 52, 'monthly' : 12, 'annual' : 1}
		self._annual = float(abs(value)) * annualise[frequency]
	
	@property
	def annual(self):
		"""Amount per annum."""
		return self._annual

	@property
	def monthly(self):
		"""Amount per month."""
		return self.annual / 12

	@property
	def weekly(self):
		"""Amount per week."""
		return self.annual / 52

class Income(_Base):
	"""Model an element of income.
	
		name : string identifying the income element
		value : currency amount
		frequency : frequency [annual (default), monthly or weekly]
		
	"""
	def __init__(self, name, value, frequency='annual'):
		_Base.__init__(self, name, value, frequency)

class Expense(_Base):
	"""Model an expense.
	
		name : string identifying the income element
		value : currency amount
		frequency : frequency [annual, monthly (default) or weekly]
		
	"""
	def __init__(self, name, value, frequency='annual'):
		_Base.__init__(self, name, value, frequency)

