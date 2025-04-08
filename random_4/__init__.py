import random

random_intiger = random.randint(1,10)
# print(random_intiger)
#
# random_floating = random.random()
# print(random_floating)
#
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
     print(fruit)

# Student heights filter with average

# student_heights = input("student Height?").split()
# for n in range(0, len(student_heights)):
#         student_heights[n] = int(student_heights[n])

# student_heights = [150,155,160,165,170]
# total_height = 0
# for height in student_heights:
#     total_height += height
#     print(f"total height = {total_height}")
#
# number_of_students = 0
# for student in student_heights:
#     number_of_students += 1
#     print(f"number of students = {number_of_students}")
#
# avrage_height = round(total_height/number_of_students)
# print(f"avrage height = {avrage_height}")


# Highest score in the class

student_scores = input("all students score?").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"highest scores in the class {highest_score}")

# -----range ----- no 1 + 100 = 5050

total = 0
for number in range(1,101):
 total += number
print(total)

# ----- addition all even no---
target = int(input("what is the number"))
even_sum = 0
for number in range(2,target + 1,2):
    even_sum += number
print(even_sum)

target1 = int(input("odd no"))
odd_num_sum = 0
for number in range(1,target1 +1,1):
    odd_num_sum += number
print(odd_num_sum)











