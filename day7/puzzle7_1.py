from day7.computer import IntCodeComputer
from itertools import permutations

best_thrust = 0

for phase_set in list(permutations(range(5), 5)):
    current_output = 0
    for phase in phase_set:
        computer = IntCodeComputer(program="input.txt")
        current_output = computer.run(program_input=[phase, current_output])
    print("Phase Set {} generates {} thrust".format(phase_set, current_output))
    if current_output > best_thrust:
        best_thrust = current_output

print("Highest Thrust Output: {}".format(best_thrust))