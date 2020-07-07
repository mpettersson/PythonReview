from enum import Enum


class GNodeState(Enum):
    UNVISITED = 1
    VISITED = 2
    VISITING = 3


class GNode:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.state = GNodeState.UNVISITED
        self.neighbors = set()

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_neighbors(self):
        return self.neighbors

    def add_neighbor(self, node):
        self.neighbors.add(node)

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def is_visited(self):
        return self.state == GNodeState.VISITED

    def set_visited(self):
        self.state = GNodeState.VISITED


class Graph:
    def __init__(self):
        self.nodes = []
        self.map = dict()

    def has_node(self, name):
        return name in self.map.keys()

    def get_node(self, name):
        if name in self.map.keys():
            return self.map[name]
        else:
            return None

    def get_nodes(self):
        return self.nodes

    def create_node(self, name, value):
        if name in self.map.keys():
            return self.map[name]
        node = GNode(name, value)
        self.nodes.append(node)
        self.map[name] = node
        return node

    def add_node(self, node):
        if node.get_name() in self.map.keys():
            return self.get_node(node.get_name())
        self.nodes.append(node)
        self.map[node.get_name()] = node

    def add_edge(self, name_one, name_two):
        node_one = self.get_node(name_one)
        node_two = self.get_node(name_two)
        if node_one is not None and node_two is not None:
            node_one.add_neighbor(node_two)
            node_two.add_neighbor(node_one)


