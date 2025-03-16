# Write definitions for the area and volume of a sphere. Solve Ex 1 from chapter 3
from math import pi


def sphere_area(radius):
    return 4 * pi * (radius ** 2)

def sphere_volume(radius):
    return (4 / 3) * pi * (radius ** 3)

radius = int(input("Provide the radius of the sphere: "))
print(f"The area is {sphere_area(radius)} and the volume is {sphere_volume(radius)}.")
