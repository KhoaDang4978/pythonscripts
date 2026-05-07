# This is a class manager
print("Welcome to the class manager!")
print("-----------------------------")
class Student:
    def __init__(self, name, id, grades_per_subject):
        self.name = name
        self.id = id
        self.grades_per_subject = grades_per_subject
students = []
import json
import os
if os.path.exists("class.json"):
    with open("class.json") as f:
        students = json.load(f)
def get_average(student):
    grades = student["grades_per_subject"]
    if len(grades) == 0:
        return 0
    total = sum(float(g["grade"]) for g in grades)
    return total / len(grades)
while True:
    operation = str(input("Please choose your operation (add student, add grade, view a student's report card, view class leaderboard, flag below avg students): "))
    if operation == "add student":
        grades_per_subject = []
        name = str(input("Enter student name: "))
        id = str(input("Enter student ID: "))
        s = Student(name, id, grades_per_subject)
        students.append({
            "name": s.name,
            "id": s.id,
            "grades_per_subject": s.grades_per_subject
        })
        with open("class.json", "w") as f:
            json.dump(students, f)
        print("Student added!")
    elif operation == "add grade":
        name = str(input("Which student you want to add their grade? "))
        found = False
        for student in students:
            if (student['name']) == name:
                found = True
                subjects = []
                grades = []
                while True:
                    subject = str(input("Enter a subject (or 'exit' to exit): "))
                    if subject == "exit":
                        break
                    grade = str(input("Enter the subject's grade: "))
                    student["grades_per_subject"].append({
                        "subject": subject, 
                        "grade": float(grade)
                    })
                with open("class.json", 'w') as f:
                    json.dump(students, f)
        if not found:
            print("Student not found. Try again.")
    elif operation == "view a student's report card":
        name = str(input("Whose report card do you want to view? "))
        found = False
        for student in students:
            if (student['name']) == name:
                found = True
                print(f"{student['name']}'s report card: ")
                avg = get_average(student)
                print(f"Student's average: {avg:.1f}")
        if not found:
            print("Student not found. Try again.")
    elif operation == "view class leaderboard":
        sorted_students = sorted(students, key=get_average, reverse=True)
        for i, student in enumerate(sorted_students):
            print(f"{i+1}. {student['name']} - {get_average(student):.1f}")
    elif operation == "flag below avg students":
        for student in students:
            if get_average(student) < 50:
                print(f"AT RISK: {student['name']}")
    else:
        print("Invalid operation. Try again.")