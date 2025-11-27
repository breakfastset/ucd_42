# supposed you are to key in your age.
# an acceptable age is between 18 to 99
#
# method 1: Look before you leap (LBYL)
valid_input = False        # assume the input is wrong
while not valid_input:     # while input is wrong
    age = input("Age (18 to 99)? ")
    if age.isnumeric():  # if possible to convert
        age = int(age)   # convert to integer
        if 18 <= age <= 99:    # if input is totally correct
            valid_input = True   # set to True to exit the loop
        else:
            print("Age is from 18 to 99 only.")
    else:
        print("Age must be a number")
print(f"Great! You are {age+1} next year!")

# method 2: Easier to Ask for Forgiveness than Permission (EAFP)
valid_input = False
while not valid_input:
    try:
        age = int(input("Age (18 to 99): "))
        if 18 <= age <= 99:
            valid_input = True
        else:
            print("Age is from 18 to 99 only.")
    except ValueError:
        print("Age must be a number")

print(f"Great! You are {age+1} next year!")