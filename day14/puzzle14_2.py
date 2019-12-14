from day14.reactions import NanoFactory
import math

factory = NanoFactory(file_name='sample3.txt')
hold_capacity = 1000000000000

max_fuel = 90000000
min_fuel = 1
attempt = math.floor((max_fuel-min_fuel)/2)

while True:

    ore_required = NanoFactory(file_name='input.txt').ore_to_produce_fuel(fuel=attempt)
    if ore_required > hold_capacity:
        print("{} HIGH".format(attempt))
        max_fuel = attempt

    if ore_required < hold_capacity:
        print("{} LOW".format(attempt))
        min_fuel = attempt

    if ore_required == hold_capacity:
        print('EXACTLY {} REQUIRED'.format(attempt))
        break

    if (max_fuel - min_fuel) < 2:
        if ore_required > hold_capacity:
            answer = attempt - 1
        else:
            answer = attempt
        break


    attempt = max_fuel - math.floor((max_fuel-min_fuel)/2)

print("You can make {} Fuel".format(answer))
