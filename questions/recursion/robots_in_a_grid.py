"""
    ROBOTS IN A GRID (CCI 8.2)

    Imagine a robot sitting on the upper left corner of a gird with R rows and C columns.
    The robot can only move in two directions, right and down, but certain cells are "off limits", such that the
    robot cannot step on them.
    Design an algorithm to find a path for the robot from the top left to the bottom right.

    Example:
        Input =  [[True, False, False, False],
                  [True,  True, False,  True],
                  [False, True, False, False],
                  [True,  True,  True,  True]]
        Output = [(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3)]

    NOTE: Variations of this question include being able to travel in multiple directions and starting/ending in
    specified locations.
"""


# Recursive Approach: Time complexity is O(2**(r+c)) where r and c are the number of elements in the rows and columns.
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


# Top Down/Dynamic Programming Approach: Time complexity is now O(rc) where r and c are the number of elements in the
# rows and columns.
def top_down_robo_path(maze):
    if maze is None or len(maze) is 0:
        return None
    path = []
    cache = {}
    if dp_robo_path(maze, len(maze) - 1, len(maze[0]) - 1, path, cache):
        return path


def dp_robo_path(maze, row, col, path, cache):
    if col < 0 or row < 0 or not maze[row][col]:
        return False
    p = (row, col)
    if p in cache:
        return cache[p]
    is_at_origin = (row == 0) and (col == 0)
    success = False
    if is_at_origin or dp_robo_path(maze, row, col - 1, path, cache) or dp_robo_path(maze, row - 1, col, path, cache):
        path.append((row, col))
        success = True

    cache[p] = success
    return success


l = [[[True,  False, True, True, True,  True,  True,  True,  True, True, True,  True,  True],
      [True,  True,  True, True, True, False,  True,  True,  True, True, True,  True,  True],
      [True,  True, False, True, True,  True,  True,  True,  True, True, True,  True,  True],
      [True,  True,  True, True, True,  True,  True,  True, False, True, True,  True,  True],
      [False, True,  True, True, True,  True,  True,  True,  True, True, True,  True,  True],
      [True,  True,  True, True, True,  True, False,  True,  True, True, True,  True,  True],
      [True,  True, False, True, True,  True,  True,  True,  True, True, True,  True,  True],
      [True,  True,  True, True, True,  True,  True, False,  True, True, True,  True,  True],
      [True,  True,  True, True, True,  True,  True, False,  True, True, True,  True,  True],
      [True,  True,  True, True, True,  True,  True, False,  True, True, True,  True,  True],
      [True,  True,  True, True, True,  True,  True, False,  True, True, True,  True, False],
      [True,  True,  True, True, True,  True,  True, False,  True, True, True,  True,  True],
      [True,  True, False, True, True,  True,  True,  True,  True, True, True, False,  True]],
     [[True, False, False, False],
      [True,  True, False,  True],
      [False, True, False, False],
      [True,  True,  True,  True]]]


for sl in l:
    print("rec_get_robo_path(sl):", rec_get_robo_path(sl))
print()

for sl in l:
    print("top_down_robo_path(sl):", top_down_robo_path(sl))

