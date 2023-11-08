"""
    FIND ANAGRAM SUBSTRINGS (leetcode.com/problems/find-all-anagrams-in-a-string)

    Write a function, which accepts a text string (t) and a pattern string (p), then returns a list of every index in
    t that an anagram of p exists.

    Two strings are anagrams of each other if the characters of one string can be rearranged to form the other string.

    Example:
        Input = "cbaebabacd", "abc"
        Output = [0,6]
"""
from collections import defaultdict


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What are the possible characters?
#   - Should lower case match with upper case?
#   - What are the possible strings lengths (empty string)?


# APPROACH: Naive
#
# This basic approach iterates over the provided text string, comparing a sorted pattern string to a sorted substring
# slice.  If the two sorted strings match, then the index is added to a result list.
#
# Time Complexity: O(nm), where n and m are the lengths of the text string (t) and a pattern string (p) respectively.
# Space Complexity (w/o return []): O(1), where n is the length of the string.
# Space Complexity (w return []): O(n), where n is the length of the provided text string (t).
def find_anagram_substrings_via_dict(t, p):
    result = []
    t_l = len(t)
    p_l = len(p)
    s = sorted(p)
    for i in range(t_l - p_l + 1):
        if sorted(t[i:i+p_l]) == s:
            result.append(i)
    return result


# APPROACH: Via Dict
#
# This approach uses a dictionary to count the number of character counts.  The dictionary is first initialized with a
# negative counts of the characters in the pattern string.  Then iterating over the characters in the text string, if
# the dictionary ever becomes empty (or all of the keys values are zero), then an anagram is found (and is added to the
# results list).  Once done, the results list is returned.
#
# Time Complexity: O(n), where n is the length of the provided text string (t).
# Space Complexity (w/o return []): O(1), where n is the length of the string.
# Space Complexity (w return []): O(n), where n is the length of the provided text string (t).
def find_anagram_substrings_via_dict(t, p):
    result = []
    if isinstance(t, str) and isinstance(p, str) and 0 < len(p) <= len(t):
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
            if len(d) == 0:                     # If d is empty, then the substring ENDING at i is an anagram;
                result.append(i - len(p))           # So since we want the BEGINNING index add i - len(p) to the result.
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
            result.append(i - len(p))
    return result


# APPROACH: Via Hash (Sum)
#
# This approach sums the hash values for each of the characters; since the initial hash sum is set to the negative hash
# sum of the pattern string, whenever the hash sum is zero THERE IS A GOOD CHANCE that an anagram is found.
#
# NOTE: This doesn't guarantee a match!
#
# Time Complexity: O(n), where n is the length of the provided text string (t).
# Space Complexity (w/o return []): O(1), where n is the length of the string.
# Space Complexity (w return []): O(n), where n is the length of the provided text string (t).
def find_anagram_substrings_via_hash(t, p):
    result = []
    if isinstance(t, str) and isinstance(p, str) and 0 < len(p) <= len(t):
        curr_hash = -sum(hash(c) for c in p)
        for c in t[:len(p)]:
            curr_hash += hash(c)
        if not curr_hash:
            result.append(0)
        for i, c in enumerate(t[len(p):]):
            curr_hash += hash(c) - hash(t[i])
            if not curr_hash:
                result.append(i+1)
    return result


args = [("cbaebabacd", "abc"),
        ("abab", "ab"),
        ("eidbaooo", "ab"),
        ("aaaaa", "aaaaa"),
        ("aaaaa", "aa"),
        ("aaaaa", "bbbbb"),
        ("", ""),
        ("", None),
        (None, ""),
        (None, None)]
fns = [find_anagram_substrings_via_dict,
       find_anagram_substrings_via_hash]

for text, string in args:
    print(f"text: {text!r}\nstring: {string!r}")
    for fn in fns:
        print(f"{fn.__name__}(text, string): {fn(text, string)!r}")
    print()


