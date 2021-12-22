"""
    TODO:
        - ADD EXPLANATION OF ALGORITHM
        - ADD VISUAL GRAPH EXAMPLE
        - ADD BETTER CODE COMMENTS
        - ADD:  Alternative Methods/Algorithms:
        - Add this:
            As already stated in the chosen answer, Bellman-Ford performs the check on all the vertices, Dijkstra only on the one with the best distance calculated so far. Again already noted, this improves the complexity of the Dijkstra approach, however it requires to compare all the vertices to find out the minimum distance value. Being this not necessary in the Bellman-Ford, it is easier to implement in a distributed environment. That's why it is used in Distance Vector routing protocols (e.g., RIP and IGRP), where mostly local information is used. To use Dijkstra in routing protocols, instead, it is necessary first to distribute the entire topology, and this is what happens in Link State protocols, such as OSPF and ISIS.
            https://stackoverflow.com/questions/19482317/bellman-ford-vs-dijkstra-under-what-circumstances-is-bellman-ford-better

    BELLMAN-FORD ALGORITHM

    Single Source Shortest Path Algorithm (SSSP); finds the shortest/minimum weight path from ONE source node, to EVERY
    other node in a weighted directed graph.

    Big O:
        - O(VE) Time
        - O(V + E) Space

    Graph Properties:
        - Graph must be directed.
        - Graph must be weighted (Positive OR Negative).
        - Graph CAN have cycles.
"""


# APPROACH: Bellman-Ford Algorithm
def bellman_ford(graph, source):
    weights = {}                                # Initialization
    previous = {}
    for node in graph:
        weights[node] = float('Inf')
        previous[node] = None
    weights[source] = 0

    for _ in range(len(graph)-1):               # "Arc Relaxation"
        for node in graph:
            for adj in graph[node]:
                if weights[adj] > weights[node] + graph[node][adj]:
                    weights[adj] = weights[node] + graph[node][adj]
                    previous[adj] = node

    for node in graph:                          # Negative-weight Cycle Check
        for adj in graph[node]:
            if weights[adj] > weights[node] + graph[node][adj]:
                return None, None               # Or Could: raise ValueError("Graph contains a negative weight cycle.")

    return weights, previous


def format_adj_list_dict(adj_list_dict):
    width = len(str(len(adj_list_dict)))
    return '\n\t' + '\n\t'.join([f"{k:>{width}}: {v}" for k, v in adj_list_dict.items()])


graphs = [{'A': {'B': -1, 'C': 4},              # Graph with arbitrary weights.
           'B': {'C': 3, 'D': 2, 'E': 2},
           'C': {},
           'D': {'B': 1, 'C': 5},
           'E': {'D': -3}},
          {'A': {'B': 1, 'C': 4},               # Graph with positive weights.
           'B': {'C': 3, 'D': 2, 'E': 2},
           'C': {},
           'D': {'B': 1, 'C': 5},
           'E': {'D': 3}},
          {'A': {'B': -1, 'C': 4},              # Graph with a negative weight cycle.
           'B': {'C': 3, 'D': 2, 'E': 2},
           'C': {},
           'D': {'B': 1, 'C': 5, 'E': 1},
           'E': {'D': -3}}]
fns = [bellman_ford]

for i, g in enumerate(graphs):
    print(f"\ngraphs[{i}]: {format_adj_list_dict(g)}\n")
    for source_node in g:
        for fn in fns:
            print(f"{fn.__name__}(graphs[{i}], {source_node!r}): ", fn(g, source_node))
    print()


