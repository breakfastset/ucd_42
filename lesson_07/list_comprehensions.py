numbers = [33, 45, -12, -5, 91, 50, 60, 20, 13, -8, 4]

# create a list from above such that it only contains positive numbers
# 1. normal method (NOT list comprehension)
positives = []
for num in numbers:
    if num >= 0:
        positives.append(num)

print(positives)

# 2. list comprehension
# <list_name> = [ element (if condition else?) for element in list (if condition?) ]
positives_1 = [num for num in numbers if num >= 0]
print(positives_1)

positive_evens = [num for num in numbers if num >= 0 and num % 2 == 0]
print(positive_evens)

squares = [num ** 2 for num in numbers]
print(squares)

# collect '+' if >= 0 '-' if < 0
signs = ["+" if num >= 0 else "-" for num in numbers]
print(signs)

positive_odd_count = len([num for num in numbers if num > 0 and num % 2 == 1])
print(f"Number of positive odd numbers: {positive_odd_count}")

positive_odd_count_1 = sum([1 for num in numbers if num > 0 and num % 2 == 1])
print(positive_odd_count_1)


