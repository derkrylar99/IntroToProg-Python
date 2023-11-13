# ------------------------------------------------------------------------------------------ #
# Title: Working With Dictionaries And Files
# Desc: Shows how work with dictionaries and files when using a table of data
# Change Log: (Who, When, What)
#   DLarson,11/07/2023,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
FILE_NAME: str = "MyLabData.csv"
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
file = open(FILE_NAME, "r")
for row in file.readlines():
    # Transform the data from the file
    student_data = row.split(',')
    student_data = {"FirstName": student_data[0],
                    "LastName": student_data[1],
                    "GPA": float(student_data[2].strip())}
    # Load it into the collection
    students.append(student_data)
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
        # Input the data
        student_first_name = input("What is the student's First Name? ")
        student_last_name = input("What is the student's Last Name? ")
        student_gpa = float(input("What is the student's GPA? "))
        # Add the student data to the dict
        student_data = {"FirstName": student_first_name,
                        "LastName": student_last_name,
                        "GPA": student_gpa}
        students.append(student_data)
        continue

    elif menu_choice == "3":
        # Save the data to the file
        file = open(FILE_NAME, "w")
        for student in students:
            file.write(f'{student["FirstName"]},{student["LastName"]},{student["GPA"]}\n')
        file.close()
        print("Data has been Saved!")
        continue

    elif menu_choice == "4":
        # Exit the program
        print("Exiting Program! \n")
        exit()
        print("*"*50,"\n","Program has been closed.")

    else:
        print("INVALID SELECTION. Please chose a Menu Option: ")
        continue
