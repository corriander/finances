import unittest
from finances.tax import CouncilTax

class TestCouncilTax(unittest.TestCase):
	def default(self):
		"""Check bands are estimated with no input."""
		ct = CouncilTax()
		self.assertAlmostEqual(ct['A'], 1468 * (6/9.))

	def test_non_default(self):
		ct = CouncilTax(1400)
		self.assertAlmostEqual(ct['A'], 1400 * (6/9.))

	def test_direct_input(self):
		ct = CouncilTax(rates=(1, 2, 3, 4, 5, 6, 7, 8)) 
		self.assertAlmostEqual(ct['A'], 1.0)

	def test_direct_input_overrides_band_d(self):
		ct = CouncilTax(band_d=1400, rates=range(1, 8+1))
		self.assertAlmostEqual(ct['A'], 1.0)

	def test_band_d_and_SDP(self):
		ct = CouncilTax(1400, SDP=True)
		self.assertAlmostEqual(ct['A'], 1400 * (6/9.) * 0.75)
	
	def test_rates_and_SDP(self):
		ct = CouncilTax(rates=range(1, 8+1), SDP=True)
		self.assertAlmostEqual(ct['A'], 0.75)


if __name__ == '__main__':
	unittest.main()
