import math


def calculate_fuel_for_module(mass: int) -> int:
    return math.floor(mass/3) - 2


fuel_counter = 0

for module in open('input.txt'):
    module_mass = int(module)
    fuel_counter += calculate_fuel_for_module(module_mass)

print("Required fuel is {}".format(fuel_counter))
