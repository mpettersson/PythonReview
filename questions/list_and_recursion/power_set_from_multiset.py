"""
    POWER SET FROM MULTISET (leetcode.com/problems/subsets-ii)

    Write a function, which accepts a multiset as an iterable, then returns all unique sub-multisets (as tuples or
    lists) of the provided iterable.

    REMEMBER: This problem accepts an iterable that may have DUPLICATE ELEMENTS.

    Definition:
        From Wikipedia; "in mathematics, the power set (or powerset) of any set S is the set of all subsets of S,
        including the empty set and S itself".  SEE: wikipedia.org/wiki/Power_set

        Also, from Wikipedia; "in mathematics, a multiset (or bag, or mset) is a modification of the concept of a set
        that, unlike a set, allows for multiple instances for each of its elements."  SEE: wikipedia.org/wiki/Multiset

    Example:
        Input = {'B', 'A', 'B'}
        Output = {('A',), ('B', 'B'), ('B',), ('A', 'B'), (), ('A', 'B', 'B')}

    Variations:
        - SEE power_set.py for a true power set, or all unique subsets from a unique set.
"""
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
# NOTE: Lexicographical order (sorting) is key to this question...


# APPROACH: Itertools Combinations
#
# This approach uses the itertools combinations function, iterating over the range of lengths (of the iterable) to
# create all unique subsets (or the power set).
#
# Time Complexity: O(2**n), where n is the number of list items.
# Space Complexity: O(2**n), where n is the number of list items.
def power_set_from_multiset_itertools_combinations(iterable):
    if iterable is not None and hasattr(iterable, '__iter__'):
        result = set()
        l = sorted(iterable)
        for r in range(len(l) + 1):
            for e in itertools.combinations(l, r):
                result.add(tuple(e))
        return result


# APPROACH: (Minimized) Itertools Combinations
#
# This is simply a refactored and minimized version of the itertools combinations approach above.
#
# Time Complexity: O(2**n), where n is the number of list items.
# Space Complexity: O(2**n), where n is the number of list items.
#
# NOTE: This is a close second to the fastest approach.
def power_set_from_multiset_itertools_combinations_min(iterable):
    if iterable is not None and hasattr(iterable, '__iter__'):
        return {tuple(comb) for r in range(len(iterable)+1) for comb in itertools.combinations(sorted(iterable), r)}


# APPROACH: DFS/Recursive
#
# This is simply a recursive DFS traversal of the elements of the iterable (which are converted to a list for
# processing), where the value for each 'node' (in the tree) is added to the results list.
#
# Time Complexity: O(2**n), where n is the number of list items.
# Space Complexity: O(2**n), where n is the number of list items.
def power_set_from_multiset_rec_list(iterable):

    def _rec(i, path):
        result.append(path)
        for j in range(i, len(l)):
            if j > i and l[j] == l[j-1]:
                continue
            _rec(j+1, path+[l[j]])

    if iterable is not None and hasattr(iterable, '__iter__'):
        result = []
        l = sorted(iterable)
        _rec(0, [])
        return result


# APPROACH: Recursive
#
# This is the classic recursive approach; pop off the head from the list, recurse on the tail, duplicate the results
# from the recursion on the tail, and on the duplicate, add the head to each of the returned lists.  Then, return the
# modified tail results (with the head) and the original tail results (unmodified) as the results.
#
# Time Complexity: O(2**n), where n is the number of list items.
# Space Complexity: O(2**n), where n is the number of list items.
def power_set_from_multiset_rec_set(iterable):

    def _rec(s):
        if s is not None:
            if len(s) == 0:
                return {tuple()}
            if len(s) == 1:
                return {tuple(s), tuple()}
            h = s.pop()
            t = _rec(s)
            return t | {(*tup, h) for tup in t}

    if iterable is not None and hasattr(iterable, '__iter__'):
        return _rec(sorted(iterable))


# APPROACH: Reduce/Fold Left & Lambda
#
# This approach uses the functools reduce method (or a left fold) to apply an anonymous function (lambda) to generate
# all uniques subsets (or, the power set) of the provided iterable.
#
# Time Complexity: O(2**n), where n is the number of list items.
# Space Complexity: O(2**n), where n is the number of list items.
def power_set_from_multiset_functools_reduce(iterable):
    if iterable is not None and hasattr(iterable, '__iter__'):
        return functools.reduce(lambda tail, head: tail | {(*tup, head) for tup in tail}, sorted(iterable), {tuple()})


# APPROACH: Combinatorics/Iterative/Bit Masking:
#
# Given that the number of all subsets is 2**n, where n is the size of the set, we can iterate through, and build, all
# possible subsets.  This is accomplished by mapping the binary representation of each integer (in the range of 0 to
# 2**n) to the elements in the set; creating a new subset with each element corresponding to a 1 in the binary string.
#
# Time Complexity: O(2**n), where n is the number of list items.
# Space Complexity: O(2**n), where n is the number of list items.
def power_set_from_multiset_combinatorics(iterable):
    if iterable is not None and hasattr(iterable, '__iter__'):
        result = set()
        l = sorted(iterable)
        for i in range(2**len(iterable)):
            result.add(tuple([x for b, x in zip([int(c) for c in f"{i:b}".zfill(len(iterable))], l) if b]))
        return result


# APPROACH: Via Dictionary
#
# This is simply a recursive DFS traversal of the elements of the iterable (which are converted to a list for
# processing), where the value for each 'node' (in the tree) is added to the results list.
#
# Time Complexity: O(2**n), where n is the number of list items.
# Space Complexity: O(2**n), where n is the number of list items.
def power_set_from_multiset_via_dict(iterable):

    def _rec(i, accumulator):
        result.append(accumulator)
        for k in d.keys():
            if d[k] > 0:
                d[k] -= 1
                if len(accumulator) == 0 or accumulator[-1] <= k:
                    _rec(i-1, accumulator + [k])
                d[k] += 1

    if iterable is not None and hasattr(iterable, '__iter__'):
        result = []
        d = dict()
        for k in iterable:
            d[k] = d.setdefault(k, 0)+1
        _rec(len(iterable), [])
        return result


iterables = [{'A', 'B', 'C'},
             ['B', 'A', 'B'],
             ['B', 'A', 'B', 'A'],
             ['A', 'A', 'A', 'A'],
             [2, 1, 2, 0],
             "aba",
             [],
             None]
fns = [power_set_from_multiset_itertools_combinations,
       power_set_from_multiset_itertools_combinations_min,
       power_set_from_multiset_rec_list,
       power_set_from_multiset_rec_set,
       power_set_from_multiset_functools_reduce,
       power_set_from_multiset_combinatorics,
       power_set_from_multiset_via_dict]

for iterable in iterables:
    print(f"iterable: {iterable}")
    for fn in fns:
        print(f"{fn.__name__}(iterable): {len(fn(iterable)) if iterable is not None else 0}:{fn(iterable)}")
    print()

s = set(range(19))
print(f"s: {s}")
for fn in fns:
    t = time.time(); print(f"{fn.__name__}(s)", end="")
    fn(set(s))
    print(f" took {time.time() - t} seconds")

