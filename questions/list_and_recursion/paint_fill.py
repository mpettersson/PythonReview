"""
    PAINT FILL (CCI 8.10)

    Implement the "paint fill" function that one might see on many image editing programs.  That is, given a screen
    (represented by two-dimensional list of colors), a point, and a new color, fill in the surrounding area until the
    color changes from the original color.
"""
import copy


# DFS/Recursive Approach: Time and space complexity is O(rc) where r is the number of rows in the screen (or matrix m)
# and c is the number of columns in the screen (or matrix m).
def paint_fill_dfs(m, row, col, new_color):
    if m is not None and len(m) > 0 and row is not None and 0 <= row < len(m) and col is not None and 0 <= col < len(m[row]) and new_color is not None:
        if m[row][col] != new_color:
            old_color = m[row][col]
            m[row][col] = new_color
            for r in range(row - 1, row + 2):
                if 0 <= r < len(m):
                    for c in range(col - 1, col + 2):
                        if 0 <= c < len(m[r]):
                            if m[r][c] is old_color:
                                paint_fill_dfs(m, r, c, new_color)


# BFS/Iterative Approach: Time complexity is O(rc), where r is the number of rows in the screen (or matrix m) and c is
# the number of columns in the screen (or matrix m).  Space complexity is O(r+c) (more precisely, it is O(2r+2c),
# however, this reduces to O(r+c)).
def paint_fill_bfs(m, row, col, new_color):
    if m is not None and len(m) > 0 and row is not None and 0 <= row < len(m) and col is not None and 0 <= col < len(m[row]) and new_color is not None:
        old_color = m[row][col]
        if old_color is not new_color:
            q = [(row, col)]
            while len(q) > 0:
                r, c = q.pop(0)
                m[r][c] = new_color
                for i in range(r-1, r+2):
                    if 0 <= i < len(m):
                        for j in range(c-1, c+2):
                            if 0 <= j < len(m[i]) and m[i][j] is old_color and (i, j) not in q:
                                q.append((i, j))


def print_screen(m):
    if not m:
        print("None")
    else:
        print('\n'.join([''.join(['{:8}'.format(item) for item in row if len(row) > 0]) for row in m if len(m) > 0]))


screen = [["red", "red", "red", "blue"],
          ["red", "red", "blue", "blue"],
          ["red", "red", "red", "blue"],
          ["red", "red", "red", "blue"],
          ["yellow", "blue", "blue", "red"]]
dfs_screen = copy.deepcopy(screen)
bfs_screen = copy.deepcopy(screen)

print(f"print_screen(dfs_screen):")
print_screen(dfs_screen)

print(f"\npaint_fill_dfs(dfs_screen, 1, 1, 'green'): {paint_fill_dfs(dfs_screen, 1, 1, 'green')}")
print_screen(dfs_screen)

print(f"\npaint_fill_dfs(dfs_screen, 4, 3, 'black'): {paint_fill_dfs(dfs_screen, 4, 3, 'black')}")
print_screen(dfs_screen)

print(f"\npaint_fill_dfs(dfs_screen, 0, 3, 'black'): {paint_fill_dfs(dfs_screen, 0, 3, 'black')}")
print_screen(dfs_screen)

print(f"\npaint_fill_dfs(dfs_screen, 0, 0, 'blue'): {paint_fill_dfs(dfs_screen, 0, 0, 'blue')}")
print_screen(dfs_screen)

print(f"\nprint_screen(bfs_screen):")
print_screen(bfs_screen)

print(f"\npaint_fill_bfs(bfs_screen, 1, 1, 'green'): {paint_fill_bfs(bfs_screen, 1, 1, 'green')}")
print_screen(bfs_screen)

print(f"\npaint_fill_bfs(bfs_screen, 4, 3, 'black'): {paint_fill_bfs(bfs_screen, 4, 3, 'black')}")
print_screen(bfs_screen)

print(f"\npaint_fill_bfs(bfs_screen, 0, 3, 'black'): {paint_fill_bfs(bfs_screen, 0, 3, 'black')}")
print_screen(bfs_screen)

print(f"\npaint_fill_bfs(bfs_screen, 0, 0, 'blue'): {paint_fill_bfs(bfs_screen, 0, 0, 'blue')}")
print_screen(bfs_screen)


