"""
    NETWORK TIME DELAY (leetcode.com/problems/network-delay-time)

    Consider a network with n nodes (labelled 1 to n) where communication from one node to another is known.  Given a
    list of connection communication time tuples (source, destination, time), the number of nodes (n), and the node
    initiating the signal (k), write a function that computes and returns the amount of time for ALL nodes to receive
    the signal, -1 otherwise.

    Consider the following graph, where the number of arrows between two nodes represents the weight of the edge:

            1
          ↗
        2   →   3 ← ← 6
          ↖   ↙      ↗
            4 ⟷ ⟷ ⟷ 5

    Example:
        times = [(2, 1, 1), (2, 3, 1), (3, 4, 1), (4, 2, 1), (6, 3, 2), (4, 5, 3), (5, 4, 3), (5, 6, 1)]
        Input = times, 6, 2
        Output = 6
"""
import collections
import heapq


# APPROACH: Dijkstra Algorithm via heapq
#
# This is a heapq implementation of Dijkstra's single source shortest path (SSSP) algorithm.
#
# Time Complexity:  O((e+v)*log(v)), where e and v are the number of edges and vertices in the graph.
# Space Complexity:  O(e + v), where e and v are the number of edges and vertices in the graph.
#
# SEE: leetcode.com/problems/network-delay-time/discuss/329376/efficient-oe-log-v-python-dijkstra-min-heap-with-explanation
def network_time_delay_via_dijkstra(times, n, k):
    graph = collections.defaultdict(dict)   # Uses default factory, so there is no need to add keys first;
    for frm, to, cost in times:             # each value defaults to an empty dict (i.e., {k0: {}, ..., kn:{}} )
        graph[frm][to] = cost               # Note: This only adds nodes WITH edges to graph (however, this is OK).
    distances = {i: float("inf") for i in range(1, n + 1)}
    distances[k] = 0                        # Resulting distances/weights for each node (start at infinity).
    min_dist = [(0, k)]                     # Min Heap/Priority Queue: [(distance, node) ... ]
    visited = set()                         # Skip duplicates (in O(1) time).

    while min_dist:
        cur_dist, cur_node = heapq.heappop(min_dist)
        if cur_node in visited:
            continue
        visited.add(cur_node)
        for neighbor in graph[cur_node]:
            if neighbor in visited:
                continue
            new_dist = cur_dist + graph[cur_node][neighbor]
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(min_dist, (new_dist, neighbor))

    if len(visited) != len(distances):
        return -1
    return distances[max(distances, key=distances.get)]


# APPROACH: Bellman-Ford Algorithm
#
# This is an implementation of the Bellman-Ford single source shortest path (SSSP) algorithm.
#
# Time Complexity:  O(ve), where v and e are the number of vertices and edges in the graph.
# Space Complexity:  O(ve), where v and e are the number of vertices and edges in the graph.
def network_time_delay_via_bellman_ford(times, n, k):
    graph = {i: dict() for i in range(1, n+1)}          # Initialize the Graph/Weight/Previous Dictionaries
    for frm, to, cost in times:
        graph[frm][to] = cost
    weights = {}
    previous = {}
    for node in graph:
        weights[node] = float('Inf')
        previous[node] = None
    weights[k] = 0

    for _ in range(len(graph)-1):                       # "Arc Relaxation"
        for node in graph:
            for adj in graph[node]:
                if weights[adj] > weights[node] + graph[node][adj]:
                    weights[adj] = weights[node] + graph[node][adj]
                    previous[adj] = node

    for node in graph:                                  # Negative-weight Cycle Check
        for adj in graph[node]:
            if weights[adj] > weights[node] + graph[node][adj]:
                raise ValueError("Graph contains a negative weight cycle.")

    result = weights[max(weights, key=weights.get)]
    return -1 if result == float('inf') else result     # Bellman-Ford would normally return (weights, previous) here.


times = [(2, 1, 1), (2, 3, 1), (3, 4, 1), (4, 2, 1), (6, 3, 2), (4, 5, 3), (5, 4, 3), (5, 6, 1)]
n = 6
fns = [network_time_delay_via_dijkstra,
       network_time_delay_via_bellman_ford]
print(f"\ntimes (Source, Destination, Time): {times}\n")

for start_node in range(1, n+1):
    for fn in fns:
        print(f"{fn.__name__}(times, {n}, {start_node}): {fn(times, n, start_node)}")
    print()


