from day9.computer import IntCodeComputer


computer = IntCodeComputer(program='input.txt')

halt = False

while halt is not True:
    output, halt = computer.run(program_input=[1])