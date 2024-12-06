students = []
courses = []
marks = {}

#Input number of students
def input_studentNumber():
    return int(input("Number of students: "))

#Input student information 
def input_student_information():
    num_students = input_number_students()
    for _ in range(num_students):
        studentID = input("Enter student ID: ")
        studentName = input("Enter student name: ")
        studentDOB = input("Enter student dob: ")

        student = {
            "ID": studentID,
            "Name": studentName,
            "Dob": studentDOB
        }   
        students.append(student)
    return students

#Input course information
def input_courseNumber():
    return int(input("Number of the course: "))

def input_course_information():
    num_course = input_courseNumber()
    for _ in range(num_course):
        courseID = input("Enter course ID: ")
        courseName = input("Enter course name: ")
        course = {
            "ID": courseID,
            "Name": courseName
        }
        courses.append(course)
    return courses

#Select course & Input mark
def input_mark():
    id_course = input("Enter the course to input mark for it: ")
    if (not any(course["ID"] == id_course for course in courses)):
        print("Course not found!")
        return
    marks[id_course] = {}

    #Input mark for each student
    for student in students:
        mark = float(input("Enter mark for student  " + student["Name"] + " ID: " + student["ID"] + ": "))
        marks[id_course][student["ID"]] = mark

#List of students
def list_student():
    for student in students:
        print("Student: ")
        print("ID: " + student["ID"] + " Name: " + student["Name"] + " Dob: " + student["Dob"])

#List of courses  
def list_course():
    for course in courses:
        print("Course: ")
        print("ID: " + course["ID"] + " Name: " + course["Name"])

#Student marks for a course:
def show_mark():
    id_course = input("Enter the course ID that you want to show mark: ")
    # Check ID course and print mark
    if id_course not in marks:
        print("marks not found for this course!")
        return
    
    for student in students:
        id_student = student["ID"]
        if student["ID"] in marks[id_course]:
            print("Mark for the student " + student["ID"] + " Name: " + student["Name"] + "in this " + id_course + ": ")
def menu():
    while True:
        print("\n****** MENU ******")
        print("1.Input student information")
        print("2.Input course information")
        print("3.Input marks for a course")
        print("4.List of all students")
        print("5.List of all courses")
        print("6.Show marks for a course")
        print("7.EXIT")

        user_choice = int(input("Enter your choice between 1 - 7 "))

        if (user_choice == 1):
            input_student_information()
        elif (user_choice == 2):
            input_course_information()
        elif (user_choice == 3):
            input_mark()
        elif (user_choice == 4):
            list_student()
        elif (user_choice == 5):
            list_course()
        elif (user_choice == 6):
            show_mark()
        elif (user_choice == 7):
            break
        else: 
            print("Choice not found,try again! ")
        continue

#Run  
menu()