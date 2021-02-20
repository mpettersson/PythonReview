"""
    GCD (GREATEST COMMON DIVISOR)

    In mathematics, the greatest common divisor (gcd) of two or more integers, which are not all zero, is the largest
    positive integer that divides each of the integers.  In the name "greatest common divisor", the adjective "greatest"
    may be replaced by "highest", and the word "divisor" may be replaced by "factor", so that other names include
    greatest common factor (gcf), etc.  Historically, other names for the same concept have included greatest common
    measure.   SEE: https://en.wikipedia.org/wiki/Euclidean_algorithm

    Write a function that returns the gcd of two supplied integers.

    Example:
        Input = 8, 12
        Output = 4

    Variations:
        - Same as above, however, *, /, or % operators may not be used. (EPI 25.1: COMPUTE THE GREATEST COMMON DIVISOR)
"""

# More GCD Rules:
#   - Zero cannot be a GCD, since anything divided by zero is undefined.
#   - The GCD of a non-zero number and zero will always be the non-zero number.
#   - The GCD a negative numbers will always be the GCD of the absolute value of the negative numbers.
#   - The GCD of a (non-zero) number and itself is always the number.


# GCD Iterative Approach.
# Time Complexity: O(log(max(a, b)).
# Space complexity: O(1).
def gcd_iter(a, b):
    if a == b == 0:
        return float('nan')
    while b:
        a, b = b, a % b
    return abs(a)


# GCD Recursive Approach.
# Time Complexity: O(log(max(a, b))).
# Space Complexity: O(log(max(a, b))).
def gcd_rec(a, b):
    if a == b == 0:
        return float('nan')
    return abs(a) if b == 0 else gcd_rec(b, a % b)


# VARIATION: Multiplication, division, or modulus may not be used.


# Euclid's Original Subtraction-Based GCD (Iterative) Algorithm
# Time Complexity: O(max(a, b)), (if min(a, b) was 1).
# Space complexity: O(1).
def gcd_euclid_iter(a, b):

    def classic_euclid(a, b):   # CLASSIC EUCLID ALG.
        if a > 0 and b > 0:     # Positive Integers ONLY
            while a != b:       # Stops when a == b.
                if a > b:
                    a = a - b
                else:
                    b = b - a
            return a

    if a == b == 0:
        return float('nan')
    if a == 0:
        return b
    if b == 0:
        return a
    if a < 0:
        a = abs(a)
    if b < 0:
        b = abs(b)
    return classic_euclid(a, b)


# Euclid's Original Subtraction-Based GCD (Recursive) Algorithm
# Time Complexity: O(max(a, b)), (if min(a, b) was 1).
# Space Complexity: O(max(a, b)), (if min(a, b) was 1).
def gcd_euclid_rec(a, b):
    if a == b == 0:
        return float('nan')
    if a < 0:
        a = abs(a)
    if b < 0:
        b = abs(b)
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a
    if a < b:
        b, a = a, b
    return gcd_euclid_rec(a - b, b)


# Stein's Algorithm, or Binary GCD:
# The algorithm reduces the problem of finding the GCD of two nonnegative numbers by repeatedly applying the identities:
#       gcd_stein(0, b) = b
#       gcd_stein(a, 0) = a
#       gcd_stein(2a, 2b) = 2 * gcd_stein(a, b)
#       gcd_stein(2a, b) = gcd_stein(a, b),     if b is odd
#       gcd_stein(a, 2b) = gcd_stein(a, b),     if a is odd
#       gcd_stein(a, b) = gcd_stein(abs(a − b|), min(a, b)),    if a and b are both odd.
# SEE: https://en.wikipedia.org/wiki/Binary_GCD_algorithm for more information.


# Iterative Binary GCD (AKA Stein's Algorithm).
# Time Complexity: O(2**n), where n is the number of bits in the binary representation of max(a, b).
# Space Complexity: O(1).
def gcd_stein(a, b):
    if a == b == 0:
        return float('nan')
    if a < 0:
        a = abs(a)
    if b < 0:
        b = abs(b)
    if a == 0:
        return b
    if b == 0:
        return a
    k = 0
    while (a | b) & 1 == 0:         # Finding K, where K is the greatest power of 2 that divides both a and b.
        a = a >> 1
        b = b >> 1
        k = k + 1
    while a & 1 == 0:               # Dividing a by 2 until a becomes odd.
        a = a >> 1                  # After this point, a is always odd.
    while b != 0:
        while b & 1 == 0:           # If b is even, remove all factors of 2 in b
            b = b >> 1
        if a > b:
            a, b = b, a
        b = b - a
    return a << k                   # restore common factors of 2


# Recursive Binary GCD (AKA Stein's Algorithm).
# Time complexity: O(2**n), where n is the number of bits in the binary representation of max(a, b).
# Space complexity: O(2**n), where n is the number of bits in the binary representation of max(a, b).
def gcd_stein_rec(a, b):
    if a == b == 0:
        return float('nan')
    if a < 0:
        a = abs(a)
    if b < 0:
        b = abs(b)
    if a is b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a
    if a & 1 == 0:
        if b & 1 == 1:                                  # a is even, b is odd
            return gcd_stein_rec(a >> 1, b)
        else:                                           # a and b is even
            return gcd_stein_rec(a >> 1, b >> 1) << 1
    if b & 1 == 0:                                      # a is odd, b is even
        return gcd_stein_rec(a, b >> 1)
    if a > b:
        return gcd_stein_rec((a - b) >> 1, b)
    return gcd_stein_rec((b - a) >> 1, a)


# Recursive Binary GCD (AKA Stein's Algorithm).
# Time Complexity: O(log2(a) + log2(b)), or, the number of bits of a plus the number of bits in b.
# Space Complexity: O(log2(a) + log2(b)), or, the number of bits of a plus the number of bits in b.
def gcd_stein_alt_rec(a, b):
    if a == b == 0:
        return float('nan')
    if a < 0:
        a = abs(a)
    if b < 0:
        b = abs(b)
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a
    elif not a & 1 and not b & 1:
        return gcd_stein_alt_rec(a >> 1, b >> 1) << 1   # a and b are even
    elif not a & 1 and b & 1:
        return gcd_stein_alt_rec(a >> 1, b)             # a is even, b is odd
    elif a & 1 and not b & 1:
        return gcd_stein_alt_rec(a, b >> 1)             # a is odd, b is even
    elif a > b:
        return gcd_stein_alt_rec(a - b, b)              # both a and b are odd, and a > b
    return gcd_stein_alt_rec(a, b - a)                  # Both a and b are odd, and a <= b.


args = [(8, 12), (3, 3), (200, 310), (10, 275), (468, 279), (120, 390), (480, 430), (33, 69), (-150, 348), (-462, -264),
        (465, -18), (19, 82), (13, 499), (1223, 4), (10, 0), (0, 10), (0, 0)]
fns = [gcd_iter,
       gcd_rec,
       gcd_euclid_iter,
       gcd_euclid_rec,
       gcd_stein,
       gcd_stein_rec,
       gcd_stein_alt_rec]

for fn in fns:
    for a, b in args:
        print(f"{fn.__name__}({a}, {b}): {fn(a, b)}")
    print()


