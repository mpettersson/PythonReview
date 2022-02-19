"""
    ANAGRAM SORT

    Write a function to sort a list of strings such that any anagrams are next to each other and are sorted according to
    their lexicographical order.

    Example:
        Input = ['dog', 'race', 'creative', 'care', 'reactive', 'acre', 'god']
        Output = ['dog', 'god', 'race', 'care', 'acre', 'creative', 'reactive']
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What type of characters?
#   - What are the estimated lengths of the strings (empty string)?
#   - What is the estimated length of the list (empty list)?


# APPROACH: Verbose Via Dictionary (Sorted Anagram Key -> List Of Anagrams)
#
# This approach build a dictionary where the keys are the sorted strings, and the values are a list containing any
# anagrams of the key.
#
# Time Complexity: O(n * k * (log(n) + log(k))), where n is the number of strings and k is the maximum string length.
# Space Complexity: O(n * k), where n is the number of strings in the list and k is the maximum string length.
def sort_anagrams_verbose(anagrams):
    if anagrams:
        d = {}
        for s in anagrams:
            k = ''.join(sorted(s.lower()))
            d[k] = d.get(k, []) + [s]
        d = {k: v for k, v in sorted(d.items(), key=lambda x: (len(x[0]), x[0]))}
        return [v for l in d.values() for v in l]


# APPROACH: Pythonic Comparison Key & Group
#
# This approach first lower-cases all of the words, then sorts the words using a key function that prioritizes length
# of the word, then the SORTED order of the characters in the word.
#
# Time Complexity: O(n * k * (log(n) + log(k))), where n is the number of strings and k is the maximum string length.
# Space Complexity: O(n * k), where n is the number of strings in the list and k is the maximum string length.
def sort_anagrams(anagrams):
    return sorted(map(str.lower, anagrams), key=lambda x: (len(x), sorted(x)))


anagrams = ["they", "race", "fights", "care", "listens", "silent", "acre", "funeral", "admirer", "married", "angered",
            "dog", "enraged", "death", "fun", "hated", "elvis", "lives", "creative", "leaf", "flea", "reactive", "god",
            "logarithmic", "levis", "algorithmic", "money"]
fns = [sort_anagrams_verbose,
       sort_anagrams]

print(f"\nanagrams: {anagrams}\n")
for fn in fns:
    print(f"{fn.__name__}(anagrams): {fn(anagrams)}")


