# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   JD Blake, 5/10/2024, CONSTANT and variable defn
#   JD Blake, 5/11/2024, (0) Read .json file, (1) Input, (2) Display and (3) Write .json file
#   JD Blake, 5/12/2024, Added Error Handling for (0) Read .json file and (1) Input
# ------------------------------------------------------------------------------------------ #
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
# Define the Data Constants
FILE_NAME: str = ("Enrollments.json")
#FILE_NAME: str = ("Enrollment.json") #Misspelled Filename for FileNotFoung test
#FILE_NAME: str = ("DEBUG.json") #Empty data file for Exception Test

import json
import io as _io

# Define the Data Variables and constants
first_name: str = ''  # Holds the first name of a student entered by the user.
last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student: dict = {} # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
json_data: str = '' # Holds string for json data
file = _io.TextIOWrapper  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

import json #Import ... json stuff

# When the program starts, read the file data into a list of lists (table)
# Step 0: Extract the data from the file

#----------------OLD AND BUSTED---------------------
#for row in file.readlines():
    # Transform the data from the file
#    student_data = row.split(',')
#    student_data = [student_data[0], student_data[1], student_data[2].strip()]
    # Load it into our collection (list of lists)
#    students.append(student_data)
#-------------------------------------------------

#-----------------THE NEW HOTNESS-----------------
try:
    students = []  #THIS STEP IS SOMEHOW VERY SUPER-DUPER IMPORTANT!!!
    file = open(FILE_NAME, "r")
    students = json.load(file) #Reads json data into list
    file.close()
except FileNotFoundError as e:
    print("Text File Must Exist\n")
    print('In ... "Technical" Terms')
    print(e,e.__doc__, type(e), sep='\n')
except Exception as e:
    print("Non-specific error\n")
    print('In "Technical" Terms')
    print(e,e.__doc__, type(e), sep='\n')
finally:
    if file.closed==False:
        file.close()

# Present and Process the data
while (True):
    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Step 1: Input user data

    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            first_name:str = input("Enter the student's first name: ")
            if not first_name.isalpha():
                raise ValueError("First name should not contain numbers.")
            last_name:str = input("Enter the student's last name: ")
            if not last_name.isalpha():
                raise ValueError("Last name should not contain numbers.")
            course_name:str = input("Please enter the name of the course: ")
            student = {'FirstName': first_name, 'LastName': last_name, 'CourseName': course_name}
            students.append(student)
            print(f"You have registered {first_name} {last_name} for {course_name}.")
        except ValueError as e:
            print(e)
            print('In ... "Technical" Terms')
            print(e, e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("Non-specific error\n")
            print('In "Technical" Terms')
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            continue

    # Step 2: Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            message = "{} {} is enrolled in {}"
            print(message.format(student["FirstName"], student["LastName"], student["CourseName"]))
        print("-"*50)
        continue

    # Step 3: Save the data to a file
    elif menu_choice == "3":
        file = open(FILE_NAME, "w")
        #----------------OLD AND BUSTED-----------------
        #for student in students:
        #    csv_data = f"{student[0]},{student[1]},{student[2]}\n"
        #    file.write(csv_data)
        #    for student in students:
        #        print(f"Student {student[0]} {student[1]} is enrolled in {student[2]}")
        #-------------------------------------------------

        #---------------THE NEW HOTNESS------------
        json.dump(students, file) #'dump' (write) to file
        file.close()
        print('The following data was saved to', FILE_NAME)
        #-------------------------------------------
        continue

    # Step 4: Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1-4")

print("Program Ended")
