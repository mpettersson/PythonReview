"""
    IS ROTATION

    Write a function, which when given two lists l1 and l2, will return True if l2 is a rotation of l1.  You can assume
    that there are no duplicate values.

    Example:
        Input = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [4, 5, 6, 7, 8, 9, 0, 1, 2, 3]
        Output = True

    Variations of this problem could include:
        - Duplicate values.
"""


def is_rotation(l1, l2):
    if l1 and l2 and len(l1) == len(l2):
        if len(l1) is 0:
            return True
        key = l1[0]
        idx = None
        for i in range(len(l1)):
            if key == l2[i]:
                idx = i
                break
        if not idx:
            return False
        for i in range(len(l1)):
            j = (idx + i) % len(l1)
            if l1[i] != l2[j]:
                return False
        return True
    return False


args = [([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [4, 5, 6, 7, 8, 9, 0, 1, 2, 3]),
        ([0, 1], [0]),
        ([0, 1], [0, 1])]

for (l1, l2) in args:
    print(f"is_rotation({l1}, {l2}):", is_rotation(l1, l2))





