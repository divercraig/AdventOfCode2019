from day15.repair import RepairRobot

robot = RepairRobot(input_file='input.txt')
answer = robot.run(debug=True)
print("Oxygen system located at {}".format(answer))
print("Begining Repair")
time_to_oxygenation = robot.repair(debug=True)
print("Oxygenation complete after {} periods".format(time_to_oxygenation))