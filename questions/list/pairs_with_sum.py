"""
    PAIRS WITH SUM

    Design an algorithm to find ALL non-duplicate pairs of integers in a list l which sum to a specified total value t.

    Example:
        Input = [-2, 1, 2, 4, 7, 11], 6
        Output = [(2, 4)]

    Variations:
        - SEE: has_two_sum.py
        - SEE: has_three_sum.py
        - SEE: has_k_sum.py
"""


# Naive/Brute Force Approach:  Time complexity is O(n**2), where n is the number of elements in the list.  Space
# complexity is O(r), where r is the number of pairs that sum to the total value.
def pairs_with_sum_naive(l, t):
    if l is not None and t is not None:
        result = []
        for i in range(len(l)):
            for j in range(i+1, len(l)):
                if l[i] + l[j] is t:
                    result.append((l[i], l[j]))
        return result


# Set Approach:  Time and space complexity is O(n), where n is the number of elements in the list.
def pairs_with_sum_via_set(l, t):
    if l is not None and t is not None:
        result = []
        elements = set()
        for x in l:
            complement = t - x
            if complement in elements and x not in elements:
                result.append((x, complement))
            elements.add(x)
        return result


# Sort & Binary Search Approach:  Time complexity is O(n**2) (or O(n * log(n)) to sort and O(n) to find pairs), where n
# is the number of elements in the list.
def pairs_with_sum_via_sort(l, t):
    if l is not None and t is not None:
        result = []
        l.sort()
        first = 0
        last = len(l) - 1
        while first < last:
            temp = l[first] + l[last]
            if temp == t:
                result.append((l[first], l[last]))
                first += 1
                last -= 1
            else:
                if temp < t:
                    first += 1
                else:
                    last -= 1
        return result


args = [([13, 0, 14, -2, -1, 7, 9, 5, 3, 6], 6),
        ([-2, 1, 2, 4, 7, 11], 6),
        ([-2, 1, 2, 4, 7, 11], 10),
        ([2, 4], 6),
        ([6], 6),
        ([-2, -1, 0, 3, 5, 6, 7, 9, 13, 14], 6),
        ([], 6),
        ([-2, 1, 2, 4, 7, 11], None),
        (None, 6),
        (None, None)]

for l, n in args:
    print(f"pairs_with_sum_naive({l}, {n}): {pairs_with_sum_naive(l, n)}")
print()

for l, n in args:
    print(f"pairs_with_sum_via_set({l}, {n}): {pairs_with_sum_via_set(l, n)}")
print()

for l, n in args:
    print(f"pairs_with_sum_via_sort({l}, {n}): {pairs_with_sum_via_sort(l, n)}")


