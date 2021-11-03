"""
    FIND LONGEST PALINDROME SUBSTRINGS (leetcode.com/problems/longest-palindromic-subsequence)

    Write a function, which when given two strings, returns the longest common substring of the two arguments.

    Example:
        Input = "ABAB", "BABA"
        Output = "ABA"
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What are the possible characters?
#   - Should lower case match with upper case?
#   - What are the possible string lengths (empty string)?
#   - What about duplicate palindromes in the list?


# APPROACH: Naive/Brute Force
#
# For each possible substring start and end index, check if the substring is a palindrome; if it is and if it is longer
# than the result update the result with the newly found palindrome.  Once all comparisons have been completed, return
# the longest found palindrome.
#
# Time Complexity:  O(n**3), where n is the length of the string.
# Space Complexity: O(1).
def find_longest_palindromic_substring_naive(s):

    def _is_palindrome(s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    if isinstance(s, str):
        result = ""
        if len(s) > 0:
            for start in range(len(s)):
                for end in range(start, len(s)):
                    if end - start + 1 > len(result) and _is_palindrome(s, start, end):
                        result = s[start:end+1]
        return result


# APPROACH: (NOT Space Optimized) Dynamic Programming
#
# NOTE: For an interview, use the 'Expand Around Center' approach below, it has a better space complexity, is easier to
#       remember, and to explain. If you have a great memory, then possibly use 'Manacher's Algorithm' (also below).
#
# Use a NxN matrix of boolean values, where N is the length of the string, to represent if a substring (at
# string[row][column]) is a palindrome.  Start with all False values, inserting True values for each character.
# Then, via memoization, update continually larger palindrome substrings.  That is:
#
#       P(i, j) = { True,     if string[i:j+1] is a palindrome,
#                 { False,    otherwise.
# Therefore:
#       P(i, i) = True
#       P(i, i+1) = (string[i] == string[i+1])
#       P(i, j) = (P(i+1, j-1) and string[i] == string[j])
#
# The following is the cache (memo) result for the string 'babad':
#        True False  True False False
#       False  True False  True False
#       False False  True False False
#       False False False  True False
#       False False False False  True
#
# Time Complexity: O(n**2), where n is the length of the string.
# Space Complexity: O(n**2), where n is the length of the string.
def find_longest_palindromic_substring_dp_suboptimal(s):
    if isinstance(s, str):
        if len(s) == 0:
            return ""
        n = len(s)
        left = 0                                            # Longest palindrome substring START index.
        right = 0                                           # Longest palindrome substring END index.
        memo = [[False] * n for _ in range(n)]              # If memo[i][j] is True, then s[i:j+1] is a palindrome.
        memo[-1][-1] = True
        for i in range(n - 1):                              # For each index (excluding the last) of the string:
            memo[i][i] = True                               # The corresponding char (on memo's main diagonal) is True.
            if s[i] == s[i + 1]:                            # If the next character is the same:
                memo[i][i + 1] = True                       # Then both chars form a palindrome (update it's memo too).
                left, right = i, i + 1                      # Update the longest palindrome substring start/end indices.
        for m in range(2, n):                               # m = current length of palindromes
            for i in range(n-m):                            # i = substring start index.
                j = i + m                                   # j = Current substrings end index.
                memo[i][j] = memo[i+1][j-1] and s[i] == s[j]
                if memo[i][j] and j - i > right - left:
                    left, right = i, j
        return s[left:right + 1]


# APPROACH: Space Optimized Dynamic Programming
#
# NOTE: Attempting this solution in an interview is not recommended, it is more difficult to conceptualize and the
#       it sometimes hard to follow the even/odd logic.
#
# This dynamic programming approach uses two lists, as opposed to a full 2D matrix, as the first dynamic programming
# approach.
#
# Seriously, stop reading this and spend your time memorizing Manacher's alg (last approach), or the 'Expand Around
# Center' approach (next), this one isn't worth it...
#
# Time Complexity: O(n**2), where n is the length of the string.
# Space Complexity: O(n), where n is the length of the string.
def find_longest_palindromic_substring_dp(s):
    if isinstance(s, str):
        n = len(s)
        left = 0                                            # Longest palindrome substring START index.
        right = 0                                           # Longest palindrome substring END index.
        memo = [[True] * n, [False] * n]                    # memo[0]: Contains palindromes of ODD length!
        for i in range(n-1):                                # memo[1]: Contains palindromes of EVEN length!
            if s[i] == s[i+1]:                              # Two consecutive char.
                memo[1][i] = True                           # Update (EVEN) memo[1].
                left, right = i, i+1
        # NOTE: At this point, memo is initialized, True can only be replaced with False from now on... (no False->True)
        # print(f"memo[0] (odds): {memo[0]}\nmemo[1] (evens):{memo[1]}\n")
        for m in range(2, n):                               # For palindromes of length m:
            for i in range(n-m):                            # i = Current substring start index.
                j = i+m                                     # j = Current substrings end index (of length m).
                x = m % 2                                   # x = Memo row (0:ODD, 1:EVEN) for this iteration.
                k = i + m // 2                              # k = Middle index (Round Down!) between i and j.
                # print(f"m:{m}, i:{i}, j:{j}, x:{x}, k:{k}")
                memo[x][k] = memo[x][k] and s[i] == s[j]    # Update
                if memo[x][k] and j-i > right-left:
                    left, right = i, j
                    # print(f"longest palindrome substring so far: {s[left:right+1]}")
                # print(f"memo[0]: {memo[0]}\nmemo[1]:{memo[1]}\n")
        return s[left:right+1]


# APPROACH: Expand Around Center
#
# Leveraging the property that a palindrome mirrors around its center; iterate over each index of the string, as if it
# was the center of a palindrome.  At each of the 2n-1 candidate centers, expand outwards (in both directions) until the
# length of the palindrome (at the candidate center) is found.  Then compare the length to the result, updating if
# needed.  After all candidates have been considered, return the (longest) result.
#
# Time Complexity: O(n**2), where n is the length of the string.
# Space Complexity: O(1).
def find_longest_palindromic_substring(s):

    def _expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1                             # Return length of largest palindrome.

    if isinstance(s, str):
        if len(s) == 0:
            return ""
        start = end = 0
        for i in range(len(s)):
            len1 = _expand_around_center(s, i, i)           # Odd length palindrome
            len2 = _expand_around_center(s, i, i + 1)       # Even length palindrome
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start: end + 1]


# APPROACH: Manacher's Algorithm
#
# Since a palindrome can be an odd length (the center lands on a character) OR of an even length (the center is between)
# two characters, there are 2n-1 possible 'centers' that need to be check (in a string of length n).  To more easily
# check the possible 'centers' the algorithm first transforms the string into one with 'boundaries' between each of the
# characters and an additional character at the beginning and end (see examples below).  A memoization list (of sorts)
# is maintained, it is a list of palindromic span for each element in the transformed string from center to either
# outermost element, where each boundary is counted towards the length of a palindrome.  One iteration over the
# transformed string, with an 'expanding' loop on each index, then populates the (memoization) list.  Once the modified
# string has been iterated over, the index and length of the longest palindrome can be obtained from the list.
#
# Examples:
#       s_original = 'abababa'
#       s_transformed = '^#a#b#a#b#a#b#a#$'
#       list = [0, 0, 1, 0, 3, 0, 5, 0, 7, 0, 5, 0, 3, 0, 1, 0, 0]
#
#       s_original = 'acncacn'
#       s_transformed = '^#a#c#n#c#a#c#n#$'
#       list = [0, 0, 1, 0, 1, 0, 5, 0, 1, 0, 5, 0, 1, 0, 1, 0, 0]
#
#       s_original = 'babad'
#       s_transformed = '^#b#a#b#a#d#$'
#       list = [0, 0, 1, 0, 3, 0, 3, 0, 1, 0, 1, 0, 0]
#
# Time Complexity: O(n + n + n/2) which reduces to O(n), where n is the length of the string.
# Space Complexity: O(n), where n is the length of the string.
#
# SEE: wikipedia.org/wiki/Longest_palindromic_substring
def find_longest_palindromic_substring_manacher(s):
    if isinstance(s, str):
        t = '#'.join('^{}$'.format(s))                  # Transform s->t, i.e., "abba" -> "^#a#b#b#a#$".
        p = [0] * len(t)                                # p = a list of palindromic span for each element in t, from
        #                                                 center to either outermost element, where each boundary is
        #                                                 counted towards the length of a palindrome (e.g. a palindrome
        #                                                 that is three elements long has a palindromic span of 1)
        c = 0                                           # c is the position of the center of the palindrome currently
        #                                                 known to include a boundary closest to the right end of t.
        r = 0                                           # r = the idx of the right-most boundary of c's palindrome.
        for i in range(1, len(t) - 1):                  # i = idx of char/boundary in t whose span is being determined
            if i < r:
                p[i] = min(r - i, p[2 * c - i])
            while t[i + 1 + p[i]] == t[i - 1 - p[i]]:       # Attempt to expand palindrome centered at i.
                p[i] += 1
            if i + p[i] > r:                                # If palindrome centered at i is past r, adjust center:
                c, r = i, i + p[i]
        max_len, center_idx = max((n, i) for i, n in enumerate(p))
        return s[(center_idx - max_len) // 2: (center_idx + max_len) // 2]


# WRONG APPROACH: Find Longest Common Substring With Reversed String
#
# Reversing the string and then finding the longest common substring SEEMS like a good idea however, consider the
# following example:
#
#         a  a  c  a  b  d  k  a  c  a  a
#       +--------------------------------
#     a | 1  1  0  1  0  0  0  1  0  1  1
#     a | 1  2  0  1  0  0  0  1  0  1  2
#     c | 0  0  3  0  0  0  0  0  2  0  0
#     a | 1  1  0  4  0  0  0  1  0  3  1
#     k | 0  0  0  0  0  0  1  0  0  0  0
#     d | 0  0  0  0  0  1  0  0  0  0  0
#     b | 0  0  0  0  1  0  0  0  0  0  0
#     a | 1  1  0  1  0  0  0  1  0  1  1
#     c | 0  0  2  0  0  0  0  0  2  0  0
#     a | 1  1  0  3  0  0  0  1  0  3  1
#     a | 1  2  0  1  0  0  0  1  0  1  4
#
# The longest common substring for 'aacabdkacaa', as can be seen by the matrix (cache, or memoization table) above, is
# 'aaca', which is clearly NOT a palindrome.  Therefore, this approach fails when there exists a reversed copy of a
# non-palindromic substring a a different part of the string.
#
# Time Complexity: O(n**2), where n is the length of the string.
# Space Complexity: O(n**2), where n is the length of the string.
#
# NOTE: To fix the issue (as described above), for each candidate, simply check if the reversed substrings indices are
# the same as the original substrings indices.
def __wrong_find_longest_palindromic_substring_wrong__(s):
    if isinstance(s, str):
        result = ''
        if len(s) == 0:
            return result
        memo = [[0] * len(s) for _ in range(len(s))]
        curr_max = 0
        for ir, cr in enumerate(reversed(s)):
            for i, c in enumerate(s):
                if ir == 0 or i == 0:
                    if cr == c:
                        memo[ir][i] = 1
                else:
                    if cr == c:
                        memo[ir][i] = memo[ir - 1][i - 1] + 1
                if memo[ir][i] > curr_max:
                    curr_max = memo[ir][i]
                    result = s[i - curr_max + 1: i + 1]
    return result


string_list = ["abracadabra",
                "aaaa",
               "aacabdkacaa",
               "Tact Coa",
               "tacocat",
               "aacadbkacc",
                "abcdedcba",
               "babad",
               "rotator",
               "##hi",
               "^^hi",
               "^$hii",
               "$$hi",
               "level",
               "foo",
               "bar",
               "abca",
               "dqmvxouqesajlmksdawfenyaqtnnfhmqbdcniynwhuywucbjzqxhofdzvposbegkvqqrdehxzgikgtibimupumaetjknrjjuygxvncvjlahdbibatmlobctclgbmihiphshfpymgtmpeneldeygmzlpkwzouvwvqkunihmzzzrqodtepgtnljribmqneumbzusgppodmqdvxjhqwqcztcuoqlqenvuuvgxljcnwqfnvilgqrkibuehactsxphxkiwnubszjflvvuhyfwmkgkmlhmvhygncrtcttioxndbszxsyettklotadmudcybhamlcjhjpsmfvvchduxjngoajclmkxiugdtryzinivuuwlkejcgrscldgmwujfygqrximksecmfzathdytauogffxcmfjsczaxnfzvqmylujfevjwuwwaqwtcllrilyncmkjdztleictdebpkzcdilgdmzmvcllnmuwpqxqjmyoageisiaeknbwzxxezfbfejdfausfproowsyyberhiznfmrtzqtgjkyhutieyqgrzlcfvfvxawbcdaawbeqmzjrnbidnzuxfwnfiqspjtrszetubnjbznnjfjxfwtzhzejahravwmkakqsmuynklmeffangwicghckrcjwtusfpdyxxqqmfcxeurnsrmqyameuvouqspahkvouhsjqvimznbkvmtqqzpqzyqivsmznnyoauezmrgvproomvqiuzjolejptuwbdzwalfcmweqqmvdhejguwlmvkaydjrjkijtrkdezbipxoccicygmmibflxdeoxvudzeobyyrutbcydusjhmlwnfncahxgswxiupgxgvktwkdxumqp",
               "",
               None]
fns = [find_longest_palindromic_substring_naive,
       find_longest_palindromic_substring_dp_suboptimal,
       find_longest_palindromic_substring_dp,
       find_longest_palindromic_substring,
       find_longest_palindromic_substring_manacher]

for s in string_list:
    print(f"s: {s}")
    for fn in fns:
        print(f"{fn.__name__}(s): {fn(s)!r}")
    print()


