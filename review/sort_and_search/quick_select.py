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
    elements such that all of the elements smaller than it comes before, and everything larger comes after.
    Recursively do this on the part with k (the only bit where Quick Select differs from Quick Sort).
"""


def quick_select(l, k):

    def _quick_select(l, k, lo, hi):
        pivot_idx = _partition(l, lo, hi)
        if pivot_idx - lo is k - 1:
            return l[pivot_idx]
        if pivot_idx - lo > k - 1:
            return _quick_select(l, k, lo, pivot_idx - 1)
        return _quick_select(l, k - pivot_idx + lo - 1, pivot_idx + 1, hi)

    def _partition(l, lo, hi):                  # Same as _lomuto_partition() in quick_sort.py
        pivot_val = l[hi]
        i = lo
        for j in range(lo, hi):
            if l[j] <= pivot_val:
                l[i], l[j] = l[j], l[i]
                i += 1
        l[i], l[hi] = l[hi], l[i]
        return i

    if l is not None and k is not None and 0 < k <= len(l):
        return _quick_select(l, k, 0, len(l) - 1)


l = [44, 77, 59, 39, 41, 69, 68, 10, 72, 33, 99, 72, 11, -1, 41, 37, 11, 72, 16, 22, 10, 33]
k_vals = [-9, -1, 1, 6, 9, 20, 22, None]

print(f"l: {l}\n")

for k in k_vals:
    print(f"quick_select(l, {k}): {quick_select(l[:], k)}")


