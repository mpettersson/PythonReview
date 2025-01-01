"""
    CLOSEST SUM TO TARGET

    Given two lists of integers, m and n, and an integer target value t, write a function that returns a value u from m
    and a value v from m, with the closest sum (u+v) to the target value t.

    Example:
        Input = [-1, 3, 8, 2, 9, 5], [4, 1, 2, 10, 5, 20], 24
        Output = 23 (= 20 + 3; the solution of 25 = 20 + 5 would also be valid)
"""


# TODO: QUESTIONS TO ASK THE INTERVIEWER


# APPROACH: Brute Force
#
# TODO
#
# Time Complexity: O(n*m), where m and n are the lengths of the lists.
# Space Complexity: O(1).
def closest_sum_to_target_bf(l1, l2, target):
    pair = None
    diff = float('inf')
    for i in l1:
        for j in l2:
            curr_diff = abs(i + j - target)
            if curr_diff < diff:
                diff = curr_diff
                pair = (i, j)
    return pair


# APPROACH: Improved/TODO
#
# TODO
#
# Time Complexity: TODO
# Space Complexity: TODO
def closest_sum_to_target(l1, l2, target):
    l1_sorted = sorted(l1)
    l2_sorted = sorted(l2)
    i = 0
    j = len(l2_sorted) - 1
    smallest_diff = abs(l1_sorted[0] + l2_sorted[0] - target)
    closest_pair = (l1_sorted[0], l2_sorted[0])
    while i < len(l1_sorted) and j >= 0:
        v1 = l1_sorted[i]
        v2 = l2_sorted[j]
        current_diff = v1 + v2 - target
        if abs(current_diff) < smallest_diff:
            smallest_diff = abs(current_diff)
            closest_pair = (v1, v2)
        if current_diff == 0:
            return closest_pair
        elif current_diff < 0:
            i += 1
        else:
            j -= 1
    return closest_pair


args = [([-1, 3, 8, 2, 9, 5], [4, 1, 2, 10, 5, 20], 24),  # (5, 20) or (3, 20)
        ([7, 4, 1, 10], [4, 5, 8, 7], 13),                # (4,8), (7, 7), (7, 5), or (10, 4)
        ([6, 8, -1, -8, -3], [4, -6, 2, 9, -3], 3),       # (-1, 4) or (6, -3)
        ([19, 14, 6, 11, -16, 14, -16, -9, 16, 13], [13, 9, -15, -2, -18, 16, 17, 2, -11, -7], -15),  # (-16,2)or(-9,-7)
        ([-1, 3, 8, 2, 9, 5], [4, 1, 2, 10, 5, 20], 0)]
fns = [closest_sum_to_target_bf,
       closest_sum_to_target]

for (m, n, t) in args:
    print(f"m: {m}\nn: {n}\nt: {t}")
    for fn in fns:
        print(f"{fn.__name__}(m, n, t): {fn(m, n, t)}")
    print()


