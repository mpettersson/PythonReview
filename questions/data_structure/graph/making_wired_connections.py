"""
    MAKING WIRED CONNECTIONS (EPI 19.6)

    Consider a collection of electrical pins on a printed circuit board (PCB).  For each pair of pins, there may or may
    not be a wire joining them.

    Design an algorithm that takes a set of pins and a set of wires connecting pairs of pins and determines if it is
    possible to place some pins on the left half of a PCB, and the remainder on the right half, such that each wire is
    between left and right halves.  Return such a division, if on exists.

    Consider the following set of 'pins' and 'wires', where the white and dark vertices are such a division:

            ⬤--◯--⬤--◯--⬤--◯--⬤--◯--⬤                  0----1--2--3---4---5---6---7---8
            ｜   ｜   ⟍  ⟍     ⟋⟍    ⟋    ｜                  ｜   ｜   ⟍  ⟍    ⟋⟍    ⟋    ｜
            ｜   ｜     ⟍  ⟍ ⟋    ⟍⟋      ｜                  ｜   ｜     ⟍  ⟍⟋    ⟍⟋      ｜
            ◯---⬤------◯-⬤      ⬤      ｜        OR        9---10------11-12     13      ｜
            ｜    ⟍      ｜ ｜      ｜      ｜                  ｜    ⟍      ｜ ｜      ｜      ｜
            ｜      ⟍    ｜ ｜      ｜      ｜                  ｜      ⟍    ｜ ｜      ｜      ｜
            ⬤-------◯--⬤-◯--⬤--◯--⬤--◯                  14------15---16-17--18--19--20-21


    Example:
                vertices = list(range(22))      # The vertices above.
                edges = [(0, 1), (0, 9), (1, 2), (1, 10), (2, 3), (2, 11), (3, 4), (3, 12), (4, 5), (5, 6), (5, 12),
                         (5, 13), (6, 7), (7, 8), (7, 13), (8, 21), (9, 10), (9, 14), (10, 11), (10, 15), (11, 12),
                         (11, 16), (12, 17), (13, 19), (14, 15), (15, 16), (16, 17), (17, 18), (18, 19), (19, 20),
                         (20, 21), (6, 13)]     # The edges above.
                graph = {v: set() for v in vertices}; [(graph[a].add(b), graph[b].add(a)) for a, b in edges]
        Input = graph
        Output = True

    Hint: Model as a graph and think about the implication of an odd length cycle.
"""


# BFS Approach:  All cycles must have an even number of edges, or length, for the division as described above. This
# approach uses a bool value to determine if a vertex is odd/even.  Time complexity is O(v + e), where v and e, are the
# number of vertices and edges in the adjacency list.  Space complexity is O(v), where v is the number of vertices in
# the adjacency list.
def is_2_colorable_bfs(adj_list_dict):

    def _is_2_colorable_bfs(adj_list_dict, v, visited):
        q = [(v, True)]
        while len(q) > 0:
            v, b = q.pop(0)
            for adj in adj_list_dict[v]:
                if (adj, b) in q or (adj, b) in visited:
                    return False
                if (adj, not b) not in q and adj not in visited.keys():
                    q.append((adj, not b))
            visited[v] = b
        return True

    if adj_list_dict is not None:
        visited = {}    # When finished, visited[vertex] = True|False AKA odd|even, black|white, or left|right
        for vertex in adj_list_dict.keys():
            if vertex not in visited.keys() and not _is_2_colorable_bfs(adj_list_dict, vertex, visited):
                return False
        return True


# BFS Distance Approach:  This approach computes the distance from an arbitrary vertex to all other reachable vertices
# in the adjacency list; if the graph is not connected, it arbitrarily picks a non-visited vertex until all nodes have
# been visited. Time complexity is O(v + e), where v and e, are the number of vertices and edges in the adjacency list.
# Space complexity is O(v), where v is the number of vertices in the adjacency list.
def is_2_colorable_bfs_alt(adj_list_dict):

    def _is_2_colorable_bfs_alt(adj_list_dict, v, visited):
        visited[v] = 0
        q = [v]
        while len(q) > 0:
            v = q[0]
            for adj in adj_list_dict[v]:
                if visited[adj] is -1:
                    visited[adj] = visited[v] + 1
                    q.append(adj)
                elif visited[adj] == visited[v]:
                    return False
            q.pop(0)
        return True

    if adj_list_dict is not None:
        visited = {v: -1 for v in adj_list_dict.keys()}  # Visited tracks distance from arbitrary vertices.
        for vertex in adj_list_dict.keys():
            if visited[vertex] is -1 and not _is_2_colorable_bfs_alt(adj_list_dict, vertex, visited):
                return False
        return True


def format_adj_list_dict(adj_list_dict):
    return '\n\t' + '\n\t'.join([f"{k:>2}: {v}" for k, v in adj_list_dict.items()])


vertices = list(range(22))
edges = [(0, 1), (0, 9), (1, 2), (1, 10), (2, 3), (2, 11), (3, 4), (3, 12), (4, 5), (5, 6), (5, 12), (5, 13), (6, 7),
         (7, 8), (7, 13), (8, 21), (9, 10), (9, 14), (10, 11), (10, 15), (11, 12), (11, 16), (12, 17), (13, 19),
         (14, 15), (15, 16), (16, 17), (17, 18), (18, 19), (19, 20), (20, 21)]
graph = {v: set() for v in vertices}; [(graph[a].add(b), graph[b].add(a)) for a, b in edges]

print(f"graph: {format_adj_list_dict(graph)}\n")
print(f"is_2_colorable_bfs(graph): {is_2_colorable_bfs(graph)}")
print(f"is_2_colorable_bfs_alt(graph): {is_2_colorable_bfs_alt(graph)}\n")

new_edges = [(1, 13), (0, 13)]
for a, b in new_edges:
    graph[a].add(b)
    graph[b].add(a)
    print(f"If there was an additional edge between {a} and {b}:")
    print(f"\tis_2_colorable_bfs(graph): {is_2_colorable_bfs(graph)}")
    print(f"\tis_2_colorable_bfs_alt(graph): {is_2_colorable_bfs_alt(graph)}\n")
    graph[a].remove(b)
    graph[b].remove(a)


