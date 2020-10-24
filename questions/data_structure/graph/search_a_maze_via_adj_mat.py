"""
    SEARCH A MAZE (VIA ADJACENCY MATRIX) (EPI 19.1)

    It is natural to apply graph models and algorithms to spatial problems.  Consider a 2D list with the following char
    values; ' ' represent open areas, 'W' are walls, 'S' is the starting location, and 'E' is the ending location.

    Given a 2D list of char entries representing a maze, as defined above, find a path from the starting location to the
    ending location, if one exists.

    Consider the 2D list, maze:
        maze = [['W', ' ', ' ', ' ', ' ', ' ', 'W', 'W', ' ', 'E'],
                [' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                ['W', ' ', 'W', ' ', ' ', 'W', 'W', ' ', 'W', 'W'],
                [' ', ' ', ' ', 'W', 'W', 'W', ' ', ' ', 'W', ' '],
                [' ', 'W', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', 'W', 'W', ' ', ' ', 'W', ' ', 'W', 'W', ' '],
                [' ', ' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' '],
                ['W', ' ', 'W', ' ', 'W', ' ', 'W', ' ', ' ', ' '],
                ['W', ' ', 'W', 'W', ' ', ' ', ' ', 'W', 'W', 'W'],
                ['S', ' ', ' ', ' ', ' ', ' ', ' ', 'W', 'W', ' ']]

    Example:
                adj_mat, orig, dest = build_adj_dict_from_2d_list(maze)
        Input = adj_mat, orig, dest
        Output = [90, 91, 81, 71, 61, 62, 63, 53, 43, 44, 45, 46, 36, 37, 27, 17, 18, 8, 9]
"""


# DFS Approach:  The DFS appends and pops off vertices until arriving at the destination vertex or running out of
# reachable vertices; then the path (if there is a path) or None is returned.  Time complexity is O(v + e), where v and
# e are the number of vertices and edges in the graph.  Space complexity is O(v), where v is the number of vertices in
# the graph.
def find_path_via_dfs(adj_mat, orig, dest):

    def _find_path_via_dfs(adj_mat, curr, dest, visited, path):
        if curr == dest:
            return True
        if curr not in visited:
            visited.append(curr)
            for adj, v in enumerate(adj_mat[curr]):
                if v is 1:
                    path.append(adj)
                    if _find_path_via_dfs(adj_mat, adj, dest, visited, path):
                        return True
                    path.pop()
        return False

    if adj_mat and orig is not None and dest is not None and 0 <= orig < len(adj_mat) and 0 <= dest < len(adj_mat):
        path = [orig]
        _find_path_via_dfs(adj_mat, orig, dest, [], path)
        return path if len(path) > 1 else None


# BFS W/ Path In Queue Approach:  This approach maintains the path (from the orig to dest) in the queue q.  This makes
# for a shorter/easier to code algorithm at the cost of additional space.  Time complexity is O(v + e), where v and e
# are the number of vertices and edges in the graph.  Space complexity is O(v**2), where v is the number of vertices in
# the graph.
def find_path_via_bfs_queue(adj_mat, orig, dest):
    if adj_mat and orig is not None and dest is not None and 0 <= orig < len(adj_mat) and 0 <= dest < len(adj_mat):
        q = [[orig]]
        visited = []
        while len(q) > 0:
            path = q.pop(0)
            curr = path[-1]
            if curr == dest:
                return path
            for c, v in enumerate(adj_mat[curr]):
                if v == 1 and c not in visited:
                    q.append(list(path) + [c])
                    visited.append(c)


# BFS W/ Backtrace Approach:  This approach maintains a previous vertex dictionary (prev_dict), in which each vertex
# points to the previous vertex in the path.  Once a valid path has been found (i.e., the current vertex is the same as
# the destination vertex), a backtrack function is called that reconstructs, then returns, the path.  The tradeoff is
# one additional iteration (of length path) and slightly more complicated/longer code, for less space.  Time complexity
# is O(v + E), where v and e are the number of vertices and edges in the graph.  Space complexity is O(v), where v is
# the number of vertices in the graph.
def find_path_via_bfs_backtrace(adj_mat, orig, dest):

    def _backtrace(prev_dict, vertex):
        path = []
        while vertex in prev_dict:
            path.insert(0, vertex)
            vertex = prev_dict[vertex]
        return path

    if adj_mat and orig is not None and dest is not None and 0 <= orig < len(adj_mat) and 0 <= dest < len(adj_mat):
        q = [orig]
        visited = [orig]
        prev_dict = {orig: None}
        while len(q) > 0:
            curr = q.pop(0)
            if curr == dest:
                return _backtrace(prev_dict, curr)
            for adj, v in enumerate(adj_mat[curr]):
                if v == 1 and adj not in visited:
                    q.append(adj)
                    visited.append(adj)
                    prev_dict[adj] = curr


# Helper Function: Takes a 2D list with ' ' representing open areas, 'W' representing walls, one 'S' as the starting
# location, and one 'E' as the ending location.  Returns an adjacency matrix, the orig vertex, and the dest vertex.
# The adjacency matrix consists of 0s and 1s only, where a 0 is a wall, and a 1 is a possible path; the orig and dest
# vertex values are returned separate, and is not reflected in the produced adjacency matrix.
def build_adj_mat_from_2d_list(l):
    if l is not None and len(l) > 0 and len(l[0]) > 0:
        num_rows = len(l)
        max_cols = max(map(len, l))
        adj_mat = [[0 for _ in range(num_rows * max_cols)] for _ in range(num_rows * max_cols)]
        orig = None
        dest = None
        for r in range(num_rows):
            for c in range(len(l[r])):
                if l[r][c] != 'W':
                    for delta_r in range(r-1, r+2, 2):
                        if 0 <= delta_r < len(l) and l[delta_r][c] != 'W':
                            adj_mat[(r * max_cols)+c][(delta_r * max_cols)+c] = 1
                    for delta_c in range(c-1, c+2, 2):
                        if 0 <= delta_c < len(l[r]) and l[r][delta_c] != 'W':
                            adj_mat[(r*max_cols)+c][(r*max_cols)+delta_c] = 1
                    if l[r][c] == 'E':
                        dest = (r * max_cols) + c
                    if l[r][c] == 'S':
                        orig = (r * max_cols) + c
        return adj_mat, orig, dest


def format_matrix(mat):
    return '\n\t' + '\n\t'.join([''.join(map(str, row)) for row in mat])


maze = [['W', ' ', ' ', ' ', ' ', ' ', 'W', 'W', ' ', 'E'],
        [' ', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['W', ' ', 'W', ' ', ' ', 'W', 'W', ' ', 'W', 'W'],
        [' ', ' ', ' ', 'W', 'W', 'W', ' ', ' ', 'W', ' '],
        [' ', 'W', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', 'W', 'W', ' ', ' ', 'W', ' ', 'W', 'W', ' '],
        [' ', ' ', ' ', ' ', 'W', ' ', ' ', ' ', ' ', ' '],
        ['W', ' ', 'W', ' ', 'W', ' ', 'W', ' ', ' ', ' '],
        ['W', ' ', 'W', 'W', ' ', ' ', ' ', 'W', 'W', 'W'],
        ['S', ' ', ' ', ' ', ' ', ' ', ' ', 'W', 'W', ' ']]
fns = [find_path_via_dfs, find_path_via_bfs_queue, find_path_via_bfs_backtrace]
adj_mat, orig, dest = build_adj_mat_from_2d_list(maze)

print(f"adj_mat: {format_matrix(adj_mat)}\n")

for fn in fns:
    print(f"{fn.__name__}(adj_mat, {orig}, {dest}): {fn(adj_mat, orig, dest)}\n")


