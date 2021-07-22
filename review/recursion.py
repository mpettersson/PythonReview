"""
    RECURSION, TAIL RECURSION, & DYNAMIC PROGRAMMING
    
    Recursion:
        - Recursion occurs when a thing is defined in terms of itself or of its type.
        - A recursive function directly, or indirectly, calls itself.
    
    Tail Recursion:
        - Special case of recursion.
        - The (one) recursion call is the LAST/FINAL action in the function. 
        - Often utilizes 'accumulator' variables to ensure the recursive call is the last action. 
        - Guido van Rossum doesn't want tail recursion in Python (because of altered stack traces):
            - http://neopythonic.blogspot.com.au/2009/04/tail-recursion-elimination.html
            - http://neopythonic.blogspot.com.au/2009/04/final-words-on-tail-calls.html
        - Tail recursive function (in Python) have improved runtime when compared to (plain) recursive functions.
        - Links for tail recursion modules:
            - https://pypi.org/project/tail-recursive/
            - https://github.com/baruchel/tco
     
    Dynamic Programming:
        - Is an optimization over plain recursion.  
        - Dynamic Programming may or may not be recursive.  
        - Each of the sub-problems are indexed some way in memory.
        - There are two different ways Dynamic Programming is done (or referred to):
            (1) Memoization - Top Down
            (2) Tabulation - Bottom up
"""
import time


# APPROACH: Recursive
#
# Plain vanilla recursion; return the result of recursive n-1 and n-2 calls.
#
# Time Complexity: O(2 ** n), (technically, the time complexity is closer to O(1.6 ** n)).
# Space Complexity: O(n).
#
# NOTE: At around n=40, this becomes very slow.
def fibonacci_rec(n):
    if n is not None and n >= 0:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


# APPROACH: Tail Recursion
#
# Using accumulator values to reduce the number of recursive calls to one (so that the tail recursion property can be
# maintained), which is the final action of the function.
#
# Time Complexity: O(n).
# Space Complexity: O(n).
#
# NOTE: Stock Python implementations DO NOT perform tail-call optimization, though third-party modules are available
# (see top). Language inventor Guido van Rossum contends that stack traces are altered by tail call elimination making
# debugging harder, and prefers that programmers use explicit iteration instead.  HOWEVER, tail recursive function do
# perform much better than plain recursive functions.
def fibonacci_tail_rec(n):

    def _go(n, a=0, b=1):           # In tail recursion, accumulator value(s) (a, b) is/are used.
        if n == 0:
            return a
        if n == 1:
            return b
        return _go(n-1, b, a + b)   # In tail recursion, the recursive call must be LAST.

    if n is not None and n >= 0:
        return _go(n)


# APPROACH: Tail Recursion As Loop
#
# This is essentially the same as the bottom up dynamic programming approach (below).
#
# Time Complexity: O(n).
# Space Complexity: O(1).
def fibonacci_tail_loop(n):
    if n is not None and n >= 0:
        a = 0
        b = 1
        while True:
            if n == 0:
                return a
            if n == 1:
                return b
            n, a, b, = n - 1, b, a + b


# APPROACH: Top Down Dynamic Programming/Memoization
#
# This approach is essentially the recursive approach (above) with a list used as a memoization cache; this guarantees
# that for any (non-base case) value of n, the result must only be computed once (then cached).
#
# Time Complexity: O(n).
# Space Complexity: O(n).
def fibonacci_top_down(n):

    def _fibonacci_top_down(n, memo):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if memo[n] is None:
            memo[n] = _fibonacci_top_down(n - 1, memo) + _fibonacci_top_down(n - 2, memo)
        return memo[n]

    if n is not None and n >= 0:
        memo = [None] * (n + 1)
        return _fibonacci_top_down(n, memo)


# APPROACH: Bottom Up Dynamic Programming/Tabulation With Memoization
#
# This iterative (looping) approach simply works in a reversed direction to the top down (recursive) approach above.
#
# Time Complexity: O(n).
# Space Complexity: O(n).
def fibonacci_bottom_up_memo(n):
    if n is not None and n >= 0:
        if n == 0:
            return 0
        if n == 1:
            return 1
        memo = [None] * n
        memo[0] = 0
        memo[1] = 1
        i = 2
        while i < n:
            memo[i] = memo[i - 1] + memo[i - 2]
            i += 1
        return memo[n - 1] + memo[n - 2]


# APPROACH: Bottom Up Dynamic Programming/Tabulation
#
# This is a space optimized version of the bottom up memoization approach above; the cache has been replaced with three
# variables thus reducing the space complexity to O(1).
#
# Time Complexity: O(n).
# Space Complexity: O(1).
#
# NOTE: Tabulation/Bottom Up Dynamic Programming is generally the best performing solution.
def fibonacci_bottom_up(n):
    if n is not None and n >= 0:
        if n == 0:
            return 0
        a = 0
        b = 1
        i = 2
        while i < n:
            c = a + b
            a = b
            b = c
            i += 1
        return a + b


nums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, None]
fns = [fibonacci_rec,
       fibonacci_tail_rec,
       fibonacci_tail_loop,
       fibonacci_top_down,
       fibonacci_bottom_up_memo,
       fibonacci_bottom_up]

for n in nums:
    for fn in fns:
        print(f"{fn.__name__}({n}): {fn(n)}")
    print()

n = 35
for fn in fns:
    t = time.time()
    print(f"{fn.__name__}({n}) took ", end="")
    fn(n)
    print(f"{time.time() - t} seconds.")


