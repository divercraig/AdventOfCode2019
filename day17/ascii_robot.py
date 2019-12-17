from day17.computer import IntCodeComputer

class AsciiRobot:
    def __init__(self, input_file:str):
        self.brain = IntCodeComputer(program = input_file)
        self.scaffold_list = []
        self.scaffold_grid = []
        self.intersections = set()


    def scan(self, debug=False):
        halted = False
        program_input = []
        ascii_map = []

        while not halted:
            output, halted = self.brain.run(program_input=program_input)
            if not halted:
                ascii_map.append(output)

        self.scaffold_list = list(map(chr, ascii_map ))
        if debug:
            print(''.join(self.scaffold_list))
        row = []
        for i in range(len(self.scaffold_list)):
            if self.scaffold_list[i] != '\n':
                row.append(self.scaffold_list[i])
            else:
                if len(row) > 0:
                    self.scaffold_grid.append(row)
                    row = []
        return 0

    def _is_intersection(self, x, y):
        points_to_check = []
        try:
            points_to_check.append(self.scaffold_grid[y][x])
            points_to_check.append(self.scaffold_grid[y+1][x])
            points_to_check.append(self.scaffold_grid[y-1][x])
            points_to_check.append(self.scaffold_grid[y][x+1])
            points_to_check.append(self.scaffold_grid[y][x-1])
        except IndexError:
            return False

        if ''.join(points_to_check) == '#####':
            return True

        return False

    def detect_intersections(self, debug=False):
        for y in range(len(self.scaffold_grid)):
            for x in range(len(self.scaffold_grid[y])):
                if self._is_intersection(x, y):
                    self.intersections.add((x, y))

        if debug:
            print("Intersections at {}".format(self.intersections))

        alignment_parameter = 0
        for intersection in self.intersections:
            value = intersection[0] * intersection[1]
            alignment_parameter = alignment_parameter + value

        return alignment_parameter
