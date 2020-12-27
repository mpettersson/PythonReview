"""
    BUILD ORDER (CCI 4.7: BUILD ORDER)

    Write a function which accepts a list of projects and a list of dependencies tuples (the first element is a project
    dependent on the second element, or project), then returns a list of projects representing a valid build order.  If
    there is no valid build order, raise an error.  For a project to be built, all of the project's dependencies must be
    built first.

    Consider the following graph:
            a       c
          ↗   ↘   ↙
        f       d
          ↘   ↗
            b       e

    Example:
                projects = ['a', 'b', 'c', 'd', 'e', 'f']
                dependencies = [('d', 'a'), ('b', 'f'), ('d', 'b'), ('a', 'f'), ('c', 'd')]
        Input = projects, dependencies
        Output = ['e', 'f', 'a', 'b', 'd', 'c']  # or ['f', 'e', 'a', 'b', 'd', 'c'] would also be acceptable.
"""


# Topological Sort (Adjacency List) Approach:  Construct an adjacency list, then execute a topological sort.
# Time Complexity: O(p + d), where p is the number of projects and d is the number of dependency pairs.
# Space Complexity: O(p), where p is the number of projects.
def build_order_adj_list(projects, dependencies):

    def _build_adj_list(projects, dependencies):
        if projects:
            adj_list = {p: [] for p in projects}
            for adj, n in dependencies:
                adj_list[n].append(adj)
            return adj_list
        raise Exception("Should be one or more project.")

    g = _build_adj_list(projects, dependencies)
    if g:
        order = []                                      # Use list as ordering queue.
        proc_next = []                                  # Use list as queue for next node to process.
        num_inbound_edges = {k: 0 for k in g.keys()}    # Most adj lists only store outgoing edges, not incoming.
        for k, v in g.items():                          # Calculate number of incoming edges for each node.
            for n in v:
                num_inbound_edges[n] += 1
        for k, v in num_inbound_edges.items():          # Add nodes w/o incoming edges to queue, IF all nodes have
            if v == 0:                                  # incoming edge(s) then the graph is cyclical!
                proc_next.append(k)
        while proc_next:
            n = proc_next.pop(0)
            for v in g[n]:
                num_inbound_edges[v] -= 1
                if num_inbound_edges[v] == 0:
                    proc_next.append(v)
            order.append(n)
        if sorted(list(g.keys())) == sorted(order):     # If order contains all nodes, then topological sort succeeded.
            return order
    raise Exception("Topological Sort Algorithm Failed")


# Topological Sort (Adjacency Matrix) Approach:  Construct an adjacency matrix, then execute a topological sort.
# Time Complexity: O(p + d), where p is the number of projects and d is the number of dependency pairs.
# Space Complexity: O(p), where p is the number of projects.
def build_order_adj_matrix(projects, dependencies):

    def _build_adj_matrix(projects, dependencies):
        if projects:
            adj_matrix = [[0 for _ in range(len(projects))] for _ in range(len(projects))]
            for proj, req in dependencies:
                adj_matrix[projects.index(req)][projects.index(proj)] = 1
            return adj_matrix
        raise Exception("Should be one or more project.")

    adj_matrix = _build_adj_matrix(projects, dependencies)
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
            order.append(projects[r])
        if sorted(projects) == sorted(order):
            return order
    raise Exception("Topological Sort Algorithm Failed")


# DFS/Recursive Approach:  This approach uses state and the recursion stack to ensure build order (that is, you can't
# add a project to the build order until you've finished/returned from all of it's recursive dependencies/calls).
# Time Complexity: O(p + d), where p is the number of projects and d is the number of dependency pairs.
# Space Complexity: O(p), where p is the number of projects.
def build_order_dfs_adj_list(projects, dependencies):

    def _dfs(n, adj_list, order):
        if adj_list[n][1] == "PARTIAL":
            return False
        if adj_list[n][1] == "BLANK":
            adj_list[n][1] = "PARTIAL"
            for a in adj_list[n][0]:
                if not _dfs(a, adj_list, order):
                    return False
            adj_list[n][1] = "COMPLETE"
            order.insert(0, n)
        return True

    def _build_adj_list(projects, dependencies):
        if projects:
            adj_list = {p: [] for p in projects}
            for adj, n in dependencies:
                adj_list[n].append(adj)
            return adj_list
        raise Exception("Should be one or more project.")

    adj_list = _build_adj_list(projects, dependencies)
    for k in adj_list.keys():
        adj_list[k] = [adj_list[k], "BLANK"]        # Add state to graph; "BLANK" -> "PARTIAL" -> "COMPLETE"
    if adj_list:
        order = []
        for n in adj_list.keys():
            if adj_list[n][1] == "BLANK":
                if not _dfs(n, adj_list, order):
                    return
        return order


projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('d', 'a'), ('b', 'f'), ('d', 'b'), ('a', 'f'), ('c', 'd')]
fns = [build_order_adj_list,
       build_order_adj_matrix,
       build_order_dfs_adj_list]

print(f"projects: {projects}")
print(f"dependencies: {dependencies}\n")
for fn in fns:
    print(f"{fn.__name__}(projects, dependencies): {fn(projects, dependencies)}")


