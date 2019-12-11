from day11.robot import PaintRobot

robot = PaintRobot(input_file='input.txt')
painted_cells = robot.run()
print("Robot has painted {} cells".format(painted_cells))