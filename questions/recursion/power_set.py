"""
    POWER SET

    Write a method to return all subsets of a set.
"""
import copy
import functools


def get_subsets(s):
    if not s or len(s) <= 1:
        return [s]

    h = s.pop()
    subset_tail_no_head = get_subsets(s)
    subset_tail_with_head = copy.deepcopy(subset_tail_no_head)

    for subset in subset_tail_with_head:
        subset.add(h)

    return [{h}] + subset_tail_no_head + subset_tail_with_head

def powerset(lst):
    return functools.reduce(lambda result, x: result + [subset + [x] for subset in result], lst, [[]])


def all_subsets(s):
    subset = [None] * len(s)
    all_subsets_rec(list(s), subset, 0)


def all_subsets_rec(s, subset, i):
    if i == len(s):
        print(subset)
    else:
        subset[i] = None
        all_subsets_rec(s, subset, i + 1)
        subset[i] = s[i]
        all_subsets_rec(s, subset, i + 1)


s = {"A", "B", "C", "D"}
r = get_subsets({"A", "B", "C", "D"})
print(r)





