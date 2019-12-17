from day17.ascii_robot import AsciiRobot

robot = AsciiRobot(input_file='input.txt')
cleaned = robot.traverse()
print("Cleaned up {} dust".format(cleaned))