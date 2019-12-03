from day3.puzzle3_1 import generate_list_of_instructions, generate_list_of_points, find_intersections

if __name__ == "__main__":
    wires = []
    for line in open('input.txt'):
        inst = generate_list_of_instructions(line=line)
        points = generate_list_of_points(inst)
        wires.append(points)

    intersections = find_intersections(points1=wires[0], points2=wires[1])

    intersections.remove((0, 0)) # remove the origin

    lowest_steps = None

    for cross_over in intersections: # walk the line until we hit the intersection
        steps = 0

        for wire in wires:
            for point in wire:
                if point == cross_over:
                    break
                steps += 1

        if (lowest_steps is None) or (steps < lowest_steps):
            lowest_steps = steps

    print(lowest_steps)
