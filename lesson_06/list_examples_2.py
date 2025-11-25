# list functions / operations
animals = ["orca", "panda", "bear", "eagle", "pigeon", "pig", "narwhal", "honey badger"]

# add to the back
animals.append("yak")
print(animals)

# remove from the bank
animals.pop()
print(animals)

# remove pigeon at index 4
del animals[4]
print(animals)

# remove eagle at index 3
animals.pop(3)
print(animals)

# insert at position 2, elephant
animals.insert(2, "elephant")
print(animals)

# modify bear to brown bear
animals[3] = "brown bear"
print(animals)

# find the number of elements
print(len(animals))
print()

for i in range(len(animals)):   # use a loop to access each element
    print(f"{i:2}) {animals[i]}")

