# ------------------------------------------------------------------------------- #
# Title: Test Processing Classes Module
# # Description: A collection of tests for the processing classes module
# ChangeLog: (Who, When, What)
# DLarson,12.03.2023,Created Script
# ------------------------------------------------------------------------------- #

import unittest
import tempfile
from datetime import date
import json
import data_classes as dc
from processing_classes import FileProcessor


class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        # Create a temp file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temporary_file_name = self.temp_file.name
        self.employee_type: object = None
        self.employee_data = []

    def tearDown(self):
        # Clean up and delete the temp file for efficiency
        self.temp_file.close()

    def test_read_employee_data_from_file(self):
        # Create sample data and write to temp file
        sample_data = [
            {"FirstName": "John", "LastName": "Doe",
             "ReviewDate": "2023-12-12", "ReviewRating": 4},
            {"FirstName": "Alice", "LastName": "Smith",
             "ReviewDate": "2023-7-22", "ReviewRating": 5},
        ]
        with open(self.temporary_file_name, "w") as file:
            json.dump(sample_data, file)

        employee_type = dc.Employee()
        # Check if the expected data is returned from the read_employee_data_from_file method
        FileProcessor.read_employee_data_from_file(self.temporary_file_name, self.employee_data, self.employee_type)

        # Validate the expected objects contained in the employee_data list
        self.assertEqual(len(self.employee_data), len(sample_data))
        self.assertEqual(self.employee_data[0].first_name, "John")
        self.assertEqual(self.employee_data[1].review_rating, 5)

    def test_write_employee_data_to_file(self):
        # Create sample employee instance objects
        sample_employees = [
            dc.Employee("John", "Doe", date(2023, 12, 12), 4),
            dc.Employee("Alice", "Smith", date(2023, 7, 22), 5),
        ]

        # write sample data to temp file using write data method
        FileProcessor.write_employee_data_to_file(self.temporary_file_name, sample_employees)

        # Read the temp file data and check if it matches JSON
        with open(self.temporary_file_name, "r") as file:
            temp_file_data = json.load(file)

        self.assertEqual(len(temp_file_data), len(sample_employees))
        self.assertEqual(temp_file_data[0]["FirstName"], "John")
        self.assertEqual(temp_file_data[1]["ReviewRating"], 5)


if __name__ == "__main__":
    unittest.main()
