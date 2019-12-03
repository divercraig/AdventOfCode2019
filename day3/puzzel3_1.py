def generate_list_of_instructions(line: str) -> list:
    instructions = []
    for instruction in line.split(','):
        direction = instruction[0]
        length = instruction[1:]
        instructions.append((direction, int(length)))

    return instructions


def generate_list_of_points(instructions: list) -> list:
    points = [(0,0)]
    for direction, distance in instructions:
        while distance > 0:
            last_point = points[-1]
            if direction is 'U': #increment Z
                new_point = (last_point[0], last_point[1] + 1)
            if direction is 'D': #decrement Z
                new_point = (last_point[0], last_point[1] - 1)
            if direction is 'R': #increment X
                new_point = (last_point[0] + 1, last_point[1])
            if direction is 'L': #decrement X
                new_point = (last_point[0] - 1, last_point[1])
            points.append(new_point)
            distance -= 1
    return points


def find_intersections(points1: list, points2: list) -> list:
    return list(set(points1).intersection(points2))


def distance_from_origin(point: tuple) -> int:
    distance = 0
    distance = distance + abs(point[0]) + abs(point[1])
    return distance

if __name__ == "__main__":
    wires = []
    for line in open('input.txt'):
        inst = generate_list_of_instructions(line=line)
        points = generate_list_of_points(inst)
        wires.append(points)

    intersections = find_intersections(points1=wires[0], points2=wires[1])

    intersections.remove((0, 0)) # remove the origin

    distances = []
    for intersection in intersections:
        distances.append(distance_from_origin(intersection))

    print(min(distances))