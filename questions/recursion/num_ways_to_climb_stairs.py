"""
    NUMBER OF WAYS TO CLIMB STAIRS (EPI 17.10: COUNT THE NUMBER OF MOVES TO CLIMB STAIRS)

    Write a program, which accepts the number of stairs (n) in a stairwell and the maximum number of stairs a person may
    be able to advance at a time (k), and computes (then returns) the number of ways said person can climb to the top of
    the (n) stairs.

    Example:
        Input = 4, 2    # n, k
        Output = 5      # or these combinations of steps [1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]
"""

# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Input Validation?
#   - Clarify and verify assumptions about the question (order matters, output formatting, etc.)?


# NOTE: IF there is ONE variable (with a few extra rules) then it MAY be easier to write down concrete examples first
# then try to deduce the relation.  However, when there is more than one variable, expand the function FIRST and try
# to find the recurrence relation, THEN try real examples.
#
# First find a recurrence:
#   f(n,k) = f(n-1,k) + f(n-2,k) + ... + f(n-(k-1),k) + f(n-k,k)
#   f(n,k) = Σ(n-i,k), for i=1 to k.
#
# Then test the recurrence:
#   f(4,2) = f(4-1,2) + f(4-2,2) = f(3,2) + f(2,2) = 3 + 2
#   f(3,2) = f(3-1,2) + f(3-2,2) = f(2,2) + f(1,2) = 2 + 1
#   f(2,2) = f(2-1,2) + f(2-2,2) = f(1,2) + f(0,2) = 1 + 1
#   f(1,2) = 1
#   f(0,2) = 1


# APPROACH: Recursive
#
# This is a plain recursive approach, which for each value of k that is less than or equal to the number of remaining
# stairs, recursively collates then returns the results (of the recursive call).
#
# Time Complexity: O(n ** k).
# Space Complexity: O(n).
def num_ways_to_climb_stairs_rec(n, k):
    if n is not None and k is not None and n >= 0 and k > 0:
        if n == 0 or n == 1:
            return 1
        res = 0
        for i in range(1, k + 1):
            if n - i >= 0:
                res += num_ways_to_climb_stairs_rec(n - i, k)
        return res
    return 0


# APPROACH: Memoization/Top Down Dynamic Programming
#
# This approach has the same logic as the recursive approach above, however, a memoization cache has been added to
# eliminate duplicate (recursive) calls.  The recursive function now checks whether the cache contains the initial value
# or computed result for the the current stair count.  If the result exists, then it is simply returned, if not, then
# the recursive call is executed and the value is updated.
#
# Time complexity is O(n * k).
# Space complexity is O(n).
def num_ways_to_climb_stairs_memo(n, k):

    def _num_ways_to_climb_stairs_memo(n, k, memo):
        if n == 0 or n == 1:
            return 1
        if memo[n] == 0:
            for i in range(1, k+1):
                if n - i >= 0:
                    memo[n] += _num_ways_to_climb_stairs_memo(n-i, k, memo)
        return memo[n]

    if n is not None and k is not None and n >= 0 and k > 0:
        memo = [0] * (n + 1)
        return _num_ways_to_climb_stairs_memo(n, k, memo)
    return 0


# APPROACH: Tabulation/Bottom Up Dynamic Programming
#
# This approach has the same logic as the recursive approach above, however, a memoization cache has been added to
# eliminate duplicate (recursive) calls.  The recursive function now checks whether the cache contains the initial value
# or computed result for the the current stair count.  If the result exists, then it is simply returned, if not, then
# the recursive call is executed and the value is updated.
#
# Time complexity is O(n * k).
# Space complexity is O(n).
def num_ways_to_climb_stairs_tab(n, k):
    if n is not None and k is not None and n >= 0 and k > 0:
        memo = [0] * (n + 1)
        memo[1] = 1
        for i in range(2, n + 1):               # For each stair in the staircase:
            for j in range(1, k + 1):               # for each number of possible steps:
                if i - j >= 0:                          # Is current stair step within k steps from a prev stair step?
                    memo[i] += memo[i - j]                  # Add prev num ways (to prev step) to this step.
                    if i == j:                          # If the current stair step is within stepping range (<= k):
                        memo[i] += 1                        # Add one (this is essentially the base case).
        return memo[n]
    return 0


args = [(4, 0),
        (4, 1),
        (4, 2),
        (4, 3),
        (4, 4),
        (10, 1),
        (10, 2),
        (10, 3),
        (10, 4),
        (10, 5),
        (10, -2),
        (-10, 2),
        (None, 2),
        (10, None)]
fns = [num_ways_to_climb_stairs_rec,
       num_ways_to_climb_stairs_memo,
       num_ways_to_climb_stairs_tab]

for n, k in args:
    for fn in fns:
        print(f"{fn.__name__}({n}, {k}): {fn(n, k)}")
    print()


