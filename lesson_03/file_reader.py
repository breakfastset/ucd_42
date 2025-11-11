filename = "quotes.txt"
# in_file is a file object with READ mode
in_file = open(filename, "r")

first_char = in_file.read(1)    # read 1 char, the position will be bookmarked
print(first_char)
next_three_chars = in_file.read(3)  # read next 3 chars
print(next_three_chars)
print(f"My file object (bookmark) is at position {in_file.tell()} ")

rest_of_line = in_file.readline()      # read until end of 1st line
print("Rest of line:", rest_of_line)
second_line = in_file.readline()
print("Second line:", second_line)    # end of second line

rest_of_passage = in_file.read()     # read all of what is left.
print("Rest of passage: ", rest_of_passage)

more_content = in_file.readline()    # try to read some more but nothing is left.
print(f"more_content: [{more_content}]")   # print an empty string

in_file.seek(0)    # go back to start, position 0
all_lines = in_file.readlines()   # read all lines into a list of strings
print(all_lines)   # printing the list of strings

in_file.close()  # close the file to release the resource