age_list = [13, 27, 10, 34, 65, 8, 43, 49, 51, 21, 23, 11]

# for each element loop
for age in age_list:         # age is a local and temporary variable
    age = age + 1            # does not affect elements in age_list
    print(f"new age: {age}")

print(age_list)   # nothing was changed!
print()

# to modify, we need to use indexed loop
for i in range(len(age_list)):
    age_list[i] = age_list[i] + 1    # will modify the actual element

print(age_list)   # the updated list