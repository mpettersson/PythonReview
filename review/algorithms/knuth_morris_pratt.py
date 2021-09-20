"""
    KNUTH MORRIS PRATT (String Search Via Pre-Computation/Lookup Table)

    Average Runtime:    O(m + n), where m is the length of the pattern and n is the length of the text.
    Worst Runtime:      O(m + n).  (When each window has a spurious, or false, match.)
    Best Runtime:       O(m + n), where m is the length of the pattern and n is the length of the text.
    Space Complexity:   O(max(m, n)), where m is the length of the pattern and n is the length of the text. If the first
                        occurrence was returned, or all occurrences were printed, then only O(m) space would be used.
    Alg Paradigm:       String Search

    NOTE: W.R.T. asymptotic times, this is the BEST we can do (we have to look at all characters once).

    The Knuth Morris Pratt (KMP) string search algorithm searches for occurrences of a pattern string within a main
    text (string) by employing the observation that when a mismatch occurs, the pattern itself contains sufficient
    information to determine where the next match could begin, thus bypassing re-examination of previously matched
    characters.

    The algorithm was conceived by James H. Morris and independently discovered by Donald Knuth. Morris and Vaughan
    Pratt published a technical report in 1970. The three also published the algorithm jointly in 1977.  Independently,
    in 1969, Matiyasevich discovered a similar algorithm, coded by a two-dimensional Turing machine, while studying a
    string-pattern-matching recognition problem over a binary alphabet. This was the first linear-time algorithm for
    string matching.

    References:
        - wikipedia.org/wiki/Knuth–Morris–Pratt_algorithm
        - youtu.be/EL4ZbRF587g
"""


# Partial Match Table (AKA Failure Function)
#
# This function builds the lookup table, which is used to 'shift' the pattern string when the search function is
# comparing characters.  The pattern string either shifted all the way back to its beginning (there were no re-usable
# matches) or to the index where a partial match occurred (and would be maintained without needing re-compare pattern
# and text).
#
# NOTE: The prefix length lookup table/partial match table sets the value at index 0 to -1; this (flag) value is used in
#       the search function to indicate that there is no match (to go to the next character of the text and to restart
#       at the beginning of the pattern string).
#
# Consider the following examples:
#
#   Example 1: pattern = "abcdefg"
#
#                                 Indices:   0, 1, 2, 3, 4, 5, 6, 7
#       Partial Match/Prefix Length Table: [-1, 0, 0, 0, 0, 0, 0, 0]
#                 Corresponding Character:      a  b  c  d  e  f  g
#
#       In this example, there are no matching characters, or prefix matches.  Thus, the lookup table consists of 0s,
#       and the pattern will always restart/shift back to its beginning.
#
#   Example 2: pattern = "abcxxxabcy"
#
#                                 Indices:   0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#       Partial Match/Prefix Length Table: [-1, 0, 0, 0, 0, 0, 0, 1, 2, 3,  0]
#                 Corresponding Character:      a  b  c  x  x  x  a  b  c   y
#
#       In this example, there are both matching/duplicate characters and a repeated prefix.  Therefore, if a mismatch
#       were to occur during the search (when comparing the characters of the pattern to the text); the pattern string
#       may start over (i.e., the index of the pattern string was between 1 and 6, or at 10) OR it may simply shift
#       to the next possible comparison (i.e., if the index of the pattern string being compared with the text was 9, or
#       'c', then the pattern string would 'shift' to index 3, or to the first occurrence of 'c').
#
# Time Complexity: O(n), where n is the length of the pattern string.
# Space Complexity: O(n), where n is the length of the pattern string.
def compute_partial_match_table(pattern):
    if isinstance(pattern, str):
        pattern_len = len(pattern)
        partial_match_table = [-1] + [0] * pattern_len          # Index 0 (-1) is a flag.  All others are SHIFT amounts.
        prefix_len = 0
        i = 1
        while i < pattern_len:
            if pattern[prefix_len] == pattern[i]:
                prefix_len += 1
                i += 1                                          # NOTE: i is incremented here.
                partial_match_table[i] = prefix_len
            elif prefix_len > 0:                                # NOTE: i IS NOT incremented here.
                prefix_len = partial_match_table[prefix_len]    # Doesn't necessarily restart, maintains longest match
            else:                                               # (i.e., if repeated subpattern was seen in pattern).
                i += 1                                          # NOTE: i is incremented here.
                partial_match_table[i] = 0
        return partial_match_table


# Knuth Morris Pratt Search
#
# REMEMBER: The key to this algorithm is the lookup table/partial match table.  You only need a pointer in the text (t)
#           and a pointer in the pattern (p).  Both p & t are incremented with a match, t is never decremented, and p is
#           only reset/rolled back when either a full match has been found or a mis-match has occurred (in which case it
#           uses itself to only rollback as far as necessary).
#
# Time Complexity: O(n), where n is the length of the pattern string.
# Space Complexity: O(n), where n is the length of the pattern string.
def knuth_morris_pratt_search(text, pattern):
    if isinstance(text, str) and isinstance(pattern, str):
        t = 0                               # Index (position) of the current character in the text string.
        p = 0                               # Index (position) of the current character in the pattern string.
        t_len = len(text)
        p_len = len(pattern)
        result = []                         # Returns a list of indices where the pattern is found.
        lookup_table = compute_partial_match_table(pattern)
        while t < t_len:
            if pattern[p] == text[t]:
                p += 1                      # NOTE: t & p are incremented with EACH match, BUT, p is rolled back with
                t += 1                              # each mismatch (or whenever a full match is found).
                if p == p_len:              # Pattern found (could stop, this fn keeps going)
                    result.append(t - p)
                    p = lookup_table[p]     # Reset (to go again).
            else:
                p = lookup_table[p]         # Reset (or rolled back to last sub-match).
                if p < 0:                   # I.e., if p == -1 (the 0th index of the lookup table).
                    t += 1
                    p += 1
        return result


args = [("---abcxxxab-----------",
         ["abcxxxabcy", "abcxxxab", "abcdefg"]),
        ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et " 
         "dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex " 
         "ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu "
         "fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt "
         "mollit anim id est laborum.",
         ["non", " ", "a", "e", "Excepteur"])]

for text, patterns in args:
    print(f"\ntext: {text!r}\n")
    for pattern in patterns:
        print(f"compute_partial_match_table({pattern!r}): {compute_partial_match_table(pattern)}")
        print(f"knuth_morris_pratt_search(text, {pattern!r}): {knuth_morris_pratt_search(text, pattern)}\n")


