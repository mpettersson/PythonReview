"""
    TODO:
        - ADD EXPLANATION OF ALGORITHM
        - ADD VISUAL GRAPH EXAMPLE
        - ADD BETTER CODE COMMENTS

    TARJAN'S STRONGLY CONNECTED COMPONENTS ALGORITHM

    Strongly Connected Components (SCCs) Algorithm; finds the TODO of a directed graph.

    Tarjan's Strongly Connected Components Algorithm: Finds strongly connected components of a graph, that is, finds sets
    of nodes in which all nodes in the set can reach all other nodes (in the set).

    Big O:
        TODO
            - ? O(V + E) ? Average Time ?
            - ? Space Complexity ?

    Graph Properties:
        TODO
            ? directed/undirected ?
            ? weighted/positive/negative ?
            ? cycles ?

    Alternative Methods/Algorithms:
        - Kosaraju's Algorithm
        - The path-based strong component algorithm.
"""


# APPROACH: Tarjan's Algorithm
def tarjans_algorithm(graph):
    pass


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
fns = [tarjans_algorithm]

for graph in graphs:
    print(f"\ngraph: {format_adj_list_dict(graph)}\n")
    for fn in fns:
        print(f"{fn.__name__}(graph): {fn(graph)}")
    print()


