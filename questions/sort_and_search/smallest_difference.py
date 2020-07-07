"""
    SMALLEST DIFFERENCE

    Given two arrays of integers, compute the pair of values (one value in each array) with the smallest (non-negative)
    difference.  Return the difference.

    Example: [1,3,15,11,2] and [23,127,235,19,8] would return 3 (the difference in the pair (11,8)).
"""


def smallest_difference(l1, l2):
    if l1 is None or l2 is None or len(l1) == 0 or len(l2) == 0:
        return None
    l1 = sorted(l1)
    l2 = sorted(l2)
    p1 = p2 = 0

    while True:
        diff = abs(l1[p1] - l2[p2])
        if l1[p1] < l2[p2]:
            if p1 + 1 < len(l1) and diff > abs(l1[p1 + 1] - l2[p2]):
                p1 += 1
                continue
            else:
                return diff, l1[p1], l2[p2]
        else:
            if p2 + 1 < len(l2) and diff > abs(l1[p1] - l2[p2 + 1]):
                p2 += 1
                continue
            else:
                return diff, l1[p1], l2[p2]


l1 = [1, 3, 15, 11, 2]
l2 = [23, 127, 235, 19, 8]
print(smallest_difference(l1, l2))
l3 = [1, 2, 4, 9]
l4 = [17, 3]
print(smallest_difference(l3, l4))

