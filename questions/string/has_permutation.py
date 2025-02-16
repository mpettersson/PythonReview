"""
    HAS PERMUTATION (leetcode.com/problems/permutation-in-string)

    Write a function, which accepts a text string (t) and a pattern string (p), then returns True if there exists a
    permutation of p in t, False otherwise.

    Example:
        Input = "cbaebabacd", "abc"
        Output = True
"""
import itertools
from collections import defaultdict


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What are the possible characters?
#   - Should lower case match with upper case?
#   - What are the possible strings lengths (empty string)?


# APPROACH: Naive Via Itertools Permutations
#
# This approach simply uses Python's itertools.permutations method to generate all permutations of p.  Each permutation
# is then checked against t; if a match is found, True is returned.
#
# Time Complexity: O(n * m!), where n is the length of t and m is the length of p.
# Space Complexity: O(n * m!), where n is the length of t and m is the length of p.
def has_permutation_via_itertools(t, p):
    if isinstance(t, str) and isinstance(p, str) and len(p) <= len(t):
        for perm in itertools.permutations(p):
            if ''.join(perm) in t:
                return True
    return False


# APPROACH: Via Dict
#
# This approach uses a dictionary to count the number of character counts.  The dictionary is first initialized with a
# negative counts of the characters in the pattern string.  Then iterating over the characters in the text string, if
# the dictionary ever becomes empty (or all of the keys values are zero), then a permutation is found and True is
# returned.  Else, once done, False is returned.
#
# Time Complexity: O(n), where n is the length of the string.
# Space Complexity: O(1), where n is the length of the string.
def has_permutation_via_dict(t, p):
    if isinstance(t, str) and isinstance(p, str) and len(p) <= len(t):
        d = defaultdict(int)                # Use a defaultdict to cut down on the code...
        for c in p:                         # Initialize the dictionary with a NEGATIVE count; this way any time the
            d[c] -= 1                       # dictionary becomes empty, an anagram is found!
        i = 0
        while i < len(p):                   # Add the first len(p) chars to the dict:
            if d[t[i]] == -1:                   # BUT, if the count was to hit zero, del it!!!  This is for faster,
                del d[t[i]]                         # or easier, anagram checking (below).
            else:                               # Otherwise, just add one to the count.
                d[t[i]] += 1
            i += 1
        while i < len(t):                   # For the remaining chars in the text:
            if len(d) == 0:                     # If d is empty, then we know there exists a permutation:
                return True                         # Return True...
            if d[t[i]] == -1:                   # Update d with char at i:
                del d[t[i]]                         # If it was -1, just del it (it's easier to check).
            else:
                d[t[i]] += 1                        # Else, add one to its value.
            if d[t[i - len(p)]] == 1:           # Remove char at i-len(p) from d:
                del d[t[i - len(p)]]                # If the count is 1, just del that entry.
            else:
                d[t[i - len(p)]] -= 1           # Else, decrement it (we just don't want a key with value zero...).
            i += 1
        if len(d) == 0:                     # Don't forget to check the last len(p) chars in t.
            return True
    return False


# APPROACH: Via Hash (Sum)
#
# This approach sums the hash values for each of the characters; since the initial hash sum is set to the negative hash
# sum of the pattern string, whenever the hash sum is zero THERE IS A GOOD CHANCE that an anagram is found; return True.
# Otherwise, when finished, return False.
#
# NOTE: This DOESN'T guarantee a match!
#
# Time Complexity: O(n), where n is the length of the string.
# Space Complexity: O(1), where n is the length of the string.
def has_permutation_via_hash(t, p):
    if isinstance(t, str) and isinstance(p, str) and len(p) <= len(t):
        curr_hash = -sum(hash(c) for c in p)
        for c in t[:len(p)]:
            curr_hash += hash(c)
        if not curr_hash:
            return True
        for i, c in enumerate(t[len(p):]):
            curr_hash += hash(c) - hash(t[i])
            if not curr_hash:
                return True
    return False


args = [("cbaebabacd", "abc"),
        ("abab", "ab"),
        ("eidbaooo", "ab"),
        ("aaaaa", "aaaaa"),
        ("aaaaa", "bbbbb"),
        ("", ""),
        ("", None),
        (None, ""),
        (None, None)]
fns = [has_permutation_via_itertools,
       has_permutation_via_dict,
       has_permutation_via_hash]

for text, string in args:
    print(f"text: {text!r}\nstring: {string!r}")
    for fn in fns:
        print(f"{fn.__name__}(text, string): {fn(text, string)!r}")
    print()


