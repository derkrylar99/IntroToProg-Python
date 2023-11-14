# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   DLarson,11/12/2023,Created Script
# ------------------------------------------------------------------------------------------ #
# Import code from Python's JSON module
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
-----------------------------------------  
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
csv_data: str = ''
file = None
menu_choice: str = ''
student_data: dict = {}
students: list = []

# When the program starts, read the file data into a list of dictionary rows (table)

# file = open(FILE_NAME, "r")
# for row in file.readlines():
#     # Transform the data from the file
#     student_data = row.split(",")
#     student_data = [student_data[0], student_data[1], student_data[2].strip()]
#     # Load the data into the collection
#     students.append(student_data)
# file.close()
#
# Extract using JSON instead of CSV
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
    print("Data has been processed!")
# Provide structured error handling
except TypeError as e:
    print("Please check the data is a valid JSON format\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file.closed == False:
        file.close()

# Present and Process the data
while True:
    # Present the menu of choices
    print(MENU)
    menu_choice = input("Please enter your Menu choice number: ")

    # Input user data
    if menu_choice == "1":
        # Structured error handling for non-letter characters
        try:
            student_first_name = input("Please enter the student's First Name: ")
            if not student_first_name.isalpha():
                raise ValueError("The First Name should only contain letters!")

            student_last_name = input("Please enter the student's Last Name: ")
            if not student_last_name.isalpha():
                raise ValueError("The Last Name should only contain letters!")

            course_name = input("Please enter the Course Name: ")
            # Add the student data to a Dictionary matching students table keys
            student_data = {'FirstName': student_first_name,
                            'LastName': student_last_name,
                            'CourseName': course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e) # Prints custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        continue

    # Present the current data
    elif menu_choice == "2":
        print("-"*50)
        for student in students:
            print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        # file = open(FILE_NAME, "w")
        # for student in students:
        #     csv_data = f"{student[0]},{student[1]},{student[2]}\n"
        #     file.write(csv_data)
        # file.close()
        #
        # Using JSON instead of CSV
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            print("*" * 50, "\n")
            print(f"Your data has been saved in {FILE_NAME}!\n")
            for student in students:
                print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
            continue
        except TypeError as e:
            print("Please check the data is a valid JSON format\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file.closed == False:
                file.close()

    # Stop the loop
    elif menu_choice == "4":
        break
    else:
        # For any non-valid selection entered into menu_choice:
        print("INVALID SELECTION! Please select  1 - 4 from the Menu options.")
        continue

print("You have selected to Close the Program.")
