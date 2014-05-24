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
	

if __name__ == '__main__':
	unittest.main()
