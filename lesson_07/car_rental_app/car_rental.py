from car_io_functions import *

MENU = """================================================
        Welcome to Minimal Car Company
================================================
1. Rent Car
2. Return Car
3. Read Terms and Conditions
4. Quit
>>> """


def display_cars(car_fleet):
    """Display the cars from the fleet in a nice format."""
    print("=-" * 20)
    print("|{:^38}|".format("Our car fleet"))
    print("=-" * 20)

    for i in range(len(car_fleet)):
        make = car_fleet[i][0]
        model = car_fleet[i][1]
        car_class = car_fleet[i][2]
        quantity = car_fleet[i][3]
        print(f"{i:2}) {make:15} {model:12} ({car_class}) {quantity:3}")
        #          4      16         13         4           3


def get_valid_choice(minimum, maximum, message):
    """Get and validate the user choice before returning."""
    choice = int(input(message))
    while choice < minimum or choice > maximum:
        print(f"Please enter a valid choice between {minimum} and {maximum}.")
        choice = int(input(message))
    return choice


def rent_car(car_fleet):
    """Allow renting of car if there are available and return the updated number of cars."""
    # 1. Display the list of cars
    display_cars(car_fleet)

    # 2. Get a valid car choice
    choice = get_valid_choice(0, len(car_fleet) - 1, "Please choose a car: ")

    # 3. Update the availability of the car selected (if available), display error otherwise.
    if car_fleet[choice][-1] > 0:
        car_fleet[choice][-1] -= 1
        print("Your car is available at checkout.")
    else:
        print("Sorry, but no cars are available at the moment.")

    return car_fleet


def return_car(car_fleet):
    """Increase the number by 1 for that car make and model and return."""
    # 1. Display the list of cars
    display_cars(car_fleet)

    # 2. Get a valid car choice
    choice = get_valid_choice(0, len(car_fleet) - 1, "Please choose a car: ")

    car_fleet[choice][-1] += 1
    print("Car returned. Thank you.")
    return car_fleet


def read_terms_conditions():
    """Read terms and conditions for renting and returning."""
    in_file = open("terms_conditions.txt", "r")
    line_count = 0
    for line in in_file:
        print(line, end="")
        line_count += 1
        if line_count % 10 == 0:   # after every 10 lines
            input("--- Press ENTER to continue...")
    print()
    in_file.close()


def main():
    """Start of program."""
    filename = "cars.txt"
    car_fleet = read_availability(filename)
    choice = input(MENU)    # 1. prime the loop

    while choice != "4":   #  2. while condition
        #####
        if choice == "1":   # 3. statements
            print("1. Rent Car")
            car_fleet = rent_car(car_fleet)
        elif choice == "2":
            print("2. Return Car")
            car_fleet = return_car(car_fleet)
        elif choice == "3":
            print("3. Read Terms and Conditions")
            read_terms_conditions()
        else:
            print("Invalid choice (Options 1 to 4 only!)")
        choice = input(MENU)  # 4. update the choice (eventually to exit)
        #####

    write_availability(filename, car_fleet)   # update availability to file
    print("Thank you for using Minimal Car Company Program!")

main()