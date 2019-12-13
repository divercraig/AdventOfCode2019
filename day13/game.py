from enum import Enum
from day13.computer import IntCodeComputer


class Tile(Enum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4

    def sprite(self):
        if self == Tile.EMPTY:
            return ' '
        if self == Tile.WALL:
            return '|'
        if self == Tile.BLOCK:
            return '*'
        if self == Tile.PADDLE:
            return '~'
        if self == Tile.BALL:
            return 'O'


class Game:
    def __init__(self, input_file:str):
        self.brain = IntCodeComputer(program=input_file)
        self.grid = dict()
        self.last_input = 0
        self.last_ball_position = (-1, -1)
        self.last_paddle_position = (-1, -1)
        self.desired_paddle_x = -1
        self.paddle_y = 23

    def print_screen(self, step, score):
        print("Score = {} Step={} Input={}".format(score, step, self.last_input))
        for y in range(26):
            row = []
            for x in range(37):
                try:
                    tile = self.grid[(x, y)]
                    row.append(tile.sprite())
                except KeyError:
                    row.append('?')
            print(''.join(row))
        print('')

    def which_direction(self):
        for cell in self.grid.keys():
            if self.grid[cell] == Tile.PADDLE:
                self.last_paddle_position = cell

            if self.grid[cell] == Tile.BALL:
                if self.last_ball_position != (-1, -1) and self.last_ball_position != cell:
                    ball_direction = cell[0] - self.last_ball_position[0]
                    y_diff = self.paddle_y - cell[1]
                    self.desired_paddle_x = cell[0] + (y_diff * ball_direction)
                self.last_ball_position = cell

        if self.last_paddle_position != (-1, -1) and self.desired_paddle_x != -1:
            if self.last_paddle_position[0] > self.desired_paddle_x:
                self.last_input = -1
            if self.last_paddle_position[0] < self.desired_paddle_x:
                self.last_input = 1
            if self.last_paddle_position[0] == self.desired_paddle_x:
                self.last_input = 0


    def run(self, debug=False):
        halted = False
        controls = []
        score = 0
        step = 0

        while not halted:
            step += 1
            self.which_direction()
            if len(controls) == 0:
                controls.append(self.last_input)
            elif controls[0] != self.last_input:
                controls[0] = self.last_input
            x, halted = self.brain.run(program_input=controls)
            y, halted = self.brain.run(program_input=controls)
            tile_or_score, halted = self.brain.run(program_input=controls)
            if x == -1 and y == 0:
                score = tile_or_score
            else:
                self.grid[(x, y)] = Tile(tile_or_score)

            if debug is True:
                self.print_screen(step, score)

        return score
