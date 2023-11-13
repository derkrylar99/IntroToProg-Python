# ------------------------------------------------------------------------------------------ #
# Title: Working With Exceptions
# Desc: Shows how work with Exceptions using Structured Error Handling
# Change Log: (Who, When, What)
#   DLarson,11/12/2023,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
FILE_NAME: str = "MyLabData.json"
MENU: str = '''
---- Student GPAs ------------------------------
  Select from the following menu:  
    1. Show current student data. 
    2. Enter new student data.
    3. Save data to a file.
    4. Exit the program.
-------------------------------------------------- 
'''

# Define the program's data
student_first_name: str = ''
student_last_name: str = ''
student_gpa: float = 0.0
message: str = ''
menu_choice: str = ''
student_data: dict = {}
students: list = []
file_data: str = ''
file = None

# When the program starts, read the file data into a list of dictionary rows (table)
# Extract the data from the file
# file = open(FILE_NAME, "r")
# for row in file.readlines():
#     # Transform the data from the file
#     student_data = row.split(',')
#     student_data = {"FirstName": student_data[0],
#                     "LastName": student_data[1],
#                     "GPA": float(student_data[2].strip())}
#     # Load it into the collection
#     students.append(student_data)
# file.close()

# use JSON instead of CSV
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()

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

while True:
    print(MENU)
    menu_choice = input("Enter your menu choice number: ")
    # Extra space for improved formatting
    print()

    # Repeat the following user-selected tasks
    if menu_choice == "1":
        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            # display the table's current data
            if student["GPA"] >= 4.0:
                message = " {} {} earned an A with a {:.2f} GPA"
            elif student["GPA"] >= 3.0:
                message = " {} {} earned a B with a {:.2f} GPA"
            elif student["GPA"] >= 2.0:
                message = " {} {} earned a C with a {:.2f} GPA"
            elif student["GPA"] >= 1.0:
                message = " {} {} earned a D with a {:.2f} GPA"
            else:
                message = " {} {}'s {:.2f} GPA was not a passing grade"

            print(message.format(student["FirstName"], student["LastName"], student["GPA"]))
        print("-"*50)
        continue

    elif menu_choice == "2":
        # Add data to the table
        try:
            # Input the data
            student_first_name = input("What is the student's First Name? ")
            if not student_first_name.isalpha():
                raise ValueError("The First Name should NOT contain numbers.")

            student_last_name = input("What is the student's Last Name? ")
            if not student_last_name.isalpha():
                raise ValueError("The Last Name should NOT contain numbers.")

            try:
                student_gpa = float(input("What is the student's GPA? "))
            except ValueError:
                raise ValueError("Grade Point Average MUST be a numeric value.")

            # Add the student data to the dict
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "GPA": student_gpa}
            students.append(student_data)
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

    elif menu_choice == "3":
        # Save the data to the file

        # file = open(FILE_NAME, "w")
        # for student in students:
        #     file.write(f'{student["FirstName"]},{student["LastName"]},{student["GPA"]}\n')
        # file.close()
        # print("Data has been Saved!")
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            print("Data has been Saved!")
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

    elif menu_choice == "4":
        # Exit the program
        print("*"*50,"\n","Exiting Program.")
        exit()

    else:
        print("INVALID SELECTION. Please chose a Menu Option: ")
        continue
