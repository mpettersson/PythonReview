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

    Pick a random element (convention uses last), then swap the elements such that all of the elements smaller than
    it comes before, and everything larger comes after. Recursively do this on the "smaller" and "larger" elements.
"""


# Hoare Partition Approach (rewritten to use while, not do while)
# SEE https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme
def quick_sort_hoare(l):

    def _quick_sort_hoare(l, left, right):
        if left < right:
            p = _hoare_partition(l, left, right)
            _quick_sort_hoare(l, left, p)
            _quick_sort_hoare(l, p + 1, right)

    def _hoare_partition(l, left, right):
        pivot_val = l[(left + right) // 2]
        while True:
            while l[left] < pivot_val:
                left += 1
            while l[right] > pivot_val:
                right -= 1
            if left >= right:
                return right
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1

    if l is not None and len(l) > 1:
        _quick_sort_hoare(l, 0, len(l) - 1)


# Lomuto Partition Approach
# SEE https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme
def quick_sort_lomuto(l):

    def _quick_sort(l, left, right):
        if left < right:
            p = _lomuto_partition(l, left, right)
            _quick_sort(l, left, p - 1)
            _quick_sort(l, p + 1, right)

    def _lomuto_partition(l, left, right):
        pivot_val = l[right]
        i = left
        for j in range(left, right):
            if l[j] < pivot_val:
                l[i], l[j] = l[j], l[i]
                i += 1
        l[i], l[right] = l[right], l[i]
        return i

    if l is not None and len(l) > 1:
        _quick_sort(l, 0, len(l) - 1)


l = [44, 77, 59, 39, 41, 69, 72, 72, 41, 37, 11, 72, 16, 22, 33]

(lambda y: (print(f"quick_sort_hoare({y}):  ", end=""), quick_sort_hoare(y), print(y, "\n")))((lambda x: x[:])(l))

(lambda y: (print(f"quick_sort_lomuto({y}): ", end=""), quick_sort_lomuto(y), print(y, "\n")))((lambda x: x[:])(l))


