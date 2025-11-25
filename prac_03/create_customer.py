from sys import argv

filename = argv[1]    # remember to provide argument

# 1. ask the user for customer information
customer_name = input("Costumer name: ")
customer_id = input("Costumer ID: ")

# 2. open and save to the file using filename
customer_out_file = open(filename, "a")  # open file for appending

line = f"{customer_name} {customer_id}\n"
customer_out_file.write(line)    # write single line

customer_out_file.close()