
# string by default goes to the left
# numbers by default aligns to the right
print("| {:10} | {:10} |".format("mouse", 25.5))

# align mouse to the right >, align 25.5 to the left <
print("| {:>10} | {:<10} |".format("mouse", 25.5))

print()
# when formatting a float, the . counts as a space taken
print("|{:010}|".format(25.5))