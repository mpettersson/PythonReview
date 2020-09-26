"""
    SORTED MERGE (CCI 10.1)

    You are given two sorted lists, a and b, where a has a large enough buffer at the end to hold b. Write a function to
    merge b into a in sorted order.

    Example:
        Input = [0, 1, 3, 11, None, None, None], [0, 10, 12]
        Output = None   # However, a is updated to be: [0, 0, 1, 3, 10, 11, 12]
"""


# Approach:  Runtime complexity is O(n + m) where n and m are the lengths of a and b.  Space complexity is O(1).
def sorted_merge(a, b):
    if a is not None and b is not None and len(b) > 0:
        insert_index = len(a) - 1
        last_a = insert_index - len(b)
        last_b = len(b) - 1
        while last_b >= 0:
            if last_a >= 0 and a[last_a] > b[last_b]:
                a[last_a], a[insert_index] = a[insert_index], a[last_a]
                last_a -= 1
            else:
                b[last_b], a[insert_index] = a[insert_index], b[last_b]
                last_b -= 1
            insert_index -= 1


lists = [([0, 1, 3, 11, None, None, None], [0, 10, 12]),
         ([0, 0, 0, 0, None, None, None], [0, 0, 0]),
         ([0, 1, 2, 4, 4, 5], []),
         ([0, 1, 2, 4, 4, 5], None),
         (None, None),
         ([None], [1])]

for a, b in lists:
    print(f"sorted_merge({a}, {b})")
    sorted_merge(a, b)
    print(f"a: {a}\n")


