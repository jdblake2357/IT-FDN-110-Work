# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   JD Blake, 5/10/2024, CONSTANT and variable defn
#   JD Blake, 5/11/2024, (0) Read .json file, (1) Input, (2) Display and (3) Write .json file
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
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
first_name: str = ''  # Holds the first name of a student entered by the user.
last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student: dict = {} # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
json_data: str = '' # Holds string for json data
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

import json #Import ... json

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file

#----------------OLD AND BUSTED---------------------
#for row in file.readlines():
    # Transform the data from the file
#    student_data = row.split(',')
#    student_data = [student_data[0], student_data[1], student_data[2].strip()]
    # Load it into our collection (list of lists)
#    students.append(student_data)

#-----------------THE NEW HOTNESS-----------------
file = open(FILE_NAME, "r")
#Don't know why I have to use a dummy variable 'data', but the script doesn't work without it?
data = json.load(file) #Reads json data into list
file.close()

students.append(data) #append data to students

# Present and Process the data
while (True):
    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        first_name:str = input("Enter the student's first name: ")
        last_name:str = input("Enter the student's last name: ")
        course_name:str = input("Please enter the name of the course: ")
        student = {'FirstName': first_name, 'LastName': last_name, 'CourseName': course_name}
        students.append(student)
        print(f"You have registered {first_name} {last_name} for {course_name}.")
        continue

    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            message = "{} {} is enrolled in {}"
            print(message.format(student["FirstName"], student["LastName"], student["CourseName"]))
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        file = open(FILE_NAME, "w")
        #----------------OLD AND BUSTED-----------------
        #for student in students:
        #    csv_data = f"{student[0]},{student[1]},{student[2]}\n"
        #    file.write(csv_data)

        #---------------THE NEW HOTNESS------------
        json.dump(students, file) #'dump' (write) to file
        file.close()
        print("The following data was saved to file!")
    #    for student in students:
    #        print(f"Student {student[0]} {student[1]} is enrolled in {student[2]}")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1-4")

print("Program Ended")
