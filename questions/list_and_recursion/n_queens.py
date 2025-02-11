"""
    N QUEENS (CCI 8.12: EIGHT QUEENS,
              leetcode.com/problems/n-queens)

    Write an function, which accepts an integer n, then generates all valid arrangements of n queens on an nxn chess
    board.  A valid arrangement is one where each queen is on it's own row, column, and diagonals.

    Example:
        Input = 4
        Output = [[1, 3, 0, 2], [2, 0, 3, 1]]  # or
                 ['0 Q 0 0\n0 0 0 Q\nQ 0 0 0\n0 0 Q 0', '0 0 Q 0\nQ 0 0 0\n0 0 0 Q\n0 Q 0 0']  # or
                 [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]

    SEE: https://sites.google.com/site/nqueensolver/home/algorithm-results for an interesting comparison of approaches.
"""
import itertools
import time


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - How should the output be formatted?


# NOTE: The following approaches produce solutions in different formats.


# APPROACH: Naive/Brute Force
#
# This approach generates a list of all possible queen placements (one per column and row) via the itertools
# permutations method, then each of the arrangements are validated, with invalid arrangements being popped/discarded.
#
# Time Complexity: O(n!)
# Space Complexity: O(n)
def n_queens_naive_list(n=8):

    def _check_arrangement(l):
        for i in range(n - 1):
            for j in range(i + 1, n):
                if l[i] is l[j] + (i - j) or l[i] is l[j] + abs(i - j):
                    return False
        return True

    if n is not None and isinstance(n, int) and n > 0:
        results = list(map(list, itertools.permutations(range(n))))
        i = 0
        while i < len(results):
            if _check_arrangement(results[i]):
                i += 1
            else:
                results.pop(i)
        return results


# APPROACH: Recursive/Backtracking
#
# This approach generates a matrix showing the queen placements on a board.  It does this by recursively trying to place
# a queen at each column on a row, when a valid position is found, it then continues on the next row.  When a series of
# recursive attempts result in all n queens being successfully placed, the arrangement is added to the results, it
# backtracks thus resulting in all possible placements.
#
# Time Complexity: O(n!)
# Space Complexity: O(n**2)
def n_queens_rec_matrix(n=8):

    def _check_diagonal(r, c, m):
        for curr_r in range(r):
            curr_left_c = c - (r - curr_r)
            curr_right_c = c + (r - curr_r)
            if (0 <= curr_left_c < len(m[r]) and m[curr_r][curr_left_c]) or (0 <= curr_right_c < len(m[r]) and m[curr_r][curr_right_c]):
                return False
        return True

    def _check_vertical(c, m):
        for r in range(len(m) - 1):
            if m[r][c]:
                return False
        return True

    def _rec(m, results, n):
        if len(m) is n:
            results.append('\n'.join([' '.join(map(str, r)) for r in m]))
        else:
            m.append([0 for _ in range(n)])
            r = len(m) - 1
            for c in range(n):
                m[r][c] = "Q"
                if _check_vertical(c, m) and _check_diagonal(r, c, m):
                    _rec(m, results, n)
                m[r][c] = 0
            m.pop()

    if n is not None and isinstance(n, int) and n > 0:
        result = []
        _rec([], result, n)
        return result


# APPROACH: Recursive/Backtracking
#
# This approach generates a list of possible queen placements (one per column and row) in a similar method to the
# approach above; it recursively generates placements, validating at each step, backtracking when necessary.
#
# Time Complexity: O(n!)
# Space Complexity: O(n)
def n_queens_rec_list(n=8):

    def _check_valid(board, curr_row, curr_col):
        for prev_col in range(curr_col):
            prev_row = board[prev_col]
            if curr_row is prev_row:            # Horizontal Check
                return False
            row_distance = curr_col - prev_col
            col_distance = abs(prev_row - curr_row)
            if row_distance is col_distance:    # Diagonal Check
                return False
        return True

    def _rec(n, col, board, result):
        if col == n:                                        # Base Case
            result.append(board[:])
        else:
            for row in range(n):
                if _check_valid(board, row, col):
                    board[col] = row                       # Place Queen
                    _rec(n, col + 1, board, result)

    if n is not None and isinstance(n, int) and n > 0:
        result = []
        board = [0] * n
        _rec(n, 0, board, result)
        return result


# APPROACH: Recursive/Backtracking (Optimal)
#
# This approach maintains sets for a much quicker placement validation; whenever a queen is placed, the column and
# diagonals are added to sets for quick lookup on subsequent placements.  Note that the rows do not need to be tracked
# and that there are two sets for the diagonals; one 'positive' (bottom left to top right) and one 'negative' (top left
# to bottom right).  The trick in tracking the diagonals is to add the row and column of a queens placement for the
# positive diagonal and to subtract the column from the row for the negative diagonal.
#
# Time Complexity: O(n!)
# Space Complexity: O(n**2)
def n_queens_backtrack(n):

    def _rec(r):        # Recursive Backtracking
        if r == n:
            result.append(["".join(row) for row in board])
        else:
            for c in range(n):
                if c in col or (r+c) in pos_diag or (r-c) in neg_diag:
                    continue
                col.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)
                board[r][c] = "Q"
                _rec(r+1)
                col.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)
                board[r][c] = "."

    if n is not None and isinstance(n, int) and n > 0:
        col = set()
        pos_diag = set()     # (r+c)
        neg_diag = set()     # (r-c)
        result = []
        board = [["."] * n for _ in range(n)]
        _rec(0)
        return result


n_vals = [0, 1, 2, 3, 4, 8]
fns = [n_queens_naive_list,
       n_queens_rec_matrix,
       n_queens_rec_list,
       n_queens_backtrack]

for n in n_vals:
    for fn in fns:
        print(f"{fn.__name__}({n}): {fn(n)}")
    print()

n = 9
for fn in fns[::-1]:
    print(f"{fn.__name__}({n}) took ", end='')
    t = time.time()
    fn(n)
    print(f"{time.time() - t} seconds.")


