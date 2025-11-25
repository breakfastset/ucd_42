# 3. if elif elif ... else
# meant for multiple possible outcomes
score = 68

if 70 <= score <= 100:
    grade = "HD"
elif 60 <= score < 70:
    grade = "D"
elif 40 <= score < 60:
    grade = "P"
elif 0 <= score < 40:
    grade = "F"
else:
    grade = "Invalid"

print(f"You received grade {grade} for {score}")

