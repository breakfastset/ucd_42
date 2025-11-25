# and - all conditions must be True to be True
# or - as long as one condition is True to be True
# not - flip True to False, False to True

gender = "f"
age = 25

entry_allowed = (gender == "f" and age >= 21)
print(entry_allowed)
print()

is_member = False
seat_type = "business"
# allow passenger to enter cafe if
#    the passenger is a member OR
#    the passenger is taking business class
# cafe_allowed = (is_member == True or seat_type == "business")
cafe_allowed = (is_member or seat_type == "business")
print(cafe_allowed)
print()

# 'not' is to negate or flip
# if it is a variable, it is comparing to False
# course will be opened if there are not less than 10 students
# course will be opened if there are 10 or more students
student_count = 15
course_opened = not (student_count < 10)
course_opened_2 = (student_count >= 10)  # same as above
print(course_opened)   # True
print(course_opened_2)   # True
print()

is_zoo_member = False
# You are not a zoo member <- is this statement True?
print(not is_zoo_member)   # not False  -> True


