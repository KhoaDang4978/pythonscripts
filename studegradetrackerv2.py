# This is a student grade tracker
print("Welcome to the student grade tracker!")
print("-------------------------------------")
grades = []
names = []
count = 0
class_sum = 0
import os
if os.path.exists("grades.txt"):
    with open("grades.txt") as f:
        for line in f:
            parts = line.split(": ")
            names.append(parts[0])
            grades.append(float(parts[1]))
            count += 1
            class_sum += float(parts[1])
while True:
    student_name = str(input("Please input student's name (or 'done' to finish): "))
    names.append(student_name)
    count += 1
    if student_name == "done":
        names.remove("done")
        count -= 1
        print("List: ")
        for i in range(len(names)):
            print(f"{names[i]}: {grades[i]}")
        print(f"Class average: ({class_sum / count})")
        highest = max(grades)
        lowest = min(grades)
        highest_index = grades.index(highest)
        print(f" Highest score: {names[highest_index]} with {highest}")
        lowest_index = grades.index(lowest)
        print(f" Lowest score: {names[lowest_index]} with {lowest}")
        break
    student_grade = float(input(f"Please input {student_name}'s grade: "))
    if student_grade > 100 or student_grade <0:
        print("Invalid grade!")
        names.remove(student_name)
        count -= 1
    else: 
        grades.append(student_grade)
        class_sum += student_grade
with open("grades.txt", "w") as f:
    for i in range(len(names)):
        f.write(f"{names[i]}: {grades[i]}\n")
