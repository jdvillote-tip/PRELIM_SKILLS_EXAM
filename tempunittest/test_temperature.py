import unittest
from temperature import Temperature 

class TestTemperature(unittest.TestCase):

    def test_inputs_error(self):
        self.assertRaises(ValueError, Temperature, None)

    def test_inputs_error(self):
        args = (5,5,5)
        self.assertRaises(ValueError, Temperature, *args)

    def test_output(self):
        fahrenheit = (1 - 32)* 5/9 +273.15
        self.assertEqual(Temperature(fahrenheit=1).kelvin, fahrenheit)

    def test_output2(self):
        self.assertEqual(Temperature(1).kelvin, 1)

    def test_output3(self):
        self.assertEqual(Temperature(celsius=1).kelvin, 274.15)

    def test_negative(self):
        self.assertRaises(ValueError, Temperature, -1)