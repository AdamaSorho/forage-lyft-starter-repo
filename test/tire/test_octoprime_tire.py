import unittest

from tire.octoprime_tire import OctoprimeTire

class TestOctoprimeTire(unittest.TestCase):
    
    def test_tire_should_be_serviced(self):
        sensors = [1, 0.5, 1, 1]

        tire = OctoprimeTire(sensors)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        sensors = [0, 0.5, 0, 0.2]

        tire = OctoprimeTire(sensors)
        self.assertFalse(tire.needs_service())


if __name__ == "__main__":
    unittest.main()