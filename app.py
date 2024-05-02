from flask import Flask, request, jsonify
from tabulate import tabulate

app = Flask(__name__)

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
        return {
            "name": self.name,
            "roll_number": self.roll_number,
            "age": self.age,
            "department": self.department,
            "mobile_number": self.mobile_number,
            "room_number": self.room_number
        }

class Hostel:
    def __init__(self):
        self.students = []
        self.rooms = {}

    def add_student(self, name, roll_number, age, department, mobile_number):
        student = Student(name, roll_number, age, department, mobile_number)
        self.students.append(student)
        return student

    def allocate_room(self, student, room_number):
        student.assign_room(room_number)
        self.rooms[room_number] = student

    def get_students(self):
        return [student.get_info() for student in self.students]

    def get_room_allocation(self):
        return [{"room_number": room_number, "student_name": student.name, "roll_number": student.roll_number} for room_number, student in self.rooms.items()]

hostel = Hostel()

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(hostel.get_students())

@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()
    student = hostel.add_student(data["name"], data["roll_number"], data["age"], data["department"], data["mobile_number"])
    return jsonify(student.get_info())

@app.route("/room_allocation", methods=["GET"])
def get_room_allocation():
    return jsonify(hostel.get_room_allocation())

@app.route("/room_allocation", methods=["POST"])
def allocate_room():
    data = request.get_json()
    student = next((s for s in hostel.students if s.roll_number == data["roll_number"]), None)
    if student:
        hostel.allocate_room(student, data["room_number"])
        return jsonify({"message": "Room allocated successfully"})
    return jsonify({"error": "Student not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
