"""
    TODO:
        - ADD EXPLANATION OF ALGORITHM
        - ADD VISUAL GRAPH EXAMPLE
        - ADD BETTER CODE COMMENTS
        - ADD:  Alternative Methods/Algorithms:

    DIJKSTRA'S ALGORITHM

    Single Source Shortest Path Algorithm (SSSP); finds the shortest/minimum weight path from ONE source node, to EVERY
    other node in a weighted directed graph.  Good for sparse graphs.

    Big O:
        - O(E log(V)) Average Time
        - O(V + E) Space Complexity.

    Graph Properties:
        - Graph must be directed.
        - Graph must be weighted with POSITIVE values only.
        - Graph CAN have cycles.
"""
import heapq


# APPROACH: Dijkstra's Algorithm Via Min Heap/heapq
def dijkstra_via_heapq(graph, orig):
    if graph is not None and orig is not None and orig in graph:
        min_heap = []
        previous = {k: None for k in graph.keys()}
        weights = {k: float('inf') for k in graph.keys()}
        weights[orig] = 0
        heapq.heappush(min_heap, (0, orig))
        while len(min_heap) > 0:
            curr_min_node_wt, min_node = heapq.heappop(min_heap)
            for adj, min_node_to_adj_edge_wt in graph[min_node].items():
                if weights[adj] == float('inf'):
                    new_wt = curr_min_node_wt + min_node_to_adj_edge_wt
                    if new_wt < weights[adj]:
                        weights[adj] = new_wt
                        previous[adj] = min_node
                        heapq.heappush(min_heap, (new_wt, adj))
        return weights, previous


# APPROACH: Dijkstra's Algorithm Via Vertices Set (Non-heapq)
def dijkstra_via_set(graph, orig):
    if graph is not None and orig is not None and orig in graph:
        weights = {orig: 0}             # Used to track min weight to vertex (from orig) AND if visited.
        previous = {}
        nodes = set(graph.keys())
        while nodes:
            min_node = None
            for node in nodes:
                if node in weights:
                    if min_node is None:
                        min_node = node
                    elif weights[node] < weights[min_node]:
                        min_node = node
            if min_node is None:        # If min_node is still None then all remaining nodes are NOT reachable from orig
                break
            nodes.remove(min_node)
            curr_min_node_wt = weights[min_node]
            for adj, min_node_to_adj_edge_wt in graph[min_node].items():
                new_wt = curr_min_node_wt + min_node_to_adj_edge_wt
                if adj not in weights or new_wt < weights[adj]:
                    weights[adj] = new_wt
                    previous[adj] = min_node
        return weights, previous


def format_adj_list_dict(adj_list_dict):
    width = len(str(len(adj_list_dict)))
    return '\n\t' + '\n\t'.join([f"{k:>{width}}: {v}" for k, v in adj_list_dict.items()])


graphs = [{'a': {'b': 3, 'c': 2},
           'b': {'a': 4, 'k': 1},
           'c': {'e': 8},
           'd': {'c': 5, 'h': 5},
           'e': {'d': 7},
           'f': {'g': 6},
           'g': {'f': 7, 'h': 4},
           'h': {},
           'i': {'j': 6},
           'j': {'f': 1, 'l': 7},
           'k': {'i': 1},
           'l': {'i': 9},
           'm': {'n': 5},
           'n': {'m': 12}},
          {1: {2: 7, 6: 14, 3: 9},
           2: {1: 7, 3: 10, 4: 15},
           3: {1: 9, 6: 2, 4: 11, 2: 10},
           4: {5: 6, 3: 11, 2: 15},
           5: {4: 6, 6: 9},
           6: {1: 14, 3: 2, 5: 9}},
          {'A': {'B': 1, 'C': 4},
           'B': {'C': 3, 'D': 2, 'E': 2},
           'C': {},
           'D': {'B': 1, 'C': 5},
           'E': {'D': 3}}]
fns = [dijkstra_via_heapq,
       dijkstra_via_set]

for graph in graphs:
    print(f"\ngraph: {format_adj_list_dict(graph)}")
    for fn in fns:
        print(f"{fn.__name__}(graph, list(graph.keys())[0]): {fn(graph, list(graph.keys())[0])}")
    print

