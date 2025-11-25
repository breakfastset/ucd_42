MENU = """Welcome to Minimal Car Rental Co.
1. Rent Car
2. Return Car
3. Read Terms & Conditions
4. Quit
Please choose an option: """

def read_availability(filename):
    """
    Read the number of cars from the file and return.
    @return num_cars    # docstrings
    """
    in_file = open(filename, "r")
    num_cars = int(in_file.readline())    # convert to int
    in_file.close()
    return num_cars


def write_availability(filename, availability):
    """Update the number of cars to the file."""
    out_file = open(filename, "w")
    line = f"{availability}\n"    # convert availability to string
    out_file.write(line)
    out_file.close()


def rent_car(availability):
    """Decrease the number of cars if count > 0."""
    if availability > 0:
        availability -= 1
        print("Your car is available at check out.")
    else:
        print("Sorry, no cars available at this time.")
    return availability   # return the updated number


def return_car(availability):
    """Increase the number of cars by 1."""
    availability += 1
    print("Thank you for returning the car.")
    return availability


def main():
    filename = "cars.txt"
    availability = read_availability(filename)   # load data from file
    choice = input(MENU)

    if choice == "1":
        print("1. Rent Car")
        availability = rent_car(availability)
    elif choice == "2":
        print("2. Return Car")
        availability = return_car(availability)
    elif choice == "3":
        print("3. Read Terms and Conditions")
    elif choice == "4":
        print("4. Quit")
    else:
        print("Invalid option! Choose 1 to 4 only!")

    print(f"Number of cars left: {availability}")

    write_availability(filename, availability)  # save updated information
    print("~= Thank you for using Minimal Car Rental =~")


main()   # call main() to run the program