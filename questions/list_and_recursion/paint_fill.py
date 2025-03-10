"""
    PAINT FILL (CCI 8.10,
                leetcode.com/problems/flood-fill)

    Create a 'paint fill', or 'flood-fill'.  The function should accept a matrix (of int values representing colors),
    the starting row index, the starting column index, and a new color.  The function then fills, or updates, all
    (horizontally and vertically) adjacent connected cells of the same original color to the new color.

    Example:
        Input:  [[0, 0, 0, 1], [0, 0, 1, 1]], 0, 0, 1
        Output: [[1, 1, 1, 1], [1, 1, 1, 1]]
"""
import copy


# Questions you should ask the interviewer (if not explicitly stated):
#   - What are the time/space complexities are you looking for?
#   - What are the size limits of the lists?
#   - How are the colors encoded/represented?


# APPROACH: DFS/Recursive
#
# This approach initiates a depth first search at the starting cell, which simply updates the color and recurses on any
# horizontal or vertically adjacent cells with the original color.
#
# Time Complexity: O(rc), where r and c are the number of rows and columns in the image matrix.
# Space Complexity: O(rc), where r and c are the number of rows and columns in the image matrix.
def paint_fill_via_dfs(m, r, c, new_color):

    def _rec(r, c):
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m[r][c] = new_color     # Update cell color.
        for rd, cd in dirs:
            if 0 <= r + rd < len(m) and 0 <= c + cd < len(m[0]) and m[r + rd][c + cd] == old_color:
                _rec(r + rd, c + cd)

    if isinstance(m, list) and all(isinstance(x, int) for x in [r, c, new_color]) and 0 <= r < len(m) and 0 <= c < len(m[r]):
        old_color = m[r][c]         # Get the old color.
        if old_color != new_color:  # Only continue if there is an actual change.
            _rec(r, c)
        return m


# APPROACH: BFS/Iterative Approach
#
# This approach initiates a breadth first search via a queue at the starting cell, which simply updates the color then
# queues any horizontal or vertically adjacent cells with the original color.
#
# Time Complexity: O(rc), where r and c are the number of rows and columns in the image matrix.
# Space Complexity: O(rc), where r and c are the number of rows and columns in the image matrix.
def paint_fill_via_bfs(m, r, c, new_color):
    if isinstance(m, list) and all(isinstance(x, int) for x in [r, c, new_color]) and 0 <= r < len(m) and 0 <= c < len(m[r]):
        old_color = m[r][c]
        if old_color != new_color:
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            q = [(r, c)]
            while q:
                r, c = q.pop(0)
                m[r][c] = new_color
                for rd, cd in dirs:
                    if 0 <= r + rd < len(m) and 0 <= c + cd < len(m[0]) and m[r + rd][c + cd] == old_color:
                        q.append((r + rd, c + cd))
        return m


fns = [paint_fill_via_dfs,
       paint_fill_via_bfs]
images = [[[0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0]],
          [[3, 3, 3, 4],
           [3, 3, 4, 4],
           [3, 3, 3, 4],
           [3, 3, 3, 4],
           [6, 4, 4, 3]],
          [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
           [1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
           [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]]
args = [(0, 0, 0, 1),
        (0, 4, 4, 1),
        (0, 2, 2, 1),
        (1, 1, 1, 5),
        (1, 4, 3, 0),
        (1, 0, 3, 0),
        (1, 0, 0, 4),
        (2, 1, 0, 8)]
for m, r, c, new_color in args:
    m_str = "\n\t".join(["  ".join(map(str, row)) for row in images[m]])
    print(f"\n\nm:\n\t{m_str}")
    for fn in fns:
        result_str = "\t" + "\n\t".join(["  ".join(map(str, row)) for row in fn(copy.deepcopy(images[m]), r, c, new_color)])
        print(f"{fn.__name__}(m, {r}, {c}, {new_color}):\n{result_str}")


