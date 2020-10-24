"""
    TEAM PHOTO DAY--2 (EPI 19.8)

    How would you generalize your solution to TEAM PHOTO DAY/team_photo_day.py, to determine the largest number of teams
    that can be photographed simultaneously subject to the same constraints?

    Team Photo Day Constraints:
        - All teams have the same number of players.
        - A team photo consists of a front row of players and a back row of players.
        - A player in the back row must be taller than the player in front of him.
        - All players in a row must be from the same team.

    Hint: Form a DAG in which paths correspond to valid placements.
"""
import random


# DAG And DFS Approach:  Create a Directed Acyclic Graph (DAG), then use DFS to find the longest path.  Time complexity
# is O(n**2) in the worst case, where n is the number of teams.  Space complexity is O(n + n**2) in the worst case,
# where n is the number of teams. 
def most_teams_in_photo(teams):

    # O(n) time.  O(1) space.
    def _can_photograph_teams(a_name, a_heights, b_name, b_heights):
        if a_heights is not None and b_heights is not None and len(a_heights) is len(b_heights) and len(a_heights) > 0:
            flag1 = flag2 = True
            i = 0
            while (flag1 or flag2) and i < len(a_heights):
                flag1 = flag1 and a_heights[i] > b_heights[i]
                flag2 = flag2 and a_heights[i] < b_heights[i]
                i += 1
            if flag1:
                return True, a_name, b_name
            if flag2:
                return True, b_name, a_name
        return False, None, None

    # O(n**2) time.  O(n) space.
    def _build_adj_list(teams):
        adj_list_dict = {k: set() for k in teams.keys()}
        [v.sort() for v in teams.values()]
        for team_a_name, team_a_heights in teams.items():
            for team_b_name, team_b_heights in teams.items():
                if team_a_name != team_b_name:
                    b, orig, dest = _can_photograph_teams(team_a_name, team_a_heights, team_b_name, team_b_heights)
                    if b:
                        adj_list_dict[orig].add(dest)
        return adj_list_dict

    # O(n**2) time.  O(n) space.
    def _dfs(adj_list_dict, stack, visited, curr=None):
        if curr is None:
            for vertex in adj_list_dict.keys():
                if vertex not in visited:
                    _dfs(adj_list_dict, stack, visited, vertex)
        else:
            visited.add(curr)
            for adj in adj_list_dict[curr]:
                if adj not in visited:
                    _dfs(adj_list_dict, stack, visited, adj)
            stack.append(curr)

    max_distance = 0
    if teams is not None:
        adj_list_dict = _build_adj_list(teams)
        dist_dict = {k: 1 for k in teams.keys()}
        stack = []
        _dfs(adj_list_dict, stack, set())
        while len(stack) > 0:
            u = stack.pop()
            max_distance = max(max_distance, dist_dict[u])
            for adj in adj_list_dict[u]:
                dist_dict[adj] = max(dist_dict[adj], dist_dict[u] + 1)
    return max_distance  #, adj_list_dict


teams_heights = {0: [4.128, 5.574, 5.794, 5.459, 4.674, 5.500, 5.549, 5.791, 5.042, 5.615, 6.437, 4.856],
                 1: [6.058, 4.976, 5.498, 5.322, 6.298, 6.900, 5.930, 6.433, 5.197, 5.510, 7.112, 4.242],
                 2: [4.702, 5.677, 6.325, 5.196, 4.848, 5.399, 6.313, 6.461, 4.753, 5.044, 5.105, 5.115],
                 3: [4.928, 5.673, 4.644, 5.381, 6.111, 5.462, 5.778, 4.536, 4.731, 5.19,  5.712, 4.39],
                 4: [4.717, 5.82,  5.532, 6.055, 4.743, 4.922, 6.358, 5.594, 5.723, 5.786, 5.304, 5.572],
                 5: [5.723, 7.188, 5.568, 7.294, 6.29,  6.394, 7.39,  5.936, 7.322, 6.779, 6.299, 5.954],
                 6: [7.884, 7.321, 6.532, 7.057, 6.861, 7.952, 7.531, 7.002, 7.647, 7.164, 6.433, 7.797],
                 7: [5.053, 4.853, 6.003, 5.707, 4.731, 5.832, 5.608, 5.735, 5.533, 6.156, 4.922, 5.897],
                 8: [5.869, 4.824, 4.61,  5.201, 5.394, 6.03,  5.322, 6.155, 5.858, 4.849, 4.808, 4.775],
                 9: [6.144, 5.924, 5.594, 4.509, 5.039, 6.22,  4.852, 5.619, 5.45,  5.974, 5.39,  4.956]}
rand_teams_heights = {i: [round(random.uniform(4, 7), 3) for _ in range(5)] for i in range(10)}

print(f"most_teams_in_photo(teams_heights): {most_teams_in_photo(teams_heights)}")
print(f"most_teams_in_photo(rand_teams_heights): {most_teams_in_photo(rand_teams_heights)}")


