# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   JD Blake, 5/19/24, Working draft initiated
#
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

FILE_NAME: str = "Enrollments_wk.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.

class FileProcessor:
    """
    File processing functions
    ChangeLog:
    JD Blake, 5/19/24, Created Class
    """
    pass
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        Function to open and read json file data into list
        ChangeLog:
        JD Blake, 5/19/24, Created Function
        Returns: student_data
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
    def write_data_to_file(file_name: str, student_data: list):
        """
        Function to write data stored in 'students' list to json file
        ChangeLog:
        JD Blake, 5/19/24, Created Function
        :param file_name:
        :param student_data:
        :return: None
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

class IO:
    """
    Functions to control input/output (IO)
    ChangeLog:
    JD Blake, 5/19/24, Created Class
    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        Function to display a custom error messages to the user
        ChangeLog:
        JD Blake, 5/19/24, Created Function
        Returns: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        Function displays the menu to the user
        ChangeLog:
        JD Blake, 5/19/24, Created Function

        Returns: None
        """
        print()
        print(menu, '\n')  # Added new line to make it look nicer
        #print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """
        Function prompts user for menu choice
        ChangeLog
        JD Blake, 5/19/24, Created Function
        Returns: choice (string with the users choice)
        """
        choice = "0"
        try:
            choice = input("What would you like to do? ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing the exception object to avoid the technical message

        return choice

    @staticmethod
    def input_student_data(student_data: list):
        """
        Function gets the first name, last name, and course name from the user
        and append it to list
        ChangeLog:
        JD Blake, 5/19/24, Created Function
        Returns: None
        """

        try:
            # Input the data
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            course_name = input("What is the course name? ")

            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}
            student_data.append(student)

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data

    @staticmethod
    def output_student_data(student_data: list):
        """
        Function displays current student registration data stored in 'students' list
        ChangeLog:
        JD Blake, 5/19/24, Created Function
        Returns: None
        """
        # Process the data to create and display a custom message
        print("-" * 50)
        for student in students:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)



# Beginning of the main body of this script
#-------------------------------------------
#
# Read In file data to 'students' list
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

#print(students) # Used to verify that file data was written to 'students' list

# These operations repeat until the user opts to quit the program

while True:  # Loop will run until it sees 'break'
    IO.output_menu(menu=MENU)  # Calls menu display function
    menu_choice = IO.input_menu_choice()  # Calls menu choice input function

#    print(menu_choice)  # Used to verify menu_choice input

    if menu_choice == '1': # Register student for course
        IO.input_student_data(student_data=students)  # Calls registration function
        continue

    elif menu_choice == '2':
        IO.output_student_data(student_data=students)
        continue

    elif menu_choice == '3':
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == '4':
        break

print("Program Ended")