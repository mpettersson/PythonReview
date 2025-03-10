"""
    NUMBER OF ISLANDS (leetcode.com/problems/number-of-islands)

    Write a function which accepts an m x n matrix (which represents a map) consisting of 1 (land) and 0 (water) values,
    then calculates and returns the number of (horizontally and vertically) connected regions of 1s (islands).

    Example:
        Input: [[1, 1, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 1, 1]]
        Output: 3
"""
import copy


# Questions you should ask the interviewer (if not explicitly stated):
#   - What are the time/space complexities are you looking for?
#   - What are the size limits?
#   - How are the islands encoded/represented?


# APPROACH: DFS/Recursive
#
# This approach iterates over each cell of the matrix.  Each time a 1 is found, the resulting count is incremented by
# one, then a depth first search converts all connected 1s to -1s.  After all cells have been checked/searched a
# second iteration over all cells converts any -1s back to 1s.
#
# Time Complexity: O(rc), where r and c are the number of rows and columns on the board.
# Space Complexity: O(rc), where r and c are the number of rows and columns on the board.
def num_islands_via_dfs(m):
    def _dfs(r, c):
        m[r][c] = -1
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for rd, cd in dirs:
            if 0 <= r + rd < len(m) and 0 <= c + cd < len(m[0]) and m[r + rd][c + cd] == 1:
                _dfs(r + rd, c + cd)

    if isinstance(m, list) and isinstance(m[0], list):
        result = 0
        for r in range(len(m)):
            for c in range(len(m[0])):
                if m[r][c] == 1:
                    result += 1
                    _dfs(r, c)
        for r in range(len(m)):
            for c in range(len(m[0])):
                if m[r][c] == -1:
                    m[r][c] = 1
        return result


# APPROACH: BFS/Iterative Approach
#
# This approach iterates over each cell of the matrix.  Each time a 1 is found, the resulting count is incremented by
# one, then a breadth first search converts all connected 1s to -1s.  After all cells have been checked/searched a
# second iteration over all cells converts any -1s back to 1s.
#
# Time Complexity: O(rc), where r and c are the number of rows and columns on the board.
# Space Complexity: O(rc), where r and c are the number of rows and columns on the board.
def num_islands_via_bfs(m):
    def _bfs(row, col):
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = [(row, col)]
        while q:
            (r, c) = q.pop(0)
            m[r][c] = -1
            for rd, cd in dirs:
                if 0 <= r + rd < len(m) and 0 <= c + cd < len(m[0]) and m[r + rd][c + cd] == 1:
                    q.append((r + rd, c + cd))

    if isinstance(m, list) and isinstance(m[0], list):
        result = 0
        for r in range(len(m)):
            for c in range(len(m[0])):
                if m[r][c] == 1:
                    result += 1
                    _bfs(r, c)
        for r in range(len(m)):
            for c in range(len(m[0])):
                if m[r][c] == -1:
                    m[r][c] = 1
        return result


fns = [num_islands_via_dfs,
       num_islands_via_bfs]
matrices = [[[1, 1, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [0, 0, 1, 0, 0],
             [0, 0, 0, 1, 1]],
            [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]],
            [[1, 0, 1],
             [0, 1, 0],
             [1, 0, 1]],
            [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]],
            [[]]]

for m in matrices:
    m_str = "\n\t".join(["  ".join(map(str, row)) for row in m])
    print(f"\nm:\n\t{m_str}")
    for fn in fns:
        print(f"{fn.__name__}(m):{fn(copy.deepcopy(m))}")


