from enum import Enum


class Mode(Enum):
    POSITION = 0
    VALUE = 1
    RELATIVE = 2

    @classmethod
    def from_string(cls, string:str):
        if string == '2':
            return cls.RELATIVE
        if string == '1':
            return cls.VALUE
        return cls.POSITION


class IntCodeComputer:

    def __init__(self, program: str):
        self.memory = []
        self.instruction_pointer = 0
        self.relative_base = 0
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
        return (int(instruction),
                Mode.from_string(op_string[-3:-2]),
                Mode.from_string(op_string[-4:-3]),
                Mode.from_string(op_string[-5:-4]))

    def _read_value(self, position, position_mode):
        if position_mode == Mode.POSITION:
            memory_loc = self.memory[position]
            try:
                return self.memory[memory_loc]
            except IndexError:
                return 0
        if position_mode == Mode.VALUE:
            try:
                return self.memory[position]
            except IndexError:
                return 0
        if position_mode == Mode.RELATIVE:
            try:
                memory_loc = self.relative_base + self.memory[position]
                return self.memory[memory_loc]
            except IndexError:
                return 0

    def _write_value(self, value, position, position_mode):
        if position_mode == Mode.POSITION:
            memory_loc = self.memory[position]
            self._write_and_extend(value, memory_loc)
        if position_mode == Mode.VALUE:
            self._write_and_extend(value, memory_loc)
        if position_mode == Mode.RELATIVE:
            memory_loc = self.relative_base + self.memory[position]
            self._write_and_extend(value, memory_loc)

    def _write_and_extend(self, value, memory_address):
        if len(self.memory) <= memory_address:
            for i in range(len(self.memory), memory_address +1):
                self.memory.append(0)
        self.memory[memory_address] = value

    def run(self, program_input=[], debug:bool = False):
        while self.instruction_pointer < len(self.memory):
            if debug:
                print("Executing Instruction @ {}".format(self.instruction_pointer))
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
                if debug:
                    print('Input: {}'.format(value))
                self._write_value(value, self.instruction_pointer + 1, instruction[1])
                self.instruction_pointer += 2

            if op_code == 4:
                self.output = self._read_value(self.instruction_pointer + 1, instruction[1])
                if debug:
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

            if op_code == 9:
                operand_1 = self._read_value(self.instruction_pointer + 1, instruction[1])
                self.relative_base = self.relative_base + operand_1
                self.instruction_pointer += 2

            if op_code == 99:
                # halt
                break

        return self.output, True
