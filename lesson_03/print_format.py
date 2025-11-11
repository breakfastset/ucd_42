name = "Chewy"       # string
height = 2.282132    # 2.28 m tall, float
age = 234            # int

# Expected output:
# Ms Chewy is 234 years old. She stands at 2.28m tall

# method 1, using commas
print("Ms Chewy is", age, "years old. She stands at", round(height, 2), "m tall")

# method 2, using + (string concatenation)
print("Ms Chewy is " + str(age) + " years old. She stands at "
      + str(round(height, 2)) + "m tall")

# method 3, using .format() -> only available in Python 3.9 onwards
print("Ms {} is {} years old. She stands at {:.2f}m tall".format(name, age, height))

# method 4, using f -> only available in Python 3.10 onwards
print(f"Ms {name} is {age} years old. She stands at {height:.2f}m tall")
