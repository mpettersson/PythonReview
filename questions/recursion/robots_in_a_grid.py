"""
    ROBOTS IN A GRID (CCI 8.2)

    Imagine a robot sitting on the upper left corner of a grid with R rows and C columns.  The robot can only move in
    two directions, right and down, but certain cells are "off limits", such that the robot cannot step on them.
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
def robot_path_rec(grid):

    def _robot_path_rec(grid, row, col, path):
        if 0 <= row <= len(grid) - 1 and 0 <= col <= len(grid[row]) - 1 and grid[row][col]:
            if (row is 0 and col is 0) or _robot_path_rec(grid, row, col - 1, path) or _robot_path_rec(grid, row - 1, col, path):
                path.append((row, col))
                return True
        return False

    if grid is not None and len(grid) > 0:
        path = []
        if _robot_path_rec(grid, len(grid) - 1, len(grid[0]) - 1, path):
            return path


# Top Down/Dynamic Programming Approach: Time complexity is now O(rc) where r and c are the number of elements in the
# rows and columns.
def robot_path_top_down(grid):

    def _robot_path_top_down(grid, row, col, path, cache):
        if 0 <= row <= len(grid) - 1 and 0 <= col <= len(grid[row]) - 1 and grid[row][col]:
            if (row, col) in cache:
                return cache[(row, col)]
            success = False
            if (row is 0 and col is 0) or _robot_path_top_down(grid, row, col - 1, path, cache) or _robot_path_top_down(grid, row - 1, col, path, cache):
                path.append((row, col))
                success = True
            cache[(row, col)] = success
            return success
        return False

    if grid is not None and len(grid) > 0:
        path = []
        cache = {}
        if _robot_path_top_down(grid, len(grid) - 1, len(grid[0]) - 1, path, cache):
            return path


# With Variations: Time and space complexity is O(rc) where r and c are the number of elements in the rows and columns.
def robot_path_rec_4_dir(grid, start_row=0, start_col=0, end_row=-1, end_col=-1):

    def _robot_path_rec_4_dir(grid, path, end_row, end_col, memo):
        row, col = path[-1]
        if row is end_row and col is end_col:
            return True
        if row < len(grid) - 1 and grid[row + 1][col] and memo[row + 1][col]:                       # Down
            path.append((row + 1, col))
            if _robot_path_rec_4_dir(grid, path, end_row, end_col, memo):
                return True
            else:
                memo[row + 1][col] = False
                path.pop()
        if col < len(grid[row]) - 1 and grid[row][col + 1] and memo[row][col + 1]:                  # Right
            path.append((row, col + 1))
            if _robot_path_rec_4_dir(grid, path, end_row, end_col, memo):
                return True
            else:
                memo[row][col + 1] = False
                path.pop()
        if row > 0 and grid[row - 1][col] and memo[row - 1][col] and (row - 1, col) not in path:    # Up
            path.append((row - 1, col))
            if _robot_path_rec_4_dir(grid, path, end_row, end_col, memo):
                return True
            else:
                memo[row - 1][col] = False
                path.pop()
        if col > 0 and grid[row][col - 1] and memo[row][col - 1] and (row, col - 1) not in path:    # Left
            path.append((row, col - 1))
            if _robot_path_rec_4_dir(grid, path, end_row, end_col, memo):
                return True
            else:
                memo[row][col - 1] = False
                path.pop()
        return False

    if grid is not None and len(grid) > 0 and grid[start_row][start_col]:
        path = [(start_row, start_col)]
        memo = [[True for c in r] for r in grid]
        if end_row is -1:
            end_row = len(grid) - 1
        if end_col is -1:
            end_col = len(grid[end_row]) - 1
        if _robot_path_rec_4_dir(grid, path, end_row, end_col, memo):
            return path


grids = [[[True,  False, True, True, True,  True,  True,  True,  True,  True, True, True,  True],
          [True,  True,  True, True, True, False,  True,  True,  True,  True, True, True,  True],
          [True,  True, False, True, True,  True,  True,  True,  True,  True, True, True,  True],
          [True,  True,  True, True, True,  True,  True,  True, False,  True, True, True,  True],
          [False, True,  True, True, True,  True,  True,  True,  True,  True, True, True,  True],
          [True,  True,  True, True, True,  True,  True,  True,  True,  True, True, True,  True],
          [True,  True, False, True, True,  True,  True,  True,  True,  True, True, True,  True],
          [True,  True,  True, True, True,  True,  True, False,  True,  True, True, True,  True],
          [True,  True,  True, True, True,  True,  True, False,  True,  True, True, True,  True],
          [True,  True,  True, True, True,  True,  True, False,  True, False, True, True,  True],
          [True,  True,  True, True, True,  True,  True, False,  True,  True, True, True, False],
          [True,  True,  True, True, True,  True,  True, False, False,  True, True, True,  True],
          [True,  True,  True, True, True,  True,  True,  True,  True,  True, True, True,  True]],
         [[True,  True,  True, True]],
         [[True,  True, False, True]],
         [[True],
          [True],
          [True],
          [True]],
         [[True],
          [True],
          [False],
          [True]],
         [[True, False, False, False],
          [True,  True, False,  True],
          [False, True, False, False],
          [True,  True,  True,  True]],
         [[True, False, False, False],
          [True,  True, False,  True],
          [False, True, False, False],
          [True,  True,  True, False]],
         [[True, False, False, False],
          [True,  True, False,  True],
          [False, True, False, False],
          [True,  True, False,  True]],
         [[ True, False,  True,  True,  True],
          [ True, False,  True, False,  True],
          [ True,  True,  True, False,  True],
          [False, False, False, False,  True],
          [ True,  True,  True,  True,  True],
          [ True, False, False, False, False],
          [ True,  True,  True,  True,  True]],
         None]

for i, grid in enumerate(grids):
    print(f"robot_path_rec(grids[{i}]): {robot_path_rec(grid)}")
print()

for i, grid in enumerate(grids):
    print(f"robot_path_top_down(grids[{i}]): {robot_path_top_down(grid)}")
print()

for i, grid in enumerate(grids):
    print(f"robot_path_rec_4_dir(grids[{i}]): {robot_path_rec_4_dir(grid)}")


