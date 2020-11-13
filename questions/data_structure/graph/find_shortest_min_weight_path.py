"""
    FIND SHORTEST MIN WEIGHT PATH (EPI 19.9: COMPUTE A SHORTEST PATH WITH FEWEST EDGES)

    Given a weighted (directed or undirected) graph with start and end nodes, write a function to find the shortest
    (number of edges) minimum weight path.

    Example:
                graph = {'a': {'b': 3, 'c': 2},
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
                         'n': {'m': 12}}
        Input = graph, 'a', 'h'
        Output = ['a', 'c', 'e', 'd', 'h']  # has a weight sum of 22.

    NOTE: ['a', 'b', 'k', 'i', 'j', 'f', 'g', 'h'] also has weight 22, however, it has 3 extra edges.

    Variations:
        - A flight is specified by a start-time, originating city, destination city, and arrival-time (possibly on a
          later day).  A time-table is a set of flights.  Given a time-table, a starting city, a starting time, and a
          destination city, how would you compute the soonest you could get to the destination city?  Assume all flights
          start and end on time, that you need 60 minutes between flights, and a flight departing from A to B cannot
          arrive earlier at B than another flight from A to B which departed earlier.
"""
import heapq


# Vertices Set/Non-heapq Dijkstra's Alg. Approach
# Time Complexity: O(v**2), where v are the number of vertices in the graph.
# Space Complexity: O(v), where v is the number of vertices in the graph.
def dijkstra(graph, orig, dest=None):
    if graph is not None and orig is not None and orig in graph and (dest is None or dest in graph):
        weights = {orig: 0}             # Used to track min weight to vertex (from orig) AND if visited.
        previous = {}
        nodes = set(graph.keys())
        while nodes:
            min_node = None
            for node in nodes:          # Find vertex with minimum weight (since no min heap/heapq)
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
        if dest is None:                # If dest is None, return weights and previous dicts.
            return weights, previous
        path = [dest]
        while True:                     # Build then return the path from orig to dest if it exists.
            if path[0] is None or path[0] is orig:
                return path if path[0] is orig else None
            path.insert(0, previous.get(path[0], None))


# Min Heap/heapq Dijkstra's Alg. Approach
# Time Complexity: O((v+e) * log(v)), where v and e are the number of vertices and edges in the graph.
# Space complexity: O(v), where v is the number of vertices in the graph.
def dijkstra_heapq(graph, orig, dest=None):
    if graph is not None and orig is not None and orig in graph and (dest is None or dest in graph):
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
        if dest is None:
            return weights, previous
        path = [dest]
        while True:                     # Build then return the path from orig to dest if it exists.
            if path[0] is None or path[0] is orig:
                return path if path[0] is orig else None
            path.insert(0, previous.get(path[0], None))


def format_adj_list_dict(adj_list_dict):
    return '\n\t' + '\n\t'.join([f"{k:>2}: {v}" for k, v in adj_list_dict.items()])


graph = {'a': {'b': 3, 'c': 2},
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
         'n': {'m': 12}}
args = [('a', 'h'),
        ('b', 'h'),
        ('a', 'n'),
        ('m', 'n'),
        ('a', 'z'),
        ('x', 'y'),
        ('a', None)]

print(f"graph: {format_adj_list_dict(graph)}\n")

for orig, dest in args:
    print(f"dijkstra(graph, {orig!r}, {dest!r}): {dijkstra(graph, orig, dest)}")
print()

for orig, dest in args:
    print(f"dijkstra_heapq(graph, {orig!r}, {dest!r}): {dijkstra_heapq(graph, orig, dest)}")


