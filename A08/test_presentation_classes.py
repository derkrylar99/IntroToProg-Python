# ------------------------------------------------------------------------------- #
# Title: Test Presentation Classes Module
# # Description: A collection of tests for the presentation classes module
# ChangeLog: (Who, When, What)
# DLarson,12.03.2023,Created Script
# ------------------------------------------------------------------------------- #
import datetime
import unittest
from unittest.mock import patch
from presentation_classes import IO
from datetime import date
import data_classes as dc


class TestIO(unittest.TestCase):
    def setUp(self):
        self.employee_data = []
        self.employee_type = None

    def test_input_menu_choice(self):
        # Simulate user input and check if the function returns the expected value
        with patch('builtins.input', return_value='2'):
            choice = IO.input_menu_choice()
            self.assertEqual(choice, '2')

    def test_input_employee_data(self):
        # Simulate user input for employee data
        with patch('builtins.input', side_effect=['John', 'Doe', "2023-12-12", 4]):
            IO.input_employee_data(self.employee_data, self.employee_type)
            self.assertEqual(len(self.employee_data), 1)
            self.assertEqual(self.employee_data[0].first_name, 'John')
            self.assertEqual(self.employee_data[0].last_name, 'Doe')
            self.assertEqual(self.employee_data[0].review_date, datetime.datetime(2023, 12, 12, 0, 0))
            self.assertEqual(self.employee_data[0].review_rating, 4)

        # Simulate invalid Review Rating input
        with patch('builtins.input', side_effect=['Alice', 'Smith', "2023-32-12", 5]):
            IO.input_employee_data(self.employee_data, self.employee_type)
            self.assertEqual(len(self.employee_data), 1)


if __name__ == "__main__":
    unittest.main()
