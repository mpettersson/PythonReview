"""
    CLONE A GRAPH (EPI 19.5)

    Consider a vertex type for a directed graph in which there are two fields: an integer label and a list of references
    to other vertices.  Design an algorithm that takes a reference to a vertex u, and creates a copy of the graph on the
    vertices reachable from u.  Return the copy of u.

    Consider the following directed graph:

               1
             ↙   ↖
           3       2
         ⤢   ⤡
        4  ⟷  6       7 ⟷ 8
             ⤢   ⤡
        9 ← 5  ⟷  0

    Example:
                vertices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]           # vertices above
                edges = [(2, 1), (1, 3), (3, 4), (4, 3), (3, 6), (6, 3), (4, 6), (6, 4), (6, 5), (5, 6), (6, 0), (0, 6),
                         (5, 0), (0, 5), (5, 9), (7, 8), (8, 7)]    # edges above
                graph = {vertex: Vertex(vertex) for vertex in vertices}; [graph[a].add_edge(graph[b]) for a, b in edges]
        Input = graph[7]
        Output = (7, [8])  # Where the total cloned graph is {7: (7, [8]), 8: (8, [7])}
"""


# BFS Approach:  Time complexity is O(v + e), where v and e are the reachable vertices and edges from the
# given vertex.  Space complexity is O(v), where v is the number of reachable vertices from the given vertex.
def clone_reachable_graph_bfs(vertex):
    if vertex is not None:
        d = {}
        visited = set()
        q = [vertex]
        while len(q) > 0:
            ver = q.pop(0)
            visited.add(ver)
            d[ver.label] = Vertex(ver.label)
            for adj in ver.edges:
                if adj not in visited:
                    q.append(adj)
        for ver in visited:
            for adj in ver.edges:
                d[ver.label].edges.append(d[adj.label])
        return d[vertex.label], d  # Adding the rest of the cloned graph.


# DFS Approach:  Time complexity is O(v + e), where v and e are the reachable vertices and edges from the
# # given vertex.  Space complexity is O(v), where v is the number of reachable vertices from the given vertex.
def clone_reachable_graph_dfs(vertex):
    if vertex is not None:
        d = {}
        visited = set()
        stack = [vertex]
        while len(stack) > 0:
            ver = stack.pop()
            visited.add(ver)
            d[ver.label] = Vertex(ver.label)
            for adj in ver.edges:
                if adj not in visited:
                    stack.append(adj)
        for ver in visited:
            for adj in ver.edges:
                d[ver.label].edges.append(d[adj.label])
        return d[vertex.label], d


class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = []

    def add_edge(self, adj_vertex):
        self.edges.append(adj_vertex)

    def __repr__(self):
        return f"({self.label}, {list(map(lambda x: x.label, self.edges))})"


vertices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
edges = [(2, 1), (1, 3), (3, 4), (4, 3), (3, 6), (6, 3), (4, 6), (6, 4), (6, 5), (5, 6), (6, 0), (0, 6), (5, 0), (0, 5),
         (5, 9), (7, 8), (8, 7)]
args = [0, 1, 7, 9]
graph = {vertex: Vertex(vertex) for vertex in vertices}; [graph[a].add_edge(graph[b]) for a, b in edges]

print(f"graph: {graph}\n")

for vertex_label in args:
    cloned_vertex, cloned_graph = clone_reachable_graph_bfs(graph[vertex_label])
    print(f"clone_reachable_graph_bfs(graph[{vertex_label}]): {cloned_vertex}  (Total Cloned Graph: {cloned_graph})")
print()

for vertex_label in args:
    cloned_vertex, cloned_graph = clone_reachable_graph_dfs(graph[vertex_label])
    print(f"clone_reachable_graph_dfs(graph[{vertex_label}]): {cloned_vertex}  (Total Cloned Graph: {cloned_graph})")


