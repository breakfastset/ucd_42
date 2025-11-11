
row = "| {:10} | {:10} | {:10} |"  # {:10} allocate 10 spaces to the var
horizontal_rule = "=" * 40
title_name = " Fruits for Sale "

print(horizontal_rule)
print(f"| {title_name:-^36} |")    # ^ means to keep string centered
print(horizontal_rule)
print(row.format("Oranges", 11, 2.50))
print(row.format("Apples", 8, 1.80))
print(row.format("Durians", 13, 24.99))
print(horizontal_rule)
