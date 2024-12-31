class Student:
    def __init__(self, studentID, studentName, studentDOB):
        self.__studentID = studentID
        self.__studentName = studentName
        self.__studentDOB = studentDOB

    def get_id(self):
        return self.studentID

    def get_name(self):
        return self.studentName

    def get_dob(self):
        return self.studentDOB

    def input():
        studentID = input("Enter student ID: ")
        studentName = input("Enter student name: ")
        studentDOB = input("Enter student dob: ")
        return Student(studentID, studentName, studentDOB)

    def __str__(self):
        return f"ID: {self.studentID}, Name: {self.studentName}, DOB: {self.studentDOB}"


class Course:
    def __init__(self, courseID, courseName):
        self.courseID = courseID
        self.courseName = courseName

    def get_id(self):
        return self.courseID

    def get_name(self):
        return self.courseName

    def input():
        courseID = input("Enter course ID: ")
        courseName = input("Enter course name: ")
        return Course(courseID, courseName)

    def __str__(self):
        return f"ID: {self.courseID}, Name: {self.courseName}"


class MarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_studentNumber(self):
        return int(input("Number of students: "))

    def input_student_information(self):
        num_students = self.input_studentNumber()
        for _ in range(num_students):
            student = Student.input()
            self.students.append(student)

    def input_courseNumber(self):
        return int(input("Number of the course: "))

    def input_course_information(self):
        num_courses = self.input_courseNumber()
        for _ in range(num_courses):
            course = Course.input()
            self.courses.append(course)

    def input_mark(self):
        id_course = input("Enter the course to input mark for it: ")
        if not any(course.get_id() == id_course for course in self.courses):
            print("Course not found!")
            return

        if id_course not in self.marks:
            self.marks[id_course] = {}

        for student in self.students:
            mark = float(input(f"Enter mark for student {student.get_name()} ID: {student.get_id()}: "))
            self.marks[id_course][student.get_id()] = mark

    def list_student(self):
        print("List of Students:")
        for student in self.students:
            print(student)

    def list_course(self):
        print("List of Courses:")
        for course in self.courses:
            print(course)

    def show_mark(self):
        id_course = input("Enter the course ID that you want to show mark: ")
        if id_course not in self.marks:
            print("Marks not found for this course!")
            return

        print(f"Marks for course {id_course}:")
        for student in self.students:
            id_student = student.get_id()
            if id_student in self.marks[id_course]:
                mark = self.marks[id_course][id_student]
                print(f"Mark for the student {student.get_name()} (ID: {id_student}): {mark}")
            else:
                print(f"Mark for the student {student.get_name()} (ID: {id_student}): Not available")

    def menu(self):
        while True:
            print("\n****** MENU ******")
            print("1.Input student information")
            print("2.Input course information")
            print("3.Input marks for a course")
            print("4.List of all students")
            print("5.List of all courses")
            print("6.Show marks for a course")
            print("7.EXIT")

            user_choice = int(input("Enter your choice between 1 - 7: "))

            if user_choice == 1:
                self.input_student_information()
            elif user_choice == 2:
                self.input_course_information()
            elif user_choice == 3:
                self.input_mark()
            elif user_choice == 4:
                self.list_student()
            elif user_choice == 5:
                self.list_course()
            elif user_choice == 6:
                self.show_mark()
            elif user_choice == 7:
                break
            else:
                print("Choice not found, try again!")
                continue


#Run
if __name__ == "__main__":
    management = MarkManagement()
    management.menu()
