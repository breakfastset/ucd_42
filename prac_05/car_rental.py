MENU_OPTION_CHECK_AVAILABILITY = "1"
MENU_OPTION_RENT_CAR = "2"
MENU_OPTION_RETURN_CAR = "3"
MENU_OPTION_TERMS = "4"
MENU_OPTION_QUIT = "5"

MENU = f"""Welcome to Minimal Car Rental Co.
{MENU_OPTION_CHECK_AVAILABILITY}. Check Car Availability
{MENU_OPTION_RENT_CAR}. Rent Car
{MENU_OPTION_RETURN_CAR}. Return Car
{MENU_OPTION_TERMS}. Read Terms & Conditions
{MENU_OPTION_QUIT}. Quit
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
    num_cars = int(input("How many cars to rent? "))

    if num_cars > 0:
        if availability >= num_cars:
            availability -= num_cars
            print("Your car(s) is/are available at check out.")
        else:
            print("Sorry, not enough cars available at this time.")
    else:
        print("Invalid number of cars (must be > 0!)")
    return availability   # return the updated number


def return_car(availability):
    """Increase the number of cars by 1."""
    num_cars = int(input("How many cars to return? "))

    if num_cars > 0:
        availability += num_cars
        print("Thank you for returning the car(s).")
    else:
        print("Invalid number of cars (must be > 0!)")
    return availability


def main():
    filename = "cars.txt"
    availability = read_availability(filename)   # load data from file
    choice = input(MENU)

    if choice == MENU_OPTION_CHECK_AVAILABILITY:
        print(f"Number of cars left: {availability}")
    elif choice == MENU_OPTION_RENT_CAR:
        print(f"{MENU_OPTION_RENT_CAR} Rent Car")
        availability = rent_car(availability)
    elif choice == MENU_OPTION_RETURN_CAR:
        print(f"{MENU_OPTION_RETURN_CAR} Return Car")
        availability = return_car(availability)
    elif choice == MENU_OPTION_TERMS:
        print(f"{MENU_OPTION_TERMS} Read Terms and Conditions")
    elif choice == MENU_OPTION_QUIT:
        print(f"{MENU_OPTION_QUIT} Quit")
    else:
        print(f"Invalid option! Choose 1 to {MENU_OPTION_QUIT} only!")   # part c)


    write_availability(filename, availability)  # save updated information
    print("~= Thank you for using Minimal Car Rental =~")


main()   # call main() to run the program