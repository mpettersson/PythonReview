"""
    TODO
        - Time and Space Complexities

    LONGEST CHAIN (LC: Longest String Chain)

    Given a list of dictionary words, write a function to find the longest 'chain' of words from the list, with the
    property that for each pair of words in the chain, the larger has all of the smaller words characters in the same
    order (but can have other characters too).

    Consider the following list with two chains ('bc' ⟶ 'abc' and 'x' ⟶ 'xz' ⟶' 'xyz'):
        ['abc', 'bc', 'foobar', 'xyz', 'x', 'xz']

    Example:
        Input = ['abc', 'bc', 'foobar', 'xyz', 'x', 'xz']
        Output = 3

    Variations:
        - Same question, however, the chain property now has the following restriction; only a single letter can be
          added (anywhere) to make a new word (in the list).
"""
import time


# APPROACH: Naive/Brute Force
#
# TODO
#
# Time Complexity: TODO
# Space Complexity:TODO
def size_longest_chain_bf(l):

    def helper(l, word):
        if word == '':
            return 0
        result = 0
        for i in range(len(word)):
            temp = word[:i] + word[i+1:]
            result = max(helper(l, temp), result)
        return result + (1 if word in l else 0)

    if l is not None:
        result = 0
        for word in l:
            result = max(helper(l, word), result)
        return result


# APPROACH: Memoization/Dynamic Programming
#
# TODO
#
# Time Complexity: O(n * w!), where n is the number of elements in the list and w is the length of the longest word.
# Space Complexity: TODO
def size_longest_chain_memo(l):

    def helper(l, word, cache):
        if word not in cache:
            result = 0
            for i in range(len(word)):                          # O(w)
                temp = word[:i] + word[i+1:]
                result = max(helper(l, temp, cache), result)
            cache[word] = result + (1 if word in l else 0)
        return cache[word]

    if l is not None:
        result = 0
        cache = {'': 0}
        for word in l:                                          # O(n)
            result = max(helper(l, word, cache), result)
        return result


# APPROACH: DFS/Graph
#
# TODO
#
# Time Complexity: TODO
# Space Complexity: TODO
def size_longest_chain_graph(l):

    # Time Complexity: O(w), where w is the longer of the two words.
    def is_connected(orig, dest):
        o_len = len(orig)
        d_len = len(dest)
        if o_len <= d_len:
            o = d = 0
            while d < d_len and o < o_len:
                while d < d_len and orig[o] != dest[d]:
                    d += 1
                if o is o_len - 1 and d < d_len and orig[o] == dest[d]:
                    return True
                o += 1
                d += 1
        return False

    # Time Complexity: O(n**2), where n is the number of words in the list.
    def build_adj_list(l):
        g = {k: [] for k in l}
        for i in range(len(l)):
            for j in range(len(l)):
                if i != j and is_connected(l[i], l[j]):
                    g[l[i]].append(l[j])
        return g

    # Time Complexity: O(v + e), where v and e are the number of vertices and edges in the graph.
    def get_longest_dfs(graph, orig):
        if graph and orig and orig in graph:
            result = []
            for adj in graph[orig]:
                temp_result = get_longest_dfs(graph, adj)
                if len(temp_result) > len(result):
                    result = temp_result
            return [orig] + result

    if l:
        g = build_adj_list(l)
        result = []
        for orig in g.keys():
            if g[orig]:
                temp_result = get_longest_dfs(g, orig)
                if len(temp_result) > len(result):
                    result = temp_result
        return result if result else [orig]
    return []


# VARIATION:  Same question, however, the chain property now has the following restriction; only a single letter can be
#             added (anywhere) to make a new word (in the list).
#
#
# Observations:
# This is the question at: leetcode.com/problems/longest-string-chain
# This actually makes searching easier than the original question; now we can quit earlier.


# APPROACH: Single Letter Changed Recursive
#
# TODO
#
# Time Complexity: TODO
# Space Complexity: TODO
def one_char_diff_longest_string_chain(words):
    words = sorted(words, key=len)
    dp = {word: 1 for word in words}
    longest = 0
    for word in words:
        for i in range(len(word)):
            predecessor = word[:i] + word[i+1:]
            if predecessor in dp:
                dp[word] = dp[predecessor] + 1
                longest = max(longest, dp[word])
    return longest


lists = [['abc', 'bc', 'dasdasda', 'xy', 'xyz', 'x'],
         ['xz', 'xyz', 'abc'],                                      # Longest Chain: xz ⟶ xyz
         ['a', 'b', 'ba', 'bca', 'bda', 'bdca'],
         ['a', 'b', 'ba', 'bcca', 'bdca', 'bdccca'],
         ['a', 'bc', 'def', 'ghij', 'klmno', 'pqrstu', 'vwxyz'],
         []]
long_list = ["Lorem",  "they", "race", "fights", "care", "listens", "silent", "acre", "funeral", "admirer", "married",
             "angered", "dog", "enraged", "death", "fun", "hated", "elvis", "lives", "creative", "leaf", "flea",
             "reactive", "god", "ipsum", "logarithmic", "levis", "algorithmic", "money", "a", "be", "better", "batter",
             "bee", "bet", "beautiful", "bit", "bits", "bitten", "bat", "batten", "battle", "battology", "brochetter"]
fns = [size_longest_chain_bf,
       size_longest_chain_memo,
       size_longest_chain_graph,
       one_char_diff_longest_string_chain]

for l in lists:
    print(f"l: {l!r}")
    for fn in fns:
        print(f"{fn.__name__}(l): {fn(l)}")
    print()

print(f"long_list: {long_list}")
for fn in fns:
    t = time.time()
    print(f"{fn.__name__}(long_list): ", end="")
    result = fn(long_list)
    print(f"{result}, and took {time.time() - t} seconds.")


