class AsteroidMap:
    def __init__(self, input_file:str):
        self.asteroid_map = []
        self.asteroid_visibility_map = {}

        for line in open('test_1_2_35.txt'):
            row = []
            for char in line.strip():
                row.append(char)
            self.asteroid_map.append(row)

        for x in range(0, len(self.asteroid_map[0])):
            for y in range(0, len(self.asteroid_map)):
                if self.asteroid_map[y][x] == '#':
                    self.asteroid_visibility_map[(x, y)] = 0

    def _calculate_visibility_for_asteroid(self, position:tuple):
        
