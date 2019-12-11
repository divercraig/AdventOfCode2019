from enum import Enum
from day11.computer import IntCodeComputer


class Direction(Enum):
    UP = (1, 0)
    RIGHT = (0, 1)
    DOWN = (-1, 0)
    LEFT = (0, -1)

    def turn_right(self):
        if self == Direction.LEFT:
            return Direction.UP
        if self == Direction.UP:
            return Direction.RIGHT
        if self == Direction.RIGHT:
            return Direction.DOWN
        if self == Direction.DOWN:
            return Direction.LEFT

    def turn_left(self):
        if self == Direction.LEFT:
            return Direction.DOWN
        if self == Direction.DOWN:
            return Direction.RIGHT
        if self == Direction.RIGHT:
            return Direction.UP
        if self == Direction.UP:
            return Direction.LEFT

    def turn(self, code: int):
        if code == 1:
            return self.turn_right()
        if code == 0:
            return self.turn_left()
        raise ValueError("Turn code {} is not 1 or 0".format(code))


class PaintRobot:
    def __init__(self, input_file: str, start_white:bool = False):
        self.position = (0, 0)
        self.direction = Direction.UP
        self.brain = IntCodeComputer(program=input_file)
        self.white_cells = set()
        self.painted_cells = set()
        self.min_x = 0
        self.max_x = 0
        self.min_y = 0
        self.max_y = 0
        if start_white:
            self.white_cells.add((0, 0))

    def _paint_cell(self, paint:int):
        self.painted_cells.add(self.position)

        if self.position[0] > self.max_x:
            self.max_x = self.position[0]
        if self.position[0] < self.min_x:
            self.min_x = self.position[0]
        if self.position[1] > self.max_y:
            self.max_y = self.position[1]
        if self.position[1] < self.min_y:
            self.min_y = self.position[1]

        if paint == 1:
            self.white_cells.add(self.position)
        elif self.position in self.white_cells:
            self.white_cells.remove(self.position)

    def run(self, debug=False):
        halted = False
        program_input = []
        while not halted:
            if self.position in self.white_cells:
                program_input.append(1)
            else:
                program_input.append(0)
            paint, halted = self.brain.run(program_input=program_input, debug=debug)
            if halted:
                break
            self._paint_cell(paint)
            turn, halted = self.brain.run(program_input=program_input, debug=debug)
            if halted:
                break
            new_direction = self.direction.turn(turn)
            new_position = (self.position[0] + new_direction.value[0], self.position[1] + new_direction.value[1])
            self.direction = new_direction
            self.position = new_position

        return len(self.painted_cells)

    def reveal(self):
        grid = []
        for y in range(self.min_y - 1, self.max_y + 1):
            row = []
            for x in range(self.min_x - 1, self.max_x + 1):
                if (x, y) in self.white_cells:
                    row.append('*')
                else:
                    row.append(' ')
            grid.append(row)

        for row in grid:
            print(''.join(row))


