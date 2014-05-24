import unittest
import finances.vehicle as vehicle

# Tests related to vehicle standing costs.
class TestStatic(unittest.TestCase):
	"""Static is a simple annual expense."""
	def test___init__(self):
		"""Check that the inherited properties are correct."""
		obj = vehicle._Static('test', 240)
		self.assertEqual(obj.name, 'Vehicle: test')
		self.assertEqual(obj.monthly, 20.0)

class TestVED(unittest.TestCase):
	"""VED is a simple annual expense."""
	def test___init__(self):
		obj = vehicle.VED(120)
		self.assertEqual(obj.name, 'Vehicle: VED (Tax)')
		self.assertEqual(obj.monthly, 10.0)


class TestInsurance(unittest.TestCase):
	"""Insurance is currently a simple annual expense."""
	def test___init__(self):
		obj = vehicle.Insurance(120)
		self.assertEqual(obj.name, 'Vehicle: Insurance')
		self.assertEqual(obj.monthly, 10.0)


class TestBreakdownCover(unittest.TestCase):
	"""Breakdown cover is a simple annual expense."""
	def test___init__(self):
		obj = vehicle.BreakdownCover(120)
		self.assertEqual(obj.name, 'Vehicle: Breakdown Cover')
		self.assertEqual(obj.monthly, 10.0)


class TestRepairFund(unittest.TestCase):
	"""Repair fund is a simple annual (potential) expense."""
	def test___init__(self):
		obj = vehicle.RepairFund(120)
		self.assertEqual(obj.name, 'Vehicle: Emergency repair fund')
		self.assertEqual(obj.monthly, 10.0)
	

class TestRunning(unittest.TestCase):
	"""Vehicle running cost is an annual mileage-based expense."""
	def test_10000(self):
		"""Check a sample annual cost for 10,000 miles."""
		obj = vehicle._Running('test', 10000, 0.015)
		self.assertEqual(obj.name, 'Vehicle running cost: test')
		self.assertEqual(obj.annual, 150.0)
	
	def test_5000(self):
		"""Check a sample annual cost for 5,000 miles."""
		obj = vehicle._Running('test', 5000, 0.015)
		self.assertEqual(obj.annual, 75.0)


class TestFuel(unittest.TestCase):
	"""Fuel based on mileage, fuel prices and fuel consumption.
	
	This is validated by a comparison with Google maps fuel estimates.
	I know from experience using the standard fuel consumption at
	144p/l fuel cost it over-estimates for my car on a typical 
	journey. I'm content to set this as the upper bound of a +-15%
	uncertainty.
	
	"""
	def test_sample_journey_defaults(self):
		distance, cost, mileage = 76.0, 16.0, 5000
		cost_per_mile = (cost / distance) * 0.85
		annual = cost_per_mile * mileage

		obj = vehicle.Fuel(mileage)
		self.assertAlmostEqual(obj.annual, annual, delta=0.15*annual)


class TestTyres(unittest.TestCase):
	"""Tyre usage based on mileage and AA average 0.023 GBP/mile"""
	def test_default_annual(self):
		mileage = 5000
		obj = vehicle.Tyres(mileage)
		self.assertEqual(obj.annual, mileage * 0.023)


class TestService(unittest.TestCase):
	"""Servicing based on mileage and AA average 0.02 GBP/mile"""
	def test_default_annual(self):
		mileage = 5000
		obj = vehicle.Service(mileage)
		self.assertEqual(obj.annual, mileage * 0.02)


class TestParts(unittest.TestCase):
	"""Parts based on mileage and AA average 0.027 GBP/mile"""
	def test_default_annual(self):
		mileage = 5000
		obj = vehicle.Parts(mileage)
		self.assertEqual(obj.annual, mileage * 0.027)


if __name__ == '__main__':
	unittest.main()
