from data import numbers
from student_analysis import (
    average_grade,
    best_student,
    students_above_average,
    worst_student,
    grade_distribution,
    student_names,
    numbers_x2,
    numbers_x2_dict,
    even_numbers,
    plus_one,
    square_numbers
)

import json


# =========================
# Load students
# =========================

with open("students.json", "r") as file:
    students = json.load(file)


# =========================
# Student analysis
# =========================

print("Student names:", student_names(students))

average = average_grade(students)
print("Average grade:", average)

best = best_student(students)
print("Best student:", best)

above_average_students = students_above_average(students)
print("Students above average:", above_average_students)

worst = worst_student(students)
print("Worst student:", worst["name"])

distribution = grade_distribution(students)
print("Grade distribution:", distribution)


# =========================
# Update students
# =========================

new_student = {
    "name": "Petra",
    "grade": 5
}

students.append(new_student)

with open("students_updated.json", "w") as file:
    json.dump(students, file, indent=4)


# =========================
# List practice
# =========================

print("Numbers x2:", numbers_x2(numbers))

print("Numbers x2 dictionary:", numbers_x2_dict(numbers))

print("Even numbers:", even_numbers(numbers))

print("Numbers +1:", plus_one(numbers))

print("Squared numbers:", square_numbers(numbers))

### što šaljem funkciji? 
### što funkcija vraća? (return)
### što zapravo ispisujem? 