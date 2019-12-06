memory = []

def read_opcode(op_code: int) -> tuple:
    op_string = str(op_code)
    instruction = op_string[-2:]
    operand_1_position_mode = True if (op_string[-3:-2] == '' or op_string[-3:-2] == '0') else False
    operand_2_position_mode = True if (op_string[-4:-3] == '' or op_string[-4:-3] == '0') else False
    operand_3_position_mode = True if (op_string[-5:-4] == '' or op_string[-5:-4] == '0') else False
    return (int(instruction), operand_1_position_mode, operand_2_position_mode, operand_3_position_mode)


def read_value(position, position_mode):
    if position_mode:
        memory_loc = memory[position]
        return memory[memory_loc]
    else:
        return memory[position]


def write_value(value, position, position_mode):
    if position_mode:
        memory_loc = memory[position]
        memory[memory_loc] = value
    else:
        memory[position] = value


def calculate() -> int:
    with open('input.txt') as input:
        line = input.readline()

    strings = line.split(',')

    for code in strings:
        memory.append(int(code))

    i = 0
    while i < len(memory):
        instruction = read_opcode(memory[i])
        op_code = instruction[0]

        if op_code == 1 or op_code == 2:
            operand_1 = read_value(i + 1, instruction[1])
            operand_2 = read_value(i + 2, instruction[2])

            if op_code == 1:
                output = operand_1 + operand_2
            else:
                output = operand_1 * operand_2

            write_value(output, i + 3, instruction[3])
            i += 4
        if op_code == 3:
            print('Input:')
            write_value(5, i + 1, instruction[1]) # hard coded value of 5 rather than input
            i += 2

        if op_code == 4:
            print('Output: {}'.format(read_value(i + 1, instruction[1])))
            i += 2

        if op_code == 5:
            operand_1 = read_value(i + 1, instruction[1])
            operand_2 = read_value(i + 2, instruction[2])
            if operand_1 is not 0:
                i = operand_2
            else:
                i += 3

        if op_code == 6:
            operand_1 = read_value(i + 1, instruction[1])
            operand_2 = read_value(i + 2, instruction[2])
            if operand_1 is 0:
                i = operand_2
            else:
                i += 3

        if op_code == 7:
            operand_1 = read_value(i + 1, instruction[1])
            operand_2 = read_value(i + 2, instruction[2])
            if operand_1 < operand_2:
                write_value(1, i + 3, instruction[3])
            else:
                write_value(0, i + 3, instruction[3])
            i += 4

        if op_code == 8:
            operand_1 = read_value(i + 1, instruction[1])
            operand_2 = read_value(i + 2, instruction[2])
            if operand_1 == operand_2:
                write_value(1, i + 3, instruction[3])
            else:
                write_value(0, i + 3, instruction[3])
            i += 4


        if op_code == 99:
            # halt
            break

    return memory[0]
