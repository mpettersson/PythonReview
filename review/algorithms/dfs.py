"""
    DEPTH FIRST SEARCH (DFS)

    Searches (or traverses) trees and graphs.
    Used for solving puzzles with only one solution (such as mazes).
    Used for Topological Sorting/Scheduling.
    Preferred for visiting every node in the graph (because it is simpler than BFS).

    NOTE: Because graphs can have cycles, there must be a check if the node has been previously visited.
"""


def dfs(graph, start_node):
    pass


def iterative_dfs(graph, start):
    seen = set()
    path = []
    q = [start]
    while q:
        v = q.pop()             # no reason not to pop from the end, where it's fast
        if v not in seen:
            seen.add(v)
            path.append(v)
            q.extend(graph[v].keys())  # adds the nodes reversed order; for in-order add use: reversed(graph[v])
    return path


graph_1 = {1: [2, 3],
           2: [1],
           3: [1, 4],
           4: [3],
           5: []}

graph_0 = {0: {1: 3, 3: 5},
           1: {0: 2, 3: 4},
           2: {1: 1},
           3: {2: 2}}

print(iterative_dfs(graph_0, 0))

