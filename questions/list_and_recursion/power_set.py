"""
    POWER SET (CCI 8.4: POWER SET,
               leetcode.com/problems/subsets)

    Write a function, which accepts a set as an iterable, then returns all unique subsets (as sets or lists) of the
    iterable.

    REMEMBER: This problem accepts an iterable with UNIQUE ELEMENTS (or, non-duplicates) only.

    Definition:
        From Wikipedia; "in mathematics, the power set (or powerset) of any set S is the set of all subsets of S,
        including the empty set and S itself".  https://en.wikipedia.org/wiki/Power_set

    Example:
        Input = {"A", "B", "C"}
        Output = [set(), {'B'}, {'C'}, {'A'}, {'C', 'A'}, {'B', 'C'}, {'B', 'A'}, {'B', 'A', 'C'}]

    Variations:
        - SEE power_set_from_multiset.py for a power set, or all unique subsets from a non-unique set (multiset).
"""
import copy
import functools
import itertools
import time


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Verify definition of power set (unique combinations, not permutations, empty set, etc.).
#   - What is the possible length of the iterable?
#   - What are the possible iterable values?
#   - Are there duplicate values in the iterable?
#   - Are unique subsets only?
#   - What order should the results list be in?
#   - Can the original iterable be modified?


# NOTE: The number of subsets is equal to the sum of all subsets, where a subset is a combination (either including, or
#       not including) each of the elements of the set.  Therefore, the size of the set is the number of combinations p,
#       or p = n**r, where n is the number of possible items (2--either include or exclude) and r is the number of items
#       in the set.


# NOTE: The following are listed in order of fastest to slowest (for an input with length 18):


# APPROACH: Reduce/Fold Left & Lambda
#
# This approach uses the functools reduce method (or a left fold) to apply an anonymous function (lambda) to generate
# all uniques subsets (or, the power set) of the provided iterable.
#
# Time Complexity: O(2**n), where n is the number of list items.
# Space Complexity: O(2**n), where n is the number of list items.
def power_set_functools_reduce(iterable):           # NOTE: This takes an iterable, so works on STRINGS (i.e., "AB")
    return functools.reduce(lambda t_result, h: t_result + [subset + [h] for subset in t_result], iterable, [[]])


# APPROACH: Itertools Combinations
#
# This approach uses the itertools combinations function, iterating over the range of lengths (of the iterable) to
# create all unique subsets (or the power set).
#
# Time Complexity: O(2**n), where n is the number of list items.
# Space Complexity: O(2**n), where n is the number of list items.
def power_set_itertools_combinations(iterable):     # NOTE: This takes an iterable, so works on STRINGS (i.e., "AB")
    results = []
    for r in range(len(iterable) + 1):
        for e in itertools.combinations(iterable, r):
            results.append(list(e))
    return results


# APPROACH: DFS/Recursive
#
# This is simply a recursive DFS traversal of the elements of the iterable (which are converted to a list for
# processing), where the value for each 'node' (in the tree) is added to the results list.
#
# Time Complexity: O(2**n), where n is the number of list items.
# Space Complexity: O(2**n), where n is the number of list items.
def power_set_dfs(iterable):

    def _dfs(i, path):
        result.append(path)
        for j in range(i, len(l)):
            _dfs(j+1, path+[l[j]])

    result = []
    l = list(iterable)
    _dfs(0, [])
    return result


# APPROACH: (Minimized) Itertools Combinations
#
# This is simply a refactored and minimized version of the itertools combinations approach above.
#
# Time Complexity: O(2**n), where n is the number of list items.
# Space Complexity: O(2**n), where n is the number of list items.
#
# NOTE: This is a close second to the fastest approach.
def power_set_itertools_combinations_min(iterable):   # NOTE: Takes an iterable, so works on STRINGS (i.e., "AB")
    return [set(combo) for r in range(len(iterable) + 1) for combo in itertools.combinations(iterable, r)]


# APPROACH: Combinatorics/Iterative/Bit Masking:
#
# Given that the number of all subsets is 2**n, where n is the size of the set, we can iterate through, and build, all
# possible subsets.  This is accomplished by mapping the binary representation of each integer (in the range of 0 to
# 2**n) to the elements in the set; creating a new subset with each element corresponding to a 1 in the binary string.
#
# Time Complexity: O(2**n), where n is the number of list items.
# Space Complexity: O(2**n), where n is the number of list items.
def power_set_combinatorics(s):
    if s is not None:
        res = []
        length = len(s)
        for i in range(2**length):
            res.append([x for b, x in zip([int(c) for c in f"{i:b}".zfill(length)], s) if b])
        return res


# APPROACH: Recursive
#
# This is the classic recursive approach; pop off the head from the list, recurse on the tail, duplicate the results
# from the recursion on the tail, and on the duplicate, add the head to each of the returned lists.  Then, return the
# modified tail results (with the head) and the original tail results (unmodified) as the results.
#
# Time Complexity: O(2**n), where n is the number of list items.
# Space Complexity: O(2**n), where n is the number of list items.
def power_set(iterable):

    def _rec(s):
        if s is not None:
            if len(s) == 0:
                return [set()]
            h = s.pop()
            t = power_set(s)
            th = copy.deepcopy(t)
            for i in th:
                i.add(h)
            return t + th

    return _rec(set(iterable))


# WRONG APPROACH: Recursive
#
# NOTE: This DOESN'T add the empty set, therefore, this DOESN'T produce a power set.
#
# Time Complexity: O(2**n), where n is the number of list items.
# Space Complexity: O(2**n), where n is the number of list items.
def __wrong_power_set__(s):
    if s is not None:
        if len(s) == 0:
            return []
        h = s.pop()
        t = __wrong_power_set__(s)
        th = copy.deepcopy(t)
        for i in th:
            i.add(h)
        return [{h}] + t + th   # NOTE: Don't use set(h) here, because if h is an int, it will fail.


iterables = [{'A', 'B', 'C'},
             [0, 1, 2, 4],
             "abc",
             range(5),
             set(),
             []]
fns = [power_set_functools_reduce,
       power_set_itertools_combinations,
       power_set_dfs,
       power_set_itertools_combinations_min,
       power_set_combinatorics,
       power_set]

for iterable in iterables:
    print(f"iterable: {iterable}")
    for fn in fns:
        print(f"{fn.__name__}(iterable): {fn(iterable)}")
    print()

s = set(range(18))
print(f"s: {s}")
for fn in fns:
    t = time.time(); print(f"{fn.__name__}(s)", end="")
    fn(set(s))
    print(f" took {time.time() - t} seconds")


