from dataclasses import dataclass

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def describe(self):
        return self.name + " - ocjena " + str(self.grade)


student1 = Student("Ana", 5)
student2 = Student("Marko", 3)
print(student1.describe())
print(student2.describe())

@dataclass
class StudentDC:
    name: str
    grade: int

s = StudentDC("Ana", 5)
print(s.name, s.grade)
print(s)

@dataclass
class StudentRecord:
    name: str
    grade: int

def average_grade(students: list[StudentRecord]) -> float:
    total = 0
    for student in students:
        total += student.grade
    average = total / len(students)
    return average

students = [
    StudentRecord("Ana", 5),
    StudentRecord("Marko", 3),
    StudentRecord("Ivana", 4),
]

print(average_grade(students))