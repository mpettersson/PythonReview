import time
"""
    DYNAMIC PROGRAMMING

    Is an optimization over plain recursion.  Where recursion is just a (recursive) function that directly or 
    indirectly calls its self.
    
    Dynamic Programming may or may not be recursive.  Each of the sub-problems are indexed some way in memory.
    
    There are two different ways Dynamic Programming is done (or referred to):
        (1) Memoization - Top Down
        (2) Tabulation - Bottom up
"""


# PLAIN RECURSIVE FIBONACCI
# Gets really slow around recursive_fib(40)
# O(2 ** n) time!!!
def recursive_fib(n):
    if n is 0:
        return 0
    if n is 1:
        return 1
    return recursive_fib(n - 1) + recursive_fib(n - 2)


# TOP DOWN DYNAMIC PROGRAMMING or MEMOIZATION FIBONACCI WITH A LIST
# Extremely fast. memoization_fib(400) takes a fraction of a second.
# O(n) runtime, O(n) space!!!
def memoization_fib(n):
    l = [None] * (n + 1)
    return memoization_fibonacci(n, l)


def memoization_fibonacci(n, l):
    if n is 0:
        return 0
    if n is 1:
        return 1
    if l[n] is None:
        l[n] = memoization_fibonacci(n - 1, l) + memoization_fibonacci(n - 2, l)
    return l[n]


# BOTTOM UP DYNAMIC PROGRAMMING or TABULATION FIBONACCI WITH A LIST
# Extremely fast. memoization_fib(400) takes a fraction of a second.
# O(n) runtime, O(n) space!!!
def tabulation_list_fib(n):
    if n is 0:
        return 0
    if n is 1:
        return 1
    l = [None] * n
    l[0] = 0
    l[1] = 1
    i = 2
    while i < n:
        l[i] = l[i - 1] + l[i - 2]
        i += 1
    return l[n - 1] + l[n - 2]


# BOTTOM UP DYNAMIC PROGRAMMING or TABULATION FIBONACCI WITHOUT A LIST
# Extremely fast. memoization_fib(400) takes a fraction of a second.
# O(n) runtime, O(1) space!!!
def tabulation_fib(n):
    if n is 0:
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


# Testing how long the functions take...
t = time.time()
recursive_fib(35)
print("recursive_fib(35) took", time.time() - t, "seconds")





