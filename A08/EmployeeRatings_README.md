# Employee Ratings : Main Module

## Description
This module imports classes and functions from other modules to present and process data for the user.

### Module: main.py

The `main.py` module serves as the main entry point for the Employee Ratings application.

#### Variables
* `FILE_NAME: str = "EmployeeRatings.json"` : The default filename for storing employee data in JSON format.
* `MENU: str` : A string containing the main menu options for the user.
```
    ---- Employee Ratings ------------------------------
      Select from the following menu:
        1. Show current employee rating data.
        2. Enter new employee rating data.
        3. Save data to a file.
        4. Exit the program.
    --------------------------------------------------
```
* `employees: list = []` : A list to store instances of the Employee class.
* `menu_choice: str = ''` : A variable to store the user's menu choice.
* `employee: dc.Employee()` : An instance of the Employee class.

## ChangeLog
- DLarson, 12.2.2023, Created Script

## Example
```python
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

```

# Employee Ratings : Processing Classes

## Description
This module contains classes and functions related to processing data.

### Module: processing_classes.py

### Class: FileProcessor

A collection of processing layer functions that work with JSON files.

### Methods

`read_employee_data_from_file(file_name: str, employee_data: list, employee_type: object)` -> list:

_Reads employee data from a file and populates the employee_data list._

Parameters:

* file_name (str): The name of the file to read data from.
* employee_data (list): The list to store employee data.
* employee_type (object): An instance of the Employee class.

Returns:
* employee_data (list): The updated list of employee data.

`write_employee_data_to_file(file_name: str, employee_data: list)` -> None:

_Writes employee data to a file in JSON format._

Parameters:

* file_name (str): The name of the file to write data to.
* employee_data (list): The list of employee data to write.

Returns:
* None

## ChangeLog
- DLarson, 12.2.2023, Created Script

## Example
```python
employees = pc.FileProcessor.read_employee_data_from_file(file_name=FILE_NAME, employee_data=employees, employee_type=employee)
```
### Output
```commandline
Bob,Smith,2023-06-28 00:00:00,3
Sue,Jones,2022-12-17 00:00:00,5
Data has been processed! 
[<data_classes.Employee object at 0x0000019F6E002270>, <data_classes.Employee object at 0x0000019F6E0022A0>]
```
# Employee Ratings : Presentation Classes

## Description
This module defines all necessary data presentation classes and functions used to present data to the user.

### Module: presentation_classes.py

### Class: IO
A collection of presentation layer functions that manage user input and output.

### Methods

`output_error_messages(message: str, error: Exception = None)` -> None:

_Displays custom error messages to the user._

Parameters:

* message (str): The error message to display.
* error (Exception): The exception (if any) associated with the error.

Returns:
* None

`output_menu(menu: str)` -> None:

_Displays the main menu of options to the user._

Parameters:

* menu (str): The string containing the main menu options.

Returns:
* None

`input_menu_choice()` -> str:

_Captures the user's menu choice and performs input validation._

Returns:
* choice (str): The user's menu choice.

`output_employee_data(employee_data: list)` -> None:

_Displays entered employee data to the user._

Parameters:
* employee_data (list): The list of employee data to display.

Returns:
* None

`input_employee_data(employee_data: list, employee_type: object)` -> list:

_Processes user-input data and adds it to the list of data._

Parameters:
* employee_data (list): The list of employee data.
* employee_type (object): An instance of the Employee class.

Returns:
* employee_data (list): The updated list of employee data.

## ChangeLog
- DLarson, 12.2.2023, Created Script

## Example
```python
# Example Usage
ioc.IO.output_menu(menu=MENU)
menu_choice = ioc.IO.input_menu_choice()
```
### Output
```commandline
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Show current employee rating data.
    2. Enter new employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------


Please enter your Menu choice number:
```
### Example
```python
employees = ioc.IO.input_employee_data(employee_data=employees, employee_type=employee)
ioc.IO.output_employee_data(employee_data=employees)
```
### Output
```commandline
Please enter your Menu choice number: 2
Please enter the employee's First Name: Vic
Please enter the employee's Last Name: Vu
Please enter the employee's Review Date= YYYY-MM-DD: 2023-12-07
Please enter the employee's Review Rating: 2

----------------------------------------------------------------------------------------------------
 Bob Smith is rated on 2023-06-28 as 3 (Solid)
 Sue Jones is rated on 2022-12-17 as 5 (Leading)
 Vic Vu is rated on 2023-12-07 as 2 (Building)
----------------------------------------------------------------------------------------------------
```

# Employee Ratings : Data Classes

## Description
This module defines all necessary classes and functions used to process data.

## ChangeLog
- DLarson, 12.2.2023, Created Script

## Class: Person
A class representing person data.

### Module: data_classes.py
The data_classes.py module contains classes and functions related to defining data structures.

### Properties
- `first_name (str)`: The person's first name.
- `last_name (str)`: The person's last name.

### Methods
`__init__(self, first_name: str = '', last_name: str = '')`: -> None

_Initializes the Person class._

Parameters:
* first_name (str): The person's first name.
* last_name (str): The person's last name.

Returns:
None

`__str__(self)` -> str:
Returns a formatted string representation of the person.


## Class: Employee
A class representing employee data, inheriting from the Person class.

### Properties
- `review_date (date)`: The date of the employee's review.
- `review_rating (int)`: The employee's review rating score.

### Methods
`__init__(self, first_name: str = '', last_name: str = '', review_date: date = date(1900, 1, 1), review_rating: int = 3)` -> None:

_Initializes an instance of the Employee class._

Parameters:
* first_name (str): The employee's first name.
* last_name (str): The employee's last name.
* review_date (date): The date of the employee's review.
* review_rating (int): The employee's review rating score.

Returns:
None

`__str__(self)` -> str:

_Returns a formatted string representation of the employee._

Returns:
str: A formatted string.

## Example
```python
# Example Usage
employee = dc.Employee(first_name="Vic", last_name="Vu", review_date=date(2023, 12, 7), review_rating=2)
```
### Output
```commandline
----------------------------------------------------------------------------------------------------
 Vic Vu is rated on 2023-12-07 as 2 (Building)
----------------------------------------------------------------------------------------------------
```