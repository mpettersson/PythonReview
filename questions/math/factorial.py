"""
    FACTORIAL

    Find the factorial of a number n.

    Remember:
        The factorial of a positive integer n, denoted by n!, is the product of all positive integers <= n.
        The value of 0! is 1.
"""


# NOTE: Google's result for -n!, where n is an int, is -(n!), soo, we will do that too...


# Recursive Approach: Time and space complexity is O(n).
def factorial_rec(n):

    def _factorial_rec(n):
        if n is 0 or n is 1:
            return 1
        elif n > 1:
            return n * factorial_rec(n - 1)

    if n is not None:
        neg_flag = True if n < 0 else False
        return _factorial_rec(abs(n)) * (-1 if neg_flag else 1)


# Top Down Dynamic Programming Approach:  Time and space complexity is O(n).
def factorial_top_down(n):

    def _factorial_top_down(memo, n):
        if memo[n] is None:
            memo[n] = n * _factorial_top_down(memo, n - 1)
        return memo[n]

    if n is not None:
        neg_flag = True if n < 0 else False
        n = abs(n)
        memo = [None] * (n + 1)
        memo[0] = 1
        return _factorial_top_down(memo,n) * (-1 if neg_flag else 1)


# Bottom Up With Memoization Dynamic Programming (Tabulation) Approach:  Time and space complexity is O(n).
def factorial_bottom_up_memo(n):
    if n is not None:
        neg_flag = True if n < 0 else False
        n = abs(n)
        memo = [1] + [None] * n
        i = 0
        while i < n:
            i += 1
            memo[i] = i * memo[i - 1]
        return memo[n] * (-1 if neg_flag else 1)


# Bottom Up Dynamic Programming Approach:  Time complexity is O(n), space complexity is O(1).
def factorial_bottom_up(n):
    if n is not None:
        neg_flag = True if n < 0 else False
        n = abs(n)
        if n is 0:
            return 1
        t = 1
        i = 1
        while i <= n:
            t = t * i
            i += 1
        return t * (-1 if neg_flag else 1)


fns = [factorial_rec, factorial_top_down, factorial_bottom_up_memo, factorial_bottom_up]
l = [-20, -10, -5, -3, -2, -1, 0, 1, 2, 3, 5, 10, 20, None]

for fn in fns:
    for n in l:
        print(f"{fn.__name__}({n}): {fn(n)}")
    print()


