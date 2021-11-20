"""
    SUDOKU VALIDATOR

    From Wikipedia (SEE: wikipedia.org/wiki/Sudoku):

        "Sudoku, 数独, (sūdoku, digit-single), originally called Number Place, is a logic-based, combinatorial
         number-placement puzzle. In classic sudoku, the objective is to fill a 9×9 grid with digits so that each
         column, each row, and each of the nine 3×3 subgrids that compose the grid (also called "boxes", "blocks",
         or "regions") contain all of the digits from 1 to 9. The puzzle setter provides a partially completed grid,
         which for a well-posed puzzle has a single solution."

    Write a function which accepts a partially filled matrix/list of lists (m) representing a 9x9 Sudoku board, then
    returns True if the cells are valid according to the following rules (False otherwise):
        - Each row must contain the digits 1-9 without repetition.
        - Each column must contain the digits 1-9 without repetition.
        - Each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

    NOTE: A partially filled Sudoku board could be valid but may NOT NECESSARILY be solvable.

    Example:
                board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                         [".", "9", "8", ".", ".", ".", ".", "6", "."],
                         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                         [".", "6", ".", ".", ".", ".", "2", "8", "."],
                         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        Input = board
        Output = True

    FYI:
        - There are 6,670,903,752,021,072,936,960 (6.67*(10**21)) possible solved Sudoku grids.
        - This reduces to 5,472,730,538 essentially different groups under the validity preserving transformations.
        - There are 26 types of symmetry, but they can only be found in about 0.005% of all filled grids.
        - A puzzle with a unique solution must have at least 17 clues.
        - There is a solvable puzzle with at most 21 clues for every solved grid.
        - The largest minimal puzzle found so far has 40 clues.
        - For more, SEE: wikipedia.org/wiki/Mathematics_of_Sudoku
"""
import collections
import time


# OBSERVATIONS:
#   - IF vals are CHARS and r/c indices are INTS then you can use ONE LIST/SET of tuples, where the tuples are:
#       (val, r), (c, val), (r//3, c//3, val).
#   - IFF vals AND r/c are INTS then USE THREE LISTS/SETS; one for columns, one for rows, one for sub-grids.
#   - It's easy to check for chars 1-9 via: 49 <= ord(val) <= 57


# APPROACH: 3 (Separate) Sets
#
# Create a set for each of the rows, columns, and grids, then iterate over the values in the Sudoku board.  For each
# value, verify that a the same value has not been used before (duplicated) in ary row, column, or grid.  If at any
# point a duplicate value has been encountered, return False.
#
# Time Complexity: O(81), which reduces to O(1).
# Space Complexity: O(3*81), which reduces to O(1).
def is_partial_sudoku_valid_via_three_sets(m):
    if isinstance(m, list) and len(m) == 9 and all([len(row) == 9 for row in m]):
        h_sets = [set() for _ in range(9)]
        v_sets = [set() for _ in range(9)]
        s_sets = [[set() for _ in range(3)] for _ in range(3)]
        for r in range(9):
            for c in range(9):
                if 49 <= ord(m[r][c]) <= 57:
                    if m[r][c] in h_sets[r] or m[r][c] in v_sets[c] or m[r][c] in s_sets[r//3][c//3]:
                        return False
                    h_sets[r].add(m[r][c])
                    v_sets[c].add(m[r][c])
                    s_sets[r//3][c//3].add(m[r][c])
        return True
    return False


# APPROACH: Single Set/list
#
# Create a SINGLE set for all of the rows, columns, and grids, then iterate over the values in the Sudoku board.  For
# each value, verify that a the same value has not been used before (duplicated) in the set.  If at any point a
# duplicate value has been encountered, return False.
#
# NOTE: Since the values are CHARS and the r/c indices are INTS the only duplicates will be if there are duplicate
#       VALUES in the sudoku board.  THEREFORE, if the board state is stored as ints, DON'T USE THIS APPROACH (use
#       three sets instead).
#
# Time Complexity: O(81), which reduces to O(1).
# Space Complexity: O(3*81), which reduces to O(1).
def is_partial_sudoku_valid_via_one_set(m):
    if isinstance(m, list) and len(m) == 9 and all([len(row) == 9 for row in m]):
        seen = set()
        for r, row_vals in enumerate(m):
            for c, val in enumerate(row_vals):
                if 49 <= ord(val) <= 57:
                    temp = {(val, c), (r, val), (r//3, c//3, val)}
                    if seen & temp:
                        return False
                    seen |= temp
        return True
    return False


# APPROACH: Minimized Single Set/list
#
# This uses the same logic as the single set approach above.
#
# Time Complexity: O(81), which reduces to O(1).
# Space Complexity: O(3*81), which reduces to O(1).
def is_partial_sudoku_valid_via_one_set_min(m):
    if isinstance(m, list) and len(m) == 9 and all([len(row) == 9 for row in m]):
        seen = set()
        return not any(tup in seen or seen.add(tup)
                       for r, row_vals in enumerate(m)
                       for c, val in enumerate(row_vals)
                       if 49 <= ord(val) <= 57
                       for tup in ((val, r), (c, val), (r/3, c/3, val)))
    return False


# APPROACH: Single Set And list
#
# This uses a similar logic to the other single set approaches; only difference is that a list is created, then the list
# is used to create a set and the result of the set length compared to the list length is returned.
#
# Time Complexity: O(81), which reduces to O(1).
# Space Complexity: O(3*81), which reduces to O(1).
def is_partial_sudoku_valid_via_one_list_and_set(m):
    if isinstance(m, list) and len(m) == 9 and all([len(row) == 9 for row in m]):
        seen = []
        for r, row_vals in enumerate(m):
            for c, val in enumerate(row_vals):
                if 49 <= ord(val) <= 57:
                    seen.extend([(val, c), (r, val), (r//3, c//3, val)])
        return len(seen) == len(set(seen))
    return False


# APPROACH: Minimized Single Set And list
#
# This approach is the Single Set And list approach above implemented with list comprehension.
#
# Time Complexity: O(81), which reduces to O(1).
# Space Complexity: O(3*81), which reduces to O(1).
def is_partial_sudoku_valid_via_list_and_set_min(m):
    if isinstance(m, list) and len(m) == 9 and all([len(row) == 9 for row in m]):
        seen = sum(([(val, r), (c, val), (r//3, c//3, val)]     # Use sum to concatenate lists of tuples.
                    for r, row_vals in enumerate(m)             # r = row index, row_vals = list (of values)
                    for c, val in enumerate(row_vals)           # c = col index, val = actual sudoku cell value,
                    if 49 <= ord(val) <= 57), [])               # IFF val was a char in range '1'-'9' (else no tuples).
        return len(seen) == len(set(seen))                      # Compare built list size to set(built list) size.
    return False


# APPROACH: Via The Max Fn On A Collections' Counter Object
#
# This approach uses the counter object to count the number of (val, r), (c, val), (r//3, c//3, val) tuples, then
# checks if any counter has a key (count) greater than one.
#
# Time Complexity: O(81), which reduces to O(1).
# Space Complexity: O(3*81), which reduces to O(1).
def is_partial_sudoku_valid_via_counter(m):
    if isinstance(m, list) and len(m) == 9 and all([len(row) == 9 for row in m]):
        return 1 == max(list(collections.Counter(tup
                                                 for r, row_vals in enumerate(m)
                                                 for c, val in enumerate(row_vals)
                                                 if 49 <= ord(val) <= 57
                                                 for tup in ((val, r), (c, val), (r//3, c//3, val))).values()) + [1])
    return False


# Old Formatting
def format_sudoku_board(board):
    if board:
        result = [''.join([f'{e:^3}' for e in r if len(r) > 0]) for r in board if len(board) > 0]
        for r in range(len(result)):
            result[r] = '｜' + result[r][:9] + '｜' + result[r][9:18] + '｜' + result[r][18:] + '｜'
        for r in [9, 6, 3, 0]:
            result.insert(r, '-' * 33)
        return '\t' + '\n\t'.join(result)
    return None


# New And Improved Formatting
# SEE: codegolf.stackexchange.com/questions/126930/draw-a-sudoku-board-using-line-drawing-characters
def print_formatted_sudoku_board(board, add_tab=False):
    b = [e if 49 <= ord(e) <= 57 else ' ' for r in board for e in r]
    q = lambda x, y: x + y + x + y + x
    r = lambda a, b, c, d, e: a + q(q(b * 3, c), d) + e + "\n"
    s = ((r(*"╔═╤╦╗") + q(q("║ %s │ %s │ %s " * 3 + "║\n", r(*"╟─┼╫╢")), r(*"╠═╪╬╣")) + r(*"╚═╧╩╝")) % tuple(b))
    if add_tab:
        s = "\t" + s.replace("\n", "\n\t")
    print(s)


boards = [[[".", ".", ".", ".", ".", ".", ".", ".", "."],   # Valid, Empty
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."]],
          [[".", ".", ".", ".", ".", ".", ".", ".", "."],   # Valid
           [".", ".", ".", ".", "1", ".", ".", ".", "."],
           [".", "1", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."]],
          [["1", "1", ".", ".", ".", ".", ".", ".", "."],  # Two 1's in first row.
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."]],
          [["5", "3", ".", ".", "7", ".", ".", ".", "."],   # Valid
           ["6", ".", ".", "1", "9", "5", ".", ".", "."],
           [".", "9", "8", ".", ".", ".", ".", "6", "."],
           ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
           ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
           ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
           [".", "6", ".", ".", ".", ".", "2", "8", "."],
           [".", ".", ".", "4", "1", "9", ".", ".", "5"],
           [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
          [["5", "3", ".", ".", "7", ".", ".", ".", "."],   # Two 5's in top left submatrix.
           ["6", ".", ".", "1", "9", "5", ".", ".", "."],
           [".", "9", "5", ".", ".", ".", ".", "6", "."],
           ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
           ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
           ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
           [".", "6", ".", ".", ".", ".", "2", "8", "."],
           [".", ".", ".", "4", "1", "9", ".", ".", "5"],
           [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
          [["8", "3", ".", ".", "7", ".", ".", ".", "."],   # Two 8's in first column.
           ["6", ".", ".", "1", "9", "5", ".", ".", "."],
           [".", "9", "8", ".", ".", ".", ".", "6", "."],
           ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
           ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
           ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
           [".", "6", ".", ".", ".", ".", "2", "8", "."],
           [".", ".", ".", "4", "1", "9", ".", ".", "5"],
           [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
          [["5", "3", ".", ".", "7", ".", ".", ".", "."],   # Two 1's in second to last row.
           ["6", ".", ".", "1", "9", "5", ".", ".", "."],
           [".", "9", "8", ".", ".", ".", ".", "6", "."],
           ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
           ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
           ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
           [".", "6", ".", ".", ".", ".", "2", "8", "."],
           [".", ".", ".", "4", "1", "9", "1", ".", "5"],
           [".", ".", ".", ".", "8", ".", ".", "7", "9"]]]
fns = [is_partial_sudoku_valid_via_three_sets,
       is_partial_sudoku_valid_via_one_set,
       is_partial_sudoku_valid_via_one_set_min,
       is_partial_sudoku_valid_via_one_list_and_set,
       is_partial_sudoku_valid_via_list_and_set_min,
       is_partial_sudoku_valid_via_counter]

for board in boards:
    print(f"boards:")
    print_formatted_sudoku_board(board)
    for fn in fns:
        print(f"{fn.__name__}(board): {fn(board)}")
    print()

board = [['5', '3', '4', '6', '7', '8', '9', '1', '2'],   # Valid, Complete
         ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
         ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
         ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
         ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
         ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
         ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
         ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
         ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
print(f"board:")
print_formatted_sudoku_board(board)
for fn in fns:
    t = time.time()
    print(f"{fn.__name__}(board): {fn(board)} took: ", end='')
    print(f"{time.time() - t} seconds.")



