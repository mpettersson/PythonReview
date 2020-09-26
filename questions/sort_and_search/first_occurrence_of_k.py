"""
    FIRST OCCURRENCE OF K (EPI 12.1)

    Write a function that takes a sorted list and a key and returns the index of the FIRST occurrence of that key in the
    list.

    Example:
        Input = 108, [-14, -10, 2, 108, 243, 285, 285, 285, 401]
        Output = 3
"""

# NOTE: Did you read the question right; return the first, or LOWEST, index with the value k!


# Naive Approach:  Time complexity is O(n), where n is the number of items in the list.  Space complexity is O(1).
def first_occurrence_of_k_naive(l, k):
    if l is not None and k is not None and len(l) > 0:
        lo = 0
        hi = len(l) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if l[mid] is k:
                while mid - 1 > 0 and l[mid - 1] is k:      # This is why it's O(n) time...
                    mid = mid - 1
                return mid
            elif k < l[mid]:
                hi = mid - 1
            else:
                lo = mid + 1


# Binary Search Approach:  Time complexity is O(log(n)), where n is the length of the list.  Space complexity is O(1).
def first_occurrence_of_k(l, k):
    result = None
    if l is not None and k is not None and len(l) > 0:
        lo = 0
        hi = len(l) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if l[mid] is k:
                result = mid        # Keep the index (if there aren't any earlier)
                hi = mid - 1        # Try for earlier ones...
            elif k < l[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
    return result


l = [-99, -14, -10, 2, 0, 108, 243, 285, 285, 285, 285, 285, 401]
vals = [-101, -99, 0, 1, 285, 401, 404, None]

print(f"l: {l}\n")

for v in vals:
    print(f"first_occurrence_of_k_naive(l, {v}): {first_occurrence_of_k_naive(l, v)}")
print()

for v in vals:
    print(f"first_occurrence_of_k(l, {v}): {first_occurrence_of_k(l, v)}")


