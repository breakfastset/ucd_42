
numbers_list_1 = [7, 4, -1, 2, 6, -5]
numbers_list_2 = [8, 3, 9, 0, 10]

new_list = numbers_list_1 + numbers_list_2   # list concatenation
print(new_list)

another_list = numbers_list_2 * 3    # list replication
print(another_list)

total = sum(new_list)   # add up all elements
highest = max(new_list)  # 10
lowest = min(new_list)   # -5
print(f"Total: {total}")
print(f"Range: {lowest} to {highest}")