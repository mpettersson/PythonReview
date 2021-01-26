"""
    COMPUTE THE BINOMIAL COEFFICIENTS (EPI 17.4)

    (n choose k) is the short form for the expression n(n-1)...(n-k+1)/k(k-1)...(3)(2)(1).  It is the number of ways to
    choose a k-element subset from an n-element set.  It is not obvious that the expression defining (n choose k) always
    yields an integer.  Furthermore, direct computation of (n choose k) from this expression quickly results in the
    numerator or denominator overflowing if integer types are used, even if the final result fits in a 32-bit integer.
    If floats are used, the expression may not yield a 32-bit integer.

    Design an efficient algorithm for computing (n choose k) which has the property that it never overflows if the final
    result fits in the integer word size.
"""

# NOTE: Python has the following ways to compute binomial coefficients:
#   - scipy:
#       import scipy.special                                            # Have to 'pip3 install scipy'
#       scipy.special.binom(n, r)
#       scipy.special.comb(n, r)
#       scipy.special.comb(n, r, exact=True)                            # NO scientific notation if very long.
#   - math:
#       math.comb(n, r)                                                 # Only in python >= 3.8!!!
#       math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


# Naive Approach: Time complexity is O(n).  Space complexity is O(1).
#
# NOTE: This works for Python, however, it wouldn't work for C++/Java/etc.
def n_choose_k_naive(n, k):
    if n is not None and k is not None and k > 0:
        numerator = n
        for i in range(n-k+1, n):
            numerator *= i
        denominator = k
        for i in range(1, k):
            denominator *= i
        return numerator // denominator


# NOTE: We could count the number of subsets provided by num_subsets_with_sum


# Analytic Approach:
# A binomial coefficient must satisfy the following formula: (n choose k) = (n-1 choose k) + (n-1 choose k-1).  This
# identity yields a straightforward recursion for (n choose k).  The base cases are (r choose r) and (r choose 0), both
# of which are 1.  The individual results from the sub-calls are 32-bit integers (for Java/C++) and if (n choose k) can
# be represented by a 32-bit integer, they can too, so it is not possible for intermediate results to overflow.
#
# Example (using the formula/identity above):
#   (5 choose 2) == (4 choose 2) + (4 choose 1)                                   == 6 + 4
#   (5 choose 2) == ((3 choose 2) + (3 choose 1)) + (4 choose 1)                  == (3 + 3) + 4
#   (5 choose 2) == (((2 choose 2) + (2 choose 1)) + (3 choose 1)) + (4 choose 1) == ((1 + 2) + 3) + 4
#
# Time and space complexity is O(n * k), (however, space complexity can easily be reduced to O(k).
def n_choose_k(n, k):

    def _n_choose_k(x, y, memo):
        if y is 0 or x is y:
            return 1
        if memo[x][y] is 0:
            without_y = _n_choose_k(x-1, y, memo)
            with_y = _n_choose_k(x-1, y-1, memo)
            memo[x][y] = without_y + with_y
        return memo[x][y]

    if n is not None and k is not None and k > 0:
        memo = [[0] * (k + 1) for _ in range(n + 1)]
        return _n_choose_k(n, k, memo)


args = [(5, 2),
        (8, 4)]

for n, k in args:
    print(f"n_choose_k_naive({n}, {k}): {n_choose_k_naive(n, k)}")
print()

for n, k in args:
    print(f"n_choose_k({n}, {k}): {n_choose_k(n, k)}")


