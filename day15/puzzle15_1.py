from day15.repair import RepairRobot

robot = RepairRobot(input_file='input.txt')
answer = robot.run(debug=True)
print("Oxygen system located at {}".format(answer))