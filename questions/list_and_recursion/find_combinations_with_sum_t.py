"""
    FIND COMBINATIONS WITH SUM T (leetcode.com/problems/combination-sum)

    Write a function, which when given a list l of distinct integers candidates and a target sum t, returns a list
    of unique combinations (of candidates), with a sum of t.  Candidates may be used multiple times in each (sub) list.

    Example:
        Input = [2, 3, 6, 7], 7
        Output = [[2, 2, 3], [7]]
"""
import time


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Verify combinations (not permutations).
#   - Are there duplicate values in the list?
#   - Are duplicates allowed in the results lists?
#   - What is the possible length of the list?
#   - What are the possible values (for both the list and the target)?
#   - What order should the results list be in?


# NOTE: W.R.T. this question, is VERY IMPORTANT to ask about NEGATIVE NUMBERS!  Since there is no given list size
#       constraint AND since duplicates ARE allowed, IF there were negative numbers then there could be infinite lists
#       (i.e., consider the input [-1, 1], 1).


# APPROACH: TODO
#
# TODO
#
# Time Complexity: O(n * (t ** 2)), where n is the length of the list.
# Space Complexity: O(M*M)
def find_combinations_with_sum_t_dp(l, t):
    dp = [[] for _ in range(t+1)]
    for c in l:                                     # O(n): for each candidate
        for i in range(c, t+1):                     # O(t): for each possible value <= target
            if i == c:
                dp[i].append([c])
            for comb in dp[i-c]:
                dp[i].append(comb + [c])            # O(t) worst: for each combination
    return dp[-1]


# APPROACH: DFS/Backtracking
#
# TODO
#
# Time Complexity: TODO
# Space Complexity: TODO
def find_combinations_with_sum_t(l, t):

    def _rec(i, rem):
        if rem == 0:
            result.append(accumulator[:])
        elif i < len(l):
            for j in range(i, len(l)):
                if l[j] <= rem:
                    accumulator.append(l[j])
                    _rec(j, rem - l[j])
                    accumulator.pop()

    result = []
    accumulator = []
    _rec(0, t)
    return result


args = [
        ([2, 3, 6, 7], 7),
        ([10, 1, 2, 7, 6, 5], 8),
        ([7, 6, 2, 3], 7),
        ([7, 2, 3, 6], 7),
        ([2, 3, 5], 8),
        ([2], 1),
        ([1], 1),
        # ([1], 500),
        # ([2, 3, 4, 6], 88),
        # ([11, 2, 5, 7, 3], 120)
]
fns = [find_combinations_with_sum_t_dp,
       find_combinations_with_sum_t]

for l, total in args:
    print(f"\nl: {l}\ntotal: {total}")
    for fn in fns:
        print(f"{fn.__name__}(l): {fn(l[:], total)}")
    print()

l = [28, 145, 85, 59, 155, 67, 20, 153, 183, 161, 80, 148, 158, 83, 162, 35, 49, 175, 117, 133, 1, 63, 136, 157, 87,
     193, 188, 39, 166, 2]
t = 500
print(f"\nl: {l}\ntotal: {total}")
for fn in fns:
    t = time.time()
    print(f"{fn.__name__}(l) took ", end='')
    fn(l[:], total)
    print(f"{time.time() - t} seconds.")
print()


