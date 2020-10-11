"""
    POWER SET (CCI 8.4)

    Write a method to return all subsets of a set.

    Definition:
        From Wikipedia; "in mathematics, the power set (or powerset) of any set S is the set of all subsets of S,
        including the empty set and S itself".  https://en.wikipedia.org/wiki/Power_set

    Example:
        Input = {"A", "B", "C"}
        Output = [set(), {'B'}, {'C'}, {'A'}, {'C', 'A'}, {'B', 'C'}, {'B', 'A'}, {'B', 'A', 'C'}]
"""
import copy
import functools
import itertools
import time


# Itertools Combinations Approach: Time and space is O(2**n), where n is the number of list items.
# NOTE: This is the FASTEST approach!!!
def power_set_itertools_combinations(iterable):     # NOTE: This takes an iterable, so works on STRINGS (i.e., "AB")
    results = []
    for r in range(len(iterable) + 1):
        for e in itertools.combinations(iterable, r):
            results.append(e)
    return results


# Reduce/Fold Left & Lambda Approach: Time and space is O(2**n), where n is the number of list items.
def power_set_functools_reduce(iterable):           # NOTE: This takes an iterable, so works on STRINGS (i.e., "AB")
    return functools.reduce(lambda t_result, h: t_result + [subset + [h] for subset in t_result], iterable, [[]])


# (One Liner) Alt. Itertools Combinations Approach: Time and space is O(2**n), where n is the number of list items.
# NOTE: This is a close second to the fastest approach.
def power_set_itertools_combinations_alt(iterable):   # NOTE: Takes an iterable, so works on STRINGS (i.e., "AB")
    return [set(combo) for r in range(len(iterable) + 1) for combo in itertools.combinations(iterable, r)]


# NOTE: The number of subsets is equal to the sum of all subsets, where a subset is a permutation (either including, or
# not including) each of the elements of the set.  Therefore, the size of the set is the number of permutations p, or
# p = n**r, where n is the number of possible items (2--either include or exclude) and r is the number of items in the
# set.

# Combinatorics/Iterative Approach (Adds Empty List):  Given that the number of all subsets is 2**n, where n is the size
# of the set, we can iterate through, and build, all possible subsets.  This is accomplished by mapping the binary
# representation of each integer (in the range of 0 to 2**n) to the elements in the set; creating a new subset with each
# element corresponding to a 1 in the binary string.
# Time and space complexity (remains the same as the other approaches, and) is O(2**n), where n is the number of list
# items (since we must build ALL 2**n items).
def power_set_combinatorics(s):
    if s is not None:
        res = []
        length = len(s)
        for i in range(2**length):
            res.append([x for b, x in zip([int(c) for c in f"{i:b}".zfill(length)], s) if b])
        return res


# Recursive Approach:  Time and space complexity is O(2**n), where n is the number of set items.
def power_set(s):
    if s is not None:
        if len(s) is 0:
            return [set()]
        h = s.pop()
        t = power_set(s)
        th = copy.deepcopy(t)
        for i in th:
            i.add(h)
        return t + th


# Wrong Recursive Approach:  This doesn't add the empty set, therefore, this DOESN'T produce a power set.  Time and
# space complexity is O(2**n), where n is the number of set items.
def power_set_wrong(s):
    if s is not None:
        if len(s) is 0:
            return []
        h = s.pop()
        t = power_set_wrong(s)
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

for iterable in iterables:
    print(f"power_set_itertools_combinations({iterable}):", power_set_itertools_combinations(iterable))
    print(f"power_set_functools_reduce({iterable}):", power_set_functools_reduce(iterable))
    print(f"power_set_itertools_combinations_alt({iterable}):", power_set_itertools_combinations_alt(iterable))
    print(f"power_set_combinatorics(set({iterable})):", power_set_combinatorics(set(iterable)))
    print(f"power_set(set({iterable})):", power_set(set(iterable)))
    print(f"power_set_wrong(set({iterable})):", power_set_wrong(set(iterable)))
    print()

fns = [power_set_itertools_combinations,
       power_set_functools_reduce,
       power_set_itertools_combinations_alt,
       power_set_combinatorics,power_set,
       power_set_wrong]
s = set(range(18))

print(f"s: {s}")
for fn in fns:
    t = time.time(); print(f"{fn.__name__}(s)", end="")
    fn(set(s))
    print(f" took {time.time() - t} seconds")


