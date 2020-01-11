"""
    LANGTON'S ANT

    An ant is sitting on an infinite grid of white and black squares.  It initially faces right.
    At each step, it does the following:

    (1) At a white square, flip the color of the square, turn 90 degrees right (clockwise), and move forward 1 unit.
    (2) At a black square, flip the color of the square, turn 90 degrees left (anti-clockwise), and move forward 1 unit.

    Write a program to simulate the first K moves that the ant makes and print the final board as a grid.
    Note that you are not provided with the data structure to represent the grid.  This is something you must design
    yourself.  The only input to your method is K.  You should print the final grid and return nothing.  The method
    signature might be something like void print_k_moves(k)
"""


# The following is from https://rosettacode.org/wiki/Langton%27s_ant
"""Langton's ant implementation."""
from enum import Enum, IntEnum


class Dir(IntEnum):
    """Possible directions."""
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Color(Enum):
    """Possible colors."""
    WHITE = " "
    BLACK = "#"


def invert_color(grid, x, y):
    """Invert the color of grid at x, y coordinate."""
    if grid[y][x] == Color.BLACK:
        grid[y][x] = Color.WHITE
    else:
        grid[y][x] = Color.BLACK


def next_direction(grid, x, y, direction):
    """Compute next direction according to current position and direction."""
    if grid[y][x] == Color.BLACK:
        turn_right = False
    else:
        turn_right = True
    direction_index = direction.value
    if turn_right:
        direction_index = (direction_index + 1) % 4
    else:
        direction_index = (direction_index - 1) % 4
    directions = [Dir.UP, Dir.RIGHT, Dir.DOWN, Dir.LEFT]
    direction = directions[direction_index]
    return direction


def next_position(x, y, direction):
    """Compute next position according to direction."""
    if direction == Dir.UP:
        y -= 1
    elif direction == Dir.RIGHT:
        x -= 1
    elif direction == Dir.DOWN:
        y += 1
    elif direction == Dir.LEFT:
        x += 1
    return x, y


def print_grid(grid):
    """Display grid."""
    print(80 * "#")
    print("\n".join("".join(v.value for v in row) for row in grid))


def ant(width, height, max_nb_steps):
    """Langton's ant."""
    grid = [[Color.WHITE] * width for _ in range(height)]
    x = width // 2
    y = height // 2
    direction = Dir.UP

    i = 0
    while i < max_nb_steps and 0 <= x < width and 0 <= y < height:
        invert_color(grid, x, y)
        direction = next_direction(grid, x, y, direction)
        x, y = next_position(x, y, direction)
        # print_grid(grid)
        i += 1
    print_grid(grid)


ant(width=75, height=52, max_nb_steps=2000)





