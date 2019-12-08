import numpy


class SpaceImage:
    def __init__(self, filename: str, width: int = 25, height: int = 6):
        self.width = width
        self.height = height

        with open(filename) as input:
            line = input.readline().strip()

        self.number_of_layers = int(len(line)/ (width * height))
        self.layers = numpy.empty([self.number_of_layers, height, width], dtype=int)

        x = 0
        y = 0
        layer = 0
        for pixel in line:
            self.layers[layer][y][x] = int(pixel)
            x += 1

            if x >= self.width:
                x = 0
                y += 1

            if y >= self.height:
                y = 0
                layer += 1

    def compact(self):
        output = numpy.empty([self.height, self.width], dtype=str)

        for x in range(self.width):
            for y in range(self.height):
                for layer in range(self.number_of_layers):
                    pixel = self.layers[layer][y][x]
                    if pixel == 0:
                        output[y][x] = ' '
                        break
                    if pixel == 1:
                        output[y][x] = '*'
                        break
        return output

    def print(self):
        output = self.compact()
        for row in output:
            print(''.join(row))

    def checksum(self) -> int:
        target_layer = 0
        fewest_zeros = None

        for layer_number, layer in enumerate(self.layers):
            zeros = 0
            for row in layer:
                for pixel in row:
                    if pixel == 0:
                        zeros += 1

            if fewest_zeros is None or zeros < fewest_zeros:
                fewest_zeros = zeros
                target_layer = layer_number

        ones = 0
        twos = 0
        for row in self.layers[target_layer]:
            for pixel in row:
                if pixel == 1:
                    ones += 1
                elif pixel == 2:
                    twos += 1

        return ones * twos

