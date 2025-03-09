"""
    CAPTURE REGIONS (leetcode.com/problems/surrounded-regions)

    Write a function which accepts an m x n matrix and captures all surrounded regions.  The provided matrix (which
    represents a board) consists of 'X' and 'O' values.  A surrounded region is defined by connected adjacent 'O' cells
    (horizontally or vertically) which are completely surrounded by 'X's.  Capturing a region simply replaces all 'O's
    with 'X's.

    Example:
        Input:  [["X", "X", "X", "X"],
                 ["X", "O", "O", "X"],
                 ["X", "X", "O", "X"],
                 ["X", "O", "X", "X"]]
        Output: [["X", "X", "X", "X"],
                 ["X", "X", "X", "X"],
                 ["X", "X", "X", "X"],
                 ["X", "O", "X", "X"]]

    Variations:
        - Go (game) captured regions.
"""
import copy


# Questions you should ask the interviewer (if not explicitly stated):
#   - What are the time/space complexities are you looking for?
#   - What are the size limits?
#   - How are the X and O encoded/represented?


# APPROACH: DFS/Recursive
#
# This approach first iterates over the board’s edges, running DFS (the _rec function) on any 'O' values to mark the "O"
# region as safe ("S"). The _rec function achieves this by recursively exploring and marking all connected 'O' cells to
# prevent them from being captured. Finally, the board is scanned again, and any 'O' not marked as safe is replaced with
# 'X', as it is fully surrounded.
#
# Time Complexity: O(rc), where r and c are the number of rows and columns on the board.
# Space Complexity: O(rc), where r and c are the number of rows and columns on the board.
def capture_regions_via_dfs(board):
    def _check(r, c):
        return 0 <= r < m and 0 <= c < n and board[r][c] == "O"

    def _rec(r, c):
        board[r][c] = "S"
        if _check(r + 1, c):
            _rec(r + 1, c)
        if _check(r - 1, c):
            _rec(r - 1, c)
        if _check(r, c + 1):
            _rec(r, c + 1)
        if _check(r, c - 1):
            _rec(r, c - 1)

    m = len(board)
    n = len(board[0])
    for r in range(m):
        for c in range(n):
            if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                if board[r][c] == "O":
                    _rec(r, c)
    for r in range(m):
        for c in range(n):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "S":
                board[r][c] = "O"
    return board


# APPROACH: BFS/Iterative Approach
#
# This approach first iterates over the board’s edges, running BFS (the _bfs function) on any 'O' values to mark the "O"
# region as safe ("S"). The _bfs function achieves this via a queue, exploring and marking all connected 'O' cells to
# prevent them from being captured. Finally, the board is scanned again, and any 'O' not marked as safe is replaced with
# 'X', as it is fully surrounded.
#
# Time Complexity: O(rc), where r and c are the number of rows and columns on the board.
# Space Complexity: O(rc), where r and c are the number of rows and columns on the board.
def capture_regions_via_bfs(board):
    def _check(r, c):
        return 0 <= r < m and 0 <= c < n and board[r][c] == "O"

    def _bfs(row, col):
        q = [(row, col)]
        while q:
            (r, c) = q.pop(0)
            board[r][c] = "S"
            if _check(r+1, c):
                q.append((r+1, c))
            if _check(r-1, c):
                q.append((r-1, c))
            if _check(r, c+1):
                q.append((r, c+1))
            if _check(r, c-1):
                q.append((r, c-1))

    m = len(board)
    n = len(board[0])
    for r in range(m):
        for c in range(n):
            if r == 0 or r == m-1 or c == 0 or c == n-1:
                if board[r][c] == "O":
                    _bfs(r, c)
    for r in range(m):
        for c in range(n):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "S":
                board[r][c] = "O"
    return board


fns = [capture_regions_via_dfs,
       capture_regions_via_bfs]
boards = [[['X', 'X', 'X', 'X', 'X', 'O'],
           ['X', 'O', 'O', 'X', 'O', 'X'],
           ['X', 'X', 'X', 'O', 'X', 'X'],
           ['O', 'O', 'X', 'X', 'X', 'X'],
           ['X', 'X', 'X', 'O', 'O', 'X'],
           ['X', 'X', 'X', 'X', 'O', 'X']],
          [["O","O","O"],
           ["O","O","O"],
           ["O","O","O"]],
          [['X', 'X', 'X'],
           ['X', 'X', 'X'],
           ['X', 'X', 'X']],
          [['X', 'X', 'X'],
           ['X', 'O', 'X'],
           ['X', 'X', 'X']],
          [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
           ['X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
           ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']],
          [['X', 'X', 'X', 'X', 'O', 'O', 'O', 'O'],
           ['X', 'X', 'X', 'X', 'O', 'O', 'O', 'O']],
          [["X", 'O', 'X']],
          [['X'],
           ['O'],
           ['X']],
          [[]]]

for board in boards:
    m_str = "\n\t".join(["  ".join(map(str, row)) for row in board])
    print(f"\n\nboard:\n\t{m_str}")
    for fn in fns:
        result_str = "\t" + "\n\t".join(["  ".join(map(str, row)) for row in fn(copy.deepcopy(board))])
        print(f"{fn.__name__}(board):\n{result_str}")


