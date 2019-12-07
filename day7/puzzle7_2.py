from day7.computer import IntCodeComputer
from itertools import permutations

best_thrust = 0
program = "input.txt"
phase_sets = list(permutations(range(5, 10), 5))

for phase_set in phase_sets:
    amp_a = IntCodeComputer(program=program)
    amp_b = IntCodeComputer(program=program)
    amp_c = IntCodeComputer(program=program)
    amp_d = IntCodeComputer(program=program)
    amp_e = IntCodeComputer(program=program)

    computers = [amp_a, amp_b, amp_c, amp_d, amp_e]
    inputs = [[phase_set[0], 0], [phase_set[1]], [phase_set[2]], [phase_set[3]], [phase_set[4]]]

    halted = False
    computer_number = 0
    final_thrust = -1
    while not halted:
        next_computer = computer_number + 1
        if next_computer == 5:
            next_computer = 0
        output, halt = computers[computer_number].run(program_input=inputs[computer_number])

        if halt and computer_number == 4:
            halted = halt
            final_thrust = output
        else:
            inputs[next_computer].append(output)
        computer_number = next_computer

    if final_thrust > best_thrust:
        best_thrust = final_thrust

print("Best Thrust is {}".format(best_thrust))
