# ------------------------------------------------- #
# Title: Assignment08 Data Classes
# Description: define all necessary classes and functions
#   used to process data
# ChangeLog: (Who, When, What)
# DLarson,12.2.2023,Created Script
# ------------------------------------------------- #

from datetime import date


# Creating a Person Class (Parent Class)
class Person:
    """
    A class representing person data.

    Properties:
    - first_name (str): The person's first name.
    - last_name (str): The person's last name.

    ChangeLog:
    - DLarson, 12/02/2023: Created the class.
    """

    # Modifying initialization to add first_name and last_name properties to the constructor
    def __init__(self, first_name: str = '', last_name: str = ''):
        self.first_name = first_name
        self.last_name = last_name

    # Create a "getter" or Accessor for first_name property
    @property
    def first_name(self):
        """
        Gets the private "first_name" property on the instance object

            ChangeLog: (Who, When, What)
            DLarson,12.02.2023,Created Function
        :return: self.__first_name.title()
        """
        return self.__first_name.title()

    # Create a "setter" or Mutator for first_name property
    @first_name.setter
    def first_name(self, value: str):
        """
        Sets the private "first_name" property on the Person Class instance after data validation

            ChangeLog: (Who, When, What)
            DLarson,11.25.2023,Created Function
        :param value: str
        :return: None
        """
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("The First Name should only contain letters. ")

    # Create a "Getter" or Accessor for last_name property
    @property
    def last_name(self):
        """
        Gets the private "last_name" property on the instance object

            ChangeLog: (Who, When, What)
            DLarson,12.02.2023,Created Function
        :return: self.__last_name.title()
        """
        return self.__last_name.title()

    # Create a "Setter" or Mutator for last_name property
    #   Include validation and Error Handling
    @last_name.setter
    def last_name(self, value: str):
        """
        Sets the private "last_name" property on the Person Class instance after data validation

            ChangeLog: (Who, When, What)
            DLarson,11.25.2023,Created Function
        :param value: str
        :return: None
        """
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("The Last Name should only contain letters. ")

    # OVERRIDE default __str__() method's behavior, return comma-separated string
    def __str__(self):
        return f'{self.first_name},{self.last_name}'


# Creating an Employee Class (Child Class of Parent "Person")
class Employee(Person):
    """
    A class representing employee data.

    Properties:
    - first_name (str): The employee's first name.
    - last_name (str): The employee's last name.
    - review_date (str): The date of the employee's review.
    - review_rating (int): The employee's review rating score.

    ChangeLog:
    - DLarson, 12.02.2023: Created the class.
    """

    # Modify the Employee constructor to pass the first_name and last name variables
    #   and reset as employee_ name variables, add new review_data + review_rating child-class
    #   specific variables
    def __init__(self, first_name: str = '', last_name: str = '',
                 review_date: date = date(1900, 1, 1), review_rating: int = 3):
        super().__init__(first_name=first_name, last_name=last_name)
        self.review_date = review_date
        self.review_rating = review_rating

    # Create a "Getter" or Accessor for the review_date property
    @property
    def review_date(self):
        """
        Gets the private "review_date" property on the Employee Class object

            ChangeLog: (Who, When, What)
            DLarson,12.02.2023,Created Function
        :return: self.__review_date
        """
        return self.__review_date

    # "Setter" or Mutator for the review_date property
    @review_date.setter
    def review_date(self, value: date):
        """
        Sets the private "review_date" property on the Employee Class object

            ChangeLog: (Who, When, What)
            DLarson,12.02.2023,Created Function
        :param value: datetime
        :return: None
        """

        if date.isoformat(value):
            self.__review_date = value
        else:
            raise ValueError("Date must be entered as YYYY-MM-DD : ex. 2000-02-30 !")

    @property
    def review_rating(self):
        """
        Gets the private "review_rating" property on the Employee Class object

            ChangeLog: (Who, When, What)
            DLarson,12.02.2023,Created Function
        :return: self.__review_rating
        """
        return self.__review_rating

    @review_rating.setter
    def review_rating(self, value: int):
        """
        Sets the private "review_rating" property on the Employee Class object

            ChangeLog: (Who, When, What)
            DLarson,12.02.2023,Created Function
        :param value: int
        :return: None
        """
        try:
            self.__review_rating = int(value)
        except ValueError:
            raise ValueError("Review Rating must be 1, 2, 3, 4, or 5! ")

    # OVERRIDE default __str__() method's behavior, return comma-separated string
    def __str__(self):
        return f'{self.first_name},{self.last_name},{self.review_date},{self.review_rating}'


if __name__ == '__main__':
    print("This file is not meant to be run. Please run 'main.py' ")
