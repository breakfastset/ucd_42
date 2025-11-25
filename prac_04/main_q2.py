from sys import argv
from math_functions import *

def main():

    if len(argv) == 3:         # if there are sufficient parameters
        num_1 = float(argv[1])
        num_2 = float(argv[2])
    else:                      # params not provided, ask the user
        num_1 = float(input("Num 1? "))
        num_2 = float(input("Num 2? "))

    print(f"{num_1:.1f} even? {not odd(num_1)}")  # 13.0 even? False
    print(f"{num_2:.1f} even? {not odd(num_2)}")  # 5.0 even? False

    print(f"{num_1}^2 = {square_of(num_1)}")   # 13^2 = 169
    print(f"{num_2}^2 = {square_of(num_2)}")   # 5^2 = 25

    print(f"{num_1}^{num_2} = {power_of(num_1, num_2):,}")
    print(f"{num_1}/{num_2} = {integer_divide(num_1, num_2)}")
    print(f"{num_1} == {num_2}? {equal(num_1, num_2)}")

main()

# 13.0 even? False
# 5.0 even? False
# 13.0^2 = 169.0
# 5.0^2 = 25.0

# 13.0^5.0 = 371293.0
# 13.0 / 5.0 = 2.0
# 13.0 equal to 5.0? False