r"""
    FIND SHORTEST PATH (50CIQ 12: SHORTEST PATH)

    Given a directed graph, a source nodes, and destination node, create a function to find the shortest path between
    the two nodes if one exists.

    Consider the following graph g:

            0  →  1
          ↙
        2   ↑     ↓
          ↖
            3  ←  4


    Example:
             g = {0: [1, 2], 1: [4], 2: [], 3: [0, 2], 4: [3]}   # This is an adjacency list of the graph above.
        Input  = g, 1, 2
        Output = [1, 3, 3, 2]   # That is, the path: 1 → 4 → 3 → 2
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Ask clarification questions about the INPUT (CYCLES, types, adj list/matrix, etc.).
#   - Input Validation (what if NO path, what if source == destination)?


# APPROACH: BFS (Adjacency List) With Copied Paths
#
# This is an implementation of the BFS for an adjacency list.
#
# Time Complexity: O(n + e), where n is the number of nodes and e is the number of edges in the graph.
# Space Complexity: O(n), where n is the number of nodes in the graph.
def find_shortest_path_adj_list(adj_list, start, dest):
    if isinstance(adj_list, dict) and start in adj_list and dest in adj_list:
        q = [[start]]
        visited = set()
        while q:
            path = q.pop(0)
            n = path[-1]
            visited.add(n)
            for adj in adj_list[n]:
                if adj == dest:
                    return path[:] + [adj]
                if adj not in visited:
                    q.append(path[:]+[adj])


# APPROACH: BFS (Adjacency List)
#
# This is an implementation of the BFS for an adjacency list.
#
# Time Complexity: O(n + e), where n is the number of nodes and e is the number of edges in the graph.
# Space Complexity: O(n), where n is the number of nodes in the graph.
def find_shortest_path_adj_matrix(adj_matrix, start, end):
    if isinstance(adj_matrix, list) and isinstance(adj_matrix[0], list) and isinstance(start, int) and \
            isinstance(end, int) and 0 <= start < len(adj_matrix) and 0 <= end < len(adj_matrix):
        q = [[start]]
        visited = set()
        while q:
            path = q.pop(0)
            n = path[-1]
            visited.add(n)
            for adj, connected in enumerate(adj_matrix[n]):
                if connected:
                    if adj == end:
                        return path + [adj]
                    if adj not in visited:
                        q.append(path[:]+[adj])


adj_list = {0: [1, 2], 1: [4], 2: [], 3: [0, 2], 4: [3]}
adj_matrix = [[0, 1, 1, 0, 0],
              [0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0],
              [1, 0, 1, 0, 0],
              [0, 0, 0, 1, 0]]
args = [(1, 2),
        (2, 1),
        (3, 0),
        (3, 1),
        (3, 4),
        (3, 3),
        (5, 2),
        (5, 5),
        (1, 5),
        (2, 2),
        (1, 1),
        (0, 4),
        (2, None),
        (None, 2),
        (None, None)]
adj_list_fns = [find_shortest_path_adj_list]
adj_matrix_fns = [find_shortest_path_adj_matrix]

print(f"\nadj_list: {adj_list}\n")
for fn in adj_list_fns:
    for source, dest in args:
        print(f"{fn.__name__}(adj_list, {source}, {dest})", fn(adj_list, source, dest))
    print()

print(f"\nadj_matrix: {adj_matrix}\n")
for fn in adj_matrix_fns:
    for source, dest in args:
        print(f"route_between_nodes_dfs(adj_matrix, {source}, {dest})", fn(adj_matrix, source, dest))
    print()


