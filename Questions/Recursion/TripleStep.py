"""
    TRIPLE STEP

    A child is running up a staircase with N steps and can hop either 1 step, 2 steps, or 3 steps at a time.
    Implement a method to count the number of ways a child can run up the staircase.
"""

# NOTE: because it's 1 OR 2 OR 3, you add, if it was something AND something, then you would multiply.


# SUPER SLOW, DON'T USE ME
def recursive_number_of_steps(n):
    if n is 1 or n is 2:
        return n
    if n is 3:
        return 4
    return recursive_number_of_steps(n - 1) + recursive_number_of_steps(n - 2) + recursive_number_of_steps(n - 3)


# This uses DYNAMIC PROGRAMMING w MEMOIZATION to be super fast!!!
def number_of_steps(n):
    l = [None] * (n + 1)
    return number_of_steps_memo(n, l)


def number_of_steps_memo(n, l):
    if n is 1 or n is 2:
        return n
    if n is 3:
        return 4
    if l[n] is None:
        l[n] = number_of_steps_memo(n - 1, l) + number_of_steps_memo(n - 2, l) + number_of_steps_memo(n - 3, l)
    return l[n]





