"""
    SHORTEST SNAKES AND LADDERS PATH

    Design an algorithm, which when given two list of tuples representing the start and end of the Snakes and Ladders
    on the board, will return the shortest path (i.e., least number of rolls) to the end.

    You can assume that the board consists of positions 1 to 100, where 1 is the start and 100 is the end.  Furthermore,
    Snakes and Ladders cannot start on position 1 or 100 (however they may end on any position), and a dice roll
    produces a random int in the range [1,6].
"""
import heapq


def find_shortest_path(snakes, ladders):
    graph = generate_graph(snakes, ladders)
    source = 1
    min_queue = []
    weights = {k: float('inf') for k in graph.keys()}
    previous = {k: None for k in graph.keys()}
    visited = {k: False for k in graph.keys()}
    weights[source] = 0
    heapq.heappush(min_queue, (0, source))
    while len(min_queue) > 0:
        w_to_node, node = heapq.heappop(min_queue)
        visited[node] = True
        for adj, w_to_adj in graph[node]:
            if not visited[adj]:
                new_w = w_to_node + w_to_adj
                if new_w < weights[adj]:
                    weights[adj] = new_w
                    previous[adj] = node
                    heapq.heappush(min_queue, (new_w, adj))
    path = []
    node = max(graph.keys())
    while node:
        path.insert(0, node)
        node = previous[node]
    return -1 if weights[100] == float('inf') else weights[100], path if path[0] == 1 and path[-1] == 100 else None


def generate_graph(num_spaces, snakes=None, ladders=None):
    if num_spaces <= 0:
        raise ValueError()
    graph = {}
    for i in range(1, num_spaces + 1):
        graph[i] = []
        j = 1
        while j < 7 and i + j <= num_spaces:
            graph[i].append((i + j, 1))
            j += 1
    for (s, e) in ladders:
        if s not in graph or e not in graph or s <= 1 or s == e or s >= num_spaces or e <= 1:
            raise ValueError()
        graph[s].append((e, 0))
    for (s, e) in snakes:
        if s not in graph or e not in graph or s <= 1 or s == e or s >= num_spaces:
            raise ValueError()
        graph[s] = [(e, 0)]
    return graph


boards = [  # Board 1 - Should be 3 dice rolls.
            ([(95, 13), (97, 25), (93, 37), (79, 27), (75, 19), (49, 47), (67, 17)], [(32, 62), (42, 68), (12, 98)]),
            # Board 2 - Should be 5 dice rolls.
            ([(51, 19), (39, 11), (37, 29), (81, 3), (59, 5), (79, 23), (53, 7), (43, 33), (77, 21)], [(8, 52), (6, 80), (26, 42), (2, 72)]),
            # Board 3 - Should be 3 dice rolls.
            ([(56, 33)], [(3, 54), (37, 100)]),
            # Board 4 - Should be 2 dice rolls.
            ([(88, 44)], [(3, 57), (8, 100)]),
            # Board 5 - Should be 2 dice rolls.
            ([(99, 1)], [(7, 98)])]

for snakes, ladders in boards:
    num_dice_rolls, path = find_shortest_path(snakes, ladders)
    print(f"Number of rolls: {num_dice_rolls}, Path: {path}")




