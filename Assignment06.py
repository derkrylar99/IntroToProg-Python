# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using Functions/Methods, Classes, + Separation of Concerns
# Change Log: (Who, When, What)
#   DLarson,11/19/2023,Created Script
# ------------------------------------------------------------------------------------------ #
# Import code from Python's JSON module
import json

# Data ------------------------------------------ #
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
-----------------------------------------  
'''

# Define the Variables
students: list = []
menu_choice: str = ''


# Processing ------------------------------------ #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

        ChangeLog: (Who, When, What)
        Dlarson,11.19.2023,Created Class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        This function reads the data from the file

            ChangeLog: (Who, When, What)
            Dlarson,11.19.2023,Created function
        :param file_name:
        :param student_data:
        :return: student_data
        """
        # When the program starts, read the file data into a list of dictionary rows (table)
        # Extract the data from JSON file
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
            print("Data has been processed!")
        # Provide structured error handling
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if not file.closed:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        This function writes data to the file

            ChangeLog: (Who, When, What)
            Dlarson,11.19.2023,Created function
        :param file_name:
        :param student_data:
        :return: None
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            print("*" * 50, "\n")
            print(f"Your data has been saved in {file_name}!\n")
        except TypeError as e:
            IO.output_error_messages("Please check the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with writing to the file.", e)
        finally:
            if not file.closed:
                file.close()


# Presentation ------------------------------------ #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

        ChangeLog: (Who, When, What)
        Dlarson,11.19.2023,Created Class
        Dlarson,11.19.2023,Added menu output and input functions
        Dlarson,11.19.2023,Added a function to display the data
        Dlarson,11.19.2023,Added a function to display custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This function displays a custom error messages to the user

            ChangeLog: (Who, When, What)
            Dlarson,11.19.2023,Created function
        :param message:
        :param error:
        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        This function displays the Main Menu of options to the user

            ChangeLog: (Who, When, What)
            Dlarson,11.19.2023,Created function
        :param menu:
        :return: None
        """
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """
        This function captures the user-selection Menu option

        ChangeLog: (Who, When, What)
        Dlarson,11.19.2023,Created function

        :return: choice
        """
        choice = "0"
        try:
            choice = input("Please enter your Menu choice number: ")
            if choice not in ("1", "2", "3", "4"):
                raise Exception("INVALID SELECTION! Please select  1 - 4 from the Menu options.")
        except Exception as e:
            IO.output_error_messages(e.__str__())

        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        """
        This function displays all entered data to the user

            ChangeLog: (Who, When, What)
            Dlarson,11.19.2023,Created function
        :param student_data:
        :return: None
        """
        print()
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """
        This function processes user-input data and adds it to the list of data

            ChangeLog: (Who, When, What)
            Dlarson,11.19.2023,Created function
        :param student_data:
        :return: student_data
        """
        try:
            # Input the data
            student_first_name = input("Please enter the student's First Name: ")
            if not student_first_name.isalpha():
                raise ValueError("The First Name should only contain letters!")
            student_last_name = input("Please enter the student's Last Name: ")
            if not student_last_name.isalpha():
                raise ValueError("The Last Name should only contain letters!")
            course_name = input("Please enter the Course Name: ")

            # Add the student data to a Dictionary matching students table keys
            student = {'FirstName': student_first_name,
                       'LastName': student_last_name,
                       'CourseName': course_name}
            student_data.append(student)

        except ValueError as e:
            IO.output_error_messages("That value is NOT the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data


# End of function / method definitions

# Beginning of the Main Body of this script
# Read the data from the JSON file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
# Repeat the following tasks
while True:
    # Present the menu of choices
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":
        students = IO.input_student_data(student_data=students)
        # Print Students list with new Student information added
        IO.output_student_courses(students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        # Print list of data before saving to file
        IO.output_student_courses(student_data=students)
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break

print("*" * 50)
print("Exiting Program.")
print("*" * 50)
