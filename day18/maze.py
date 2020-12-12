import string
import sys


class State:

    def __init__(self, position: tuple, keys: set):
        self.position = position
        self.keys = keys

    def __eq__(self, other):
        if self.position == other.position and self.keys == other.keys:
            return True
        else:
            return False

    def __hash__(self):
        return hash(repr(self))


class Maze:

    def __init__(self, file_name: str):
        self.empty_spaces = set()
        self.doors = {}
        self.keys = {}
        self.memory = {}

        with open(file_name) as file:
            y = -1
            for line in file:
                y += 1
                for x, c in enumerate(line):
                    if c in string.ascii_lowercase:
                        self.empty_spaces.add((x, y))
                        self.keys[(x, y)] = c
                    if c in string.ascii_uppercase:
                        self.empty_spaces.add((x, y))
                        self.doors[(x, y)] = c
                    if c == '.':
                        self.empty_spaces.add((x, y))
                    if c == '@':
                        self.empty_spaces.add((x, y))
                        self.starting_location = (x, y)

    def shortest_path(self, position: tuple = None, previous_states: list = []) -> int:
        shortest = sys.maxsize
        if position is None:
            position = self.starting_location

        if len(previous_states) > 0:
            keys = previous_states[-1].keys.copy()
        else:
            keys = set()

        if position in self.doors.keys():
            door = self.doors[position]
            required_key = door.lower()
            if required_key not in keys:
                return shortest

        if position in self.keys.keys():
            keys.add(self.keys[position])
            if len(keys) == len(self.keys):
                return len(previous_states)
        new_state = State(position, keys)

        if new_state in previous_states:
            return shortest

        new_previous_states = previous_states.copy()
        new_previous_states.append(new_state)

        for change in [(1,0), (-1,0), (0, 1), (0, -1)]:
            next_position = (position[0] + change[0], position[1] + change[1])
            if next_position in self.empty_spaces:
                if (next_position, tuple(new_previous_states)) in self.memory.keys():
                    print("Hit the optimisation")
                    cost = self.memory[(next_position, tuple(new_previous_states))]
                else:
                    cost = self.shortest_path(next_position, new_previous_states)
                if cost < shortest:
                    shortest = cost

        self.memory[(position, tuple(previous_states))] = shortest
        return shortest
