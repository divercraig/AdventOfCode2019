from day12.planet import Planet
from copy import deepcopy

planets = []
with open("input.txt") as file:
    planets = []
    i = 0
    for line in file:
        planets.append(Planet(index=i, string=line.strip()))
        i+=1
original_planets = deepcopy(planets)

def planets_are_equal():
    equal = True
    for i in range(len(planets)):
        if planets[i] != original_planets[i]:
            equal = False
            break
    return equal


def axis_is_equal(axis:int):
    equal = True
    for i in range(len(planets)):
        if planets[i].positions[axis] != original_planets[i].positions[axis] or planets[i].velocities[axis] != original_planets[i].velocities[axis]:
            equal = False
            break
    return equal


def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    test = greater

    while(True):
        if((test % x == 0) and (test % y == 0)):
            lcm = test
            break
        test += greater
    return lcm


periods_found = False
step = 0
x_period = 0
y_period = 0
z_period = 0

while not periods_found:
    step += 1

    if step % 1000000 == 0:
        print("After {} steps:".format(step + 1))

    for i in range(len(planets)):
        for j in range(i + 1, len(planets)):
            planets[i].apply_gravity(planets[j])
            planets[j].apply_gravity(planets[i])

    for planet in planets:
        planet.apply_velocity()

    if x_period == 0 and axis_is_equal(0):
        print("X axis repeats after {} steps".format(step))
        x_period = step

    if y_period == 0 and axis_is_equal(1):
        print("Y axis repeats after {} steps".format(step))
        y_period = step

    if z_period == 0 and axis_is_equal(2):
        print("Z axis repeats after {} steps".format(step))
        z_period = step

    if x_period > 0 and y_period > 0 and z_period > 0:
        print("Found all periods")
        periods_found = True

answer = lcm(x_period, lcm(y_period, z_period))

print("Answer is {}".format(answer))


