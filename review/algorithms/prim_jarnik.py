"""
    PRIM & JARNIK'S ALGORITHM

    TODO:
        - ADJACENCY LIST VERSION
        - COMMENT/REFACTOR ADJACENCY MATRIX VERSION
        - REVIEW DESCRIPTION
        - ADD ASYMPTOTIC COMPLEXITIES

    Prim's algorithm (a.k.a. Jarník's algorithm) is a greedy algorithm to find the MINIMUM SPANNING TREE in a weighted
    undirected graph; that is, it finds a subset of the edges that forms a tree that includes EVERY VERTEX, where the
    TOTAL WEIGHT of all the edges in the tree is MINIMIZED.

    Average Runtime:    O() TODO
    Worst Runtime:      O() TODO
    Best Runtime:       O() TODO
    Space Complexity:   O() TODO
    Alg Paradigm:       Greedy Minimum Spanning Tree

    Graph Properties:
        - Graph must be UNDIRECTED.
        - Graph must be WEIGHTED (todo: can it have negative weights?).
        - Graph CAN have cycles.
        - Graph must be CONNECTED. (Else, need to run the alg on each connected component of the graph!)

    The algorithm was developed in 1930 by Czech mathematician Vojtěch Jarník and later rediscovered and republished by
    computer scientists Robert C. Prim in 1957 and Edsger W. Dijkstra in 1959.

    Other well-known algorithms for this problem include Kruskal's algorithm and Borůvka's algorithm. These algorithms
    find the minimum spanning forest in a possibly disconnected graph; in contrast, the most basic form of Prim's
    algorithm only finds minimum spanning trees in connected graphs. However, running Prim's algorithm separately for
    each connected component of the graph, it can also be used to find the minimum spanning forest. In terms of their
    asymptotic time complexity, these three algorithms are equally fast for sparse graphs, but slower than other more
    sophisticated algorithms. However, for graphs that are sufficiently dense, Prim's algorithm can be made to run in
    linear time, meeting or improving the time bounds for other algorithms.

    References:
        - wikipedia.org/wiki/Prim%27s_algorithm
        - geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5

"""


# A Python program for Prim's Minimum Spanning Tree (MST) algorithm.
# The program is for adjacency matrix representation of the graph
class Graph:

    def __init__(self, number_of_nodes):
        self.size = number_of_nodes
        self.graph = [[0] * self.size for _ in range(self.size)]

    # A utility function to print the constructed MST stored in parent[]
    def print_mst(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.size):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    # finds the vertex with min distance value, from the set of vertices not yet included in shortest path tree
    def min_key(self, key, mst_set):
        min_val = float('inf')
        for v in range(self.size):
            if key[v] < min_val and mst_set[v] is False:
                min_val = key[v]
                min_index = v
        return min_index

    # Function to construct and print MST for a graph represented using adjacency matrix representation
    def find_min_spanning_tree_via_prim(self):
        key = [float('inf')] * self.size    # Key values used to pick minimum weight edge in cut
        parent = [None] * self.size         # list to store constructed MST
        key[0] = 0                          # Make key 0 so that this vertex is picked as first vertex
        mst_set = [False] * self.size
        parent[0] = -1                      # First node is always the root of
        for _ in range(self.size):          # Pick the min distance vertex from the set of vertices not yet processed.
            u = self.min_key(key, mst_set)  # u is always equal to src in first iteration
            mst_set[u] = True               # Put the minimum distance vertex in the shortest path tree
            for v in range(self.size):
                if 0 < self.graph[u][v] < key[v] and not mst_set[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        self.print_mst(parent)


g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]

g.find_min_spanning_tree_via_prim()


