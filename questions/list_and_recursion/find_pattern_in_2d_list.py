"""
    FIND PATTERN IN 2D LIST (EPI 17.5: SEARCH FOR A SEQUENCE IN A 2D ARRAY)

    Write a function which accepts a 2D list/matrix (m) of values and a list (l) of pattern values (both the same type),
    then returns a list of index tuples (row, column) if the pattern can be found (traversed) in the 2D list/matrix,
    None otherwise.

    Example:
        Input = [[1, 2, 3],[3, 4, 5],[5, 6, 7]], [1, 3, 4, 6]
        Output = [(0, 0), (1, 0), (1, 1), (2, 1)]

    Variations:
        - Solve the same problem when you cannot visit an entry in m more than once.
        - Enumerate all solutions when you cannot visit an entry in m more than once.
        - NOTE: Some variations of this problem use the term 'WORD SEARCH'.
"""
import copy
import time


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What type of values will be matched (if chars/strings, should case matter)?
#   - What are the possible sizes of the 2D list and pattern list?
#   - Will the 2D list be square or will there be ragged lists?
#   - Can a value in the 2D matrix be used/visited MORE THAN ONCE?
#   - Can the matrix be modified?


# APPROACH: Recursive
#
# TODO
#
# Time Complexity: O(rc(4**n)), where r and c the num of rows & cols in the 2D list, and n is the len of the pattern.
# Space Complexity: O(n), where where n is the length of the pattern.
def find_pattern_in_2d_orig_list_rec(m, p):

    def _rec(r, c, idx):
        if idx == len(p):
            result.insert(0, (r, c))
            return True
        for r_delta, c_delta in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_r = r + r_delta
            next_c = c + c_delta
            if (0 <= next_r < len(m) and                # if next row in range and
                    0 <= next_c < len(m[next_r]) and    # if next col in range and
                    m[next_r][next_c] == p[idx]):       # if the values match:
                if _rec(next_r, next_c, idx+1):             # If it (recursively) works:
                    result.insert(0, (r, c))                    # Add it to the results.
                    return True                                 # And return success.

    if isinstance(m, list) and all(isinstance(sl, list) for sl in m):
        result = []
        for r in range(len(m)):
            for c in range(len(m[r])):
                if m[r][c] == p[0]:
                    if _rec(r, c, 1):
                        return result


# APPROACH:
#
# TODO
#
# Time Complexity: TODO
# Space Complexity: TODO
def find_pattern_in_2d_list_rec(m, p, allow_duplicates_in_path=True):

    def _rec(r, c, i):
        if i == len(p):                 # base case: we find match for each letter in the word
            return []
        if (r < 0 or r == rows or       # Check the current status, before jumping into backtracking
                c < 0 or c == cols or
                m[r][c] != p[i]):
            return None
        result = None
        if not allow_duplicates_in_path:    # ONLY needed for preventing path duplicates.
            m[r][c] = '#'                   # ONLY needed for preventing path duplicates; mark visited, or '#'.
        for r_delta, c_delta in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            result = _rec(r+r_delta, c+c_delta, i+1)
            if result is not None:
                result = [(r, c)] + result
                break
        if not allow_duplicates_in_path:    # ONLY needed for preventing path duplicates.
            m[r][c] = p[i]                  # ONLY needed for preventing path duplicates; REMOVE visited, or '#' status.
        return result

    if isinstance(m, list) and all(isinstance(sl, list) for sl in m) and isinstance(allow_duplicates_in_path, bool):
        rows = len(m)
        cols = len(m[0])
        for row in range(rows):
            for col in range(cols):
                result = _rec(row, col, 0)
                if result is not None:
                    return result


# APPROACH: Memoization/Dynamic Programming
#
# Using a set to record failed attempts of a given row, column, and list index (stored as a tuple), duplicate recursive
# searches are avoided.
#
# Time Complexity: O(rcn), where r & c are the numb of rows and cols in the 2D list, and n is the len of the pattern.
# Space Complexity: O(rcn), where r & c are the numb of rows and cols in the 2D list, and n is the len of the pattern.
def find_pattern_in_2d_list(m, p):

    def _rec(r, c, idx):
        if idx == len(p):
            result.insert(0, (r, c))
            return True
        for r_delta, c_delta in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_r = r + r_delta
            next_c = c + c_delta
            if (0 <= next_r < len(m) and
                    0 <= next_c < len(m[next_r]) and
                    m[next_r][next_c] == p[idx] and
                    (next_r, next_c, idx+1) not in dp):
                if _rec(next_r, next_c, idx+1):
                    result.insert(0, (r, c))
                    return True
                dp.add((next_r, next_c, idx+1))         # If here, then it failed; add the failed tuple to dp.

    if m is not None and p is not None:
        result = []
        m_flat = [e for sl in m for e in sl]
        for c in set(p):
            if m_flat.count(c) < p.count(c):            # OPTIMIZATION: Check if m has p's char count;
                return result                               # If not, return early!
        if m_flat.count(p[-1]) < m_flat.count(p[0]):    # OPTIMIZATION: If m has less occurrences of p's last char:
            p = p[::-1]                                     # Reverse p (there will be fewer start locations).
        dp = set()                                      # dp = 3-tuple(r, c, idx) & are previous failed search attempts.
        for r in range(len(m)):
            for c in range(len(m[r])):
                if m[r][c] == p[0]:
                    if _rec(r, c, 0+1):
                        return result
                    dp.add((r, c, 0))


# NOTE: This approach uses more graph terminology; it has pros and cons, maybe it'll help you conceptualize the problem.
def has_pattern_in_2d_list_via_dfs(m, p):

    def dfs(i, j, k):
        if (i, j) in path:
            return False
        if m[i][j] == p[k]:
            if k+1 == len(p):
                return True
            path.add((i, j))
            if dfs(i, j+1, k+1) or dfs(i+1, j, k+1) or dfs(i, j-1, k+1) or dfs(i-1, j, k+1):
                return True
            path.remove((i, j))
        return False

    rows, cols = len(m), len(m[0])
    m_flat = [e for sl in m for e in sl]
    for c in set(p):
        if m_flat.count(c) < p.count(c):            # OPTIMIZATION: If there aren't enough chars in m for any char in p:
            return False                                # Return False
    if m_flat.count(p[-1]) < m_flat.count(p[0]):    # OPTIMIZATION: If m has less occurrences of p's last char:
        p = p[::-1]                                     # Reverse p (there will be fewer start locations).
    path = set()                                    # Add a boundary path around m, as opposed to checking boundaries.
    for i in range(-1, rows + 1):
        path.add((i, -1))
        path.add((i, cols))
    for j in range(cols):
        path.add((-1, j))
        path.add((rows, j))
    for i in range(len(m)):
        for j in range(len(m[0])):
            if dfs(i, j, 0):
                return True
    return False


def format_matrix(m):
    return "\n\t" + '\n\t'.join([''.join(['{:3}'.format(item) for item in row]) for row in m])


args = [([[1, 2, 3],
          [3, 4, 5],
          [5, 6, 7]], [1, 3, 4, 6]),
        ([[1, 2, 3],
          [3, 4, 5],
          [5, 6, 7]], [1, 2, 3, 4]),
        ([['A', 'B', 'C', 'E'],
          ['S', 'F', 'C', 'S'],
          ['A', 'D', 'E', 'E']], ['A', 'B', 'C', 'C', 'E', 'D']),
        ([['A', 'B', 'C', 'E'],
          ['S', 'F', 'C', 'S'],
          ['A', 'D', 'E', 'E']], ['S', 'E', 'E']),
        ([['A', 'B', 'C', 'E'],
          ['S', 'F', 'C', 'S'],
          ['A', 'D', 'E', 'E']], ['A', 'B', 'C', 'B'])]
fns = [find_pattern_in_2d_orig_list_rec,
       find_pattern_in_2d_list_rec,
       find_pattern_in_2d_list]

for m, p in args:
    print(f"m: {format_matrix(m)}\np: {p}")
    for fn in fns:
        t = time.time()
        print(f"{fn.__name__}(m, p): {fn(copy.deepcopy(m), p)}", end='')
        print(f" (took {time.time() - t} seconds.")
    print()


