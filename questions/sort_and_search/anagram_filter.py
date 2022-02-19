"""
    ANAGRAM FILTER

    Write a function, which accepts a list of strings, then filters and returns only a list of lists of anagrams.

    Example:
        Input = ['money', 'dog', 'race', 'creative', 'care', 'acre', 'god']
        Output = [['dog', 'god'], ['race', 'care', 'acre']]
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What type of characters?
#   - What are the estimated lengths of the strings (empty string)?
#   - What is the estimated length of the list (empty list)?


# APPROACH: Via Dictionary/Hash Table
#
# Add all words into a dictionary, where the keys are sorted words and the values are the provided words; then, for any
# values that have more than one entry (anagram) add the entry to a list, and return the list.
#
# Time Complexity:  O(n * m * log(m)), where n is the number of strings in the list and m is the max string length.
# Space Complexity: O(s), where s is the size of the list of strings.
def filter_anagrams(l):
    if l:
        d = {}
        for s in l:
            sorted_s = ''.join(sorted(s))
            d[sorted_s] = d[sorted_s] + [s] if sorted_s in d else [s]
        return [values for values in d.values() if len(values) > 1]


word_list = ["Lorem",  "they", "race", "fights", "care", "listens", "silent", "acre", "funeral", "admirer", "married",
             "angered", "dog", "enraged", "death", "fun", "hated", "elvis", "lives", "creative", "leaf", "flea", "bar",
             "foo", "reactive", "god", "ipsum", "logarithmic", "levis", "algorithmic", "money"]
fns = [filter_anagrams]

print(f"word_list: {word_list}\n")
for fn in fns:
    print(f"{fn.__name__}(word_list): {fn(word_list)}")
    print()


