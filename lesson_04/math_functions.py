import math   # math library needed for pi

def sphere_volume(radius):   # 1 parameter (input)
    volume = 4 / 3 * math.pi * (radius ** 3)
    return volume   # returns the value of the volume

def sphere_surface_area(radius):
    surface_area = 4 * math.pi * (radius ** 2)
    return surface_area

def calculate_hypotenuse(height, length):
    hypotenuse = math.sqrt(height ** 2 + length ** 2)
    return hypotenuse