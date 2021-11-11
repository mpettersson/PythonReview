"""
    EIGHT QUEENS (CCI 8.12)

    Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board so that none of them share the
    same row, column, or diagonal. In this case, "diagonal" means all diagonals, not just the two that bisect the board.
"""
import copy
import itertools

# SEE: https://sites.google.com/site/nqueensolver/home/algorithm-results for an interesting comparison of approaches.


# Naive/Brute Force List Approach:  Get all permutations of a list representation of the queens arrangements, then check
# and remove invalid arrangements.
def arrange_queens_via_list_naive(size=8):

    def _check_arrangement(l):
        for i in range(size - 1):
            for j in range(i + 1, size):
                if l[i] is l[j] + (i - j) or l[i] is l[j] + abs(i - j):
                    return False
        return True

    results = list(map(list, itertools.permutations(range(size), size)))

    i = 0
    while i < len(results):
        if _check_arrangement(results[i]):
            i += 1
        else:
            results.pop(i)

    if len(results) is 0:
        print(f"No possible queen arrangement for {size}x{size} board.")
    else:
        for i, result in enumerate(results):
            print(f"Arrangement {i}:\n{result}\n")


# Recursive/Backtracking Matrix Approach:  Try to arrange a queen at each column on a row, if the attempt is a valid
# placement, then recurse to the next row.  When a series of recursive attempts has all queens arranged, the arrangement
# is added to the results and control 'backtracks' to a previous row (stack state) to continue placements (and possibly
# more recursive calls).
def arrange_queens_via_matrix(size=8):

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

    def _arrange_queens_via_matrix(m, results, size):
        if len(m) is size:
            results.append('\n'.join([' '.join(map(str, r)) for r in m]))
        else:
            m.append([0 for _ in range(size)])
            r = len(m) - 1
            for c in range(size):
                m[r][c] = "Q"
                if _check_vertical(c, m) and _check_diagonal(r, c, m):
                    _arrange_queens_via_matrix(m, results, size)
                m[r][c] = 0
            m.pop()

    if size is not None and 0 < size:
        results = []
        _arrange_queens_via_matrix([], results, size)
        if len(results) is 0:
            print(f"No possible queen arrangement for {size}x{size} board.")
        else:
            for i, result in enumerate(results):
                print(f"Arrangement {i}:\n{result}\n")


# Recursive/Backtracking List Approach:  Similar to the above matrix approach, however, just using a list to represent
# the queens position in a matrix.
def arrange_queens_via_list(size=8):

    def _check_valid(queens, curr_row, curr_col):
        for prev_col in range(curr_col):
            prev_row = queens[prev_col]
            if curr_row is prev_row:            # Horizontal Check
                return False
            row_distance = curr_col - prev_col
            col_distance = abs(prev_row - curr_row)
            if row_distance is col_distance:    # Diagonal Check
                return False
        return True

    def _arrange_queens_via_list(size, col, queens, results):
        if col is size:                                     # Base Case
            results.append(copy.deepcopy(queens))
        else:
            for row in range(size):
                if _check_valid(queens, row, col):
                    queens[col] = row                       # Place Queen
                    _arrange_queens_via_list(size, col+1, queens, results)

    if size is not None and size > 0:
        results = []
        queens = [0] * size
        _arrange_queens_via_list(size, 0, queens, results)
        if len(results) is 0:
            print(f"No possible queen arrangement for {size}x{size} board.")
        else:
            for i, result in enumerate(results):
                print(f"Arrangement {i}:\n{result}\n")


n = 8
print(f"arrange_queens_via_list_naive({n}):")
arrange_queens_via_list_naive(n)

print(f"arrange_queens_via_matrix({n}):")
arrange_queens_via_matrix(n)

print(f"arrange_queens_via_list({n}):")
arrange_queens_via_list(n)


