"""
    KRUSKAL'S ALGORITHM

    TODO:
        - CONSIDER ADDING AN ADJACENCY LIST VERSION
        - REVIEW DESCRIPTION
        - ADD ASYMPTOTIC COMPLEXITIES

    Kruskal's algorithm finds a MINIMUM SPANNING FOREST of an UNDIRECTED edge-WEIGHTED graph. If the graph is connected,
    it finds a minimum spanning tree. (A minimum spanning tree of a connected graph is a subset of the edges that forms
    a tree that includes every vertex, where the sum of the weights of all the edges in the tree is minimized. For a
    disconnected graph, a minimum spanning forest is composed of a minimum spanning tree for each connected component.)
    It is a greedy algorithm in graph theory as in each step it adds the next lowest-weight edge that will not form a
    cycle to the minimum spanning forest.

    Average Runtime:    O(E log E) time, or equivalently, O(E log V) TODO
    Worst Runtime:      O() TODO
    Best Runtime:       O() TODO
    Space Complexity:   O() TODO
    Alg Paradigm:       Greedy Minimum Spanning Tree

    Graph Properties:
        - Graph must be UNDIRECTED.
        - Graph must be WEIGHTED (todo: can it have negative weights?).
        - Graph CAN have cycles.
        - Graph can be CONNECTED OR DISCONNECTED.

    This algorithm first appeared in Proceedings of the American Mathematical Society, pp. 48–50 in 1956, and was
    written by Joseph Kruskal.

    Algorithm:
        Given a forest F (a set of trees), where each vertex in the graph is a separate tree.
        1.  Create a set S containing all the edges in the graph.
        2.  While S is nonempty and F is not yet spanning:
            2.1  Remove an edge with minimum weight from S
            2.2  If the removed edge connects two   different trees then add it to the forest F, combining two trees into
                 a single tree.
        At the termination of the algorithm, the forest forms a minimum spanning forest of the graph. If the graph is
        connected, the forest has a single component and forms a minimum spanning tree.

    References:
        - wikipedia.org/wiki/Kruskal%27s_algorithm
        - geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5

"""
from collections import defaultdict


# Kruskal's algorithm to find Minimum Spanning Tree of a given connected, undirected and weighted graph.
class Graph:
    def __init__(self, vertices):
        self.size = vertices                    # No. of vertices
        self.graph = []                         # default dictionary to store graph

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):        # Union of x and y by rank.
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)
        if rank[x_root] < rank[y_root]:         # Attach smaller ranked tree under the root of the high ranked tree.
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:                                   # If ranks are the same, select one as root & increment its rank by one.
            parent[y_root] = x_root
            rank[x_root] += 1

    def find_min_spanning_tree_via_kruskal(self):
        result = []                             # This will store the resultant MST
        i = 0                                   # An index variable, used for sorted edges
        e = 0                                   # An index variable, used for result[]
        self.graph = sorted(self.graph, key=lambda x: x[2]) # Step 1:  Sort all edges by non-decreasing weight order.
        parent = []
        rank = []
        for node in range(self.size):           # Create size subsets with single elements
            parent.append(node)
            rank.append(0)
        while e < self.size - 1:                # Number of edges to be taken is equal to size-1
            u, v, w = self.graph[i]             # Step 2: Pick the smallest edge and increment the index for next iter.
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:                          # If including this edge doesn't cause a cycle, include it in the result
                e = e + 1                       # and increment the index of the result for the next edge, otherwise
                result.append([u, v, w])        # discard the edge.
                self.union(parent, rank, x, y)
        minimum_cost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimum_cost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree", minimum_cost)


g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

g.find_min_spanning_tree_via_kruskal()


