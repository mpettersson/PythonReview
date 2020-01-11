"""
    POWER SET

    Write a method to return all subsets of a set.
"""
import copy


def get_subsets(s):
    if len(s) is 1:
        return [{s.pop()}]

    h = s.pop()
    subset_tail_no_head = get_subsets(s)
    subset_tail_with_head = copy.deepcopy(subset_tail_no_head)

    for subset in subset_tail_with_head:
        subset.add(h)

    return [{h}] + [ss for ss in subset_tail_no_head] + [ss for ss in subset_tail_with_head]


s = {"A", "B", "C", "D"}
r = get_subsets(s)
print(r)



