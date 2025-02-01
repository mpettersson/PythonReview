"""
    MERGE SORT

    Average Runtime:    O(n log(n))
    Worst Runtime:      O(n log(n))
    Best Runtime:       O(n log(n))
    Space Complexity:   O(n)
    Alg Paradigm:       Divide and Conquer
    Sorting In Place:   No      (in a typical implementation)
    Stable:             Yes     (does not change the relative order of elements with equal keys)
    Online:             No      (can sort a list as it receives it)

    Algorithm:
        Given an unsorted list l:
        1.  Divide the unsorted list l into n sub-lists, each containing one element via:
        2.  Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining.

    Find the middle index.
    Call Merge Sort on everything up to (and including) the middle.
    Call Merge Sort on everything after the middle.
    Merge the sorted halves.
"""


def merge_sort(l):
    if len(l) > 1:
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):     # Merge from (temporary) left/right lists into l.
            if left[i] < right[j]:
                l[k] = left[i]
                i += 1
            else:
                l[k] = right[j]
                j += 1
            k += 1

        while i < len(left):                        # Merge any remaining elements from left/right into l.
            l[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            l[k] = right[j]
            j += 1
            k += 1
    return l


def merge_sort_bottom_up(l):
    def merge(l, temp, left, mid, right):
        i, j, k = left, mid, left
        while i < mid and j < right:
            if l[i] <= l[j]:
                temp[k] = l[i]
                i += 1
            else:
                temp[k] = l[j]
                j += 1
            k += 1
        while i < mid:
            temp[k] = l[i]
            i += 1
            k += 1
        while j < right:
            temp[k] = l[j]
            j += 1
            k += 1

    n = len(l)
    temp = [None] * n
    width = 1
    while width < n:
        for i in range(0, n, 2 * width):
            left = i
            mid = min(i + width, n)
            right = min(i + 2 * width, n)
            merge(l, temp, left, mid, right)
        for i in range(n):
            l[i] = temp[i]
        width *= 2
    return l


# APPROACH: 
def bottom_up_merge_sort(a, b, n):
    # //  Left run is A[iLeft :iRight-1].
    # // Right run is A[iRight:iEnd-1  ].
    def bottom_up_merge(a, left, i_right, i_end, b):
        i = left
        j = i_right
        for k in range(left, i_end):
            if i < i_right and (j >= i_end or a[i] <= a[j]):
                b[k] = a[i]
                i += 1
            else:
                b[k] = a[j]
                j += 1

    def copy_array(b, a, n):
        for j in range(n):
            a[i] = b[i]

    width = 1
    while width < n:        # Make successively longer sorted runs of length 2, 4, 8, 16... until the whole array is sorted.
        i = 0
        while i < n:
            #             // Merge two runs: A[i:i+width-1] and A[i+width:i+2*width-1] to B[]
            #             // or copy A[i:n-1] to B[] ( if (i+width >= n) )
            bottom_up_merge(a, i, min(i+width, n), min(i + 2 * width, n), b)
            i = i + 2 * width
            copy_array(b, a, n)
        width *= 2


def top_down_merge_sort(a):            # a has items to sort, b is a work list, n is the number of items.

    def _merge(b, left, mid, right, a):
        i = left
        j = mid
        for k in range(left, right):
            if i < mid and (j >= right or a[i] <= a[j]):
                b[k] = a[i]
                i += 1
            else:
                b[k] = a[j]
                j += 1

    def _rec(b, left, right, a):            # left is INCLUSIVE; right is EXCLUSIVE
        if (right - left) <= 1:                 # if size is 1
            return                                  # then it's sorted
        mid = (right + left) // 2
        _rec(a, left, mid, b)                   # recursively sort left
        _rec(a, mid, right, b)                  # recursively sort right
        _merge(b, left, mid, right, a)          # merge results into a

    n = len(a)
    b = a[:]                                 # Work/temporary/auxiliary list.
    _rec(a, 0, n, b)                     # sort data from b into a
    return a


string_list = list("ZzxX209,&*4ASDFasdfqwerQWER12")
print(string_list)
merge_sort_bottom_up(string_list)
print(string_list)
print()



lists = [[4, 65, 2, -31, 0, 99, 83, 782, 1],
         [44, 77, 59, 39, 41, 69, 72, 72, 41, 37, 11, 72, 16, 22, 33],
         [170, 45, 2, 75, 90, 802, 24, 2, 66, 0, -1],
         [44, 77, 59, 39, 41, 69, 68, 10, 72, 99, 72, 11, 41, 37, 11, 72, 16, 22, 10, 100],
         [44, 77, 59, 39, 41, 69, 68, 10, 72, 99, 72, 11, 41, 37, 11, 72, 16, 22, 10, 33],
         [],
         [10, -28, -75, -95, -29, -28, 27, 92, -59, 80, 45, 49, -62, 21, -79, 75, 99, 52, -28, 41],
         [44, 77, 59, 39, 41, 69, 72, 72, 41, 37, 11, 72, 16, 22, 33],
         [0],
         [0, 0],
         [1, 0, -1]]
fns = [merge_sort,
       top_down_merge_sort]

for l in lists:
    print(f"l: {l}")
    for fn in fns:
        print(f"{fn.__name__}(l): {fn(l[:])}")
    print()



