

with open('input.txt') as input:
    line = input.readline()

strings = line.split(',')

memory = []

for code in strings:
    memory.append(int(code))

memory[1] = 12
memory[2] = 2

print("memory size is {}".format(len(memory)))

for i in range(0, len(memory), 4):
    print("instruction location = {}".format(i))
    op_code = memory[i]
    print("Op Code = {}".format(op_code))

    if op_code == 1 or op_code == 2:
        operand_1 = memory[i + 1]
        operand_2 = memory[i + 2]
        output_location = memory[i + 3]
        print("op1 = {}".format(operand_1))
        print("op2 = {}".format(operand_2))
        print("output_loc = {}".format(output_location))

        if op_code == 1:
            output = operand_1 + operand_2
        else:
            output = operand_1 * operand_2

        print("output = {}".format(output))

        memory[output_location] = output
        print(','.join(str(x) for x in memory))
        print("----------------------------")

    if op_code == 99:
        #halt
        print("HALT")
        break

print("Output Value = {}".format(memory[0]))
