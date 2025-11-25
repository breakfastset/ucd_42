# this is not good
name_1 = "xiaomi"
name_2 = "pop mart"
name_3 = "broadcom"
name_4 = "arm"
name_5 = "alibaba"
name_6 = "apple"

# a list is a collection of items, better way of organizing items
names = ["xiaomi", "popmart", "broadcom", "arm", "alibaba", "apple"]
#           0         1           2         3         4         5
#          -6        -5          -4        -3        -2        -1
print(names[1])   # popmart
print(names[-5])  # popmart
print(names[-1])  # last item (apple)
print(names[0])   # first item (xiaomi)

# print(names[6])   # IndexError, runtime error

# slicing   -> list_name[start:end:step], end is excluded
print(names[:3])    # names[0:3:1]  xiaomi popmart broadcom
print(names[2:])    # names[2:6:1]  broadcom arm alibaba apple
print(names[1:5])   # popmart broadcom arm alibaba
print(names[1:5:2]) # popmart arm
print(names[::-1])  # in reverse
# slicing makes a copy of the list and its elements, does not affect original list
