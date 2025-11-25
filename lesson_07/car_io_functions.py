def read_availability(filename):
    """ Read from file to create a list of cars and return a list of lists."""
    cars = []
    in_file = open(filename, "r", encoding="utf-8")
    for line in in_file.readlines():
        new_car = line.split(",")
        new_car[-1] = int(new_car[-1])  # convert to int
        cars.append(new_car)
    in_file.close()
    return cars

def write_availability(filename, car_fleet):
    """Write the updated list of cars to the file."""
    # in order to write to the file,
    # each list must join all elements as a single line
    # to do the above, all elements must be strings

    out_file = open(filename, "w")
    for car in car_fleet:
        car[-1] = str(car[-1]) # convert all to string
        line = ",".join(car) # put all elements in a line
        out_file.write(line + "\n")   # write to the file
    out_file.close()

# def main():
#     cars = read_availability("cars.txt")
#     cars[0][-1] += 1   # update quantity of first list
#     print(cars)
#     print("---------------")
#     # write the list back to the file
#     write_availability("cars.txt", cars)
#
# main()