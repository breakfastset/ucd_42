filename = "blog.txt"
horizontal_rule = "-" * 50

# --- File input ----- #
in_file = open(filename, "r")
contents = in_file.read()  # read everything
in_file.close()

print(horizontal_rule)
print("| {:^46} |".format("Previous entries"))
print(horizontal_rule)
print(contents)
print(horizontal_rule)

new_entry = input("What do you wish to write today? ")

# --- File output ------- #
out_file = open(filename, "a")   # append to the file
out_file.write(new_entry + "\n")
out_file.close()