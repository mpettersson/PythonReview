"""
    QUICK SORT

    Average Runtime:    O(n log(n))
    Worst Runtime:      O(n**2)
    Best Runtime:       O(n log(n))
    Space Complexity:   O(log(n))
    Alg Paradigm:       Divide and Conquer
    Sorting In Place:   Yes
    Stable:             No      (the default alg changes the relative order of elements with equal keys)
    Online:             No      (can sort a list as it receives it)

    Pick a random element (convention uses last), then swap the elements such that all the elements smaller than it
    comes before, and everything larger comes after. Recursively do this on the "smaller" and "larger" elements.
"""


# APPROACH: Hoare Partition
#
# NOTE: This partition's approach has fewer swaps than Lomuto's, however, this approach requires data structures with
#       bi-directionality (i.e., singly linked lists wouldn't work).
#
# SEE: https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme
def quick_sort_hoare(l):

    def _rec(l, left, right):
        if left < right:
            p = _hoare_partition(l, left, right)
            _rec(l, left, p)
            _rec(l, p + 1, right)

    def _hoare_partition(l, left, right):
        pivot_val = l[(left + right) // 2]
        while True:
            while l[left] < pivot_val:
                left += 1
            while pivot_val < l[right]:
                right -= 1
            if left >= right:
                return right
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1

    if l is not None and isinstance(l, list):
        _rec(l, 0, len(l) - 1)
        return l


# APPROACH: Lomuto Partition
#
# NOTE: This partition's approach will involve more swaps than Hoare's, however, this can be used with singly linked
#       list or any other forward-only data structures.
#
# SEE: https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme
def quick_sort_lomuto(l):

    def _rec(l, left, right):
        if left < right:
            p = _lomuto_partition(l, left, right)
            _rec(l, left, p - 1)
            _rec(l, p + 1, right)

    def _lomuto_partition(l, left, right):
        pivot_val = l[right]
        p = left
        for i in range(left, right):
            if l[i] < pivot_val:
                l[p], l[i] = l[i], l[p]
                p += 1
        l[p], l[right] = l[right], l[p]
        return p

    if l is not None and isinstance(l, list):
        _rec(l, 0, len(l) - 1)
        return l


lists = [[4, 65, 2, -31, 0, 99, 83, 782, 1],
         [44, 77, 59, 39, 41, 69, 72, 72, 41, 37, 11, 72, 16, 22, 33],
         [170, 45, 2, 75, 90, 802, 24, 2, 66, 0, -1],
         [170, 45, -1, -1, 2, 75, 90, 802, 24, 2, 66, 0, -1, 0, 0, 170, 45, 2, 75, 90, 802, 0, 0, 24, 2, 66, 0, -1],
         [44, 77, 59, 39, 41, 69, 68, 10, 72, 99, 72, 11, 41, 37, 11, 72, 16, 22, 10, 100],
         [44, 77, 59, 39, 41, 69, 68, 10, 72, 99, 72, 11, 41, 37, 11, 72, 16, 22, 10, 33],
         [],
         [10, -28, -75, -95, -29, -28, 27, 92, -59, 80, 45, 49, -62, 21, -79, 75, 99, 52, -28, 41],
         [44, 77, 59, 39, 41, 69, 72, 72, 41, 37, 11, 72, 16, 22, 33],
         [-1],
         [0],
         [1],
         [0, 0],
         [1, 0, -1]]
fns = [sorted,
       quick_sort_hoare,
       quick_sort_lomuto]

for l in lists:
    print(f"l: {l}")
    for fn in fns:
        print(f"{fn.__name__}(l): {fn(l[:])}")
    print()


