r"""
    ROUTE BETWEEN NODES (CCI 4.1)

    Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

    Consider the following graph (where each link represents a bi-directional link):

              1
            /   \
           3     2
         /  \
        4----6   7---8
            / \
           5---0

    Example:
        Input = graph, 0, 2   # where graph is the graph above
        Output = True
"""


# DFS Approach (w/ set of visited nodes): Time complexity is O(n + e), where n is the number of nodes and e is the
# number of edges in the graph. Space complexity is O(n).
def route_between_nodes_dfs(graph, start, end, visited_set=None):
    if isinstance(graph, Graph) and isinstance(start, Node) and isinstance(end, Node):
        if start is end:
            return True
        s = visited_set if visited_set else set()
        s.add(start)
        for n in start.neighbors:
            if n not in s:
                if route_between_nodes_dfs(graph, n, end, s):
                    return True
        return False


# DFS Approach (w/ tracked state in the node): Time complexity is O(n + e), where n is the number of nodes and e is the
# number of edges in the graph. Space complexity is O(n).
def route_between_graph_nodes_dfs(graph, start, end):
    def _dfs(start, end):
        if start == end:
            return True
        if not start.searched:
            start.searched = True
            for n in start.neighbors:
                if _dfs(n, end):
                    return True
        return False

    if isinstance(graph, Graph) and isinstance(start, Node) and isinstance(end, Node):
        graph.clear_searched()
        return _dfs(start, end)


# BFS Approach (w/ set of visited nodes): Time complexity is O(n + e), where n is the number of nodes and e is the
# number of edges in the graph. Space complexity is O(n).
def route_between_nodes_bfs(graph, node, dest):
    if isinstance(graph, Graph) and isinstance(node, Node) and isinstance(dest, Node):
        s = set()
        s.add(node)
        q = [node]
        while len(q) > 0:
            n = q.pop(0)
            if n is dest:
                return True
            for adj in n.neighbors:
                if adj not in s:
                    s.add(adj)
                    q.append(adj)
        return False


# DFS Approach (w/ tracked state in the node): Time complexity is O(n + e), where n is the number of nodes and e is the
# number of edges in the graph. Space complexity is O(n).
def route_between_graph_nodes_bfs(graph, start, end):
    if isinstance(graph, Graph) and isinstance(start, Node) and isinstance(end, Node):
        graph.clear_searched()
        queue = [start]
        start.searched = True
        while len(queue) > 0:
            curr_node = queue.pop(0)
            if curr_node == end:
                return True
            for n in curr_node.neighbors:
                if not n.searched:
                    queue.append(n)
                    n.searched = True
        return False


class Node:
    def __init__(self, value, neighbors=None):
        self.value = value
        self.neighbors = []
        self.searched = False
        if neighbors:
            if type(neighbors) is list:
                self.neighbors += neighbors
            else:
                self.neighbors.append(neighbors)

    def add_adj(self, n):
        if n not in self.neighbors:
            self.neighbors.append(n)

    def __repr__(self):
        return repr(self.value)


class Graph:
    def __init__(self, n=None):
        self.nodes = []
        if n:
            self.nodes = self.nodes + n if type(n) is list else self.nodes + [n]

    def __repr__(self):
        return "[" + ', '.join(map(repr, self.nodes)) + "]"

    def __getitem__(self, item):
        if 0 <= item < len(self.nodes):
            return self.nodes[item]

    def __iter__(self):
        return iter(self.nodes)

    def add_node(self, value, neighbors=None):
        for node in self.nodes:
            if node.value == value:
                raise ValueError
        self.nodes.append(Node(value, neighbors))

    def clear_searched(self):
        for n in self.nodes:
            n.searched = False

    def to_adj_matrix(self):
        v_dict = {i: k for i, k in enumerate(self.nodes)}
        return [[1 if v_dict[i] in n.neighbors else 0 for i in range(len(self.nodes))] for n in self.nodes]

    def to_adj_list(self):
        return {n.value: n.neighbors for n in self.nodes}

    def populate_from_adj_matrix(self, adj_mat, values=None):
        length = len(adj_mat)
        if values and len(values) != length:
            raise Exception("values must be None or have the same length as adj_mat")
        if not values:
            values = list(range(len(self.nodes), len(self.nodes) + length))  # Doesn't guarantee valid names/values.
        for v in values:
            self.add_node(v)
        for i, l in enumerate(adj_mat):
            for j, is_adj in enumerate(l):
                if is_adj:
                    self.nodes[-(length - i)].neighbors.append(self.nodes[-(length - j)])

    def populate_from_adj_list(self, adj_list):
        temp = {}
        offset = len(self.nodes)
        for i, k in enumerate(adj_list.keys()):
            temp[k] = offset + i
            self.add_node(k)
        for k, v in adj_list.values():
            for adj in v:
                self.nodes[temp[k]].neighbors.append(self.nodes[temp[adj]])

    def display_adj_matrix(self):
        adj_mat = self.to_adj_matrix()
        if not adj_mat:
            print("None")
        else:
            print('\n'.join([''.join(['{:4}'.format(i) for i in r if len(r) > 0]) for r in adj_mat if len(adj_mat) > 0]))

    def display_adj_list(self):
        adj_list = self.to_adj_list()
        if not adj_list:
            print("None")
        else:
            [print(f"{k:4}: {v}") for k, v in adj_list.items()]


graph = Graph()
adj_mat = [[0, 0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0],
           [0, 1, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 1, 0, 0],
           [1, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1, 0]]
graph.populate_from_adj_matrix(adj_mat)
args = [(graph[0], graph[2]),   # True
        (graph[2], graph[0]),   # True
        (graph[0], graph[7]),   # False
        (graph[7], graph[0]),   # False
        (graph[7], graph[8]),   # True
        (graph[8], Node(9)),    # False
        (graph[0], None),       # None
        (None, graph[0]),       # None
        (None, None)]           # None

print("graph:")
graph.display_adj_list()
print()

for source, dest in args:
    print(f"route_between_nodes_dfs(graph, {source}, {dest})", route_between_nodes_dfs(graph, source, dest))
print()

for source, dest in args:
    print(f"route_between_nodes_bfs(graph, {source}, {dest})", route_between_nodes_bfs(graph, source, dest))


