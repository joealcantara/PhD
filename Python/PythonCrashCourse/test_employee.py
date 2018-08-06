import unittest
from employee import Employee

class TestEmployeeCases(unittest.TestCase):
    """ Tests for the Employee Classes"""
    def setUp(self):
        self.my_employee = Employee("Joe", "Alcantara", 0)
        self.raises = ['', 5500]

    def test_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 5000)
    
    def test_custom_raise(self):
        self.my_employee.give_raise(5500)
        self.assertEqual(self.my_employee.salary, 5500)

unittest.main()
