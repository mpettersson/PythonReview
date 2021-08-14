"""
    TODO:
        - ADD EXAMPLE GRAPHS (USED IN PROBLEMS)
        - ADD VISUAL EXAMPLES OF EACH ADJ LIST/MATRIX
        - ADD CODE COMMENTS
"""


def adj_list_to_adj_mat(graph_as_adj_list):
    reference_dict = {k: i for i, k in enumerate(graph_as_adj_list.keys())}
    graph_as_adj_mat = [[float('inf') for _ in range(len(graph_as_adj_list))] for _ in range(len(graph_as_adj_list))]
    for node, adjs in graph_as_adj_list.items():
        for adj, w in adjs.items():
            graph_as_adj_mat[reference_dict[node]][reference_dict[adj]] = w
    return graph_as_adj_mat


def adj_mat_to_adj_list(graph_as_adj_mat):
    graph_as_adj_list = {i: dict() for i in range(len(graph_as_adj_mat))}
    for row in range(len(graph_as_adj_mat)):
        for col in range(len(graph_as_adj_mat)):
            if graph_as_adj_mat[row][col] != float('inf'):
                graph_as_adj_list[row][col] = graph_as_adj_mat[row][col]
    return graph_as_adj_list


graphs = [{1: {2: 7, 6: 14, 3: 9},
           2: {1: 7, 3: 10, 4: 15},
           3: {1: 9, 6: 2, 4: 11, 2: 10},
           4: {5: 6, 3: 11, 2: 15},
           5: {4: 6, 6: 9},
           6: {1: 14, 3: 2, 5: 9}},
          {'A': {'B': -1, 'C': 4},              # Graph with arbitrary weights.
           'B': {'C': 3, 'D': 2, 'E': 2},
           'C': {},
           'D': {'B': 1, 'C': 5},
           'E': {'D': -3}},
          {'A': {'B': 1, 'C': 4},               # Graph with only positive weights.
           'B': {'C': 3, 'D': 2, 'E': 2},
           'C': {},
           'D': {'B': 1, 'C': 5},
           'E': {'D': 3}},
          {'A': {'B': -1, 'C': 4},              # Graph with a negative weight cycle.
           'B': {'C': 3, 'D': 2, 'E': 2},
           'C': {},
           'D': {'B': 1, 'C': 5, 'E': 1},
           'E': {'D': -3}}]




