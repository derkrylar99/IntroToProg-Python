# ------------------------------------------------------------------------------- #
# Title: Test Data Classes Module
# # Description: A collection of tests for the data classes module
# ChangeLog: (Who, When, What)
# DLarson,12.03.2023,Created Script
# ------------------------------------------------------------------------------- #

import unittest
from datetime import date
from data_classes import Person
from data_classes import Employee


class TestPerson(unittest.TestCase):

    # Test the constructor
    def test_person_init(self):
        person = Person("Jane", "Doe")
        self.assertEqual(person.first_name, "Jane")
        self.assertEqual(person.last_name, "Doe")

    # Test the first and last name validation
    def test_person_invalid_name(self):
        with self.assertRaises(ValueError):
            person = Person("123", "Doe")
        with self.assertRaises(ValueError):
            person = Person("Jane", "123")

    # Test the __str__() magic method
    def test_person_string(self):
        person = Person("Jane", "Doe")
        self.assertEqual(str(person), "Jane,Doe")


class TestEmployee(unittest.TestCase):

    # Test the constructor
    def test_employee_init(self):
        employee = Employee("Alan", "Smith", date(2022, 12, 12), 4)
        self.assertEqual(employee.first_name, "Alan")
        self.assertEqual(employee.last_name, "Smith")
        self.assertEqual(employee.review_date, date(2022, 12, 12))
        self.assertEqual(employee.review_rating, 4)

    # Test the validation
    def test_employee_datetime_type(self):
        pass

    def test_employee_rating_type(self):
        with self.assertRaises(ValueError):
            employee = Employee("Alan", "Smith", date(2022, 12, 12), "invalid_rating")

    # Test the __str__() magic method for Child Class
    def test_employee_string(self):
        employee = Employee("Eve", "Brown", date(2022, 11, 12), 5)
        self.assertEqual(str(employee), "Eve,Brown,2022-11-12,5")


if __name__ == '__main__':
    unittest.main()
