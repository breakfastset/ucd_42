from car_io_functions import *

MENU = """Welcome to Minimal Car Rental Co.
1. Rent Car
2. Return Car
3. Read Terms & Conditions
4. Quit
Please choose an option: """

def rent_car(availability):        # TODO: NEED TO MODIFY to use List of Lists
    """Decrease the number of cars if count > 0."""
    if availability > 0:
        availability -= 1
        print("Your car is available at check out.")
    else:
        print("Sorry, no cars available at this time.")
    return availability   # return the updated number


def return_car(availability):     # TODO: NEED TO MODIFY to use List of Lists
    """Increase the number of cars by 1."""
    availability += 1
    print("Thank you for returning the car.")
    return availability


def read_terms_conditions():
    """Read the company's terms and conditions with appropriate pauses."""
    in_file = open("terms.txt", "r")
    line_count = 0
    for line in in_file.readlines():
        print(line, end="")  # remove the new lines
        line_count += 1

        if line_count % 10 == 0:   # after every 10 lines
            input(":: Enter to read more...")  # ask user to press enter
    in_file.close()


def main():
    filename = "cars.txt"
    car_fleet = read_availability(filename)   # load data from file
    print(car_fleet)  # for debugging
    choice = input(MENU)      #  1. prime the loop

    while choice != "4":      #  while 2. condition is True
        # start of repetition        # 3. statements
        if choice == "1":
            print("1. Rent Car")
            # availability = rent_car(availability)
        elif choice == "2":
            print("2. Return Car")
            # availability = return_car(availability)
        elif choice == "3":
            print("3. Read Terms and Conditions")
            read_terms_conditions()
        else:
            print("Invalid option! Choose 1 to 4 only!")
        # end of repetition #  end of statements

        choice = input(MENU)  # 4. update var (to exit the loop eventually)

    write_availability(filename, car_fleet)  # save updated information
    print("~= Thank you for using Minimal Car Rental =~")


main()   # call main() to run the program