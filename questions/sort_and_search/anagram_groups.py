"""
    ANAGRAM GROUPS (CCI 10.2:  GROUP ANAGRAMS,
                    leetcode.com/problems/group-anagrams/)

    Write a function to sort a list of strings such that any anagrams are next to each other.

    Example:
        Input = ['dog', 'race', 'creative', 'care', 'reactive', 'acre', 'god']
        Output = ['dog', 'god', 'race', 'care', 'acre', 'creative', 'reactive']
"""
from collections import defaultdict


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What type of characters?
#   - What are the estimated lengths of the strings (empty string)?
#   - What is the estimated length of the list (empty list)?


# APPROACH: Verbose Comparison Via Sorted Key
#
# Group the list of words based on the words sorted order.
#
# Time Complexity: O(n * k * (log(n) + log(k))), where n is the number of strings and k is the maximum string length.
# Space Complexity: O(n * k), where n is the number of strings in the list and k is the maximum string length.
def group_anagrams_verbose(anagrams):
    def _anagram_cmp(s):
        return sorted(s)
    return sorted(anagrams, key=_anagram_cmp)


# APPROACH: Pythonic Comparison Via Sorted Key
#
# Same as above, however, pythonic.
#
# Time Complexity: O(n * k * (log(n) + log(k))), where n is the number of strings and k is the maximum string length.
# Space Complexity: O(n * k), where n is the number of strings in the list and k is the maximum string length.
def group_anagrams_pythonic(anagrams):
    return sorted(anagrams, key=sorted)


# APPROACH: Via Dictionary (Sorted Anagram Key -> List Of Anagrams)
#
# This approach build a dictionary where the keys are the sorted strings, and the values are a list containing any
# anagrams of the key.
#
# Time Complexity: O(n * (k * log(k))), where n is the number of strings and k is the maximum string length.
# Space Complexity: O(n * k), where n is the number of strings in the list and k is the maximum string length.
def group_anagrams_via_dict(anagrams):
    if anagrams:
        d = {}
        for s in anagrams:
            k = ''.join(sorted(s))
            d[k] = d.get(k, []) + [s]
        return [v for l in d.values() for v in l]


# APPROACH: Optimal Via Dictionary (Letter Count Key -> List Of Anagrams)
#
# This approach has one improvement over the previous; this simply counts the letters as opposed to SORTING the letters
# (as in the previous solution).  The letter count is then converted to a tuple (so it is immutable and able to be used
# as a key) and flattened before being returned.  Thus, each character, in each string is counted only once.
#
# Time Complexity: O(n * k) where n is the length of the list, and k is the maximum string length in the list.
# Space Complexity: O(n * k), the total information content stored in ans.
def group_anagrams(anagrams):
    d = defaultdict(list)
    for s in anagrams:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        d[tuple(count)].append(s)
    return [v for sl in d.values() for v in sl]


anagrams = ["they", "race", "fights", "care", "listens", "silent", "acre", "funeral", "admirer", "married", "angered",
            "dog", "enraged", "death", "fun", "hated", "elvis", "lives", "creative", "leaf", "flea", "reactive", "god",
            "logarithmic", "levis", "algorithmic", "money"]
fns = [group_anagrams_verbose,
       group_anagrams_pythonic,
       group_anagrams_via_dict,
       group_anagrams]

print("anagrams:", anagrams, "\n")
for fn in fns:
    print(f"{fn.__name__}(anagrams): {fn(anagrams)}")


