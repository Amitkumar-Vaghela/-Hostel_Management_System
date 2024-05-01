from tabulate import tabulate

class Student:
    def __init__(self, n, r, a, d, m):
        self.name = n
        self.roll_number = r
        self.age = a
        self.department = d
        self.mobile_number = m
        self.room_number = None

    def assign_room(self, room_number):
        self.room_number = room_number

    def get_info(self):
        return f"Name: {self.name}, Roll Number: {self.roll_number}, Age: {self.age}, Department: {self.department}, Mobile Number: {self.mobile_number}, Room Number: {self.room_number}"

class Hostel:
    def __init__(self):
        self.students = []
        self.rooms = {}

    def add_student(self):
        name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")
        age = input("Enter age: ")
        department = input("Enter department: ")
        mobile_number = input("Enter mobile number: ")
        student = Student(name, roll_number, age, department, mobile_number)
        self.students.append(student)
        return student

    def allocate_room(self, student):
        room_number = input(f"Enter room number for {student.name}: ")
        student.assign_room(room_number)
        self.rooms[room_number] = student

    def display_students(self):
        print("Students:")
        table = [["Name", "Roll Number", "Age", "Department", "Mobile Number", "Room Number"]]
        for student in self.students:
            table.append([student.name, student.roll_number, student.age, student.department, student.mobile_number, student.room_number])
        print(tabulate(table, headers="firstrow"))

    def display_room_allocation(self):
        print("Room Allocation:")
        table = [["Room Number", "Student Name", "Roll Number"]]
        for room_number, student in self.rooms.items():
            table.append([room_number, student.name, student.roll_number])
        print(tabulate(table, headers="firstrow"))

hostel = Hostel()


num_students = int(input("Enter the number of students to add: "))
for _ in range(num_students):
    hostel.add_student()


for student in hostel.students:
    hostel.allocate_room(student)

hostel.display_students()
hostel.display_room_allocation()

