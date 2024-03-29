"""
    FIND LONGEST COMMON SUBSEQUENCE (leetcode.com/problems/longest-common-subsequence,
                                     leetcode.com/problems/maximum-length-of-repeated-subarray)

    Write a function, which when given two strings, returns the length of the longest common subsequence (of the two
    arguments). Where a subsequence of a string is a new string generated from the original string, with zero or more
    characters removed and the same relative order (of the remaining characters).

    Example:
        Input = "ABAB", "BABA"
        Output = 3
"""
import functools


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What type of characters will there be?
#   - Should lower case match with upper case?
#   - What are the estimated lengths of the strings?


# APPROACH: Naive/Plain Recursive
#
# When matching characters in two strings, there are only three cases:
#       1: There are not two things to compare (or the counter is past the end of one/both strings).  Return 0.
#       2: The current characters match.  Return 1 plus the result of recursion (incrementing BOTH pointers).
#       3: The current characters don't match. Return the BEST result from the two recursive possibilities:
#           a) Recurse with the FIRST words pointer incremented.
#           b) Recurse with the SECOND words pointer incremented.
#
# Consider the recursive structure for the example above:
#                                      lcs('ABAB', 'BABA')
#                                     /                   \
#                      lcs('BAB', 'BABA')                   lcs('ABAB', 'ABA')
#                     /                 \                   /                 \
#           lcs('AB', 'BABA')    lcs('BAB', 'ABA')  lcs('BAB', 'ABA')    lcs('ABAB', 'BA')
#              /        \           /        \         /        \            /        \
#  lcs('B', 'BABA')     ...       ...        ...     ...        ...         ...   lcs('ABAB', 'A')
#
# Recursively check each i and j index of the a and b strings with the following cases:  If i or j are greater than the
# length of their respective string, return zero.  If the characters in a and b (at i and j respectively) are equal,
# then return one plus the recursive result of incrementing i and j.  Finally, if the characters at a (index i) and b
# (index j) are not equal, then return the maximum of a recursive call with i incremented and a recursive call with j
# incremented.
#
# Time Complexity: O(2 ** max(m * n)), where m and n are the lengths of strings a and b.
# Space Complexity: O(max(m, n)), where m and n are the lengths of strings a and b.
def len_longest_common_subsequence_rec(a, b):

    def _rec(a, b, i, j):
        if i >= len(a) or j >= len(b):                              # Base Case:
            return 0                                                    # Return 0
        if a[i] == b[j]:                                            # Case 1: Current characters match.
            return 1 + _rec(a, b, i + 1, j + 1)                         # Return: 1 + rec result (i++ AND j++).
        else:                                                       # Case 2:
            return max(_rec(a, b, i + 1, j), _rec(a, b, i, j + 1))      # Return max of rec results (i++ OR j++).

    if isinstance(a, str) and isinstance(b, str):
        return _rec(a, b, 0, 0)


# APPROACH: Via LRU Cache
#
# This approach is almost exactly like the plain recursive approach above, however, an unbounded lru cache is used (via
# the decorator) for memoization, or caching, the calls.
#
# Time Complexity: O(m * n), where n and m are the lengths of the strings.
# Space Complexity: O(m * n), where n and m are the lengths of the strings.
def len_longest_common_subsequence_lru(a, b):

    @functools.lru_cache(None)
    def _rec(i, j):
        if i < 0 or j < 0:
            return 0
        if a[i] == b[j]:
            return _rec(i-1, j-1) + 1
        return max(_rec(i-1, j), _rec(i, j-1))

    if isinstance(a, str) and isinstance(b, str):
        return _rec(len(a)-1, len(b)-1)


# APPROACH: Dynamic Programming (Full 2D Matrix)
#
#   Let string 'a' be "XMJYAUZ" and string 'b' be "MZJAWXU" (with the longest common subsequence of a and b is "MJAU").
#   Then the (completed) memoization table will be as follows:
#
#            0       1       2       3       4       5       6       7
#                    M       Z       J       A       W       X       U
#       0  [[0,      0,      0,      0,      0,      0,      0,      0],
#       1 X [0,      0,      0,      0,      0,      0,      1,      1],
#       2 M [0,      1,      1,      1,      1,      1,      1,      1],
#       3 J [0,      1,      1,      2,      2,      2,      2,      2],
#       4 Y [0,      1,      1,      2,      2,      2,      2,      2],
#       5 A [0,      1,      1,      2,      3,      3,      3,      3],
#       6 U [0,      1,      1,      2,      3,      3,      3,      4],
#       7 Z [0,      1,      2,      2,      3,      3,      3,      4]]
#
# The value at memo[r][c] is:
#       1 + memo[r-1][c-1] if the characters match, else:
#       max(memo[r-1][c], memo[r][c-1]))
#
# The following table shows how one could build the LCS, working backwards from the memoization table.
#
#            0       1       2       3       4       5       6       7
#                    M       Z       J       A       W       X       U
#     0  [['',      '',     '',     '',     '',     '',     '',     ''],
#     1 X ['',      '',     '',     '',     '',     '',    'X',    'X'],
#     2 M ['',     "M",    'M',    'M',    'M',    'M',    'M',    'M'],
#     3 J ['',     'M',    'M',   "MJ",   'MJ',   'MJ',   'MJ',   'MJ'],
#     4 Y ['',     'M',    'M',   'MJ',   'MJ',   'MJ',   'MJ',   'MJ'],
#     5 A ['',     'M',    'M',   'MJ',  "MJA",  'MJA',  'MJA',  'MJA'],
#     6 U ['',     'M',    'M',   'MJ',  'MJA',  'MJA',  'MJA', "MJAU"],
#     7 Z ['',     'M',   'MZ',   'MZ',  'MJA',  'MJA',  'MJA', 'MJAU']]
#
# Alternatively, this can be seen as:
#
#          0  1  2  3  4  5  6  7                    0  1  2  3  4  5  6  7
#             M  Z  J  A  W  X  U                       M  Z  J  A  W  X  U
#     0  [[0, 0, 0, 0, 0, 0, 0, 0],             0  [[                      ],
#     1 X [0, 0, 0, 0, 0, 0, 1, 1],             1 X [                1(X)  ],
#     2 M [0, 1, 1, 1, 1, 1, 1, 1],             2 M [   1(M)               ],
#     3 J [0, 1, 1, 2, 2, 2, 2, 2],             3 J [         2(MJ)        ],
#     4 Y [0, 1, 1, 2, 2, 2, 2, 2],             4 Y [                      ],
#     5 A [0, 1, 1, 2, 3, 3, 3, 3],             5 A [             3(MJA)   ],
#     6 U [0, 1, 1, 2, 3, 3, 3, 4],             6 U [                     4(MJAU)],
#     7 Z [0, 1, 2, 2, 3, 3, 3, 4]]             7 Z [   2(MZ)              ]]
#
# Time Complexity: O(m * n), where n and m are the lengths of the strings.
# Space Complexity: O(m * n), where n and m are the lengths of the strings.
def len_longest_common_subsequence_memo(a, b):
    if isinstance(a, str) and isinstance(b, str):
        dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
        for r, char_in_a in enumerate(a):
            for c, char_in_b in enumerate(b):
                dp[r + 1][c + 1] = 1 + dp[r][c] if char_in_a == char_in_b else max(dp[r][c + 1], dp[r + 1][c])
        return dp[-1][-1]


# APPROACH: Space Optimized Dynamic Programming (List)
#
# This approach uses the same dynamic programming process as the approach above, however, this approach optimizes the
# space used by (first) finding the minimum length string and (second) only using two 1D lists (as opposed to a full 2D
# matrix).  At the beginning of each iteration, a new current list (with length equal to the shorter word plus one) is
# created and (during the loop) is populated according to the character matches and previous list; then at the end (of
# the loop) the current list becomes the previous list.
#
# Time Complexity: O(m * n), where n and m are the lengths of the strings.
# Space Complexity: O(min(m, n)), where n and m are the lengths of the strings.
def len_longest_common_subsequence(a, b):
    if isinstance(a, str) and isinstance(b, str):
        if len(a) < len(b):                         # b should be sorter for best space complexity.
            a, b = b, a
        prev = [0] * (len(b) + 1)                   # Memoization (1D) list.
        for r, char_in_a in enumerate(a):
            curr = [0] * (len(b) + 1)                   # Create new curr memo list.
            for c, char_in_b in enumerate(b):
                if char_in_a == char_in_b:                  # Case 1 (chars match): Increment last match.
                    curr[c + 1] = 1 + prev[c]                   # (Or, 1 + memo[r-1][c-1], if 2D matrix.)
                else:                                       # Case 2 (no match): Use greatest seen match.
                    curr[c + 1] = max(prev[c + 1], curr[c])     # (Or, max(memo[r-1][c], memo[r][c-1])) if 2D matrix.)
            prev = curr                                 # After each iteration, prev is updated (to be curr).
        return curr[-1]


args = [('ABAB', 'BABA'),
        ('creative', 'reactive'),
        ('race', 'acre'),
        ('10101', '1001'),
        ('aabcccccaaa', 'caabccccccaaab'),
        ('abcd', 'efgh'),
        ('abc', ''),
        ('', 'abc'),
        ('abc', None),
        (None, 'abc'),
        (None, None)]
fns = [len_longest_common_subsequence_rec,
       len_longest_common_subsequence_lru,
       len_longest_common_subsequence_memo,
       len_longest_common_subsequence]

for a, b in args:
    for fn in fns:
        print(f"{fn.__name__}({a!r}, {b!r}): {fn(a, b)!r}")
    print()


