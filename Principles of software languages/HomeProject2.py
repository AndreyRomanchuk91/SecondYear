class Course:
    def __init__(self, name, grade=101):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"{self.name}: {self.grade}"


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.__id = student_id
        self.courses = []

    def getName(self):
        return self.name

    def getID(self):
        return self.__id

    def addCourse(self, course):
        if 0 <= course.grade <= 100:
            self.courses.append(course)
        else:
            print(f"Invalid grade for course '{course.name}'. Course not added.")

    def getAverageGrade(self):
        if not self.courses:
            return None
        total_grade = sum(course.grade for course in self.courses)
        return total_grade / len(self.courses)

    def __str__(self):
        return f"Student: {self.name}, ID: {self.__id}, Courses: {', '.join(str(course) for course in self.courses)}"


def read_student_data(file_path):
    '''
    Reads student data from a file
    :param file_path: A path of a file
    :return: List of students
    '''
    students = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    data = line.split('\t')
                    name_id = data[0].split()
                    name = ' '.join(name_id)
                    student_id = data[1]
                    courses_info = data[2].split(';')
                    student = Student(name, student_id)
                    for course_info in courses_info:
                        course_data = course_info.split('#')
                        course_name, grade = course_data[0], int(course_data[1])
                        course = Course(course_name, grade)
                        student.addCourse(course)
                    students.append(student)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    finally:
        file.close()
    return students


def calculate_average_grade(students, student_name):
    '''
    Canculate the average grade of a specific student
    :param students: List of all the students
    :param student_name: Name of a specific student
    :return: Prints the average grade
    '''
    student_name = student_name.strip().lower()
    matching_students = filter(lambda student: student_name in student.getName().strip().lower(), students)
    avg_grades = list(map(lambda student: (student.getID(), student.getAverageGrade()), matching_students))
    if not avg_grades:
        print("Student not found.")
        return
    for student_id, avg_grade in avg_grades:
        if avg_grade is not None:
            print(f"Student ID: {student_id}, Average Grade: {avg_grade:.2f}")
        else:
            print(f"Student ID: {student_id} has no courses.")






def calculate_course_average(students, course_name):
    '''
    Calculating a given course average grade for all the students
    :param students: A list of all the students
    :param course_name: A given course name to calculate average
    :return: Printing a given course average grade
    '''
    students_with_course = filter(
        lambda student: any(course for course in student.courses if course.name == course_name), students)
    grades = map(lambda student: next(course.grade for course in student.courses if course.name == course_name),
                 students_with_course)
    grades_list = list(grades)
    if not grades_list:
        print(f"No grades found for the course '{course_name}'.")
        return
    average_grade = sum(grades_list) / len(grades_list)
    print(f"Average grade for {course_name}: {average_grade:.2f}")


def write_students_average_to_file(students, file_path):
    '''
    Writes to a txt file all of the average grades
    :param students: List of all the students
    :param file_path: A path to a file to write tp
    :return: None
    '''
    with open(file_path, 'w') as file:
        for student in students:
            avg_grade = student.getAverageGrade()
            if avg_grade is not None:
                file.write(f"{student.getID()} {avg_grade:.2f}\n")
            else:
                file.write(f"{student.getID()} No grades available\n")



def main():
    file_path = input("Enter the path to the file containing student information: ")
    try:
        students = read_student_data(file_path)
        while True:
            print("\nMenu:")
            print("1. Calculate average grade for a student")
            print("2. Calculate average grade for a course")
            print("3. Calculate and write all students' averages to a file")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                student_name = input("Enter the name of the student: ")
                calculate_average_grade(students, student_name)
            elif choice == "2":
                course_name = input("Enter the name of the course: ")
                calculate_course_average(students, course_name)
            elif choice == "3":
                output_file = input("Enter the name for the output file (without extension): ")
                if not output_file.lower().endswith('.txt'):
                    output_file += '.txt'
                write_students_average_to_file(students, output_file)
                print(f"Average grades written to {output_file}.")
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter '1', '2', '3', or '4'.")
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print("An error occurred:", e)




if __name__ == "__main__":
    main()
