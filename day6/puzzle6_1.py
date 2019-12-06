from day6.orbit_map import OrbitMap

orbit_map = OrbitMap(input="input.txt")
print("Map contains {} direct and indirect orbits".format(orbit_map.count_orbits()))