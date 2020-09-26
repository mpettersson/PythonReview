"""
    FIND (THE) DUPLICATE AND MISSING ELEMENTS (EPI 12.10)

    You are given a list of n integers, each between 0 and n-1, inclusive.  Exactly one element appears twice, implying
    that exactly one number between 0 and n-1 is missing from the list.  How would you compute the duplicate and missing
    numbers?

    Example:
        Input = [5, 3, 0, 1, 2, 3]
        Output = 3, 4

    Variations:
        SEE: find_duplicate_element.py, find_missing_elements.py, and missing_two.py.
"""
import random


# Dictionary (Brute Force) Approach:  Time and space complexity is O(n), where n is the size of the list.
def find_duplicate_and_missing_elements_via_dict(l):
    if l is not None:
        d = {}
        dup = None
        for e in l:
            d[e] = d.setdefault(e, 0) + 1
            if d[e] > 1:
                dup = e
        for i in range(len(l)):
            if i not in d:
                return dup, i


# Sort (Brute Force) Approach:  Time complexity is O(n log(n)), where n is the length of the list.  Space complexity is
# O(1).
def find_duplicate_and_missing_elements_via_sort(l):
    if l is not None:
        l.sort()
        dup = mis = None
        for i in range(len(l)):
            if i not in l:
                mis = i
                break
        for i in range(1, len(l)):
            if l[i] == l[i-1]:
                dup = l[i]
                break
        return dup, mis


# XOR Approach:  Computing the XOR of all the numbers from 0 to n-1, inclusive, AND the entries in the list provides
# the missing value XOR duplicate value.  Since the missing value isn't the same as the duplicate value, it has a one
# bit somewhere in its binary representation.  Isolating that bit (diff_bit) allows us to take the XOR of all numbers
# from 0 to n-1 that have a matching diff_bit and the XOR with all of the list values with a matching diff_bit. The
# resulting value, mis_or_dup, will be either the missing value OR the duplicate value.  One last traversal of the list
# will reveal what mis_or_dup is (either missing or duplicate value).  The other value will be XOR'ed from mis_or_dup.
# Time complexity is O(n), where n is the length of the list.  Space complexity is O(1).
def find_duplicate_and_missing_elements_via_xor(l):
    if l is not None:
        mis_xor_dup = 0
        for i, e in enumerate(l):                           # Since missing != duplicate, mis_xor_dup will not stay 0:
            mis_xor_dup ^= i ^ e                            # mis_xor_dup == missing ^ duplicate
        diff_bit = mis_xor_dup & ~(mis_xor_dup - 1)         # diff_bit == least significant 1 bit in mis_xor_dup
        mis_or_dup = 0
        for i in range(len(l)):                             # XOR'ing all numbers 0 to n-1 that have a 1 in diff_bit pos
            if i & diff_bit:                                # with all values in l that have a 1 in the diff_bit pos
                mis_or_dup ^= i                             # will yield either the missing value OR the duplicate value
            if l[i] & diff_bit:                             # mis_or_dup == missing  OR  mis_or_dup == duplicate
                mis_or_dup ^= l[i]
        for e in l:                                         # Traverse l one last time to see what mis_or_dup is:
            if e is mis_or_dup:                             # mis_or_dup == duplicate value
                return mis_or_dup, mis_or_dup ^ mis_xor_dup
        return mis_or_dup ^ mis_xor_dup, mis_or_dup         # mis_or_dup == missing value


nums = [2, 10, 100]

for n in nums:
    l = [i for i in range(n)]
    random.shuffle(l)
    duplicate = l.pop()
    missing = l.pop()
    l.extend([duplicate, duplicate])
    print(sorted(l))
    random.shuffle(l)
    print(f"List l:", l)
    print(f"Duplicate element: {duplicate}")
    print(f"Missing element: {missing}")
    print(f"find_duplicate_and_missing_elements_via_dict(l): {find_duplicate_and_missing_elements_via_dict(l)}")
    print(f"find_duplicate_and_missing_elements_via_sort(l): {find_duplicate_and_missing_elements_via_sort(l[:])}")
    print(f"find_duplicate_and_missing_elements_via_xor(l): {find_duplicate_and_missing_elements_via_xor(l)}\n")


