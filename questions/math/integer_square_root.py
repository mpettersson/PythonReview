"""
    (COMPUTE THE) INTEGER SQUARE ROOT (EPI 12.4)

    Write a program which takes a nonnegative integer and returns the largest integer whose square is less than or equal
    to the given integer.

    Example:
        Input = 300
        Output = 17
"""


# Naive/Brute Force Approach: Time complexity is O(n), space complexity is O(1).
def integer_square_root_naive(n):
    if n is not None and n > 0:
        i = 1
        while (i + 1) ** 2 <= n:
            i += 1
        return i


# Binary Search Approach:  Time complexity is O(log(n)), space complexity is O(1).
def integer_square_root(n):
    result = None
    if n is not None and n > 0:
        lo = 0
        hi = n
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid ** 2 is n:
                return mid
            if mid ** 2 > n:
                hi = mid - 1
            else:
                result = mid
                lo = mid + 1
    return result


args = [-420, 0, 1, 10, 25, 300, None]

for a in args:
    print(f"integer_square_root_naive({a}): {integer_square_root_naive(a)}")
print()

for a in args:
    print(f"integer_square_root({a}): {integer_square_root(a)}")


