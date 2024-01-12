# Create a program to calculate the area of a circle given its radius.
from math import pi
radius = float(input('\nPlease provide a radius: '))
my_area = pi * radius ** 2
print(f"\nThe area of a circle with radius {radius} is {my_area}.\n")