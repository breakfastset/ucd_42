filename = "quotes.txt"

in_file = open(filename, "r")
first_line = in_file.readline()
print(len(first_line))  # how many chars in the line

thousand_chars = in_file.read(1000)
print("Actual number of chars:", len(thousand_chars))

in_file.close()