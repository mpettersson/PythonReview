"""
    MAGIC INDEX (CCI 8.3)

    A magic index in a list l[0...n-1] is defined to be an index such that l[i] = i.  Given a sorted array of distinct
    integers, write a method to find a magic index, if one exists, in list l.

    Example:
        Input = [-2, 0, 1, 3, 7, 8, 12]
        Output = 3

    Variation:
        Values are not distinct.
"""


# Naive/Brute Force Approach:  Time is O(n), where n is the length of the list, space is O(1).
def magic_index_naive(l):
    for i, v in enumerate(l):
        if i is v:
            return i


# Binary Search Approach:  Due to the list being unique and sorted, after examining the value of the middle element,
# we can dismiss half the list (similar to the binary search algorithm).  Time and space is O(log(n)), where n is the
# length of the list.
def magic_index_rec(l):

    def _magic_index_rec(l, _left, _right):
        if 0 <= _left <= _right:
            mid = (_left + _right) // 2
            if l[mid] is mid:
                return mid
            elif l[mid] < mid:
                return _magic_index_rec(l, mid + 1, _right)
            else:
                return _magic_index_rec(l, _left, mid - 1)

    if l and len(l) > 0:
        return _magic_index_rec(l, 0, len(l) - 1)


# Duplicate Variation:  This approach searches all of one side and from the start of the other side to the index
# corresponding to the previous middle value (therefore, a portion of the list can be skipped).
def magic_index_with_dups_rec(l):

    def _magic_index_with_dups_rec(l, _left, _right):
        if 0 <= _left <= _right <= len(l) - 1:
            mid = (_left + _right) // 2
            if l[mid] is mid:
                return mid
            elif l[mid] < mid:
                res = _magic_index_with_dups_rec(l, mid + 1, _right)
                return res if res is not None else _magic_index_with_dups_rec(l, _left, l[mid])
            else:
                res = _magic_index_with_dups_rec(l, _left, mid - 1)
                return res if res is not None else _magic_index_with_dups_rec(l, mid + 1, l[mid])

    if l and len(l) > 0:
        return _magic_index_with_dups_rec(l, 0, len(l) - 1)


lists = [[-2, 0, 1, 3, 7, 8, 12],
         [-15, -14, -13, -12, -11, -10, 6],
         [-15, -14, -13, -12, -11, -10],
         [0, 10, 20, 30, 40, 50, 60, 70],
         [10, 20, 30, 40, 50, 60, 70]]

for l in lists:
    print(f"magic_index_naive({l}): {magic_index_naive(l)}")
print()

for l in lists:
    print(f"magic_index_rec({l}): {magic_index_rec(l)}")
print()

lists_w_dups = [[0 for _ in range(10)],
                [-15, -14, -13, -12, 9, 9, 9, 9, 9, 9, 10, 100],
                [8 for _ in range(10)]]

for l in lists + lists_w_dups:
    print(f"magic_index_with_dups_rec({l}): {magic_index_with_dups_rec(l)}")


