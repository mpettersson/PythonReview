"""
    SORTED MERGE (CCI 10.1)

    You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B. Write a method to
    merge B into A in sorted order.

    Example:
        Input = [0, 1, 3, 11, None, None, None], [0, 10, 12]
        Output = [0, 0, 1, 3, 10, 11, 12]
"""


# Complexity:  Runtime is O(N + M) where N and M are the lengths of A and B, Space is O(1).
def sorted_merge(a, b):
    if not a or not b or b is []:
        return a

    idx_merged = len(a) - 1
    idx_a = idx_merged - len(b)
    idx_b = len(b) - 1

    while idx_b >= 0:
        if idx_a > 0 and a[idx_a] > b[idx_b]:
            a[idx_merged] = a[idx_a]
            idx_a -= 1
        else:
            a[idx_merged] = b[idx_b]
            idx_b -= 1
        idx_merged -= 1

    return a


lists = [([0, 1, 3, 11, None, None, None], [0, 10, 12]),
         ([0, 0, 0, 0, None, None, None], [0, 0, 0]),
         ([0, 1, 2, 4, 4, 5], []),
         ([0, 1, 2, 4, 4, 5], None),
         (None, None),
         ([None], [1])]

for a, b in lists:
    print(f"sorted_merge({a}, {b}):", sorted_merge(a, b))



