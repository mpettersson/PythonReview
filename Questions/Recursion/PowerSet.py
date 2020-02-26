"""
    POWER SET

    Write a method to return all subsets of a set.
"""
import copy


def get_subsets(s):
    if not s or len(s) <= 1:
        return [s]

    h = s.pop()
    subset_tail_no_head = get_subsets(s)
    subset_tail_with_head = copy.deepcopy(subset_tail_no_head)

    for subset in subset_tail_with_head:
        subset.add(h)

    return [{h}] + subset_tail_no_head + subset_tail_with_head


s = {"A", "B", "C", "D"}
r = get_subsets(s)
print(r)



