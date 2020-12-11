"""
    ANAGRAM SORT (CCI 10.2:  GROUP ANAGRAMS)

    Write a function to sort a list of strings such that any anagrams are next to each other.

    Example:
        Input = ['dog', 'race', 'creative', 'care', 'reactive', 'acre', 'god']
        Output = ['dog', 'god', 'race', 'care', 'acre', 'creative', 'reactive']
"""


# Verbose Comparison Key Approach:  Sort the list of words based on the words sorted order.
# Time Complexity: O(n * k * (log(n) + log(k))), where n is the number of strings and k is the maximum string length.
# Space Complexity: O(n * k), where n is the number of strings in the list and k is the maximum string length.
def sort_anagrams_verbose(anagrams):
    def _anagram_cmp(s):
        return sorted(s)
    return sorted(anagrams, key=_anagram_cmp)


# Pythonic Comparison Key Approach:  Same as above, however, pythonic.
# Time Complexity: O(n * k * (log(n) + log(k))), where n is the number of strings and k is the maximum string length.
# Space Complexity: O(n * k), where n is the number of strings in the list and k is the maximum string length.
def sort_anagrams(anagrams):
    return sorted(anagrams, key=sorted)


# Pythonic Comparison Key & Group Approach:  Similar to above, however, sort first on length then on sorted value.
# Time Complexity: O(n * k * (log(n) + log(k))), where n is the number of strings and k is the maximum string length.
# Space Complexity: O(n * k), where n is the number of strings in the list and k is the maximum string length.
def sort_and_group_anagrams(anagrams):
    return sorted(map(str.lower, anagrams), key=lambda x: (len(x), sorted(x)))


# Optimal Solution: Build a dictionary where the keys are the sorted strings, and the values are a list containing any
# anagrams of the key.
# Time Complexity: O(n * (k * log(k))), where n is the number of strings and k is the maximum string length.
# Space Complexity: O(n * k), where n is the number of strings in the list and k is the maximum string length.
def sort_anagrams_via_dict(anagrams):
    if anagrams:
        d = {}
        for s in anagrams:
            k = ''.join(sorted(s))
            d[k] = d.get(k, []) + [s]
        return [v for l in d.values() for v in l]


anagrams = ["they", "race", "fights", "care", "listens", "silent", "acre", "funeral", "admirer", "married", "angered",
            "dog", "enraged", "death", "fun", "hated", "elvis", "lives", "creative", "leaf", "flea", "reactive", "god",
            "logarithmic", "levis", "algorithmic", "money"]
fns = [sort_anagrams_verbose,
       sort_anagrams,
       sort_and_group_anagrams,
       sort_anagrams_via_dict]

print("anagrams:", anagrams, "\n")
for fn in fns:
    print(f"{fn.__name__}(anagrams): {fn(anagrams)}")


