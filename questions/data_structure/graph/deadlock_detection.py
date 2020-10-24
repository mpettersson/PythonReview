"""
    DEADLOCK DETECTION (EPI 19.4)

    High performance database systems use multiple processes and resource locking.  These systems may not provide
    mechanisms to avoid or prevent deadlock: a situation in which two or more competing actions are each waiting for the
    other to finish, which precludes all these actions from progressing.  Such systems must support a mechanism to
    detect deadlocks, as well as an algorithm for recovering from them.

    One deadlock detection algorithm makes use of a "wait-for" graph to track which other processes a process is
    currently blocking on.  In a wait-for graph, processes are represented as nodes, and an edge from process P to Q
    implies Q is holding a resource that P needs and thus P is waiting for Q to release its lock on that resource.  A
    cycle in this graph implies the possibility of a deadlock.  This motivates the following problem.

    Write a program that takes as input a directed graph and checks if the graph contains a cycle.

    Consider the following graph:
            a       c
          ↗   ↘   ↙
        f       d
          ↘   ↗
            b       e

    Example:
        Input = {'a': ['d'], 'b': ['d'], 'c': ['d'], 'd': [], 'e': [], 'f': ['a', 'b']}  # or, the graph above.
        Output = False

    Variations:
        - Solve the same problem for an undirected graph.
        - Write a program that takes as input an undirected graph, which you can assume to be connected, and checks if
          the graph remains connected if any one edge is removed.
        - SEE: build_order.py
"""


# DFS Approach: Perform a DFS while maintaining the states of the vertices, where each node has a color code; white
# (un-searched), gray (currently searching), or black (already searched).  If, during the DFS, a gray node comes across
# another gray node, then a cycle exists.  Time complexity is O(v + e), where v and e are the number of vertices and
# edges in the graph.  Space complexity is O(v), where v is the number of vertices in the graph (if it was more than v,
# that would imply a loop).
def is_directed_graph_cyclic_dfs(adj_list_dict):

    def _is_directed_graph_cyclic_dfs(adj_list_dict, vertex, states):
        if states[vertex] is 'gray':
            return True
        states[vertex] = 'gray'
        for adj in adj_list_dict[vertex]:
            if states[adj] != 'black' and _is_directed_graph_cyclic_dfs(adj_list_dict, adj, states):
                return True
        states[vertex] = 'black'
        return False

    if adj_list_dict is not None:
        states = {k: 'white' for k in adj_list_dict.keys()}
        for vertex in adj_list_dict.keys():
            if states[vertex] is 'white' and _is_directed_graph_cyclic_dfs(adj_list_dict, vertex, states):
                return True
        return False


# BFS/Topological Sort Approach:  This approach depends on the number of incoming/inbound edges for each vertex; once
# the inbound counter for a vertex is zero, that vertex is added to the queue.  When a vertex is popped from the queue
# a total visited counter is incremented.  At the end of the algorithm, if the total visited counter is equal to the
# total number of vertices return True, False otherwise.  Time complexity is O(v + e), where v and e are the number of
# vertices and edges in the graph.  Space complexity is O(v), where v is the number of vertices in the graph.
def is_directed_graph_cyclic_bfs(adj_list_dict):
    if adj_list_dict is not None:
        q = []
        num_visited = 0
        num_inbound_edges = {k: 0 for k in adj_list_dict.keys()}    # Topological Sort need # of INBOUND edges
        for outbound_edges in adj_list_dict.values():
            for edge in outbound_edges:
                num_inbound_edges[edge] += 1
        for vertex, num_edges in num_inbound_edges.items():         # Add all vertices w/o inbound edges; if None,
            if num_edges is 0:                                      # then the graph has a cycle...
                q.append(vertex)
        while len(q) > 0:
            vertex = q.pop(0)
            num_visited += 1
            for adj in adj_list_dict[vertex]:
                num_inbound_edges[adj] -= 1
                if num_inbound_edges[adj] is 0:
                    q.append(adj)
        return len(adj_list_dict) != num_visited


def format_adj_list_dict(adj_list_dict):
    return '\n\t' + '\n\t'.join([f"{k:>2}: {v}" for k, v in adj_list_dict.items()])


directed_graphs = [{'a': ['d'], 'b': ['d'], 'c': ['d'], 'd': [], 'e': [], 'f': ['a', 'b']},     # Not Cyclic
                   {'a': ['d'], 'b': ['d'], 'c': ['d'], 'd': ['f'], 'e': [], 'f': ['a', 'b']},  # Cyclic
                   {'a': ['b'], 'b': ['a']}]                                                    # Cyclic
directed_graph_fns = [is_directed_graph_cyclic_dfs, is_directed_graph_cyclic_bfs]
for i, directed_graph in enumerate(directed_graphs):
    print(f"directed_graph[{i}]: {format_adj_list_dict(directed_graph)}")
    for fn in directed_graph_fns:
        print(f"{fn.__name__}(directed_graph[{i}]): {fn(directed_graph)}")
    print()


# VARIATION: Solve the same problem for an UNDIRECTED GRAPH.

# DFS Approach: Perform a DFS while maintaining the states of the vertices, where each node has a color code; white
# (un-searched), gray (currently searching), or black (already searched).  If, during the DFS, a gray node comes across
# another gray node, then a cycle exists.  Time complexity is O(v + e), where v and e are the number of vertices and
# edges in the graph.  Space complexity is O(v), where v is the number of vertices in the graph (if it was more than v,
# that would imply a loop).
#
# NOTE: In an undirected graph you MUST ALSO track the PREVIOUS vertex, so to not check the path from the last vertex.
def is_undirected_graph_cyclic_dfs(adj_list_dict):

    def _is_undirected_graph_cyclic_dfs(adj_list_dict, vertex, states, prev_v=None):
        if states[vertex] is 'gray':
            return True
        states[vertex] = 'gray'
        for adj in adj_list_dict[vertex]:
            if states[adj] != 'black' and adj != prev_v and _is_undirected_graph_cyclic_dfs(adj_list_dict, adj, states,
                                                                                            vertex):
                return True
        states[vertex] = 'black'
        return False

    if adj_list_dict is not None:
        states = {k: 'white' for k in adj_list_dict.keys()}
        for vertex in adj_list_dict.keys():
            if states[vertex] is 'white' and _is_undirected_graph_cyclic_dfs(adj_list_dict, vertex, states):
                return True
        return False


# BFS/Topological Sort Approach:  This approach tracks the 'parent' of each vertex, or the previous vertex in the path
# (unlike the inbound edge BFS approach for directed graphs).  If an adjacent vertex IS visited, and you didn't come
# from the adjacent vertex (i.e., the current vertex's parent is not the adjacent vertex), then there is a cycle, and
# return True, False otherwise.  Time complexity is O(v + e), where v and e are the number of vertices and edges in the
# graph.  Space complexity is O(v), where v is the number of vertices in the graph.
def is_undirected_graph_cyclic_bfs(adj_list_dict):

    def _has_cycle_undirected_bfs(adj_list_dict, vertex, visited):
        visited[vertex] = True
        q = [(vertex, None)]            # Second tuple item is parent.
        while q:
            vertex, parent = q.pop(0)
            for adj in adj_list_dict[vertex]:
                if not visited[adj]:
                    visited[adj] = True
                    q.append((adj, vertex))
                elif adj != parent:     # If a vertex HAS been visited by a vertex other than parent, that is, if there
                    return True         # is another way to get there, then return True (there is a cycle).
        return False

    if adj_list_dict is not None and len(adj_list_dict) > 1:
        visited = {k: False for k in adj_list_dict.keys()}
        for vertex in adj_list_dict.keys():
            if not visited[vertex] and _has_cycle_undirected_bfs(adj_list_dict, vertex, visited):
                return True
    return False


undirected_graphs = [{0: [1], 1: [0, 2], 2: [1, 3], 3: [2]},                                    # Not Cyclic
                     {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [2, 0]},                              # Cyclic
                     {0: [1], 1: [0]}]                                                          # Not Cyclic
undirected_graph_fns = [is_undirected_graph_cyclic_dfs, is_undirected_graph_cyclic_bfs]

for i, undirected_graph in enumerate(undirected_graphs):
    print(f"undirected_graph[{i}]: {format_adj_list_dict(undirected_graph)}")
    for fn in undirected_graph_fns:
        print(f"{fn.__name__}(undirected_graph[{i}]): {fn(undirected_graph)}")
    print()


