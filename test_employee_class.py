import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    '''Tests for the class Employee'''
    def setUp(self):
        self.new_employee = Employee('gabriel', 'fonseca', 50000)
    
    def test_give_default_raise(self):
        raise_income = self.new_employee.give_raise()
        self.assertEqual(raise_income, 5000)
    
    def test_give_custom_raise(self):
        raise_income = self.new_employee.give_raise(10000)
        self.assertEqual(raise_income, 10000)
#if __name__ == '__main__':
unittest.main()