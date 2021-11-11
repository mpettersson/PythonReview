"""
    FIND MAX SCORE POPPED BALLOONS (leetcode.com/problems/burst-balloons/)

    The balloon game is a single player game consisting of an ordered series of balloons, where each balloon has a
    discrete and positive point value.  The objective of the game is to remove all of the targets via popping balloons,
    while maximizing points.  Points are accumulated with each balloon pop, where the number of points gained is equal
    to the product of the targeted balloon and the targets neighbor's value, if the target has neighbors.  After a pop,
    the target is gone, however, the neighbors remain.

    Write a function to find the maximum possible balloon game score for a given target list (of positive integers).

    Example:
        Input = [3, 1, 5, 8]
        Output = 167  # Where the order was 1, then 5, then 3, then 8, or 3*1*5 + 3*5*8 * 3*8 * 8

    Variations:
        - Matrix Chain Multiplication (matrix_chain_multiplication.py)
        - Same question, however, the values may be negative.
        - Same question, however, also provide the order of the balloons to be popped for the (returned) max score.
"""
import copy
import functools
import time


# APPROACH: Plain Recursion
#
# This is the plain vanilla recursive approach; for each index of the list, calculate the points
# gained if the balloon at the index was popped PLUS the recursive result of a new list without the value at the index.
#
# Time Complexity: O(n!), where n is the length of the list (SEE NOTE below).
# Space Complexity: O(n**2), where n is the length of the list (due to slicing; could be improved to O(n) w/o slicing).
#
# NOTE: The actual time complexity of this approach is defined with the recurrence relation: T(n) = (n * T(n-1)) + n;
#       this is, by far, the slowest approach...
def find_max_score_rec(l):
    result = min(l) if l else 0
    if l:
        for i in range(len(l)):
            curr_points = l[i]
            if i > 0:
                curr_points *= l[i - 1]
            if i + 1 < len(l):
                curr_points *= l[i + 1]
            result = max(curr_points + find_max_score_rec(l[:i] + l[i+1:]), result)
    return result


# OBSERVATIONS:
# To be able to optimize the solutions runtime, we must be able to cache the intermediate results; a natural way to do
# this is via referencing the indices of the list.
# Padding the list (with a 1 at the beginning and end) may, or may not, help.


# APPROACH: Top Down Dynamic Programming With Memoization
#
# This approach is essentially an optimized version of the plain recursion approach above; it calculates the cost of
# each possible pop combination via recursion.  The difference (compared to the plain recursive solution above) is that
# this approach uses a cache to store the results of computations, thus eliminating redundant calculations.
#
# Time Complexity: O(.5 * n * n**2), which reduces to O(n**3), where n is the length of the list.
# Space Complexity: O(n**2), where n is the length of the list.
def find_max_score_top_down(l):

    def _find_max_score_top_down(i, j):         # Start/End Indices
        if cache[i][j] or j == i + 1:           # Value In Cache OR No Balloon In Start End Range
            return cache[i][j]
        result = 0
        for k in range(i+1, j):                 # Index To Pop
            result = max(result, l[i] * l[k] * l[j] + _find_max_score_top_down(i, k) + _find_max_score_top_down(k, j))
        cache[i][j] = result
        return result

    if l is not None and len(l) > 0:
        l = [1] + l + [1]
        cache = [[0] * len(l) for _ in range(len(l))]
        return _find_max_score_top_down(0, len(l)-1)
    return 0


# APPROACH: Top Down Dynamic Programming With Memoization Via LRU Cache
#
# This is also an optimized recursive approach; here, functools' lru cache is used inplace of a 2D memoization list.
#
# Time Complexity: O(.5 * n * n**2), which reduces to O(n**3), where n is the length of the list.
# Space Complexity: O(n**2), where n is the length of the list.
def find_max_score_lru_cache(l):

    @functools.lru_cache(None)
    def _rec(i, j):
        return max([l[i] * l[k] * l[j] + _rec(i, k) + _rec(k, j) for k in range(i+1, j)] or [0])

    if l is not None and len(l) > 0:
        l = [1] + l + [1]
        return _rec(0, len(l) - 1)
    return 0


# APPROACH: Tabulation/Bottom Up Dynamic Programming With Memoization
#
# This approach also builds a memoization table of the optimal (max) points, however, since it is 'bottom up' it starts
# by finding the best value for two popped balloons, and iteratively increases until ending will all balloons popped
# (and the max score).
#
# Time Complexity: O(.5 * n * n**2), which reduces to O(n**3), where n is the length of the list.
# Space Complexity: O(n**2), where n is the length of the list.
def find_max_score_bottom_up_no_pad(l):
    result = 0
    if l is not None and len(l) > 0:
        memo = [[0] * len(l) for _ in range(len(l))]
        for num_to_pop in range(1, len(l) + 1):                     # Number Of Balloons To Pop (This Loop)
            for i in range(len(l) - num_to_pop + 1):                # Start Index (Inclusive)
                j = i + num_to_pop - 1                              # End Index (Inclusive)
                for k in range(i, j+1):                             # Index To Pop
                    left_val = l[i - 1] if i != 0 else 1
                    right_val = l[j + 1] if j != len(l) - 1 else 1
                    left_sum = memo[i][k-1] if i != k else 0       # The points for anything popped on the left.
                    right_sum = memo[k+1][j] if j != k else 0      # The points for anything popped on the right.
                    memo[i][j] = max(left_val * l[k] * right_val + left_sum + right_sum, memo[i][j])
        result = memo[0][-1]
    return result


# APPROACH: Tabulation/Bottom Up Dynamic Programming With (Padded) Memoization Approach
#
# This is similar to the above bottom up dynamic programming approach, with the exception that this approach pads the
# provided list with a 1 at the front and rear so that additional index checks are not required.
#
# Time Complexity: O(.5 * n * n**2), which reduces to O(n**3), where n is the length of the list.
# Space Complexity: O(n**2), where n is the length of the list.
#
# NOTE: This is the fastest approach (out of these approaches) for large lists.
def find_max_score_bottom_up(l):
    result = 0
    if l is not None and len(l) > 0:
        l = [1] + l + [1]                       # Padding with a 1 will not change the score, but will simplify the code
        n = len(l)
        cache = [[0] * n for _ in range(n)]
        for num_to_pop in range(2, n):          # Number Of Balloons To Pop (This Loop)
            for i in range(n - num_to_pop):     # Start Index (Exclusive)
                j = i + num_to_pop              # End Index (Exclusive)
                for k in range(i+1, j):         # Index To Pop
                    # print(f"diff: {num_to_pop}, i: {i}, j: {j}, k: {k}")
                    cache[i][j] = max(cache[i][j], l[i] * l[k] * l[j] + cache[i][k] + cache[k][j])
        result = cache[0][n - 1]
    return result


args = [[3, 1, 5, 8],
        [2, 7, 9, 3, 1],
        [7, 9, 8, 0, 7, 1, 3, 5, 5, 2],
        [955, 912, 660, 753, 924, 754, 748, 40, 445, 714],
        [1, 2],
        [2],
        [0],
        [],
        None]
alt_args = [[3, 1, -5, 8],
            [3, -1, 5, 8],
            [-3, -1, -5, -8],
            [904, 40, 523, 12, 0, -385, -124, 481, -31],
            [-2, 1, -3, 4, -1, 2, 1, -5, 4],
            [-2]]
fns = [find_max_score_rec,
       find_max_score_top_down,
       find_max_score_lru_cache,
       find_max_score_bottom_up_no_pad,
       find_max_score_bottom_up]

for l in args:
    print(f"l: {l}")
    for fn in fns:
        print(f"{fn.__name__}(l): {fn(copy.copy(l))}")
    print()

for l in args:
    for fn in fns:
        t = time.time()
        print(f"{fn.__name__}({l}): {fn(copy.copy(l))}, took ", end="")
        print(time.time() - t)
    print()


