from copy import copy

class FFT:
    def __init__(self, file_name:str):
        self.original_input = []
        self.phase_output = []
        self.base_pattern = [0, 1, 0, -1]
        with open(file_name) as file:
            line = file.readline().strip()
            for char in line:
                self.original_input.append(int(char))

    def pattern_for_digit(self, digit_position:int):
        pattern = []
        for pattern_number in self.base_pattern:
            for i in range(digit_position):
                pattern.append(pattern_number)

        return pattern

    def process_input(self, phase_input):
        phase_output = []
        for output_index in range(len(phase_input)):
            pattern = self.pattern_for_digit(output_index + 1)
            sum = 0
            pattern_index = 1 + output_index
            for input_index in range(output_index, len(phase_input)):
                input_digit = phase_input[input_index]
                pattern_digit = pattern[pattern_index]
                sum = sum + (input_digit * pattern_digit)
                if pattern_index == len(pattern) - 1:
                    pattern_index = 0
                else:
                    pattern_index += 1
            selected_digit = int(str(sum)[-1])
            phase_output.append(selected_digit)
        return phase_output

    def process_phase(self, phase_number:int):
        if phase_number == 0:
            phase_input = self.original_input
        else:
            phase_input = self.phase_output[phase_number - 1]

        self.phase_output.append(self.process_input(phase_input))

    def cleanup_signal(self, phases:int = 100):
        for phase in range(phases):
            self.process_phase(phase)

        return self.phase_output[phases - 1][0:8]

    def process_input2(self, phase_input):
        phase_output = [None] * len(phase_input)
        phase_output[-1] = phase_input[-1]

        for index in range(len(phase_input)-2, -1, -1):
            phase_output[index] = (phase_output[index + 1] + phase_input[index]) % 10

        return phase_output

    def process_phase2(self, phase_number:int):
        if phase_number == 0:
            phase_input = self.original_input
        else:
            phase_input = self.phase_output[phase_number - 1]

        self.phase_output.append(self.process_input2(phase_input))

    def cleanup_full_signal(self, phases:int = 100):
        offset_list = self.original_input[0:7]
        offset_string = ''
        for offset_digit in offset_list:
            offset_string = offset_string + str(offset_digit)
        offset_value = int(offset_string)

        copy_of_input = copy(self.original_input)

        for loop in range(9999):
            self.original_input.extend(copy_of_input)

        self.original_input = self.original_input[offset_value:]

        for phase in range(phases):
            self.process_phase2(phase)

        return self.phase_output[phases - 1][0:8]
