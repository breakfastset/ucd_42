# A teacher wishes to distribute
# her sweets equally to her 23 students.
# She has 400 sweets.
# How many sweets does each student get?
# How many sweets are left over?

num_sweets = 400
num_students = 23

sweets_per_student = num_sweets // num_students
remainder = num_sweets % num_students

print("Sweets per student:", sweets_per_student)
print("  Sweets left over:", remainder)