"""
    SORTED MERGE

    You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B.
    Write a method to merge B into A in sorted order.
"""


# NOTE: It's super easy if you start from the end.
def sorted_merge(a, b):
    if a is None or b is None or b is []:
        return a

    end = len(a) - 1
    x = end - len(b)
    y = len(b) - 1

    while y >= 0:
        if a[x] > b[y]:
            a[end] = a[x]
            x -= 1
        else:
            a[end] = b[y]
            y -= 1
        end -= 1
    return a


a = [0, 1, 3, 11, None, None, None]
b = [0, 10, 12]

print(sorted_merge(a, b))




