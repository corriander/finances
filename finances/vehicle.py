"""Classes relating to costs of vehicle ownership."""
from finances.base import Expense

class _Static(Expense):
	"""Standing cost (on a per-annum basis) for vehicle ownership."""
	def __init__(self, name, cost):
		name = 'Vehicle: {}'.format(name)
		Expense.__init__(self, name, cost, 'annual')


class VED(_Static):
	"""Vehicle Excise Duty (Road Tax)."""
	def __init__(self, cost):
		_Static.__init__(self, 'VED (Tax)', cost)


class Insurance(_Static):
	"""Vehicle insurance (on a per-annum basis)."""
	def __init__(self, cost):
		_Static.__init__(self, 'Insurance', cost)


class BreakdownCover(_Static):
	"""Breakdown cover (on a per-annum basis)."""
	def __init__(self, cost):
		_Static.__init__(self, 'Breakdown Cover', cost)


class RepairFund(_Static):
	"""Slush fund for vehicle repairs."""
	def __init__(self, cost):
		_Static.__init__(self, 'Emergency repair fund', cost) 


# The following classes are included for completeness and may well be
# implemented when considering a new vehicle! There are other
# considerations likely to be included here as well.

# class Capital(_Static):
# 	"""Capital cost of vehicle.
# 	
# 	Represents the loss presented by having money tied up in the 
# 	vehicle that could be earning interest in a savings account. 
# 	
# 	By default this uses the same interest rate as the AA.
# 	
# 	"""
# 	def __init__(self, purchase_cost, interest=2.2):
# 		annual_loss = purchase_cost * (interest / 100)
# 		_Static.__init__(self, 'Capital cost', annual_loss)

# class Depreciation(_Static):
#	"""Depreciation of vehicle value."""
#	pass

# class Purchase(_Static):
# 	"""Purchase cost spread over expected life/ownership.
# 	
# 	This applies to a non-finance type purchase. Expected life is used
# 	to estimate annual cost (default 5 yr). Care should be taken 
# 	
# 		a) not to double count this.
# 		b) in applying it to historic purchases.
# 		c) not applying it to a finance-based purchase.
# 	
# 	"""
# 	def __init__(self, purchase_cost, lifetime=5):
# 		cost = purchase_cost / lifetime
# 		_Static.__init__(self, 'Distributed purchase cost', cost)

