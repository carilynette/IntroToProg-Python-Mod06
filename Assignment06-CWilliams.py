# ------------------------------------------------------------------------------------------ #
# Title: Assignment06 - Working with Functions, Classes and SoC.
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
# RRoot,1/1/2020,Created Script
# CWilliams, 11/17/25, Modified Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

# --- Program Data -------------------------------- #
# This is the main list we work with throughout the program.
students: list =[] #a table (list) of student records (dict).
menu_choice: str = ""

#Processing_____________#
class FileProcessor:
    """
    A collection of processing layer functions that work with JSON files.

    ChangeLog: (Who, When, What)
    RRoot,1.1.2020,Created Class
    CWilliams, 11/20/25, Modified Class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        Reads student data from a JSON file and returns an updated list.

        :param file_name:  name of the JSON file to read from.
        :param student_data: the current list of students.
        :return: the list of students in the file already.
        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str,student_data:list):
        """
        Writes the current list of students into the JSON file.
        :param file_name: the JSON file name being written.
        :param student_data: the list of students to be saved.
        :return:
        """

        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()

#Presentation____________###
class IO:
    """
    A collection of presentation layer functions that manage user input and output.

    Changelog: (Who,When, What)
    CWilliams, 11/20/25, Created Class
    CWilliams,11/20/25,Added a function to display the data
    """

    @staticmethod
    def output_error_messages(message: str,error: Exception = None):
        """This function displays a custom error message to the user

        Changelog (Who, When, What)
        CWilliams, 11/17/25, Created function , added function to display the message.

        :param message: the custom error message.
        :param error: the custom error message.
        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """This function displays a custom menu to the user

        Changelog (Who, When, What)
        CWilliams, 11/20/25, Added a function to display the menu text
        CWilliams,11/20/25,Added a function to display custom error messages

        :param menu: the menu being displayed
        :return: None
        """
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """This function displays a custom menu to the user
        Gets a menu choice from the user, with basic validation.

        Changelog (Who, When, What)
        CWilliams, 11/20/25, Added a function to display the data

        :return: the user's menu choice as a string
        """
        menu_choice: str = "0"
        try:
            menu_choice = input("Enter menu choice: ")
            if menu_choice not in ("1","2","3","4"):
                raise Exception("Invalid option. Please only choose 1, 2, 3 or 4.")
        except Exception as e:
                IO.output_error_messages(str(e), e)

        return menu_choice

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the student's first and last name and a course name from the user
        :param student_data: the current list of students.
        :return: the list after adding the new student registration.
        """

        try:
            # Get the first name
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("Only alphabetic characters are allowed.")

            # Get the last name
            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            # Get the Course Name
            course_name = input("What is the name of the course? ")

            # Build a student dictionary
            new_student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}

            # Add the new student to the existing list
            student_data.append(new_student)
        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data


    @staticmethod
    def output_student_courses(student_data: list):
        """This function displays each student's name and courses.

        Changelog (Who, When, What)
        CWilliams, 11/20/25, Added a function to display the data
        :param student_data: the list of students records (dicts).
        :return: None
        """
        for student in student_data:
            print(student["FirstName"], student["LastName"], student["CourseName"])


#  End of function definitions
# --- Main Script --------------------------------- #

# 1. Load any existing students from the JSON file into students
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

#2 Main program loop
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # Register a new student, then display updated student_data
    if menu_choice == "1":
        students= IO.input_student_data(student_data=students)
        IO.output_student_courses(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME,student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break
    else:
        print("Please only choose option 1, 2, 3 or 4")

print("Program Ended")
