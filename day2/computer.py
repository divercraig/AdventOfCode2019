def calculate(noun:int, verb:int) -> int:
    with open('input.txt') as input:
        line = input.readline()

    strings = line.split(',')

    memory = []

    for code in strings:
        memory.append(int(code))

    memory[1] = noun
    memory[2] = verb

    for i in range(0, len(memory), 4):
        op_code = memory[i]

        if op_code == 1 or op_code == 2:
            operand_1_loc = memory[i + 1]
            operand_2_loc = memory[i + 2]
            output_location = memory[i + 3]
            operand_1 = memory[operand_1_loc]
            operand_2 = memory[operand_2_loc]

            if op_code == 1:
                output = operand_1 + operand_2
            else:
                output = operand_1 * operand_2

            memory[output_location] = output

        if op_code == 99:
            #halt
            break

    return memory[0]
