"""
    TRANSFORM ONE STRING TO ANOTHER (EPI 19.7)

    Let s and t be strings and dict_set a set of dictionary strings.  define s to produce t if there exists a sequence
    of strings from the dictionary p=[s0, s1, ..., sn-1] such that the first string is s, the last string is t, and
    adjacent strings have the same length and differ in exactly one character. The sequence p is called a production
    sequence.

    Given a dictionary set dict_set and two strings s and t, write a program to determine if s produces t.  Assume that
    all characters are lowercase alphabets.  If s does not produce t, output the length of a shortest production
    sequence; otherwise, output None.

    Example:
        Input = {'bat', 'cot', 'dog', 'dag', 'dot', 'cat'}, 'cat', 'dog'
        Output = 3  # i.e., the production sequence ['cat', 'cot', 'dot', 'dog']

    Hint: Treat strings as vertices in an undirected graph, with an edge between u and v IFF the corresponding strings
    differ in one character.
"""


# APPROACH: Naive Via Graph & BFS
#
# Build a graph from the words in the dictionary set, where each word is a vertex and edges exists only between vertices
# that are the same length and have a single char difference.
#
# Time Complexity: O(l * (n ** 2)), where n is the number of words and l is the length of the longest word.
# Space Complexity: O(n * (n ** 2)) at worst, or O(n ** 3), where n is the number of strings in the dictionary set;
#                   this is larger than O(n), or, the queue space used by BFS.
#
# NOTE: The time complexity to build the graph is O(l * (n ** 2)), where the time complexity to execute a DFS is
#       O(min(n, l) + (n**2)), where l is the length of the longest word, and n is the number of words in the dict set.
#       Therefore O(l * (n ** 2)) is the time complexity; since O(l * (n ** 2)) is greater than O(min(n, l) + (n**2)).
def num_steps_to_transform_string_naive(dict_set, s, t):

    def _is_one_away(s, t):
        diff_count = 0
        for i in range(len(s)):     # Assumes s and t have same len
            if s[i] != t[i]:
                diff_count += 1
        return True if diff_count < 2 else False

    def _build_graph(dict_list):
        adj_list = {k: set() for k in dict_list}
        dict_list.sort(key=lambda x: len(x))
        for i in range(len(dict_list) - 1):
            s = dict_list[i]
            length = len(s)
            for j in range(i+1, len(dict_list)):
                if len(dict_list[j]) != length:
                    break
                t = dict_list[j]
                if s not in adj_list[t] and _is_one_away(s, t):
                    adj_list[s].add(t)
                    adj_list[t].add(s)
        return adj_list

    def _bfs(adj_list, s, t):
        q = [(s, 0)]
        visited = set()
        while len(q) > 0:
            ver, dist = q.pop(0)
            if ver == t:
                return dist
            for adj in adj_list[ver]:
                if adj not in visited:
                    q.append((adj, dist + 1))
                    visited.add(adj)

    if dict_set is not None and s is not None and t is not None and s in dict_set and t in dict_set:
        dict_list = list(dict_set)
        adj_list = _build_graph(dict_list)
        return _bfs(adj_list, s, t)


# APPROACH: Optimal Via BFS (Only--No Graph)
#
# We don't actually have to build a graph; we can account for 'edges' by checking if any described transformation of the
# current 'vertex'/word is in the dictionary set.  Furthermore, by using the provided dictionary set to indicate search
# status (if visited), we don't need an additional "visited" list.
#
# Time complexity, in the worst case, is O(n + n ** 2), where the first n represent the vertices, and the n**2 is the
# max number of edges, and the size of n
# is the number of words in dictionary set.  If the max length of the words in the dictionary set is l, then the time
# complexity is O(n + n * l), or O(n * l), where n is the number of words and l is size of the longest string, in the
# dictionary set.
# Space Complexity: O(n), where n represents the number of vertices (or strings in the dictionary set).
def num_steps_to_transform_string(dict_set, s, t):
    if dict_set is not None and s is not None and t is not None and s in dict_set and t in dict_set:
        dict_set.remove(s)                                  # Use dict_set as the visited set.
        q = [(s, 0)]
        while q:
            s, d = q.pop(0)
            if s == t:
                return d
            for i in range(len(s)):                         # For each char in the current string:
                for j in range(ord('a'), ord('z') + 1):     # For each char in a..z: Transform the string.
                    u = s[:i] + chr(j) + s[i+1:]            # Note: Since string was already removed, don't need to
                    if u in dict_set:                       # skip the case where new char == old char.
                        dict_set.remove(u)                  # Remove the matched word from dict_set.
                        q.append((u, d + 1))                # Add matched word and new distance to the q.


dict_set = {'bat', 'cot', 'dog', 'dag', 'dot', 'cat', 'mat', 'hat', 'bag', 'hag', 'zip', 'zap'}
args = [('cat', 'dog'),
        ('cat', 'cat'),
        ('cot', 'dot'),
        ('zip', 'zap'),
        ('cat', 'zap'),
        ('cat', 'nob')]
fns = [num_steps_to_transform_string_naive,
       num_steps_to_transform_string]

print(f"\ndict_set: {dict_set}\n")
for s, t in args:
    for fn in fns:
        print(f"{fn.__name__}(dict_set, {s!r}, {t!r}): {fn(set(dict_set), s, t)}")
    print()


