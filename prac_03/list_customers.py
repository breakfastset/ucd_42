from sys import argv

filename = argv[1]   # get filename from argument

# 1. open the file and read in all contents
customer_in_file = open(filename, "r")
contents = customer_in_file.read()   # read everything
customer_in_file.close()

# 2. print the output
print(f"Customers saved in file '{filename}'")
print(contents)