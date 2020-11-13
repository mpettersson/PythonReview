"""
    GREATEST COMMON DIVISOR (GCD)

    In mathematics, the greatest common divisor (gcd) of two or more integers, which are not all zero, is the largest
    positive integer that divides each of the integers.

    In the name "greatest common divisor", the adjective "greatest" may be replaced by "highest", and the word "divisor"
    may be replaced by "factor", so that other names include greatest common factor (gcf), etc.  Historically, other
    names for the same concept have included greatest common measure.

    SEE: https://en.wikipedia.org/wiki/Euclidean_algorithm
"""


# GCD Iterative Approach
# Time Complexity: O(log(max(a, b)).
# Space complexity: O(1).
def gcd(a, b):
    while b:
        print(a, b)
        a, b = b, a % b
    return abs(a)


# GCD Recursive Approach
# Time Complexity: O(log(max(a, b))).
# Space Complexity: O(log(max(a, b))).
def gcd_rec(a, b):
    return abs(a) if b is 0 else gcd_rec(b, a % b)


# Euclid's Original (Subtraction-Based) GCD Algorithm
# Time Complexity: O(n), (if one of the two values were 1).
# Space complexity: O(1).
def gcd_euclid(a, b):
    if a > 0 and b > 0:     # Positive Integers ONLY
        while a != b:       # Stops when a == b.
            print(a, b)

            if a > b:
                a = a - b
            else:
                b = b - a
        return a


# Stein's Algorithm, or Binary GCD:
# The algorithm reduces the problem of finding the GCD of two nonnegative numbers by repeatedly applying the identities:
#       gcd_stein(0, b) = b
#       gcd_stein(a, 0) = a
#       gcd_stein(2a, 2b) = 2 * gcd_stein(a, b)
#       gcd_stein(2a, b) = gcd_stein(a, b),     if b is odd
#       gcd_stein(a, 2b) = gcd_stein(a, b),     if a is odd
#       gcd_stein(a, b) = gcd_stein(abs(a − b|), min(a, b)),    if a and b are both odd.
# SEE: https://en.wikipedia.org/wiki/Binary_GCD_algorithm for more information.


# Iterative Binary GCD (AKA Stein's Algorithm):
# Time Complexity: O(2**n), where n is the number of bits in the binary representation of max(a, b).
# Space Complexity: O(1).
def gcd_stein(a, b):
    if a >= 0 and b >= 0:               # Zero or Positive Integers ONLY
        if a is 0:
            return b
        if b is 0:
            return a
        k = 0
        while (a | b) & 1 is 0:         # Finding K, where K is the greatest power of 2 that divides both a and b.
            a = a >> 1
            b = b >> 1
            k = k + 1
        while a & 1 is 0:               # Dividing a by 2 until a becomes odd.
            a = a >> 1                  # After this point, a is always odd.
        while b is not 0:
            while b & 1 is 0:           # If b is even, remove all factors of 2 in b
                b = b >> 1
            if a > b:
                a, b = b, a
            b = b - a
        return a << k                   # restore common factors of 2


# Recursive Binary GCD (AKA Stein's Algorithm)
# Time complexity: O(2**n), where n is the number of bits in the binary representation of max(a, b).
# Space complexity: O(2**n), where n is the number of bits in the binary representation of max(a, b).
def gcd_stein_rec(a, b):
    if a >= 0 and b >= 0:                                   # Zero or Positive Integers ONLY
        if a is b:
            return a
        if a is 0:
            return b
        if b is 0:
            return a
        if a & 1 is 0:
            if b & 1 is 1:                                  # a is even, b is odd
                return gcd_stein_rec(a >> 1, b)
            else:                                           # a and b is even
                return gcd_stein_rec(a >> 1, b >> 1) << 1
        if b & 1 is 0:                                      # a is odd, b is even
            return gcd_stein_rec(a, b >> 1)
        if a > b:
            return gcd_stein_rec((a - b) >> 1, b)
        return gcd_stein_rec((b - a) >> 1, a)


args = [(200, 310), (10, 275), (468, 279), (120, 390), (480, 430), (33, 69), (-150, 348), (-462, -264), (465, -18),
        (19, 82), (13, 499), (1223, 4), (10, 0), (0, 10), (0, 0)]
fns = [gcd, gcd_rec, gcd_euclid, gcd_stein, gcd_stein_rec]

for fn in fns:
    for a, b in args:
        print(f"{fn.__name__}({a}, {b}): {fn(a, b)}")
    print()


