class IntCodeComputer:

    def __init__(self, program: str):
        self.memory = []
        self.instruction_pointer = 0
        self.output = None
        with open(program) as program:
            line = program.readline()

        strings = line.split(',')

        for code in strings:
            self.memory.append(int(code))

    @staticmethod
    def _read_opcode(op_code: int) -> tuple:
        op_string = str(op_code)
        instruction = op_string[-2:]
        operand_1_position_mode = True if (op_string[-3:-2] == '' or op_string[-3:-2] == '0') else False
        operand_2_position_mode = True if (op_string[-4:-3] == '' or op_string[-4:-3] == '0') else False
        operand_3_position_mode = True if (op_string[-5:-4] == '' or op_string[-5:-4] == '0') else False
        return (int(instruction), operand_1_position_mode, operand_2_position_mode, operand_3_position_mode)

    def _read_value(self, position, position_mode):
        if position_mode:
            memory_loc = self.memory[position]
            return self.memory[memory_loc]
        else:
            return self.memory[position]

    def _write_value(self, value, position, position_mode):
        if position_mode:
            memory_loc = self.memory[position]
            self.memory[memory_loc] = value
        else:
            self.memory[position] = value

    def run(self, program_input=[]):
        while self.instruction_pointer < len(self.memory):
            instruction = self._read_opcode(self.memory[self.instruction_pointer])
            op_code = instruction[0]

            if op_code == 1 or op_code == 2:
                operand_1 = self._read_value(self.instruction_pointer + 1, instruction[1])
                operand_2 = self._read_value(self.instruction_pointer + 2, instruction[2])

                if op_code == 1:
                    result = operand_1 + operand_2
                else:
                    result = operand_1 * operand_2

                self._write_value(result, self.instruction_pointer + 3, instruction[3])
                self.instruction_pointer += 4
            if op_code == 3:
                value = program_input.pop(0)
                print('Input: {}'.format(value))
                self._write_value(value, self.instruction_pointer + 1, instruction[1])
                self.instruction_pointer += 2

            if op_code == 4:
                self.output = self._read_value(self.instruction_pointer + 1, instruction[1])
                print('Output: {}'.format(self.output))
                self.instruction_pointer += 2
                return self.output, False

            if op_code == 5:
                operand_1 = self._read_value(self.instruction_pointer + 1, instruction[1])
                operand_2 = self._read_value(self.instruction_pointer + 2, instruction[2])
                if operand_1 is not 0:
                    self.instruction_pointer = operand_2
                else:
                    self.instruction_pointer += 3

            if op_code == 6:
                operand_1 = self._read_value(self.instruction_pointer + 1, instruction[1])
                operand_2 = self._read_value(self.instruction_pointer + 2, instruction[2])
                if operand_1 is 0:
                    self.instruction_pointer = operand_2
                else:
                    self.instruction_pointer += 3

            if op_code == 7:
                operand_1 = self._read_value(self.instruction_pointer + 1, instruction[1])
                operand_2 = self._read_value(self.instruction_pointer + 2, instruction[2])
                if operand_1 < operand_2:
                    self._write_value(1, self.instruction_pointer + 3, instruction[3])
                else:
                    self._write_value(0, self.instruction_pointer + 3, instruction[3])
                self.instruction_pointer += 4

            if op_code == 8:
                operand_1 = self._read_value(self.instruction_pointer + 1, instruction[1])
                operand_2 = self._read_value(self.instruction_pointer + 2, instruction[2])
                if operand_1 == operand_2:
                    self._write_value(1, self.instruction_pointer + 3, instruction[3])
                else:
                    self._write_value(0, self.instruction_pointer + 3, instruction[3])
                self.instruction_pointer += 4

            if op_code == 99:
                # halt
                break

        return self.output, True
