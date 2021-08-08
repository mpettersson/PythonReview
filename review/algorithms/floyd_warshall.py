"""
    FLOYD-WARSHALL ALGORITHM

    All Pairs Shortest Path (APSP) Algorithm; finds the weights of the shortest paths to all nodes. Best for dense
    graphs (most or all nodes are connected). Can be implemented on distributed systems.

    Big O:
        - O(V^3) Time
        - O(V^2) Space

    Graph Properties:
        - Graph must be directed.
        - Graph must be weighted with POSITIVE values only.
        - Graph CAN have cycles.
"""


def floyd_warshall_adj_mat(graph):
    rng = range(len(graph))
    dist = [[float('inf') for _ in rng] for _ in rng]
    nxt = [[0 for _ in rng] for _ in rng]

    for i in rng:
        dist[i][i] = 0

    for row in rng:
        for col in rng:
            dist[row][col] = graph[row][col]
            if graph[row][col] != float('inf'):
                nxt[row][col] = col

    for k in rng:
        for i in rng:
            for j in rng:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    nxt[i][j] = nxt[i][k]

    return dist, nxt


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


graph = [[0, 3, float('inf'), 5],
         [2, 0, float('inf'), 4],
         [float('inf'), 1, 0, float('inf')],
         [float('inf'), float('inf'), 2, 0]];

print(floyd_warshall_adj_mat(graph))
print()


graphs = [{1: {2: 7, 6: 14, 3: 9},
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

# print(graph)
# print(adj_list_to_adj_mat(adj_mat_to_adj_list(graph)))




