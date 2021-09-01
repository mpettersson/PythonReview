"""
    FIND LONGEST COMMON SUBSTRING (50CIQ 47: LONGEST COMMON SUBSTRING)

    Write a function, which when given two strings, returns the longest common substring of the two arguments.

    Example:
        Input = "ABAB", "BABA"
        Output = "ABA"
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What type of characters will there be?
#   - Should lower case match with upper case?
#   - What are the estimated lengths of the strings?


# APPROACH: Naive/Brute Force Iterative (3 Pointers)
#
# Using three pointers; an index for string a, an index for string b, and a delta (offset) between the two.  Whenever
# the pointers have the same character values in the two words, the delta pointer/counter will be incremented as far as
# possible.  Initially, set the result to an empty string, when a match occurs (and after the maximum delta value has
# been found), update the result with the longest common substring.  Finally, return the result.
#
# Time Complexity: O(m * n * min(m, n)), where n and m are the lengths of the strings.
# Space Complexity: O(l), where l is the length of the longest common substring.
def find_longest_common_substring_naive(a, b):
    if isinstance(a, str) and isinstance(b, str):
        result = ""
        for i in range(len(a)):
            for j in range(len(b)):
                if a[i] == b[j]:
                    delta = 1
                    while i + delta < len(a) and j + delta < len(b) and a[i + delta] == b[j + delta]:
                        delta += 1
                    if delta > len(result):
                        result = a[i:i+delta]
        return result


# APPROACH: Memoization/Dynamic Programming (Via 2D List)
#
# Use a cache to record the (previous) matches, adding one to the previous match (cache[r-1][c-1]) if the current
# characters (at a[c] and b[r]) match.
#
# Consider the following states of the cache, when a is "ABAB" and b is "BABA", after each iteration of the main loop:
#
#   After i = 0:                After i = 1:                After i = 2:                After i = 3:
#          A  B  A  B                  A  B  A  B                  A  B  A  B                  A  B  A  B
#       B[[0, 1, 0, 1],             B[[0, 1, 0, 1],             B[[0, 1, 0, 1],             B[[0, 1, 0, 1],
#       A [0, 0, 0, 0],             A [1, 0, 2, 0],             A [1, 0, 2, 0],             A [1, 0, 2, 0],
#       B [0, 0, 0, 0],             B [0, 0, 0, 0],             B [0, 2, 0, 3],             B [0, 2, 0, 3],
#       A [0, 0, 0, 0]]             A [0, 0, 0, 0]]             A [0, 0, 0, 0]]             A [1, 0, 3, 0]]
#
# Time Complexity: O(m * n), where n and m are the lengths of the strings.
# Space Complexity: O(n * m), where n and m are the lengths of the strings.
def find_longest_common_substring_memo(a, b):
    if isinstance(a, str) and isinstance(b, str):
        result = ""
        if len(a) > 0 and len(b) > 0:
            memo = [[0 for _ in range(len(a))] for _ in range(len(b))]
            for r in range(len(b)):
                for c in range(len(a)):
                    if a[c] == b[r]:                                    # If there is a match:
                        if r == 0 or c == 0:                                # If it involves first row or col:
                            memo[r][c] = 1                                      # Then num matched can only be 1.
                        else:                                               # Else:
                            memo[r][c] = memo[r-1][c-1] + 1                     # Add one to the previous matched count.
                        if memo[r][c] > len(result):                       # If new matched len is longer than result:
                            result = a[c - memo[r][c] + 1: c+1]                 # Update result.
        return result


# APPROACH: Space Optimized Memoization/Dynamic Programming (Via 2 1D Lists)
#
# This is the same approach as as the Memoization/Dynamic Programming approach above, however, two 1D lists (prev and
# curr) have been used in place of the 2D matrix (memo) to minimize the space usage.
#
# Time Complexity: O(m * n), where n and m are the lengths of the strings.
# Space Complexity: O(min(m, n)), where n and m are the lengths of the strings.
def find_longest_common_substring(a, b):
    if isinstance(a, str) and isinstance(b, str):
        result = ""
        if len(a) > 0 and len(b) > 0:
            if len(a) > len(b):                         # Ensure 'a' is the shorter string (to save space).
                a, b = b, a
            prev = [0 for _ in range(len(a))]           # This holds the previous match counts.
            for r in range(len(b)):                     # For each char in 'b' (the longer string).
                curr = [0 for _ in range(len(a))]           # This hold the current match counts.
                for c in range(len(a)):                     # for each char in 'a' (the shorter string).
                    if a[c] == b[r]:                            # If current chars match:
                        if r == 0 or c == 0:                        # If it involves first row or col:
                            curr[c] = 1                                 # Then num matched can only be 1.
                        else:                                       # Else (or, it's not on the first row or col):
                            curr[c] = prev[c-1] + 1                     # Add one to the previous matched count.
                        if curr[c] > len(result):                   # Update result if needed.
                            result = a[c - curr[c] + 1: c+1]
                prev = curr
        return result


args = [('ABAB', 'BABA'),
        ('creative', 'reactive'),
        ('race', 'acre'),
        ('10101', '1001'),
        ('aabcccccaaa', 'caabccccccaaab'),
        ('abc', ''),
        ('', 'abc'),
        ('abc', None),
        (None, 'abc'),
        (None, None)]
fns = [find_longest_common_substring_naive,
       find_longest_common_substring_memo,
       find_longest_common_substring]

for a, b in args:
    for fn in fns:
        print(f"{fn.__name__}({a!r}, {b!r}): {fn(a, b)!r}")
    print()


