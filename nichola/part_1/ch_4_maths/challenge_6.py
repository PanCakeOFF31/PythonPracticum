import math


def calculate_cylinder_volume(r: float, h: float) -> float:
    return round(r ** 2 * math.pi * h, 3)


radius = float(input("Enter a cylinder radius: "))
height = float(input("Enter a cylinder height: "))

volume = calculate_cylinder_volume(radius, height)
print("The cylinder volume is", volume)
