import unittest

from tire.carrigan_tire import CarriganTire

class TestCarriganTire(unittest.TestCase):
    
    def test_tire_should_be_serviced(self):
        sensors = [0.9, 0, 0.1, 0.5]

        tire = CarriganTire(sensors)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        sensors = [0.3, 0, 0.7, 0.5]

        tire = CarriganTire(sensors)
        self.assertFalse(tire.needs_service())


if __name__ == "__main__":
    unittest.main()