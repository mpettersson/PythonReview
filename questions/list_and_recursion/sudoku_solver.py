r"""
    SUDOKU SOLVER (leetcode.com/problems/sudoku-solver)

    From Wikipedia (SEE: wikipedia.org/wiki/Sudoku):

        "Sudoku, 数独, (sūdoku, digit-single), originally called Number Place, is a logic-based, combinatorial
         number-placement puzzle. In classic sudoku, the objective is to fill a 9×9 grid with digits so that each
         column, each row, and each of the nine 3×3 subgrids that compose the grid (also called "boxes", "blocks",
         or "regions") contain all of the digits from 1 to 9. The puzzle setter provides a partially completed grid,
         which for a well-posed puzzle has a single solution."

    Write a function which accepts a 9x9 matrix m (representing a Sudoku puzzle) and find a valid solution to the
    puzzle.  A sudoku solution must satisfy all of the following rules:
        - Each of the digits 1-9 must occur exactly once in each row.
        - Each of the digits 1-9 must occur exactly once in each column.
        - Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
        - The '.' character indicates empty cells.

    Consider the following empty and completed Sudoku puzzle:
            ---------------------------------           ---------------------------------
            ｜       5 ｜         ｜         ｜         ｜ 1  3  5 ｜ 9  8  4 ｜ 6  7  2 ｜
            ｜         ｜       7 ｜    3  1 ｜         ｜ 9  4  6 ｜ 2  5  7 ｜ 8  3  1 ｜
            ｜       8 ｜ 6       ｜    4    ｜         ｜ 7  2  8 ｜ 6  1  3 ｜ 5  4  9 ｜
            ---------------------------------           ---------------------------------
            ｜    9  4 ｜ 8       ｜         ｜         ｜ 6  9  4 ｜ 8  3  2 ｜ 1  5  7 ｜
            ｜    5    ｜       6 ｜         ｜         ｜ 3  5  7 ｜ 1  9  6 ｜ 2  8  4 ｜
            ｜ 8  1    ｜       5 ｜         ｜         ｜ 8  1  2 ｜ 7  4  5 ｜ 3  9  6 ｜
            ---------------------------------          ---------------------------------
            ｜         ｜ 3  7    ｜ 4     5 ｜         ｜ 2  6  9 ｜ 3  7  8 ｜ 4  1  5 ｜
            ｜       1 ｜ 4       ｜    6    ｜         ｜ 5  8  1 ｜ 4  2  9 ｜ 7  6  3 ｜
            ｜    7    ｜         ｜         ｜         ｜ 4  7  3 ｜ 5  6  1 ｜ 9  2  8 ｜
            ---------------------------------          ---------------------------------

    Example:
                m = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                     [".", "9", "8", ".", ".", ".", ".", "6", "."],
                     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                     [".", "6", ".", ".", ".", ".", "2", "8", "."],
                     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]  # Or, the Sudoku puzzle above.
        Input = m
        Output = m  # m's values will be updated with the corresponding values in the solution above.

    FYI:
        - There are 6,670,903,752,021,072,936,960 (6.67*(10**21)) possible solved Sudoku grids.
        - This reduces to 5,472,730,538 essentially different groups under the validity preserving transformations.
        - There are 26 types of symmetry, but they can only be found in about 0.005% of all filled grids.
        - A puzzle with a unique solution must have at least 17 clues.
        - There is a solvable puzzle with at most 21 clues for every solved grid.
        - The largest minimal puzzle found so far has 40 clues.
        - For more, SEE: wikipedia.org/wiki/Mathematics_of_Sudoku
"""
import time


# APPROACH: Recursion/Backtracking With Three Bit Vectors (As Opposed To Sets)
#
# For each empty cell, all possible values in the range [1..9] are tried if the value is not already in the row/col/box.
#
# Time Complexity: O(9!**9), which reduces to O(1).  This is because (in the worst case) an empty row has 9!
#                  possibilities, and there are 9 rows.
# Space Complexity: O(81), which reduces to O(1).
def sudoku_solver_via_bit_vectors(m):

    def get_bit(x, k):
        return (x >> k) & 1

    def set_bit(x, k):
        return (1 << k) | x

    def clear_bit(x, k):
        return ~(1 << k) & x

    def _rec(i):
        if i == len(empties):
            return True                                         # Check if we filled all empty cells?
        r, c = empties[i]
        box = (r // 3) * 3 + c // 3
        for val in range(1, 10):
            if get_bit(rows[r], val) or get_bit(cols[c], val) or get_bit(boxes[box], val):
                continue                                        # skip if the value is already used!
            m[r][c] = str(val)
            rows[r] = set_bit(rows[r], val)
            cols[c] = set_bit(cols[c], val)
            boxes[box] = set_bit(boxes[box], val)
            if _rec(i + 1):
                return True
            rows[r] = clear_bit(rows[r], val)
            cols[c] = clear_bit(cols[c], val)
            boxes[box] = clear_bit(boxes[box], val)
        return False

    if isinstance(m, list) and len(m) == 9 and all([len(row) == 9 for row in m]):
        rows, cols, boxes, empties = [0] * 9, [0] * 9, [0] * 9, []
        for r in range(9):
            for c in range(9):
                if not 49 <= ord(m[r][c]) <= 57:
                    empties.append([r, c])
                else:
                    val = int(m[r][c])
                    box = (r // 3) * 3 + (c // 3)
                    if get_bit(rows[r], val) or get_bit(cols[c], val) or get_bit(boxes[box], val):
                        raise ValueError("ValueError: Provided Sudoku board is invalid.")
                    rows[r] = set_bit(rows[r], val)
                    cols[c] = set_bit(cols[c], val)
                    boxes[box] = set_bit(boxes[box], val)
        if _rec(0):
            return m
    raise ValueError("ValueError: Provided Sudoku board is invalid.")


# APPROACH: Candidate/Possible Value Sets
#
# NOTE: This is one of the fastest solutions from leetcode; I haven't really looked at it yet, but it does appear to
#       create sets of possible values for each cell in the matrix.
#
# TODO: Analyze this solution.
#
# Time Complexity: O(1).
# Space Complexity: O(1).
def sudoku_solver_via_candidates(m):

    def find_empty_cell_with_min_candidates(candidates):
        i, j, min_v_len = -1, -1, 10
        for k, v in candidates.items():
            if len(v) == 1:                         # There is not a smaller value than 1,
                return k                                # so just return it.
            if len(v) < min_v_len:
                (i, j), min_v_len = k, len(v)
        return i, j

    def place_candidate(m, candidates):
        i, j = find_empty_cell_with_min_candidates(candidates)
        vals = candidates.pop((i, j))
        for n in vals:
            m[i][j] = n
            if not candidates:
                return
            discarded = []
            for (i2, j2), v in candidates.items():
                if (i == i2 or j == j2 or i // 3 == i2 // 3 and j // 3 == j2 // 3) and n in v:
                    if len(v) == 1:  # If only one value available, then something is wrong from the previous steps.
                        for v in discarded:  # Rollback/Backtrack
                            v.add(n)
                        candidates[i, j] = vals
                        return
                    v.discard(n)
                    discarded.append(v)
            place_candidate(m, candidates)
            if not candidates:
                return
            for v in discarded:
                v.add(n)
        candidates[i, j] = vals

    if isinstance(m, list) and len(m) == 9 and all([len(row) == 9 for row in m]):   # Is the board a 9x9, list of lists?
        r_sets = [set() for _ in range(9)]                                          # Check if valid board:
        c_sets = [set() for _ in range(9)]
        g_sets = [[set() for _ in range(3)] for _ in range(3)]
        for r in range(9):
            for c in range(9):
                if 49 <= ord(m[r][c]) <= 57:
                    if m[r][c] in r_sets[r] or m[r][c] in c_sets[c] or m[r][c] in g_sets[r//3][c//3]:
                        raise ValueError("ValueError: Provided Sudoku board is invalid.")
                    r_sets[r].add(m[r][c])
                    c_sets[c].add(m[r][c])
                    g_sets[r//3][c//3].add(m[r][c])

        values = list("123456789")                                                  # Find each cell's candidates.
        candidates = {(r, c): set(values) - r_sets[r] - c_sets[c] - g_sets[r//3][c//3]
                           for r in range(9)
                           for c in range(9)
                           if m[r][c] == '.'}

        r, c = find_empty_cell_with_min_candidates(candidates)
        while candidates and len(candidates[r, c]) == 1:
            val = candidates.pop((r, c)).pop()            # Pop the set returned by popping dict key (r, c).
            m[r][c] = val
            for (x, y), vals in candidates.items():
                if (r == x or c == y or (r//3, c//3) == (x//3, y//3)) and val in vals:
                    vals.discard(val)
            if candidates:
                r, c = find_empty_cell_with_min_candidates(candidates)
        if candidates:
            place_candidate(m, candidates)
        return m
    else:
        raise ValueError("ValueError: Provided Sudoku board is invalid.")


# APPROACH: Recursion/Backtracking With One Seen Set And Fn To Find Empty Cells
#
# This approach uses a SINGLE seen set where the tuples are (value: str, row: int), (column: int, value str), and
# (row//3:int, column//3: int, value: str).  First the seen set is populated with the current state of the provided
# board; if at any point a duplicate is seen (indicating an invalid board) a ValueError is raised.  After the seen set
# is populated, simply try to fill all empty cells (via the recursive function), that is; find an empty cell (row and
# column), then try each value that is not used in the corresponding row, column or grid and continue (with with another
# recursive call).  If all of the values are tried for a given row/column/grid, with none of them working, then the
# function returns False, indicating that the previous calling function needs to try a different value (or backtrack).
# Once all of the cells are filled with valid values (there are 243 unique tuples in the seen set), the board is
# returned.
#
# NOTE: The value in the seen tuples is always a str, this allows for a single seen set (of max size 243 when full).
#
# Time Complexity: O(9!**9), which reduces to O(1).  This is because (in the worst case) an empty row has 9!
#                  possibilities, and there are 9 rows.
# Space Complexity: O(81), which reduces to O(1).
def sudoku_solver(m):

    def _rec(i, todo, m, seen):
        values = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
        r, c = todo[i]
        for v in values:                                    # For each possible value:
            temp = {(v, r), (c, v), (r//3, c//3, v)}            # The sets with the value we will try this iteration.
            if not temp & seen:                                 # IF TEMP DOESN'T CONTAIN DUPLICATES.
                m[r][c] = v                                         # Let's try v at m[r][c]
                seen |= temp                                        # Update seen with current temp set.
                if len(seen) == 243 or _rec(i+1, todo, m, seen):               # If board is Full, OR if RECURSION works;
                    return m                                            # return the board.
                m[r][c] = '.'                                       # Else, backtrack (remove the last tried value and
                seen -= temp                                        # restoring the seen set) for the next iteration...
        return False

    if isinstance(m, list) and len(m) == 9 and all([len(row) == 9 for row in m]):
        seen = set()                                        # Set of filled cells (used to Validate Board State).
        todo = []
        for r, row_vals in enumerate(m):
            for c, val in enumerate(row_vals):
                if 49 <= ord(val) <= 57:
                    for t in ((val, r), (c, val), (r//3, c//3, val)):
                        if t in seen:                       # If provided board is invalid, raise ValueError.
                            raise ValueError("ValueError: Provided Sudoku board is invalid.")
                        seen.add(t)
                else:
                    todo.append((r, c))
        if len(seen) == 243 or _rec(0, todo, m, seen):               # If board is full, or the alg works:
            return m                                        # Return the solved board.
    raise ValueError("ValueError: Provided Sudoku board is invalid.")


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
          [[".", ".", "5", ".", ".", ".", ".", ".", "."],   # Valid, Expert Level
           [".", ".", ".", ".", ".", "7", ".", "3", "1"],
           [".", ".", "8", "6", ".", ".", ".", "4", "."],
           [".", "9", "4", "8", ".", ".", ".", ".", "."],
           [".", "5", ".", ".", ".", "6", ".", ".", "."],
           ["8", "1", ".", ".", ".", "5", ".", ".", "."],
           [".", ".", ".", "3", "7", ".", "4", ".", "5"],
           [".", ".", "1", "4", ".", ".", ".", "6", "."],
           [".", "7", ".", ".", ".", ".", ".", ".", "."]],
          [[".", ".", ".", ".", ".", ".", ".", ".", "."],   # Valid, Inferno Level
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", "1", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", "2", ".", "."],
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
          [["5", "3", ".", ".", "7", ".", ".", ".", "."],   # Valid
           ["6", ".", ".", "1", "9", "5", ".", ".", "."],
           [".", "9", "8", ".", ".", ".", ".", "6", "."],
           ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
           ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
           ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
           [".", "6", ".", ".", ".", ".", "2", "8", "."],
           [".", ".", ".", "4", "1", "9", ".", ".", "5"],
           [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
          [["5", "3", ".", ".", "7", ".", ".", ".", "."],   # Valid
           ["6", ".", ".", "1", "9", "5", ".", ".", "."],
           [".", "9", "8", ".", ".", ".", ".", "6", "."],
           ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
           ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
           ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
           [".", "6", ".", ".", ".", ".", "2", "8", "."],
           [".", ".", ".", "4", "1", "9", ".", ".", "5"],
           [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
          [["1", "1", ".", ".", ".", ".", ".", ".", "."],  # Two 1's in first row.
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."]],
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
           [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
          [['5', '3', '4', '6', '7', '8', '9', '1', '2'],  # Valid, Complete
           ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
           ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
           ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
           ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
           ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
           ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
           ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
           ['3', '4', '5', '2', '8', '6', '1', '7', '9']]]
fns = [sudoku_solver_via_bit_vectors,
       sudoku_solver_via_candidates,
       sudoku_solver]

for i, board in enumerate(boards):
    print(f"\nboards[{i}]:")
    print_formatted_sudoku_board(board)
    for fn in fns:
        print(f"{fn.__name__}(board): ", end='')
        try:
            t = time.time()
            result = fn([r[:] for r in board])
            print("took:", time.time() - t, "seconds.")
            # print_formatted_sudoku_board(result)
        except ValueError as e:
            print('\t', e)
    print()


