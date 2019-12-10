import math

class AsteroidMap:
    def __init__(self, input_file:str):
        self.asteroids = []

        with open(input_file) as file:
            rows = [line.strip() for line in file]

        for y in range(len(rows)):
            for x in range(len(rows[y])):
                if rows[y][x] == '#':
                    self.asteroids.append((x, y))

    @staticmethod
    def get_angle(target, candidate):
        offset_from_candidate = (target[0] - candidate[0], candidate[1] - target[1])
        radians = math.atan2(offset_from_candidate[0], offset_from_candidate[1])
        return radians % (2 * math.pi)

    @staticmethod
    def get_distance(target, candidate):
        offset_from_candidate = (target[0] - candidate[0], candidate[1] - target[1])
        return math.hypot(offset_from_candidate[0], offset_from_candidate[1])

    def get_asteroid_visibility_counts(self):
        visibility_counts = {}
        for candidate_asteroid in self.asteroids:
            angles_with_visible_asteroids = set()
            for target_asteroid in self.asteroids:
                if target_asteroid == candidate_asteroid:
                    continue
                angle_between_candidate_and_target = AsteroidMap.get_angle(target_asteroid, candidate_asteroid)
                angles_with_visible_asteroids.add(angle_between_candidate_and_target)

            visibility_counts[candidate_asteroid] = len(angles_with_visible_asteroids)
        return visibility_counts

    def most_visible_asteroids(self):
        visibility_counters = self.get_asteroid_visibility_counts()
        best = (None, 0)
        for asteroid in visibility_counters.keys():
            count = visibility_counters[asteroid]
            if count > best[1]:
                best = (asteroid, count)
        return best

    def get_destruction_order_from_asteroid(self, laser_loc:tuple):
        targets = []
        for target_asteroid in self.asteroids:
            if target_asteroid == laser_loc:
                continue
            angle_between_candidate_and_laser = AsteroidMap.get_angle(target_asteroid, laser_loc)
            distance_between_candidate_and_laser = AsteroidMap.get_distance(target_asteroid, laser_loc)
            targets.append((angle_between_candidate_and_laser, distance_between_candidate_and_laser, target_asteroid))

        return sorted(targets)

    def get_200th_target(self, laser_loc:tuple):
        targets = self.get_destruction_order_from_asteroid(laser_loc)
        destroyed = [targets.pop(0)]
        blocked = []
        while len(destroyed) < 200:
            if len(targets) == 0:
                targets = blocked
                blocked = []
            target = targets.pop(0)
            if target[0] == destroyed[-1][0]:
                blocked.append(target)
            else:
                destroyed.append(target)

        winner_coords = destroyed.pop(-1)[2]
        return (winner_coords[0] * 100) + winner_coords[1]




