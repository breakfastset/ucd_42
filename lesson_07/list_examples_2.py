
names = ["jo", "ben", "tan", "kim", "sai", "siti", "anh", "tan", "tan", "tan"]

# names = ["jo", "ben", "kim", "sai", "siti", "anh", "tan", "tan", "tan"]

target = "tan"
while target in names:
    names.remove(target)

print(names)

names = ["jo", "ben", "tan", "kim", "sai", "siti", "anh", "tan", "tan", "tan"]
target = "tan"
index = 0
while index < len(names):
    if names[index] == target:
        names.pop(index)
    else:
        index += 1
print(names)

