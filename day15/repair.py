from enum import Enum
from day15.computer import IntCodeComputer
from random import randint


class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4

    def get_change(self):
        if self == Direction.NORTH:
            return (0, 1)
        if self == Direction.SOUTH:
            return (0, -1)
        if self == Direction.EAST:
            return (1, 0)
        if self == Direction.WEST:
            return (-1, 0)

    @classmethod
    def get_direction_from_change(cls, change):
        if change == (0, 1):
            return Direction.NORTH
        if change == (0, -1):
            return Direction.SOUTH
        if change == (1, 0):
            return Direction.EAST
        if change == (-1, 0):
            return Direction.WEST

    def get_new_position(self, old_position):
        x = old_position[0] + self.get_change()[0]
        y = old_position[1] + self.get_change()[1]
        return (x, y)

    @classmethod
    def get_direction_to(cls, current, target):
        x = target[0] - current[0]
        y = target[1] - current[1]
        return cls.get_direction_from_change((x, y))


class RepairRobot:
    def __init__(self, input_file:str):
        self.search_position = (0, 0)
        self.position = (0, 0)
        self.brain = IntCodeComputer(program=input_file)
        self.min_x = 0
        self.max_x = 0
        self.min_y = 0
        self.max_y = 0
        self.wall_locations = set()
        self.clear_locations = set()
        self.searched_locations = set()
        self.dead_ends = set()
        self.clear_locations.add((0, 0))
        self.oxygen_generator_location = None
        self.oxygenated_locations = set()

    def _process_status(self, direction, status):
        new_location = direction.get_new_position(self.position)
        if status == 0:
            wall_location = new_location
            self.wall_locations.add(wall_location)
        if status == 1:
            self.position = new_location
            self.clear_locations.add(new_location)
        if status == 2:
            self.position = new_location
            self.oxygen_generator_location = new_location

        if new_location[0] > self.max_x:
            self.max_x = new_location[0]

        if new_location[0] < self.min_x:
            self.min_x = new_location[0]

        if new_location[1] > self.max_y:
            self.max_y = new_location[1]

        if new_location[1] < self.min_y:
            self.min_y = new_location[1]

    def _print_map(self):
        print('-----------------------------------------------------------------')
        for y in range(self.max_y, self.min_y - 1, -1):
            row = []
            for x in range(self.min_x, self.max_x + 1):
                position = (x, y)

                if position in self.wall_locations:
                    row.append('#')
                elif position == self.oxygen_generator_location:
                    row.append('O')
                elif position == self.position:
                    row.append('D')
                elif position == (0, 0):
                    row.append('X')
                elif position in self.dead_ends:
                    row.append('+')
                elif position in self.clear_locations:
                    row.append('.')
                else:
                    row.append(' ')
            print(''.join(row))

    def completed_search_position(self, position):
        still_searching = False
        for direction in Direction:
            adjacent_position = direction.get_new_position(position)
            if adjacent_position not in self.wall_locations and adjacent_position not in self.clear_locations and adjacent_position != self.oxygen_generator_location:
                still_searching = True
        return not still_searching

    def choose_direction(self):
        if self.completed_search_position(self.position):
            self.searched_locations.add(self.position)
            self.search_position = None

        if self.search_position is not None:
            if self.position != self.search_position and not self.completed_search_position(self.search_position):
                return Direction.get_direction_to(self.position, self.search_position)

        if not self.completed_search_position(self.position):
            self.search_position = self.position

        unsearched_positions = []
        unreached_positions = []
        clear_positions = []
        bad_positions = []

        for direction in Direction:
            new_position = direction.get_new_position(self.position)
            if new_position in self.wall_locations or new_position in self.dead_ends:
                bad_positions.append(new_position)
                continue
            if new_position not in self.clear_locations:
                unreached_positions.append(new_position)
                continue
            else:
                clear_positions.append(new_position)
            if new_position not in self.searched_locations:
                unsearched_positions.append(new_position)

        if len(bad_positions) == 3:
            self.dead_ends.add(self.position)

        # CHOOSE A NEW POSITION TO SEARCH BASED ON SURROUNDING POSITIONS
        if len(unreached_positions) > 0:
            target_position = unreached_positions[randint(0, len(unreached_positions) - 1)]
            return Direction.get_direction_to(self.position, target_position)

        if len(unsearched_positions) > 0:
            target_position = unsearched_positions[randint(0, len(unsearched_positions) - 1)]
            return Direction.get_direction_to(self.position, target_position)

        if len(clear_positions) == 0:
            return None

        random_clear_position = clear_positions[randint(0, len(clear_positions) - 1)]
        return Direction.get_direction_to(self.position, random_clear_position)

    def run(self, debug=False):
        halted = False
        program_input = []

        while not halted:
            direction = self.choose_direction()
            if direction is None:
                print("Searched the whole grid")
                halted = True
                break
            program_input.append(direction.value)

            status, halted = self.brain.run(program_input=program_input)
            self._process_status(direction=direction, status=status)
            if debug:
                self._print_map()

        return self.oxygen_generator_location

    def repair(self, debug=False):
        time = 0
        oxygenation_completed = False
        self.oxygenated_locations.add(self.oxygen_generator_location)
        new_oxygen_locations = []
        new_oxygen_locations.append(self.oxygen_generator_location)

        while not oxygenation_completed:
            oxygenating = []
            for oxygen_location in new_oxygen_locations:
                for direction in Direction:
                    adjacent_position = direction.get_new_position(oxygen_location)
                    if adjacent_position not in self.wall_locations and adjacent_position not in self.oxygenated_locations:
                        oxygenating.append(adjacent_position)
                        self.oxygenated_locations.add(adjacent_position)

            if len(oxygenating) == 0:
                return time
            new_oxygen_locations = oxygenating
            time += 1
            if debug:
                self._print_map()




