from day6.orbit_map import OrbitMap

orbit_map = OrbitMap(input="input.txt")
steps = orbit_map.plan_route(you='YOU', target='SAN')
print("There are {} steps to reach the target".format(steps))
