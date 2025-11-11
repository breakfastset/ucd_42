number_str1 = "13"
number_str2 = "3.14"

# a string can be converted to a float
# provided it contains only digits and .
number_1 = float(number_str1)
number_2 = float(number_str2)
print(number_1 + 1)
print(number_2 + 1)

# a string can be converted to an int
# provided it contains only digits
number_3 = int(number_str1)
# number_4 = int(number_str2)  # error, has .
print(number_3 + 1)
# print(number_4 + 1)  # error due to above

# a float can be converted to an int
# and vice versa
x = 10
y = 9.81
print(float(x))   # 10.0
print(int(y))     # 9, truncate the decimal points

print(bool(False))     # False value
print(bool("False"))   # string -> True



