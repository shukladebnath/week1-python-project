class Student:
    def __init__(self, name, age, address, student_id):
        # str: stores student's name
        self.name = name

        # int: stores student's age
        self.age = age

        # str: stores student's address
        self.address = address

        # str: stores Student ID
        self.student_id = student_id


def main():
    # list: stores multiple Student objects
    students = []

    # int: number of students
    number = int(input("Enter number of students: "))

    for i in range(number):
        print("\nStudent", i + 1)

        # str
        name = input("Enter name: ")

        # int
        age = int(input("Enter age: "))

        # str
        address = input("Enter address: ")

        # str
        student_id = input("Enter Student ID: ")

        student = Student(name, age, address, student_id)

        # Add student to the list
        students.append(student)

    # Sort students by age
    students.sort(key=lambda student: student.age)

    print("\nStudents sorted by age:")
    print("-----------------------")

    for student in students:
        print(
            student.name,
            "-", student.age,
            "-", student.address,
            "-", student.student_id
        )


main()