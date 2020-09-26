"""
    (COMPUTE THE REAL) SQUARE ROOT (EPI 12.5)

    Implement a function which takes as input a floating point value and returns its square root.

    Example:
        Input = 3.141592653589793
        Output = 1.7724533469195394

    HINT:  Iteratively compute a seq. of intervals, each contained in the previous interval, that contains the result.
"""
import math


# Binary Search Approach:  Using a low and high bound, repetitively find a middle value that tightens the bound, until
# the desired precision is achieved.
# NOTE: When picking bounds be careful; if n is 1/2, the square root of n will be LARGER than n (so don't start with the
# wrong bounds or you will not get the correct solution)!
def square_root(n, tolerance=.00001):
    if n is not None and tolerance is not None and 0 < tolerance < 1:
        lo = 1
        hi = n
        if n < 1:
            lo, hi = hi, lo                     # Reverse if n is a decimal; the sqrt of a decimal INCREASES in size!
        while lo < hi:
            mid = lo + .5 * (hi - lo)           # Get the real middle (float).
            sq_mid = mid ** 2
            if abs(sq_mid - n) <= tolerance:    # How to check for tolerance (since it's a float).
                return mid
            if sq_mid < n:
                lo = mid
            else:
                hi = mid
    else:
        raise ValueError("Invalid arguments.")


args = [math.pi, math.e, 9.8, 77]

for a in args:
    print(f"square_root({a}): {square_root(a)}")


