"""
    FACTORIAL

    Find the factorial of a number n.

    Remember:
        The factorial of a positive integer n, denoted by n!, is the product of all positive integers <= n.
        The value of 0! is 1.

    NOTE: We will emulate Google's result for -n!, where n is an int; we will return -(n!).

    Example:
        Input = 5
        Output = 120
"""
import time


# APPROACH: Recursive
#
# Time Complexity: O(n).
# Space Complexity: O(n).
def factorial_rec(n):

    def _factorial_rec(n):
        if n == 0 or n == 1:
            return 1
        elif n > 1:
            return n * factorial_rec(n - 1)

    if n is not None:
        neg_flag = True if n < 0 else False
        return _factorial_rec(abs(n)) * (-1 if neg_flag else 1)


# APPROACH: Tail Recursion
#
# This is similar to above, however, the recursive call is a tail call or tail recursive, (the final action of the fn).
#
# Time Complexity: O(n).
# Space Complexity: O(n).
#
# NOTE: Stock Python implementations DO NOT perform tail-call optimization, though a third-party module is available to
# do this (SEE: https://github.com/baruchel/tco).  Language inventor Guido van Rossum contends that stack traces are
# altered by tail call elimination making debugging harder, and prefers that programmers use explicit iteration instead.
def factorial_tail_rec(n):

    def _go(n, a=1):                # In tail recursion, accumulator value(s) (a) is/are used.
        if n == 0 or n == 1:
            return a
        return _go(n - 1, a * n)    # In tail recursion, the recursive call must be LAST.

    if n is not None:
        neg_flag = True if n < 0 else False
        return _go(abs(n)) * (-1 if neg_flag else 1)


# APPROACH: Top Down Dynamic Programming
#
# Time Complexity: O(n).
# Space Complexity: O(n).
def factorial_top_down(n):

    def _factorial_top_down(n, memo):
        if memo[n] is None:
            memo[n] = n * _factorial_top_down(n - 1, memo)
        return memo[n]

    if n is not None:
        neg_flag = True if n < 0 else False
        n = abs(n)
        memo = [None] * (n + 1)
        memo[0] = 1
        return _factorial_top_down(n, memo) * (-1 if neg_flag else 1)


# APPROACH: Bottom Up With Memoization Dynamic Programming (Tabulation)
#
# Time Complexity: O(n).
# Space Complexity: O(n).
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


# APPROACH: Bottom Up Dynamic Programming
#
# Time Complexity: O(n).
# Space Complexity: O(1).
def factorial_bottom_up(n):
    if n is not None:
        neg_flag = True if n < 0 else False
        n = abs(n)
        if n == 0:
            return 1
        t = 1
        i = 1
        while i <= n:
            t = t * i
            i += 1
        return t * (-1 if neg_flag else 1)


l = [-20, -10, -5, -3, -2, -1, 0, 1, 2, 3, 5, 10, 20, None]
fns = [factorial_rec,
       factorial_tail_rec,
       factorial_top_down,
       factorial_bottom_up_memo,
       factorial_bottom_up]

for n in l:
    for fn in fns:
        print(f"{fn.__name__}({n}): {fn(n)}")
    print()

n = 400
for fn in fns:
    t = time.time()
    print(f"{fn.__name__}({n}) took ", end="")
    fn(n)
    print(f"{time.time() - t} seconds.")


