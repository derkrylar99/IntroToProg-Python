# ------------------------------------------------- #
# Title: Assignment08 Processing Classes
# Description: define all necessary data processing
#   classes and functions used to process data
# ChangeLog: (Who, When, What)
# DLarson,12.2.2023,Created Script
# ------------------------------------------------- #
import json
from data_classes import Employee
import presentation_classes as pc
import datetime
from datetime import datetime
from datetime import date


# Creating a Class for file processing tasks
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

        ChangeLog: (Who, When, What)
        DLarson,12.02.2023,Created Class
    """

    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list, employee_type: object):
        """
        This function reads the data from the file

            ChangeLog: (Who, When, What)
            DLarson,12.02.2023,Created function
        :param file_name:
        :param employee_data:
        :param employee_type:
        :return: employee_data
        """
        # When the program starts, extract the JSON file data into a list of dictionary rows (table)
        # Create a list of Employee objects from the dictionary rows

        try:
            file = open(file_name, "r")
            list_of_dictionary_data = json.load(file)

            for employee in list_of_dictionary_data:
                employee_entry: object = employee_type
                employee_type = Employee()
                employee_entry = employee_type
                employee_entry.first_name = employee["FirstName"]
                employee_entry.last_name = employee["LastName"]
                review_date_string = employee["ReviewDate"]
                review_date_obj: date = datetime.strptime(review_date_string, "%Y-%m-%d")
                employee_entry.review_date = review_date_obj
                employee_entry.review_rating = employee["ReviewRating"]
                employee_data.append(employee_entry)
            file.close()
            print("Data has been processed! ")
        # Provide structured error handling
        except FileNotFoundError as e:
            pc.IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            pc.IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if not file.closed:
                file.close()
        return employee_data

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list):
        """
        This function writes data to the file

            ChangeLog: (Who, When, What)
            DLarson,12.02.2023,Created function
        :param file_name: str
        :param employee_data: list
        :return: None
        """
        # Create a new list to hold JSON data for json.dump() function
        list_of_dictionary_data: list = []

        # Convert the list of Student objects to JSON compatible list of dictionaries
        for employee in employee_data:
            review_date_obj = employee.review_date
            review_date_string = review_date_obj.strftime('%Y-%m-%d')
            employee_json: dict = {"FirstName": employee.first_name,
                                   "LastName": employee.last_name,
                                   "ReviewDate": review_date_string,
                                   "ReviewRating": employee.review_rating}
            list_of_dictionary_data.append(employee_json)

        # Attempt to save the file, otherwise provide structured Error Handling
        try:
            file = open(file_name, "w")
            json.dump(list_of_dictionary_data, file)
            file.close()
            print(f"Your data has been saved in {file_name}!\n")
            print("-" * 100, "\n")
        except TypeError as e:
            pc.IO.output_error_messages("Please check the data is a valid JSON format", e)
        except Exception as e:
            pc.IO.output_error_messages("Error: There was a problem with writing to the file.", e)
        finally:
            if not file.closed:
                file.close()


if __name__ == '__main__':
    print("This file is not meant to be run. Please run 'main.py' ")
