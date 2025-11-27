def read_availability(filename):
    """Read data into a list of cars (lists)."""
    car_fleet = []
    in_file = open(filename, 'r')
    for line in in_file.readlines():
        new_car = line.split(",")  # break string into a list.
        new_car[-1] = int(new_car[-1])  # last column -> int
        car_fleet.append(new_car)  # append the list into the bigger list.
    in_file.close()
    return car_fleet


def write_availability(filename, car_fleet):
    """Write the list of lists into the file."""
    out_file = open(filename, 'w')
    for car in car_fleet:
        car[-1] = str(car[-1])  # convert to string
        line = ",".join(car)
        out_file.write(line + "\n")
    out_file.close()

# the following lines will only run if you execute this file directly.
if __name__ == '__main__':    # if the current file is executed, then execute the following statements
    car_fleet = read_availability('cars.txt')
    car_fleet[0][-1] += 1  # increase the quantity by 1
    print(car_fleet)   # debug purposes
    print("----" * 10)
    write_availability('cars.txt', car_fleet)  # update

