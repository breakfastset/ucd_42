print("-- Our simple division program --")

try:
    num_1 = int(input("Enter a number: "))
    num_2 = int(input("Enter the divisor: "))
    print(f"Quotient of {num_1} / {num_2} = {num_1 // num_2}")
except ZeroDivisionError:
    print("The divisor cannot be zero!")
except ValueError:
    print("Both number and divisor must be integers!")

print("-- End of simple division program --")