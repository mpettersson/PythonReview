"""
    LEN LONGEST PALINDROME SUBSEQUENCE (leetcode.com/problems/longest-palindromic-subsequence)

    Write a function, which when given one string s, returns the length of the longest palindromic subsequence.

    A subsequence is a sequence that can be derived from another sequence by deleting 0 or more elements without
    changing the order of the remaining elements.

    Example:
        Input = 'abracadabra'
        Output = 7  # either 'abaaaba' or 'araaara'
"""
import time


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What are the possible characters?
#   - Should lower case match with upper case?
#   - What are the possible string lengths (empty string)?


# APPROACH: Brute Force (NOT IMPLEMENTED)
#
# This approach iterates starting with i as length of the string, ending with i equal to 1.  For each iteration, all
# combinations of length i of the string tested as a palindrome.  When the first palindrome is encountered, the length
# of the string is returned.
#
# Time Complexity:  O(n!), where n is the size of the list.
# Space Complexity: Depends On Implementation.


# APPROACH: Naive Recursion
#
# Using two pointers one at either end of the string, recursively expand inward, comparing characters in the string,
# each time returning the maximum result of only three possibilities/cases.
#   1: There are not two things to compare (or the counter is past the end of one/both strings).  Return 0.
#   2: The current characters match.  Return 2 plus the result of recursion (incrementing BOTH pointers).
#   3: The current characters don't match. Return the BEST result from the two recursive possibilities:
#       a) Recurse with the FIRST words pointer incremented.
#       b) Recurse with the SECOND words pointer incremented.
#
# Time Complexity:  O(2**n), where n is the length of the string.
# Space Complexity: O(n), where n is the length of the string.
def len_longest_palindromic_subsequence_naive(s):

    def _rec(s, lo, hi):
        if lo > hi:                             # Base Case: Pointers have crossed, return 0.
            return 0
        if lo == hi:                            # Base Case: A char is always a palindrome, of len 1, of itself.
            return 1
        if s[lo] == s[hi]:                      # Rec. Case: The two (different) chars at the pointers match;
            return 2 + _rec(s, lo+1, hi-1)          # add 2 to the result of the rec call on next pair of chars.
        return max(_rec(s, lo+1, hi),           # Rec. Case: (Pointers don't match) Return the best/max result of the
                   _rec(s, lo, hi-1))               # next two comparison options (increase low, or decrease high).

    if isinstance(s, str):
        n = len(s)
        if s == s[::-1]:                        # Easy Optimization: First check if the whole string is a palindrome.
            return n
        return _rec(s, 0, n-1)


# APPROACH: Memoization/Top Down Dynamic Programming
#
# This approach uses the same concept as the naive recursive approach above, with one simple optimization; the results
# of the recursive calls are caches to prevent duplicate computations/work.
#
# The following is a (top down) completed cache, or memoization, (dp) table for the string 'abracadabra'.
#
#               0     1     2     3     4     5     6     7     8     9    10
#               a     b     r     a     c     a     d     a     b     r     a
#     0  a [[None, None, None, None, None, None, None, None, None, None,    7], <-- Start and End at dp[0][-1].
#     1  b  [None, None, None, None, None, None, None, None,    5,    5, None],
#     2  r  [None, None, None,    1,    1,    3,    3,    3, None,    5, None],
#     3  a  [None, None, None, None,    1,    3,    3,    3,    3, None, None],
#     4  c  [None, None, None, None, None,    1,    1,    3,    3, None, None],
#     5  a  [None, None, None, None, None, None,    1,    3,    3, None, None],
#     6  d  [None, None, None, None, None, None, None,    1,    1, None, None],
#     7  a  [None, None, None, None, None, None, None, None,    1, None, None],
#     8  b  [None, None, None, None, None, None, None, None, None, None, None],
#     9  r  [None, None, None, None, None, None, None, None, None, None, None],
#    10  a  [None, None, None, None, None, None, None, None, None, None, None]]
#
# REMEMBER: Top Down doesn't always need to calculate ALL the values (unlike Bottom Up), only what is required for the
#           preceding calls.
#
# Time Complexity:  O(n**2), where n is the length of the string.
# Space Complexity: O(n**2), where n is the length of the string.
def len_longest_palindromic_subsequence_top_down(s):

    def _rec(s, dp, r, c):
        if r > c:                                       # Base Case: Pointers have crossed, return 0.
            return 0
        if r == c:                                      # Base Case: A char is always a palindrome, of len 1, of itself.
            return 1
        if dp[r][c] is None:                            # If the cache/memoization table is empty, do the calculation:
            if s[r] == s[c]:                                # Rec. Case: The 2 (different) chars at the pointers match;
                dp[r][c] = 2 + _rec(s, dp, r+1, c-1)            # add 2 to the res of the rec call on next pair of chars
            else:
                dp[r][c] = max(_rec(s, dp, r+1, c),         # Rec. Case: (Pointers don't match) Return the best/max res
                               _rec(s, dp, r, c-1))             # from (low+1, high) and (low, high-1) comparisons.
        return dp[r][c]                                 # Return the  cached value.

    if isinstance(s, str):
        n = len(s)
        if s == s[::-1]:                                # Easy Optimization: 1st check if the string is a palindrome.
            return n
        dp = [[None] * n for _ in range(n)]
        return _rec(s, dp, 0, len(s)-1)


# APPROACH: Tabulation/Bottom Up Dynamic Programming
#
# This iterative approach is based on the same concept as the recursive approaches above; it works on the three cases
# (as outlined above) and uses a cache, or memoization table, to store intermediate results.  However, being iterative
# this approach doesn't have a recursion stack, and therefore, must solve all comparisons/calculations to produce the
# result (where Top Down only computes any required, or referenced cases, leaving all others uncompleted).
#
# The following is a (bottom up) completed cache, or memoization, (dp) table for the string 'abracadabra'.
#
#            0  1  2  3  4  5  6  7  8  9  10
#            a  b  r  a  c  a  d  a  b  r  a
#     0  a [[1, 1, 1, 3, 3, 3, 3, 5, 5, 5, 7],  <-- End at dp[0][-1].
#     1  b  [0, 1, 1, 1, 1, 3, 3, 3, 5, 5, 5],
#     2  r  [0, 0, 1, 1, 1, 3, 3, 3, 3, 5, 5],
#     3  a  [0, 0, 0, 1, 1, 3, 3, 3, 3, 3, 5],
#     4  c  [0, 0, 0, 0, 1, 1, 1, 3, 3, 3, 3],
#     5  a  [0, 0, 0, 0, 0, 1, 1, 3, 3, 3, 3],
#     6  d  [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 3],
#     7  a  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 3],                  (etc...)
#     8  b  [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],              (Then at dp[-3][-3] and fill in it's row...)
#     9  r  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],          (Then start at dp[-2][-2] and fill in remainder of row.)
#    10  a  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]  <-- Start at dp[-1][-1].
#               (i = rows, j = columns)
#
#   Starting at the END (dp[-1][-1]) of the main diagonal, working towards the BEGINNING (dp[0][0]), fill in each row,
#   according to the following rules:
#       1: If the current characters match: Return 2 + dp[row+1][col-1].
#       2: The current characters don't match. Return the BEST/MAX from:
#           a) dp[row+1][col].
#           b) dp[row][col-1].
#
# Time Complexity:  O(n**2), where n is the length of the string.
# Space Complexity: O(n**2), where n is the length of the string.
def len_longest_palindromic_subsequence_bottom_up(s):
    if isinstance(s, str):
        n = len(s)
        if s == s[::-1]:                            # Easy Optimization: 1st check if the string is a palindrome.
            return n
        dp = [[0] * n for _ in range(n)]            # Construct an empty cache, or memoization, table.
        for i in range(n-1, -1, -1):                # For chars at i: (Reverse order will res in filled TOP of matrix).
            dp[i][i] = 1                                # Every character is a palindrome of length 1.
            for j in range(i + 1, n):                   # For comparison char at j: (will res in mat RIGHT side filled).
                if s[i] == s[j]:                            # If the 2 (different) chars at the pointers (i & j) match;
                    dp[i][j] = 2 + dp[i + 1][j - 1]             # Add 2 to res of the prev call (on next pair of chars)
                else:                                       # Else, use the best, or max result from dp[low+1, high] and
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])  # dp[low, high-1] (previous) comparisons.
        return dp[0][-1]                            # Return the length of the longest palindrome subsequence.


# APPROACH: Optimized Space Tabulation/Bottom Up Dynamic Programming
#
# This is the Tabulation/Bottom Up Dynamic Programming approach from above with a single optimization; two lists (of
# size n) are used in place of an nxn matrix.  Since only previous rows are referenced, a duplicate of the previous rows
# result can be saved (and updated each iteration) thus reducing the space complexity by n.
#
# NOTE: Since only TWO lists are being used, printing the cache/memoization list over time (to emulate a table) will
#       produce a HORIZONTALLY FLIPPED table.  Consider dp over i iterations, for the string 'abracadabra':
#
#       i=9: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
#       i=8: [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
#       i=7: [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
#       i=6: [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 3]
#       i=5: [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 3]
#       i=4: [0, 0, 0, 0, 0, 1, 1, 3, 3, 3, 3]
#       i=3: [0, 0, 0, 0, 1, 1, 1, 3, 3, 3, 3]
#       i=2: [0, 0, 0, 1, 1, 3, 3, 3, 3, 3, 5]
#       i=1: [0, 0, 1, 1, 1, 3, 3, 3, 3, 5, 5]
#       i=0: [0, 1, 1, 1, 1, 3, 3, 3, 5, 5, 5]
#
#     Final: [1, 1, 1, 3, 3, 3, 3, 5, 5, 5, 7]
#
# SEE: The Bottom Up Description (above) for more information.
#
# Time Complexity:  O(n**2), where n is the length of the string.
# Space Complexity: O(n), where n is the length of the string.
def len_longest_palindromic_subsequence(s):
    if isinstance(s, str):
        n = len(s)
        if s == s[::-1]:                        # Easy Optimization: 1st check if the string is a palindrome.
            return n
        dp = [0] * n                            # Construct an empty cache, or memoization, list.
        dp[-1] = 1                              # Initialize the base case.
        for i in range(n-2, -1, -1):            # For chars at i (start with n-2 bc 'dp[-1] = 1' handles n-1):
            prev = dp[:]                            # Create a copy of dp as a reference of the 'previous' row.
            dp[i] = 1                               # (Base Case) A char is always a palindrome, of len 1, of itself.
            for j in range(i+1, n):                 # For comparison char at j:
                if s[i] == s[j]:                        # If the 2 (different) chars at the pointers (i & j) match;
                    dp[j] = 2 + prev[j - 1]                 # Add 2 to the res of the prev call (on next pair of chars)
                else:                                   # Else, use the best, or max result from dp[low+1, high] and
                    dp[j] = max(prev[j], dp[j - 1])         # dp[low, high-1] (previous) comparisons.
        return dp[-1]                           # Return the length of the longest palindrome subsequence.


string_list = ['bbbab',
               'd',
               'abcddefg',
               'abracadabra',
               'aaaa',
               'aacabdkacaa',
               'Tact Coa',
               'tacocat',
               'aacadbkacc',
               'abcdedcba',
               'babad',
               'rotator',
               'level',
               'abca',
               '',
               None]
fns = [len_longest_palindromic_subsequence_naive,
       len_longest_palindromic_subsequence_top_down,
       len_longest_palindromic_subsequence_bottom_up,
       len_longest_palindromic_subsequence]

for s in string_list:
    print(f"s: {s!r}")
    for fn in fns:
        print(f"{fn.__name__}(s): {fn(s)!r}")
    print()

s = 'dqmvxouqesajlmksdawfenyaqtnnfhmqbdcniynwhuywucbjzqxhofdzvposbegkvqqrdehxzgikgtibimupumaetjknrjjuygxvncvjlahdbibatmlobctclgbmihiphshfpymgtmpeneldeygmzlpkwzouvwvqkunihmzzzrqodtepgtnljribmqneumbzusgppodmqdvxjhqwqcztcuoqlqenvuuvgxljcnwqfnvilgqrkibuehactsxphxkiwnubszjflvvuhyfwmkgkmlhmvhygncrtcttioxndbszxsyettklotadmudcybhamlcjhjpsmfvvchduxjngoajclmkxiugdtryzinivuuwlkejcgrscldgmwujfygqrximksecmfzathdytauogffxcmfjsczaxnfzvqmylujfevjwuwwaqwtcllrilyncmkjdztleictdebpkzcdilgdmzmvcllnmuwpqxqjmyoageisiaeknbwzxxezfbfejdfausfproowsyyberhiznfmrtzqtgjkyhutieyqgrzlcfvfvxawbcdaawbeqmzjrnbidnzuxfwnfiqspjtrszetubnjbznnjfjxfwtzhzejahravwmkakqsmuynklmeffangwicghckrcjwtusfpdyxxqqmfcxeurnsrmqyameuvouqspahkvouhsjqvimznbkvmtqqzpqzyqivsmznnyoauezmrgvproomvqiuzjolejptuwbdzwalfcmweqqmvdhejguwlmvkaydjrjkijtrkdezbipxoccicygmmibflxdeoxvudzeobyyrutbcydusjhmlwnfncahxgswxiupgxgvktwkdxumqp'
print(f"s: {s!r}")
for fn in fns[1:]:  # SKIPPING the naive approach, it takes too long...
    t = time.time()
    print(f"{fn.__name__}(s) took:", end=' ')
    result = fn(s)
    print(f"{time.time() - t} seconds.")
print()


