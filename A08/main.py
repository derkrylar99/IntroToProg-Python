# ------------------------------------------------- #
# Title: Assignment08 Main Module
# Description: import classes and functions from modules
#   to present and process the data to the User
# ChangeLog: (Who, When, What)
# DLarson,12.2.2023,Created Script
# ------------------------------------------------- #

import data_classes as dc
import processing_classes as pc
import presentation_classes as ioc

FILE_NAME: str = "EmployeeRatings.json"
MENU: str = '''
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Show current employee rating data.
    2. Enter new employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
'''
employees: list = []
menu_choice = ''
employee = dc.Employee()

employees = pc.FileProcessor.read_employee_data_from_file(file_name=FILE_NAME, employee_data=employees,
                                                          employee_type=employee)

# Present and Process the data
#   Repeat the following tasks
while True:
    # Present the menu of choices
    ioc.IO.output_menu(menu=MENU)
    menu_choice = ioc.IO.input_menu_choice()

    # Present the current data
    if menu_choice == "1":
        ioc.IO.output_employee_data(employee_data=employees)
        continue

    # Input user data
    #   Print the updated Employee List with newly added Employee Information
    elif menu_choice == "2":
        employees = ioc.IO.input_employee_data(employee_data=employees, employee_type=employee)
        ioc.IO.output_employee_data(employee_data=employees)
        continue

    # Save the data to a file
    #   Print list of data before saving to file
    elif menu_choice == "3":
        ioc.IO.output_employee_data(employee_data=employees)
        pc.FileProcessor.write_employee_data_to_file(file_name=FILE_NAME, employee_data=employees)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break

print("*" * 100)
print("Exiting Program.")
print("*" * 100)
