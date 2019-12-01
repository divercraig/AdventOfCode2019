import math


def calculate_fuel_for_module(mass: int) -> int:
    fuel_required = math.floor(mass/3) - 2
    if fuel_required < 0:
        return 0
    else:
        return fuel_required + calculate_fuel_for_module(fuel_required)


fuel_counter = 0

for module in open('input.txt'):
    module_mass = int(module)
    fuel_counter += calculate_fuel_for_module(module_mass)

print("Required fuel for modules, including mass of fuel, is {}".format(fuel_counter))
