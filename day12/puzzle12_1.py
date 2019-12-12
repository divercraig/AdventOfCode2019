from day12.planet import Planet

planets = []
number_of_steps = 1000
with open("input.txt") as file:
    planets = []
    i = 0
    for line in file:
        planets.append(Planet(index=i, string=line.strip()))
        i+=1

for step in range(0, number_of_steps):
    for i in range(len(planets)):
        for j in range(i + 1, len(planets)):
            planets[i].apply_gravity(planets[j])
            planets[j].apply_gravity(planets[i])

    for planet in planets:
        planet.apply_velocity()

    if (step +1) % 10 == 0:
        print("After {} steps:".format(step + 1))
        for planet in planets:
            print(planet)
        print("")

total_energy = 0

for planet in planets:
    total_energy = total_energy + planet.calculate_total_energy()

print("Sum of total Energy: {}".format(total_energy))
