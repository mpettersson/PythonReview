"""
    ROUTE BETWEEN NODES (CCI 4.1)

    Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

    For example, given the following graph, node 6, and node 7, the algorithm will return False.  If the graph, node 1,
    and node 0 were supplied, the algorithm would return True.

              1
            /   \
           3     2
         /  \
        4----6   7---8---9
            / \
           5---0

    The above graph as an adjacency matrix:

        # 0  1  2  3  4  5  6  7  8  9
        [[0, 0, 0, 0, 0, 1, 1, 0, 0, 0],  # 0
         [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],  # 1
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
         [0, 1, 0, 0, 1, 0, 1, 0, 0, 0],  # 3
         [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],  # 4
         [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # 5
         [1, 0, 0, 1, 1, 1, 0, 0, 0, 0],  # 6
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # 7
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],  # 8
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]  # 9
"""


def route_between_nodes_via_bfs(g, start_node, end_node):
    g.clear_searched()
    queue = [start_node]
    start_node.searched = True
    while len(queue) > 0:
        curr_node = queue.pop(0)
        if curr_node == end_node:
            return True
        for n in curr_node.adj:
            if not n.searched:
                queue.append(n)
                n.searched = True
    return False


def route_between_nodes_via_dfs(g, start_node, end_node):
    g.clear_searched()
    return depth_first_search(start_node, end_node)


def depth_first_search(curr_node, target_node):
    if curr_node == target_node:
        return True
    if not curr_node.searched:
        curr_node.searched = True
        for n in curr_node.adj:
            if depth_first_search(n, target_node):
                return True
    return False


class GNode:
    def __init__(self, value, adj=None):
        self.value = value
        self.adj = []
        self.searched = False
        if adj:
            if type(adj) is list:
                self.adj += adj
            else:
                self.adj.append(adj)

    def add_adj(self, n):
        if n not in self.adj:
            self.adj.append(n)

    def __repr__(self):
        return repr(self.value)


class Graph:
    def __init__(self, n=None):
        self.nodes = []
        if n:
            self.nodes = self.nodes + n if type(n) is list else self.nodes + [n]

    def __repr__(self):
        nodes = []
        for n in self.nodes:
            nodes.append(repr(n))
        return "[" + ", ".join(nodes) + "]"

    def add_node(self, n):
        if n in self.nodes:
            raise ValueError
        else:
            self.nodes.append(n)

    def to_adj_list(self):
        nodes = ""
        for n in self.nodes:
            nodes += f"{n.value}:{str(n.adj)}\n"
        return nodes

    def clear_searched(self):
        for n in self.nodes:
            n.searched = False


nodes = []
graph = Graph()

for i in range(10):
    nodes.append(GNode(i))
    graph.add_node(nodes[i])

adjs = [[0, 0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]

for row in range(len(adjs)):
    for col in range(len(adjs[0])):
        if adjs[row][col]:
            nodes[row].add_adj(nodes[col])

print(graph)
print(graph.to_adj_list())

for row in range(len(adjs)):
    for col in range(len(adjs[0])):
        if row != col:
            print(f"route_between_nodes_via_bfs(graph, {nodes[row].value}, {nodes[col].value})", route_between_nodes_via_bfs(graph, nodes[row], nodes[col]))
            print(f"route_between_nodes_via_dfs(graph, {nodes[row].value}, {nodes[col].value})", route_between_nodes_via_dfs(graph, nodes[row], nodes[col]))



