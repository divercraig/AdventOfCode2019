from day10.asteroid_map import AsteroidMap

asteroid_map = AsteroidMap(input_file='input.txt')
best = asteroid_map.most_visible_asteroids()
print("{} Asteroids visible from {}".format(best[0], best[1]))
