import sys
from day18.maze import Maze

sys.setrecursionlimit(10000)
maze = Maze(file_name="input.txt")
print("Shortest Path is {}".format(maze.shortest_path()))
