"""
    FIND DUPLICATE ELEMENTS (50CIQ 4: FIND DUPLICATES)

    Write a function which accepts a list of integers in the range 1 <= x <= len(list), and may or may not contain
    duplicate integers, then finds and returns any duplicate integers in a list.

    Example:
        Input = [1, 2, 2, 3]
        Output = [2]
"""


# APPROACH: Naive Brute Force
#
# Compare every set of indices adding any duplicates to a result set, which is returned as a list.
#
# Time Complexity: O(n**2), where n is the size of the list.
# Space Complexity: O(u), where u is the size of the set of unique items in the list.
def find_duplicate_elements_naive_bf(l):
    if l is not None:
        result = set()
        for i in range(len(l)-1):
            for j in range(i+1, len(l)):
                if l[j] is l[i]:
                    result.add(l[j])
        return list(result)


# APPROACH: Naive Set
#
# Use a set to maintain seen values, if a duplicate value is then found, add it to the result set, then return the
# results set as a list.
#
# Time Complexity: O(n), where n is the size of the list.
# Space Complexity: O(max(u, d)), where u and d are the sizes of the unique and duplicate item sets.
def find_duplicate_elements_naive_set(l):
    if l is not None:
        result = set()
        s = set()
        for e in l:
            if e in s:
                result.add(e)
            else:
                s.add(e)
        return list(result)


# APPROACH: (Optimal) Negate List Values
#
# Leveraging the property that all values are greater than zero, and that the values are in the range of the list's
# indices, use negation as a flag value.  That is, iterate over the values in the list, using each value as an index,
# if the value stored at the index is negative, then that index (or value) has been seen previously (therefore, adding
# it to the results).  Finally, iterate over the list undoing any negations.
#
# Time Complexity: O(n), where n is the size of the list.
# Space Complexity: O(d), where d is the size of the set of duplicate items in the list.
def find_duplicate_elements(l):
    if l is not None:
        result = set()
        for i in range(len(l)):
            index = abs(l[i]) - 1
            if l[index] > 0:                # Value is positive (not seen before), so
                l[index] *= -1                  # Negate the value.
            else:                           # Value is negative (seen before)
                result.add(index + 1)           # Add to result set.
        for i in range(len(l)):             # Cleanup (return values to positive) before returning.
            if l[i] < 0:
                l[i] *= -1
        return list(result)


lists = [[1, 2, 3],     # returns []
         [1, 2, 2, 3],  # returns [2]
         [3, 3, 3],     # returns [3]
         [2, 1, 2, 1],  # returns [1, 2]
         [],
         None]
fns = [find_duplicate_elements_naive_bf,
       find_duplicate_elements_naive_set,
       find_duplicate_elements]

for l in lists:
    for fn in fns:
        print(f"{fn.__name__}({l}): {fn(l)}")
    print()


