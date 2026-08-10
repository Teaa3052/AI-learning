def average_grade(students):
    total = 0

    for student in students:
        total += student["grade"]

    average = total / len(students)

    return average

def best_student(students): 

    current_best = students[0]

    for student in students: 
        if student["grade"] > current_best["grade"]: 
            current_best = student

    return current_best


def students_above_average(students): 

    average = average_grade(students)

    above_average= []

    for student in students:
        if student["grade"] > average:
            above_average.append(student)

    if not above_average:
        print("No students found")

    return above_average


def worst_student(students): 

    current_worst = students[0]

    for student in students: 
        if student["grade"] < current_worst["grade"]:
            current_worst = student

    return current_worst


def grade_distribution(students): 

    counts = {}

    for student in students:

        grade = student["grade"]

        if grade in counts:
            counts[grade] +=1
        else: 
            counts[grade] = 1

    return counts 

def num_x2(numbers):
    return [ num * 2 for num in numbers ] ## list 

def numx2(numbers): 
    return {
        num: num * 2
        for num in numbers
    } ## dict 

def student_names(students):
    return [ student["name"] for student in students ]

def even_numbers(numbers): 
    return [
        num
        for num in numbers
        if num % 2 == 0
    ]

def plusOne(numbers):
    return list(map(lambda x: x + 1, numbers))

def square_numbers(numbers): 
    return list(map(lambda x: x ** 2, numbers))

def student_names_map(students):
    return list(map(lambda x: x["name"], students))