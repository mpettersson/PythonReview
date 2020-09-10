"""
    POWER SET (CCI 8.4)

    Write a method to return all subsets of a set.

    Example:
        Input = {"A", "B", "C"}
        Output = [{'B'}, {'C'}, {'A'}, {'C', 'A'}, {'B', 'C'}, {'B', 'A'}, {'B', 'A', 'C'}]
"""
import copy
import functools
import time


# Recursive Approach (Doesn't Add Empty Set):  Time and space complexity is O(2**n), where n is the number of set items.
def power_set_wo_empty_set(s):
    if s is not None:
        if len(s) is 0:
            return []
        h = s.pop()
        t = power_set_wo_empty_set(s)
        th = copy.deepcopy(t)
        for i in th:
            i.add(h)
        return [{h}] + t + th   # NOTE: Don't use set(h) here, because if h is an int, it will fail.


# Recursive Approach (Adds Empty Set):  Time and space complexity is O(2**n), where n is the number of set items.
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


# Reduce/Fold Left & Lambda Approach (Adds Empty Set): Time and space is O(2**n), where n is the number of list items.
# NOTE: This is, by far, the fastest solution!!!
def power_set_lambda(lst):
    return functools.reduce(lambda t_result, h: t_result + [subset + [h] for subset in t_result], lst, [[]])


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


sets = [{'A', 'B', 'C'}, {0, 1, 2, 4}, set()]

for s in sets:
    print(f"power_set_wo_empty_set({s}):", power_set_wo_empty_set(s.copy()))
print()

for s in sets:
    print(f"power_set({s}):", power_set(s.copy()))
print()

for s in sets:
    print(f"power_set_lambda({s}):", power_set_lambda(s.copy()))
print()

for s in sets:
    print(f"power_set_combinatorics({s}):", power_set_combinatorics(s.copy()))
print()

s = set(range(18))
t = time.time(); print(f"power_set_wo_empty_set({s})", end=""); power_set_wo_empty_set(s.copy()); print(f" took {time.time() - t} seconds")
t = time.time(); print(f"power_set({s})", end=""); power_set(s.copy()); print(f" took {time.time() - t} seconds")
t = time.time(); print(f"power_set_lambda({s})", end=""); power_set_lambda(s.copy()); print(f" took {time.time() - t} seconds")
t = time.time(); print(f"power_set_combinatorics({s})", end=""); power_set_combinatorics(s.copy()); print(f" took {time.time() - t} seconds")


