"""
    FIND FIRST POSITIVE MISSING ELEMENT  (EPI 25.2: FIND THE FIRST MISSING POSITIVE ENTRY)

    Write a function which accepts a list of integers and returns the smallest positive integer not in the list; the
    contents of the list do not need to be preserved.

    Example:
        Input = [3, 5, 4, -1, 5, 1, -1]
        Output = 2

    Variations:
        SEE: find_duplicate_element.py, find_duplicate_and_missing_elements.py, and missing_two.py.
"""
import copy


# Sort Approach:  Sort the list, then iterate through the values of the list, returning the first positive value that
# is not found in the sorted list.
# Time Complexity: O(n * log(n)), where n is the number of elements in the list.
# Space Complexity: O(1)
def find_first_pos_missing_ele_via_sort(l):
    result = 1
    l.sort()
    for e in l:
        if e == result:
            result += 1
        elif e > result:
            return result
    return result


# Set Approach:  Convert the list into a set, then starting at one, check for the first missing value in the range of
# the size of the set plus one, that is not in the set.
# Time Complexity: O(n), where n is the number of distinct elements in the list.
# Space Complexity: O(n), where n is the number of distinct elements in the list.
def find_first_pos_missing_ele_via_set(l):
    s = set(l)
    for i in range(1, len(s) + 2):
        if i not in s:
            return i


# Optimal Approach:  Find the first missing positive element by reordering the list, writing the value at l[i] to the
# index l[i] - 1 if the value (l[i]) is between 1 and the size of the list (inclusive), then iterating over the list to
# find the result.
# Time Complexity: O(n), where n is the number of distinct elements in the list.
# Space Complexity: O(1).
def find_first_pos_missing_ele(l):
    i = 0
    while i < len(l):                                   # FIRST: Re-order The Values
        if 0 < l[i] <= len(l) and l[l[i] - 1] != l[i]:      # If the value at l[i] is in the range 1 - len(l), then move
            j = l[i] - 1                                    # it to the index equal to one less it's value.
            l[i], l[j] = l[j], l[i]                         # NOTE: l[i], l[l[i]-1] = l[l[i]-1], l[i] won't work.
        else:
            i += 1                                          # Otherwise, increment the counter.
    for i in range(len(l)):                             # SECOND: Check For Missing Value
        if l[i] != i + 1:
            return i + 1
    return len(l) + 1                                       # If the list was empty.


args = [[3, 5, 4, -1, 5, 1, -1],
        [5, 3, 0, 1, 2],
        [5, 3, 4, 1, 2],
        [3, 4, 0, 2],
        [-3, -4, -1, -2],
        []]
fns = [find_first_pos_missing_ele_via_sort,
       find_first_pos_missing_ele_via_set,
       find_first_pos_missing_ele]

for fn in fns:
    for l in args:
        print(f"{fn.__name__}({l!r}): {fn(copy.deepcopy(l))}")
    print()


