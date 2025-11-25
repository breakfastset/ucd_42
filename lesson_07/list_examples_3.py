numbers = [13, 7, 8, 2, 5, 0, 5, 9, 1, 20, 5, 16, 17, 4]

print(numbers.count(5))   # 3 instances of 5

numbers.reverse()         # reverse the order (not sort)
print(numbers)

sorted_numbers = sorted(numbers)   # sorted() does not change orig list
print(f"sorted_numbers: {sorted_numbers}")
print(f"       numbers: {numbers}")

numbers.sort(reverse=True)   # sort in descending order, modifies orig list
print(f"numbers.sort(reverse=True): {numbers}")

