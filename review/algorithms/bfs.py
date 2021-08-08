"""
    BREADTH FIRST SEARCH (BFS)

    Searches (or traverses) trees and graphs.
    Used for finding shortest paths in O(k^d) time where k is num of adj nodes and d is len of path.
    Bidirectional (Breadth-First) Search is even faster with O(k^(d/2)) time.

    NOTE: Because graphs can have cycles, there must be a check if the node has been previously visited.

    NOTE: Implemented via QUEUE, NOT RECURSION.
"""
import queue


# Find distance from start node to all other nodes.
def bfs_dist(graph, start_node):
    if start_node not in graph.keys():
        raise ValueError("Start node not in graph.")

    q = queue.Queue()
    q.put(start_node)

    visited = {k: False for k in graph.keys()}
    visited[start_node] = True

    dist = {k: -1 for k in graph.keys()}
    dist[start_node] = 0

    while not q.empty():
        node = q.get()
        for adj in graph[node]:
            if not visited[adj]:
                visited[adj] = True
                q.put(adj)
                dist[adj] = dist[node] + 1

    return dist


# Find path from start to end node.
def bfs_path(graph, start_node, end_node):
    pass


graph_1 = {1: [2, 3],
           2: [1],
           3: [1, 4],
           4: [3],
           5: []}


print(bfs_dist(graph_1, 1))


