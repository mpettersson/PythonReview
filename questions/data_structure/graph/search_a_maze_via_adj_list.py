"""
    SEARCH A MAZE (VIA ADJACENCY LIST) (EPI 19.1)

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
                adj_list, orig, dest = build_adj_dict_from_2d_list(maze)
        Input = adj_list, orig, dest
        Output = [90, 91, 81, 71, 61, 62, 63, 53, 43, 44, 45, 46, 36, 37, 27, 17, 18, 8, 9]
"""


# DFS Approach:  The DFS appends and pops off vertices until arriving at the destination vertex or running out of
# reachable vertices; then the path (if there is a path) or None is returned.  Time complexity is O(v + e), where v and
# e are the number of vertices and edges in the graph.  Space complexity is O(v), where v is the number of vertices in
# the graph.
def find_path_via_dfs(adj_list_dict, orig, dest):

    def _find_path_via_dfs(adj_list, curr, dest, visited, path):
        if curr == dest:
            return True
        if curr not in visited:
            visited.append(curr)
            for adj in adj_list[curr]:
                path.append(adj)
                if _find_path_via_dfs(adj_list, adj, dest, visited, path):
                    return True
                path.pop()
        return False

    if adj_list_dict is not None and orig is not None and orig in adj_list_dict and dest is not None:
        path = [orig]
        _find_path_via_dfs(adj_list_dict, orig, dest, [], path)
        return path if len(path) > 1 else None


# BFS W/ Path In Queue Approach:  This approach maintains the path (from the orig to dest) in the queue q.  This makes
# for a shorter/easier to code algorithm at the cost of additional space.  Time complexity is O(v + e), where v and e
# are the number of vertices and edges in the graph.  Space complexity is O(v**2), where v is the number of vertices in
# the graph.
def find_path_via_bfs_queue(adj_list_dict, orig, dest):
    if adj_list_dict is not None and orig is not None and orig in adj_list_dict and dest is not None:
        q = [[orig]]
        visited = []
        while len(q) > 0:
            path = q.pop(0)
            curr = path[-1]
            if curr == dest:
                return path
            if curr in adj_list_dict:
                for adj in adj_list_dict[curr]:
                    if adj not in visited:
                        q.append(list(path) + [adj])
                        visited.append(adj)


# BFS W/ Backtrace Approach:  This approach maintains a previous vertex dictionary (prev_dict), in which each vertex
# points to the previous vertex in the path.  Once a valid path has been found (i.e., the current vertex is the same as
# the destination vertex), a backtrack function is called that reconstructs, then returns, the path.  The tradeoff is
# one additional iteration (of length path) and slightly more complicated/longer code, for less space.  Time complexity
# is O(v + E), where v and e are the number of vertices and edges in the graph.  Space complexity is O(v), where v is
# the number of vertices in the graph.
def find_path_via_bfs_backtrace(adj_list_dict, orig, dest):

    def _backtrace(prev_dict, vertex):
        path = []
        while vertex in prev_dict:
            path.insert(0, vertex)
            vertex = prev_dict[vertex]
        return path

    if adj_list_dict is not None and orig is not None and orig in adj_list_dict and dest is not None:
        q = [orig]
        visited = [orig]
        prev_dict = {orig: None}
        while len(q) > 0:
            curr = q.pop(0)
            if curr == dest:
                return _backtrace(prev_dict, curr)
            if curr in adj_list_dict:
                for adj in adj_list_dict[curr]:
                    if adj not in visited:
                        q.append(adj)
                        visited.append(adj)
                        prev_dict[adj] = curr


# Helper Function: Takes a 2D list with ' ' representing open areas, 'W' representing walls, one 'S' as the starting
# location, and one 'E' as the ending location.  Returns an adjacency list, the orig vertex, and the dest vertex.
def build_adj_list_from_2d_list(l):
    if l is not None:
        adj_list = dict()
        orig = None
        dest = None
        num_rows = len(l)
        max_cols = max(map(len, l))
        for r in range(num_rows):
            for c in range(len(l[r])):
                if l[r][c] != 'W':
                    v = (r * max_cols) + c
                    adj_list[v] = []
                    for delta_r in range(r-1, r+2, 2):
                        if 0 <= delta_r < num_rows and l[delta_r][c] != 'W':
                            adj_list[v].append((delta_r * max_cols) + c)
                    for delta_c in range(c-1, c+2, 2):
                        if 0 <= delta_c < len(l[r]) and l[r][delta_c] != 'W':
                            adj_list[v].append((r * max_cols) + delta_c)
                    if l[r][c] == 'S':
                        orig = v
                    if l[r][c] == 'E':
                        dest = v
        return adj_list, orig, dest


def format_adj_list_dict(adj_list_dict):
    return '\n\t' + '\n\t'.join([f"{k:>2}: {v}" for k, v in adj_list_dict.items()])


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
adj_list_dict, orig, dest = build_adj_list_from_2d_list(maze)

print(f"adj_list: {format_adj_list_dict(adj_list_dict)}\n")

for fn in fns:
    print(f"{fn.__name__}(adj_list, {orig}, {dest}): {fn(adj_list_dict, orig, dest)}\n")


