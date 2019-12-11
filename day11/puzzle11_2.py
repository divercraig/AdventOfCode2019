from day11.robot import PaintRobot

robot = PaintRobot(input_file='input.txt', start_white=True)
painted_cells = robot.run()
print("Robot has painted {} cells".format(painted_cells))
print("------------------------------------------------")
robot.reveal()