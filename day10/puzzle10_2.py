from day10.asteroid_map import AsteroidMap

asteroid_map = AsteroidMap(input_file='input.txt')
best = asteroid_map.most_visible_asteroids()
print("{} Asteroids visible from {}".format(best[1], best[0]))
print("200th asteroid destroyed is {}".format(asteroid_map.get_200th_target(best[0])))
