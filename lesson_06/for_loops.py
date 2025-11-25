# 1. for item in iterable_object:
#        statements
#
# iterable_objects are objects containing objects
# eg. strings, list, set, tuple etc.
#
for char in "hello":   # string as an iterable
    print(char)
print("==" * 20)

for animal in ["dogs", "cats", "mice", "sharks"]:
    print(animal)   # list is an iterable
print("==" * 20)

# 2. for i in range(start, end, step):
#        statements

# eg. 1 arg only, start=0, end=arg, step=1
for i in range(3):   # range(0, 3, 1)
    print(i)    # 0 1 2
print("==" * 20)

# eg. 2 args, start=arg1, end=arg2, step=1
for i in range(7, 13):
    print(i)   # 7 8 9 10 11 12
print("==" * 20)

# eg. 3 args, start=3, end=19, step=4
for i in range(3, 19, 4):
    print(i)   # 3 7 11 15
print("==" * 20)

# descending order
for i in range(10, 0, -1):
    print(i)  # 10 9 8 ... 1












