# ------------------------------------------------------------------------------- #
# Title: Test Data Classes Module
# # Description: A collection of tests for the data classes module
# ChangeLog: (Who, When, What)
# JD Blake, 6/7/24, Created Test
# ------------------------------------------------------------------------------- #


import unittest

from data_classes import Person
from data_classes import Employee

class Test_Person(unittest.TestCase):

    def test_person_class(self):  # Test the constructor
        person = Person("John", "Doe")
        self.assertEqual("John", person.first_name)
        self.assertEqual("Doe", person.last_name)
        print(person)

    def test_person_invalid_name(self): # Test first and last name validations
        with self.assertRaises(ValueError):
            person = Person("123", "Doe")
        with self.assertRaises(ValueError):
            person = Person("John", "456")


class Test_Employee(unittest.TestCase):  # Test the constructor
    def test_employee_class(self):
        employee = Employee("James", "May", "1999-01-02", 3)
        self.assertEqual("James", employee.first_name)
        self.assertEqual("May", employee.last_name)
        self.assertEqual("1999-01-02", employee.review_date)
        self.assertEqual(3, employee.review_rating)
        print(employee)

    def test_employee_invalid_review_info(self):  # Test first and last names, and review date and ra