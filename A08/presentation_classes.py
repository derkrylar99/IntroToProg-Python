# ------------------------------------------------- #
# Title: Assignment08 Presentation Classes
# Description: define all necessary data presentation
#   classes and functions used to present data to user
# ChangeLog: (Who, When, What)
# DLarson,12.2.2023,Created Script
# ------------------------------------------------- #
import data_classes as dc
import datetime
from datetime import datetime
from datetime import date


class IO:
    """
    A collection of presentation layer functions that manage user input and output

        ChangeLog: (Who, When, What)
        DLarson,12.02.2023,Created Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This function displays a custom error messages to the user

            ChangeLog: (Who, When, What)
            DLarson,12.02.2023,Created function
        :param message: str
        :param error: Exception
        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- TECHNICAL ERROR MESSAGE: -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        This function displays the Main Menu of options to the user

            ChangeLog: (Who, When, What)
            DLarson,12.02.2023,Created function
        :param menu: str
        :return: None
        """
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """
        This function captures the user-selection Menu option

            ChangeLog: (Who, When, What)
            DLarson,12.02.2023,Created function
        :return: choice
        """
        choice = "0"
        try:
            choice = input("Please enter your Menu choice number: ")
            if choice not in ("1", "2", "3", "4"):
                raise Exception("INVALID SELECTION! Please select  1 - 4 from the Menu options. ")
        except Exception as e:
            IO.output_error_messages(e.__str__())

        return choice

    @staticmethod
    def output_employee_data(employee_data: list):
        """
        This function displays all entered data to the user

            ChangeLog: (Who, When, What)
            DLarson,12.02.2023,Created function
        :param employee_data: list
        :return: None
        """
        message: str = ''
        print()
        print("-" * 100)
        for employee in employee_data:
            if employee.review_rating == 5:
                message = " {} {} is rated on {} as {} (Leading)"
            elif employee.review_rating == 4:
                message = " {} {} is rated on {} as {} (Strong)"
            elif employee.review_rating == 3:
                message = " {} {} is rated on {} as {} (Solid)"
            elif employee.review_rating == 2:
                message = " {} {} is rated on {} as {} (Building)"
            elif employee.review_rating == 1:
                message = " {} {} is rated on {} as {} (Not Meeting Expectations)"
            else:
                print("Invalid input. Please enter rating 1-5!")
                continue
            review_date_obj = employee.review_date
            review_date_string = review_date_obj.strftime('%Y-%m-%d')
            print(message.format(employee.first_name, employee.last_name, review_date_string,
                                 employee.review_rating))
        print("-" * 100)

    @staticmethod
    def input_employee_data(employee_data: list, employee_type: object):
        """
        This function processes user-input data and adds it to the list of data

            ChangeLog: (Who, When, What)
            DLarson,12.02.2023,Created function
        :param employee_data:
        :param employee_type:
        :return: employee_data
        """
        try:
            # Input the data
            employee_type = dc.Employee()
            employee_add = employee_type
            employee_add.first_name = input("Please enter the employee's First Name: ")
            employee_add.last_name = input("Please enter the employee's Last Name: ")
            review_date_string = input("Please enter the employee's Review Date= YYYY-MM-DD: ")
            review_date_obj: date = datetime.strptime(review_date_string, "%Y-%m-%d")
            employee_add.review_date = review_date_obj
            employee_add.review_rating = input("Please enter the employee's Review Rating: ")
            employee_data.append(employee_add)
        except ValueError as e:
            IO.output_error_messages("That value is NOT the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return employee_data


if __name__ == '__main__':
    print("This file is not meant to be run. Please run 'main.py' ")
