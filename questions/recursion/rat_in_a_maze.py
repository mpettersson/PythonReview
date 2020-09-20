"""
    RAT IN A MAZE

    Given a maze represented in matrix form, find a path from the source to the destination.  The source will be the
    first element (maze[0][0]) and the destination will be the last element (maze[-1][-1]).  A blocked and unblocked
    paths are represented by 0 and 1 respectively.  You are only allowed to move down or right.

    Example:
        Input =  [[1, 0, 0, 0],
                  [1, 1, 0, 1],
                  [0, 1, 0, 0],
                  [1, 1, 1, 1]]
        Output = [[1, 0, 0, 0],
                  [1, 1, 0, 0],
                  [0, 1, 0, 0],
                  [0, 1, 1, 1]]

    NOTE: Variations of this question include being able to travel in multiple directions and starting/ending in
    specified locations.
"""


# Recursive Approach: Time complexity is O(2**(r+c)) where r and c are the number of elements in the rows and columns.
def rat_path(maze):
    path = []
    if maze and rec_rat_path(maze, len(maze) - 1, len(maze[0]) - 1, path):
        res = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]
        for col, row in path:
            res[col][row] = 1
        return res


def rec_rat_path(maze, col, row, path):
    if col < 0 or row < 0 or not maze[row][col]:
        return False
    is_at_origin = (row == 0) and (col == 0)
    if is_at_origin or rec_rat_path(maze, col-1, row, path) or rec_rat_path(maze, col, row-1, path):
        path.append([row, col])
        return True
    return False


# Top Down/Dynamic Programming Approach: Time complexity is now O(rc) where r and c are the number of elements in the
# rows and columns.
def rat_path_tddp(maze):
    path = []
    cache = {}
    if maze and rat_path_td(maze, len(maze) - 1, len(maze[0]) - 1, path, cache):
        res = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]
        for col, row in path:
            res[col][row] = 1
        return res


def rat_path_td(maze, col, row, path, cache):
    if col < 0 or row < 0 or not maze[row][col]:
        return False
    p = (row, col)
    if p in cache:
        return cache[p]
    success = False
    is_at_origin = (row == 0) and (col == 0)
    if is_at_origin or rat_path_td(maze, col - 1, row, path, cache) or rat_path_td(maze, col, row - 1, path, cache):
        path.append([row, col])
        success = True
    cache[p] = success
    return success


def print_maze(maze):
    for i in maze:
        for j in i:
            print(str(j) + " ", end="")
        print("")


maze1 = [[1, 0, 0, 0],
         [1, 1, 0, 1],
         [0, 1, 0, 0],
         [1, 1, 1, 1]]

print_maze(rat_path(maze1))
print()

print_maze(rat_path_tddp(maze1))






