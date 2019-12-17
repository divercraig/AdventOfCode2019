from day17.ascii_robot import AsciiRobot

robot = AsciiRobot(input_file='input.txt')
robot.scan(debug=True)
alignment_parameter = robot.detect_intersections(debug=True)
print("Alignment is {}".format(alignment_parameter))