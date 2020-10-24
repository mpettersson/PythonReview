"""
    TEAM REACHABILITY

    Given teams a and b, is there a sequence of teams starting with a and ending with b such that each team in the
    sequence has beaten the next team in the sequence?

    Example:
                graph = {'Texas': ['Cal'], 'Cal': ['Stanford'], 'Stanford': ['Texas', 'MIT', 'CIT'], 'UCLA': ['USC']}
        Input = graph, 'Texas', 'MIT'
        Output = True  # Texas -> Cal -> Stanford -> MIT
"""


# Adjacencies Dict DFS  Approach:  Time and space complexity is O(g), where g is the number of distinct game results.
def is_reachable_dfs(adj_dict, curr, dest, visited_set=None):
    if curr is dest:
        return True
    if curr in adj_dict:
        if visited_set is None:
            visited_set = set()
        elif curr in visited_set:
            return False
        visited_set.add(curr)
        for team in adj_dict[curr]:
            if is_reachable_dfs(adj_dict, team, dest, visited_set):
                return True
    return False


# Adjacencies Dict BFS Approach: Time and space complexity is O(g), where g is the number of distinct game results.
def is_reachable_bfs(adj_dict, curr, dest):
    q = [curr]
    visited_set = {curr}
    while len(q) > 0:
        v = q.pop(0)
        if v is dest:
            return True
        if v in adj_dict:
            for n in adj_dict[v]:
                if n not in visited_set:
                    visited_set.add(n)
                    q.append(n)
    return False


#  Time and Space complexity is dependent on the search_fn (see is_reachable_dfs and is_reachable_bfs above).
def can_team_a_beat_team_b(adj_dict, team_a, team_b, search_fn):
    if adj_dict is not None and team_a is not None and team_b is not None and team_a in adj_dict:
        return search_fn(adj_dict, team_a, team_b)


def build_adjacency_dict(games_results):
    if games_results is not None:
        d = {}
        for winner, looser in games_results:
            d.setdefault(winner, [])
            d[winner].append(looser)
        return d


adj_dict = build_adjacency_dict([("Texas", "Cal"),
                                 ("Cal", "Stanford"),
                                 ("Stanford", "Texas"),
                                 ("Stanford", "MIT"),
                                 ("Stanford", "CIT"),
                                 ("UCLA", "USC")])
search_fns = [is_reachable_dfs, is_reachable_bfs]
args = [("Texas", "MIT"),
        ("Cal", "UCLA")]

print(f"adj_dict: {adj_dict}\n")

for team_a, team_b in args:
    for search_fn in search_fns:
        print(f"can_team_a_beat_team_b(adj_dict, {team_a!r}, {team_b!r}, {search_fn.__name__}):",
              can_team_a_beat_team_b(adj_dict, team_a, team_b, search_fn))
    print()


