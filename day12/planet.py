import re


class Planet:
    def __init__(self, index:int, string:str, debug:bool = False):
        self.index = index
        result = re.search('\<x\=(.*), y\=(.*), z\=(.*)\>', string)
        self.positions = []
        self.velocities = []
        for i in range(3):
            self.positions.append(int(result.group(i + 1)))
            self.velocities.append(0)

        if debug:
            print(self)

    def __eq__(self, other):
        return self.calculate_total_energy() == other.calculate_total_energy()

    def __repr__(self):
            return 'Planet {}: pos=<x={}, y={}, z={}>, vel=<x={}, y={}, z={}>'.format(
                self.index,
                self.positions[0], self.positions[1], self.positions[2],
                self.velocities[0], self.velocities[1], self.velocities[2]
            )

    def apply_gravity(self, other_planet):
        for i in range(3):
            if self.positions[i] > other_planet.positions[i]:
                self.velocities[i] = self.velocities[i] - 1
            if self.positions[i] < other_planet.positions[i]:
                self.velocities[i] = self.velocities[i] + 1

    def apply_velocity(self):
        for i in range(3):
            self.positions[i] = self.positions[i] + self.velocities[i]

    def calculate_kinetic_engergy(self):
        total = 0
        for i in range(3):
            total = total + abs(self.velocities[i])

        return total

    def calculate_potential_energy(self):
        total = 0
        for i in range(3):
            total = total + abs(self.positions[i])

        return total

    def calculate_total_energy(self):
        return self.calculate_kinetic_engergy() * self.calculate_potential_energy()
