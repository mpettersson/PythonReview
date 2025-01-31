"""
    QUICK SELECT

    Average Runtime:    O(n)
    Worst Runtime:      O(n**2)
    Best Runtime:       O(n)
    Space Complexity:   O(log(n))
    Alg Paradigm:       Divide and Conquer
    Sorting In Place:   Yes
    Stable:             No      (the default alg changes the relative order of elements with equal keys)
    Online:             No      (can search a list as it receives it)

    Select the kth smallest element in an unordered list; pick a random element (convention uses last), then swap the
    elements such that all the elements smaller than it comes before, and everything larger comes after.
    Recursively do this on the part with k (the only bit where Quick Select differs from Quick Sort).
"""


# APPROACH: Quick Select With Lomuto Partition
def quick_select(l, k):

    def _rec(l, k, left, right):
        p = _partition(l, left, right)
        if p - left is k - 1:
            return l[p]
        if p - left > k - 1:
            return _rec(l, k, left, p - 1)
        return _rec(l, k + left - p - 1, p + 1, right)

    def _partition(l, left, right):                  # Same as _lomuto_partition() in quick_sort.py
        pivot_val = l[right]
        p = left
        for i in range(left, right):
            if l[i] < pivot_val:
                l[p], l[i] = l[i], l[p]
                p += 1
        l[p], l[right] = l[right], l[p]
        return p

    if l is not None and isinstance(l, list) and k is not None and 0 < k <= len(l):
        return _rec(l, k, 0, len(l) - 1)


# For comparison's sake.
def sort_and_select(l, k):
    if l is not None and isinstance(l, list) and k is not None and 0 < k <= len(l):
        return sorted(l)[k-1]


l = [44, 77, 59, 39, 41, 3, 2, 69, 68, 10, 72, 33, 99, 72, 11, -1, 41, 37, 11, 3, 2, 72, 16, 1, 22, 10, 33]
k_vals = [-9, -1, 1, 2, 3, 4, 5, 6, 9, 20, 22, None] + list(range(1, len(l)+1))
fns = [quick_select,
       sort_and_select]

print(f"l: {l}")
print(f"sorted(l): {sorted(l)}\n")
for k in k_vals:
    print(f"l: {l}")
    for fn in fns:
        print(f"{fn.__name__}(l, {k}): {fn(l[:], k)}")
    print()


