"""
    ROBOTS IN A GRID

    Imagine a robot sitting on the upper left corner of a gird with R rows and C columns.
    The robot can only move in two directions, right and down, but certain cells are "off limits", such that the
    robot cannot step on them.
    Design an algorithm to find a path for the robot from the top left to the bottom right.
"""


def rec_get_robo_path(maze):
    if maze is None or len(maze) is 0:
        return None
    path = []
    if rec_get_path(maze, len(maze) - 1, len(maze[0]) - 1, path):
        return path


def rec_get_path(maze, row, col, path):
    if col < 0 or row < 0 or not maze[row][col]:
        return False
    is_at_origin = (row == 0) and (col == 0)

    if is_at_origin or rec_get_path(maze, row, col - 1, path) or rec_get_path(maze, row - 1, col, path):
        path.append((row, col))
        return True

    return False


def get_robo_path(maze):
    if maze is None or len(maze) is 0:
        return None
    path = []
    cache = {}
    if get_path(maze, len(maze) - 1, len(maze[0]) - 1, path, cache):
        return path


def get_path(maze, row, col, path, cache):
    if col < 0 or row < 0 or not maze[row][col]:
        return False
    p = (row, col)
    if p in cache:
        return cache[p]
    is_at_origin = (row == 0) and (col == 0)
    success = False
    if is_at_origin or get_path(maze, row, col - 1, path, cache) or get_path(maze, row - 1, col, path, cache):
        path.append((row, col))
        success = True

    cache[p] = success
    return success


l = [[True, False, True, True, True, True, True, True, True, True, True, True, True],
     [True, True, True, True, True, False, True, True, True, True, True, True, True],
     [True, True, False, True, True, True, True, True, True, True, True, True, True],
     [True, True, True, True, True, True, True, True, False, True, True, True, True],
     [False, True, True, True, True, True, True, True, True, True, True, True, True],
     [True, True, True, True, True, True, False, True, True, True, True, True, True],
     [True, True, False, True, True, True, True, True, True, True, True, True, True],
     [True, True, True, True, True, True, True, False, True, True, True, True, True],
     [True, True, True, True, True, True, True, False, True, True, True, True, True],
     [True, True, True, True, True, True, True, False, True, True, True, True, True],
     [True, True, True, True, True, True, True, False, True, True, True, True, False],
     [True, True, True, True, True, True, True, False, True, True, True, True, True],
     [True, True, False, True, True, True, True, True, True, True, True, False, True]]

path = get_robo_path(l)

print(path)
