"""
    PAINT FILL (CCI 8.10,
                leetcode.com/problems/flood-fill)

    Create a 'paint fill', or 'flood-fill', function which accepts a matrix representing the colors of an image, the
    starting row, the starting column, and a new color, and then fills in the surrounding area until the
    color changes from the original color.

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
# This approach uses a depth first search to make the color changes.
#
# Time Complexity: O(rc), where r and c are the number of rows and columns in the image matrix.
# Space Complexity: O(rc), where r and c are the number of rows and columns in the image matrix.
def paint_fill_via_dfs(m, r, c, new_color):

    def _rec(r, c):
        if m[r][c] == old_color:    # Only continue if this cell needs to be updated.
            m[r][c] = new_color     # Update cell color.
            if r-1 >= 0:            # Recurse on the cell to the left (if it exists).
                _rec(r-1, c)
            if r+1 < len(m):        # Recurse on the cell to the right (if it exists).
                _rec(r+1, c)
            if c-1 >= 0:            # Recurse on the cell above (if it exists).
                _rec(r, c-1)
            if c+1 < len(m[0]):     # Recurse on the cell below (if it exists).
                _rec(r, c+1)

    if isinstance(m, list) and all(isinstance(x, int) for x in [r, c, new_color]) and 0 <= r < len(m) and 0 <= c < len(m[r]):
        old_color = m[r][c]         # Get the old color.
        if old_color != new_color:  # Only continue if there is an actual change.
            _rec(r, c)
        return m


# APPROACH: BFS/Iterative Approach
#
# This approach uses a breadth first search to make the color changes.
#
# Time Complexity: O(rc), where r and c are the number of rows and columns in the image matrix.
# Space Complexity: O(rc), where r and c are the number of rows and columns in the image matrix.
def paint_fill_via_bfs(m, r, c, new_color):
    if isinstance(m, list) and all(isinstance(x, int) for x in [r, c, new_color]) and 0 <= r < len(m) and 0 <= c < len(m[r]):
        old_color = m[r][c]
        if old_color != new_color:
            q = [(r, c)]
            while q:
                r, c = q.pop(0)
                if m[r][c] == old_color:    # Only continue if this cell needs to be updated.
                    m[r][c] = new_color     # Update cell color.
                    if r-1 >= 0:            # Queue the cell to the left (if it exists).
                        q.append((r-1, c))
                    if r+1 < len(m):        # Queue the cell to the right (if it exists).
                        q.append((r+1, c))
                    if c-1 >= 0:            # Queue the cell above (if it exists).
                        q.append((r, c-1))
                    if c+1 < len(m[0]):     # Queue the cell below (if it exists).
                        q.append((r, c+1))
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
           [6, 4, 4, 3]]]
args = [(0, 0, 0, 1),
        (0, 4, 4, 1),
        (0, 2, 2, 1),
        (1, 1, 1, 5),
        (1, 4, 3, 0),
        (1, 0, 3, 0),
        (1, 0, 0, 4)]
for m, r, c, new_color in args:
    m_str = "\n\t".join(["  ".join(map(str, row)) for row in images[m]])
    print(f"\n\nm:\n\t{m_str}")
    for fn in fns:
        result_str = "\t" + "\n\t".join(["  ".join(map(str, row)) for row in fn(copy.deepcopy(images[m]), r, c, new_color)])
        print(f"{fn.__name__}(m, {r}, {c}, {new_color}):\n{result_str}")


