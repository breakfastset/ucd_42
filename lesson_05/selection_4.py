# 4. nested if
# used when you are testing > 1 variables' values

# if the person's age is 65 and above and
#     the person is not working
#    amount_given = 800
# if the person is 65 and above and working
#    amount_given = 500
# if the person is 40 to 65 and not working
#    amount_given = 600
# if the person is 40 to 65 and working
#    amount_given = 200

age = 68
is_working = False
amount_given = 0

if age >= 65 and not is_working:
    amount_given = 800
elif age >= 65 and is_working:
    amount_given = 500
elif 40 <= age < 65 and not is_working:
    amount_given = 600
elif 40 <= age < 65 and is_working:
    amount_given = 200

print(f"You will receive ${amount_given:.2f}")

print("--" * 30)
if age >= 65:
    if not is_working:
        amount_given = 800
    else:
        amount_given = 500

elif 40 <= age < 65:
    if not is_working:
        amount_given = 600
    else:
        amount_given = 200

print(f"You will receive ${amount_given:.2f} (nested if)")