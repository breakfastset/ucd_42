seatings = [
    ["Aik", "Sim", "Abu"],        # 0
    ["Mae", "Yum", "Snoop"],      # 1
    ["Baba", "Ali", "Mama"],      # 2
    ["Tammy", "Chuen", "Raj"]     # 3
]    # 0        1        2

print(seatings[2][1])   # Ali
print(seatings[0][0])   # Aik
print(seatings[-1][-1]) # Raj   # seatings[3][2]
print()

for row in range(len(seatings)):            # for each row
    for col in range(len(seatings[row])):   #   for col in that row
        print(f"{seatings[row][col]:10}", end="")
    print()  # end of row