from math_functions import *   # from math_functions module, import all functions

def print_introduction():  # function has 0 parameters
    print("------------------------------")
    print("Welcome to functions in Python")
    print("------------------------------")
    # function does not return any value

def main(): # The first function to call
    print_introduction()
    radius_1 = 10
    volume_1 = sphere_volume(radius_1)  # sphere_volume(10)
    surface_area_1 = sphere_surface_area(radius_1)
    print(f"Volume of sphere with radius {radius_1} = {volume_1}")
    print(f"Surface area of sphere = {surface_area_1}")
    print()

    radius_2 = 8
    volume_2 = sphere_volume(radius_2)  # sphere_volume(8)
    surface_area_2 = sphere_surface_area(radius_2)
    print(f"Volume of second sphere with radius {radius_2} = {volume_2}")
    print(f"Surface area of sphere = {surface_area_2}")
    print()

    hypotenuse = calculate_hypotenuse(4, 3)
    print(f"Length of hypotenuse = {hypotenuse}")

# --------------------------------
# not part of main() function
main()  # Run main()