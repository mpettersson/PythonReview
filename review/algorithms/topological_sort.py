"""
    TOPOLOGICAL SORT

    Orders a list of nodes such that if edge(a, b) is in the graph, a will be ordered before b in the list.

    Complexity (where v is number of vertices (nodes) and e is number of edges in graph):
        Average Runtime:    O(v + e)
        Worst Runtime:      O(v + e)
        Best Runtime:       O(v + e)
        Worst Space:        O(v + e)

    Requirements:
        Graph MUST be directed.
        Graph CAN NOT have cycles.

    Uses:
        Scheduling jobs or tasks with dependencies (jobs are nodes, dependencies are edges).
        Data serialization.

    NOTE: Requires the count of each nodes INBOUND edges; most nodes/adjacency lists typically store outbound edges.

"""


def topological_sort(g):
    if g:
        result = []                                     # Use list as ordering queue.
        queue = []                                      # Use list as queue for next node to process.
        num_inbound_edges = {k: 0 for k in g.keys()}    # Most adj lists only store outgoing edges, not incoming.
        for k, v in g.items():                          # Calculate number of incoming edges for each node.
            for n in v:
                num_inbound_edges[n] += 1
        for k, v in num_inbound_edges.items():          # Add nodes w/o incoming edges to queue, IF all nodes have
            if v == 0:                                  # incoming edge(s) then the graph is cyclical!
                queue.append(k)
        while queue:
            n = queue.pop(0)
            for v in g[n]:
                num_inbound_edges[v] -= 1
                if num_inbound_edges[v] == 0:
                    queue.append(v)
            result.append(n)
        if sorted(list(g.keys())) == sorted(result):    # If order contains all nodes, then topological sort succeeded.
            return result
    raise Exception(f"Graph {g} has failed the Topological Sort algorithm.")


def build_order_adj_matrix(adj_matrix):
    if adj_matrix:
        order = []                                      # Use list as ordering queue.
        proc_next = []                                  # Use list as queue for next node to process.
        num_inbound_edges = [sum([r[c] for r in adj_matrix]) for c in range(len(adj_matrix))]
        for i, v in enumerate(num_inbound_edges):
            if v == 0:
                proc_next.append(i)
        while proc_next:
            r = proc_next.pop(0)
            for c in range(len(adj_matrix)):
                if adj_matrix[r][c]:
                    num_inbound_edges[c] -= 1
                    if num_inbound_edges[c] == 0:
                        proc_next.append(c)
            order.append(r)
        if len(order) == len(adj_matrix):
            return order
    raise Exception("Topological Sort Algorithm Failed")


def iterative_dfs(graph, start):
    seen = set()
    path = []
    q = [start]
    while q:
        v = q.pop()             # no reason not to pop from the end, where it's fast
        if v not in seen:
            seen.add(v)
            path.append(v)
            q.extend(graph[v])  # adds the nodes reversed order; for in-order add use: reversed(graph[v])
    return path


def iterative_topological_sort(graph, start):
    seen = set()
    stack = []    # path variable is gone, stack and order are new
    order = []    # order will be in reverse order at first
    q = [start]
    while q:
        v = q.pop()
        if v not in seen:
            seen.add(v)  # no need to append to path any more
            q.extend(graph[v])
            while stack and v not in graph[stack[-1]]:   # new stuff here!
                order.append(stack.pop())
            stack.append(v)
    return stack + order[::-1]   # new return value!


def recursive_dfs(graph, node):
    result = []
    seen = set()

    def recursive_helper(node):
        for neighbor in graph[node]:
            if neighbor not in seen:
                result.append(neighbor)     # this line will be replaced below
                seen.add(neighbor)
                recursive_helper(neighbor)

    recursive_helper(node)
    return result


def recursive_topological_sort(graph, node):
    result = []
    seen = set()

    def recursive_helper(node):
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                recursive_helper(neighbor)
        result.insert(0, node)              # this line replaces the result.append line

    recursive_helper(node)
    return result


graphs = [{'a': ['b', 'c'],         # Acyclic Connected Graph
           'b': ['d'],
           'c': ['d'],
           'd': ['e'],
           'e': []},
          {'a': ['d'],              # Acyclic Graph with Isolated Subgraph (node is e is not connected to other nodes)
           'b': ['d'],
           'c': [],
           'd': ['c'],
           'e': [],
           'f': ['a', 'b']},
          {'a': ['b'],              # (Connected) Cyclic Graph
           'b': ['c'],
           'c': ['a']},
          {}
          ]

for i, graph in enumerate(graphs):
    try:
        print(f"topological_sort(graph[{i}]):", topological_sort(graph))
    except Exception as e:
        print(f"topological_sort(graph[{i}]): Exception: {e.args}")
print()

for i, graph in enumerate(graphs):
    try:
        print(f"iterative_dfs(graph[{i}], 'a']):", iterative_dfs(graph, 'a'))
    except Exception as e:
        print(f"topological_sort(graph[{i}]): Exception: {e.args}")
print()

for i, graph in enumerate(graphs):
    try:
        print(f"iterative_topological_sort(graph[{i}], 'a']):", iterative_topological_sort(graph, 'a'))
    except Exception as e:
        print(f"iterative_topological_sort(graph[{i}]): Exception: {e.args}")
print()

for i, graph in enumerate(graphs):
    try:
        print(f"recursive_dfs(graph[{i}], 'a']):", recursive_dfs(graph, 'a'))
    except Exception as e:
        print(f"recursive_dfs(graph[{i}]): Exception: {e.args}")
print()

for i, graph in enumerate(graphs):
    try:
        print(f"recursive_topological_sort(graph[{i}], 'a']):", recursive_topological_sort(graph, 'a'))
    except Exception as e:
        print(f"recursive_topological_sort(graph[{i}]): Exception: {e.args}")
print()



