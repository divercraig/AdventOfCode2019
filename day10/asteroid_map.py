from copy import deepcopy

def _printMap(map:dict):
    for row in map:
        print(row)

class AsteroidMap:
    def __init__(self, input_file:str):
        self.asteroid_map = []
        self.asteroid_visibility_map = {}
        self.min_x = 0
        self.min_y = 0

        for line in open('input.txt'):
            row = []
            for char in line.strip():
                row.append(char)
            self.asteroid_map.append(row)

        self.max_x = len(self.asteroid_map[0]) -1
        self.max_y = len(self.asteroid_map) -1

        for x in range(self.min_x, self.max_x):
            for y in range(self.min_y, self.max_y):
                if self.asteroid_map[y][x] == '#':
                    self.asteroid_visibility_map[(x, y)] = 0

        print('Input Map')
        _printMap(self.asteroid_map)
        print('--------------------------------------------------------------------')

        for asteroid in self.asteroid_visibility_map.keys():
            self.asteroid_visibility_map[asteroid] = self._calculate_visibility_for_asteroid(asteroid)

        biggest_number = 0
        for value in self.asteroid_visibility_map.values():
            if value > biggest_number:
                biggest_number = value

        print("The most asteroids visible is {}".format(biggest_number))

    def _calculate_search_positions_offsets(self, search_level:int):
        search_positions = []
        # top_row
        y = search_level
        for x in range(-search_level, search_level):
            search_positions.append((x, y))

        # right column
        x = search_level
        for y in range(-search_level + 1, search_level + 1):
            search_positions.append((x, y))

        # bottom row
        y = -search_level
        for x in range(-search_level + 1, search_level + 1):
            search_positions.append((x, y))

        # left column
        x = -search_level
        for y in range(-search_level, search_level):
            search_positions.append((x, y))

        return search_positions

    def _calculate_visibility_for_asteroid(self, candidate:tuple) -> int:
        all_out_of_bounds = False
        search_level = 0
        visible_asteroids = 0

        line_of_sight_map = deepcopy(self.asteroid_map)

        while not all_out_of_bounds:
            any_in_bounds = False
            search_level += 1
            search_position_offsets = self._calculate_search_positions_offsets(search_level=search_level)
            for search_offset in search_position_offsets:
                search_position = (candidate[0] + search_offset[0], candidate[1] + search_offset[1])
                if search_position[0] >= self.min_y and search_position[0] <= self.max_x and search_position[1] >= self.min_y and search_position[1] <= self.max_y:
                    any_in_bounds = True
                    if line_of_sight_map[search_position[1]][search_position[0]] == '#':
                        visible_asteroids += 1
                        line_of_sight_map[search_position[1]][search_position[0]] = 'O'
                        # if offset x = 0 then remaining y offsets are blocked
                        if search_offset[0] == 0:
                            if search_offset[1] > 0:
                                for y in range(search_position[1]+1, self.max_y + 1):
                                    line_of_sight_map[y][search_position[0]] = 'B'
                            else:
                                for y in range(search_position[1]-1, -1, -1):
                                    line_of_sight_map[y][search_position[0]] = 'B'

                        # if offset y = 0 then remaining x offsets are blocked
                        elif search_offset[1] == 0:
                            if search_offset[0] > 0:
                                for x in range(search_position[0]+1, self.max_x + 1):
                                    line_of_sight_map[search_position[1]][x] = 'B'
                            else:
                                for x in range(search_position[0]-1, -1, -1):
                                    line_of_sight_map[search_position[1]][x] = 'B'
                        # else each point with the same offset is blocked
                        else:
                            line_of_sight_out_of_bounds = False
                            new_search_position = search_position
                            x_absolute_offset = abs(search_offset[0])
                            y_absolute_offset = abs(search_offset[1])
                            if(x_absolute_offset == y_absolute_offset):
                                x_offset = int(search_offset[0] / x_absolute_offset)
                                y_offset = int(search_offset[1] / y_absolute_offset)
                            elif(x_absolute_offset > y_absolute_offset and x_absolute_offset % y_absolute_offset == 0):
                                x_offset = int(search_offset[0]/y_absolute_offset)
                                y_offset = int(search_offset[1]/y_absolute_offset)
                            elif(x_absolute_offset < y_absolute_offset and y_absolute_offset % x_absolute_offset == 0):
                                x_offset = int(search_offset[0] / x_absolute_offset)
                                y_offset = int(search_offset[1] / x_absolute_offset)
                            else:
                                x_offset = search_offset[0]
                                y_offset = search_offset[1]
                            while not line_of_sight_out_of_bounds:
                                new_search_position = (new_search_position[0] + x_offset, new_search_position[1] + y_offset)
                                if new_search_position[0] < 0 or new_search_position[0] > self.max_x or new_search_position[1] < 0 or new_search_position[1] > self.max_y:
                                    line_of_sight_out_of_bounds = True
                                else:
                                    line_of_sight_map[new_search_position[1]][new_search_position[0]] = 'B'


            if not any_in_bounds:
                all_out_of_bounds = True
        print('Asteroid {}'.format(candidate))
        _printMap(line_of_sight_map)
        print('--------------------------------------------------------------------')
        print('{} visible asteroids'.format(visible_asteroids))
        print('--------------------------------------------------------------------')

        return visible_asteroids
