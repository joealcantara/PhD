import unittest

from city_functions import city

class TestCitiesFunctions (unittest.TestCase):
    
    def test_city(self):
        print("Start Test")
        formatted_test = city('Santiago', 'Chile')
        self.assertEqual(formatted_test, 'Santiago, Chile')

    def test_city2(self):
        formatted_test2 = city('santiago', 'chile')
        self.assertEqual(formatted_test2, 'Santiago, Chile')

    def test_city_population(self):
        formatted_test3 = city('santiago', 'chile', '5000000')
        self.assertEqual(formatted_test3, 'Santiago, Chile - 5000000')

unittest.main()