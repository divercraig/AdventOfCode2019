from day18.maze import Maze


def test_shortest_path_1():
    maze = Maze(file_name="test_input1.txt")
    assert maze.shortest_path() == 8


def test_shortest_path_2():
    maze = Maze(file_name="test_input2.txt")
    assert maze.shortest_path() == 86


def test_shortest_path_3():
    maze = Maze(file_name="test_input3.txt")
    assert maze.shortest_path() == 132


# def test_shortest_path_4():
#     maze = Maze(file_name="test_input4.txt")
#     assert maze.shortest_path() == 136


def test_shortest_path_5():
    maze = Maze(file_name="test_input5.txt")
    assert maze.shortest_path() == 81