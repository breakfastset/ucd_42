# \n is 1 char, \t is 1 char
text = "From the Alps.\nClean."
print(text)
print("Num of chars ", len(text))
print("-=" * 20)   # print a horizontal rule

print("To break a line, use \\n.")  # \\ is to escape \

# First line
# Second line

print("Bored? Yes\b\b\b  No")    # \b is backspace for 1 character
# \b\b\b means deleting 3 characters before current cursor
# hence "Yes" is deleted


