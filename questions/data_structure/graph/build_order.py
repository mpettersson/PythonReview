"""
    BUILD ORDER (CCI 4.7)

    You are given a list of dependencies (which is a list of pairs of projects, where the first project is dependent on
    the second project).  All of a project's dependencies must be built before the project is.  Find a build order that
    will allow the projects to be built.  If there is no valid build order, return an error.

    Example:
        Input = {projects:['a', 'b', 'c', 'd', 'e', 'f'],
                 dependencies:[('d', 'a'), ('b', 'f'), ('d', 'b'), ('a', 'f'), ('c', 'd')]}
        Output = ['e', 'f', 'a', 'b', 'd', 'c']  # or ['f', 'e', 'a', 'b', 'd', 'c'] would also be acceptable.
"""


# Topological Sort (Adjacency List) Approach:  Takes O(p + d) time, where p is the number of projects and d is the
# number of dependency pairs.  Takes O(p) space.
def build_order_adj_list(projects, dependencies):
    g = _build_adj_list(projects, dependencies)
    if g:
        order = []                                      # Use list as ordering queue.
        proc_next = []                                  # Use list as queue for next node to process.
        num_inbound_edges = {k: 0 for k in g.keys()}    # Most adj lists only store outgoing edges, not incoming.
        for k, v in g.items():                          # Calculate number of incoming edges for each node.
            for n in v:
                num_inbound_edges[n] += 1
        for k, v in num_inbound_edges.items():          # Add nodes w/o incoming edges to queue, IF all nodes have
            if v is 0:                                  # incoming edge(s) then the graph is cyclical!
                proc_next.append(k)
        while proc_next:
            n = proc_next.pop(0)
            for v in g[n]:
                num_inbound_edges[v] -= 1
                if num_inbound_edges[v] is 0:
                    proc_next.append(v)
            order.append(n)
        if sorted(list(g.keys())) == sorted(order):     # If order contains all nodes, then topological sort succeeded.
            return order
    raise Exception("Topological Sort Algorithm Failed")


def _build_adj_list(projects, dependencies):
    if projects:
        adj_list = {p: [] for p in projects}
        for adj, n in dependencies:
            adj_list[n].append(adj)
        return adj_list
    raise Exception("Should be one or more project.")


# Topological Sort (Adjacency Matrix) Approach:  Takes O(p + d) time, where p is the number of projects and d is the
# number of dependency pairs.  Takes O(p) space.
def build_order_adj_matrix(projects, dependencies):
    adj_matrix = _build_adj_matrix(projects, dependencies)
    if adj_matrix:
        order = []                                      # Use list as ordering queue.
        proc_next = []                                  # Use list as queue for next node to process.
        num_inbound_edges = [sum([r[c] for r in adj_matrix]) for c in range(len(adj_matrix))]
        for i, v in enumerate(num_inbound_edges):
            if v is 0:
                proc_next.append(i)
        while proc_next:
            r = proc_next.pop(0)
            for c in range(len(adj_matrix)):
                if adj_matrix[r][c]:
                    num_inbound_edges[c] -= 1
                    if num_inbound_edges[c] is 0:
                        proc_next.append(c)
            order.append(projects[r])
        if sorted(projects) == sorted(order):
            return order
    raise Exception("Topological Sort Algorithm Failed")


def _build_adj_matrix(projects, dependencies):
    if projects:
        adj_matrix = [[0 for _ in range(len(projects))] for _ in range(len(projects))]
        for proj, req in dependencies:
            adj_matrix[projects.index(req)][projects.index(proj)] = 1
        return adj_matrix
    raise Exception("Should be one or more project.")


# DFS/Recursive Approach:  This approach uses state and the recursion stack to ensure build order (that is, you can't
# add a project to the build order until you've finished/returned from all of it's recursive dependencies/calls).
# Similar to Topological Sort, this takes O(p + d) time, where p is the number of projects and d is the number of
# dependency pairs, and O(p) space.
def build_order_dfs_adj_list(projects, dependencies):
    adj_list = _build_adj_list(projects, dependencies)
    for k in adj_list.keys():
        adj_list[k] = [adj_list[k], "BLANK"]        # Add state to graph; "BLANK" -> "PARTIAL" -> "COMPLETE"
    if adj_list:
        order = []
        for n in adj_list.keys():
            if adj_list[n][1] is "BLANK":
                if not _dfs(n, adj_list, order):
                    return None
        return order


def _dfs(n, adj_list, order):
    if adj_list[n][1] is "PARTIAL":
        return False
    if adj_list[n][1] is "BLANK":
        adj_list[n][1] = "PARTIAL"
        for a in adj_list[n][0]:
            if not _dfs(a, adj_list, order):
                return False
        adj_list[n][1] = "COMPLETE"
        order.insert(0, n)
    return True


projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('d', 'a'), ('b', 'f'), ('d', 'b'), ('a', 'f'), ('c', 'd')]
print(f"projects: {projects}")
print(f"dependencies: {dependencies}")
print(f"build_order_adj_list(projects, dependencies): {build_order_adj_list(projects, dependencies)}")
print(f"build_order_adj_matrix(projects, dependencies): {build_order_adj_matrix(projects, dependencies)}")
print(f"build_order_dfs_adj_list(projects, dependencies): {build_order_dfs_adj_list(projects, dependencies)}")


