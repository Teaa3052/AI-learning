from data import students 
from data import numbers
from student_analysis import average_grade, best_student, students_above_average, worst_student, grade_distribution, student_names
from student_analysis import num_x2, numx2, even_numbers, plusOne, square_numbers

average = average_grade(students)
print(average)

best = best_student(students)
print(best)

above_average_students = students_above_average(students)
print(above_average_students)

worst = worst_student(students)
print(worst["name"])

distribution = grade_distribution(students)
print(distribution)

list_of_numbers = num_x2(numbers)
print(list_of_numbers)

dictionary_of_nums = numx2(numbers)
print(dictionary_of_nums)

### što šaljem funkciji? 
### što funkcija vraća? (return)
### što zapravo ispisujem? 

list_of_names = student_names(students)
print(list_of_names)

list_of_even = even_numbers(numbers)
print(list_of_numbers)

addOne = plusOne(numbers)
print(addOne)

squareNumbers = square_numbers(numbers)
print (squareNumbers)
