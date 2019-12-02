from day2.computer import calculate


target = 19690720

for noun in range (0, 100):
    for verb in range (0, 100):
        result = calculate(noun = noun, verb = verb)
        if result == target:
            print("answer is {}".format(100 * noun + verb))
