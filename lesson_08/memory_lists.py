birds = ["sparrow", "crow", "pigeon", "mynah", "bulboa"]

birds_1 = birds   # both birds and birds_1 point to SAME list.

birds_2 = list(birds)   # makes a COPY of birds
birds_3 = birds[:]      # use slicing to make a COPY
birds_4 = [b for b in birds]   # using list comprehension COPY

birds[0] = "kingfisher"   # affect birds and birds_1
birds_2[0] = "hornbill"   # affect only birds_2
birds_3[-1] = "munia"     # affect only birds_3
birds_4[2] = "swift"      # affect only birds_4

print("  birds:", birds)    # ['kingfisher', 'crow', 'pigeon', 'mynah', bulboa']
print("birds_1:", birds_1)  # ['kingfisher', 'crow', 'pigeon', 'mynah', bulboa']
print("birds_2:", birds_2)  # ['hornbill', 'crow', 'pigeon', 'mynah', bulboa']
print("birds_3:", birds_3)  # ['sparrow', 'crow', 'pigeon', 'mynah', munia']
print("birds_4:", birds_4)  # ['sparrow', 'crow', 'swift', 'mynah', bulboa']
