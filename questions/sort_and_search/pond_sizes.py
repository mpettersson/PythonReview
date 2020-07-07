"""
    POND SIZES

    You have an integer matrix representing a plot of land, where the value at that location represents the height
    above sea level.  A value of zero indicates water.  A pond is a region of water connected vertically, horizontally,
    or diagonally.  The size of the pond is the total number of connected water cells.  Write a method to compute the
    size of all ponds in the matrix.

    Example:
        input = [[0,2,1,0],
                 [0,1,0,1],
                 [1,1,0,1],
                 [0,1,0,1]]
        output = [2, 4, 1] (any order works)
"""


def compute_pond_sizes(land):
    pond_sizes = []
    r = 0
    while r < len(land):
        c = 0
        while c < len(land[r]):
            if land[r][c] == 0:
                size = compute_size(land, r, c)
                pond_sizes.append(size)
            c += 1
        r += 1
    return pond_sizes


def compute_size(land, row, col):
    if row < 0 or col < 0 or row >= len(land) or col >= len(land[row]) or land[row][col] != 0:
        return 0
    size = 1
    land[row][col] = -1  # How it's marked as visited...
    dr = -1
    while dr <= 1:
        dc = -1
        while dc <= 1:
            size += compute_size(land, row + dr, col + dc)
            dc += 1
        dr += 1
    return size


input = [[0, 2, 1, 0],
         [0, 1, 0, 1],
         [1, 1, 0, 1],
         [0, 1, 0, 1]]
output = [2, 4, 1]
print("compute_pond_sizes(input):", compute_pond_sizes(input))