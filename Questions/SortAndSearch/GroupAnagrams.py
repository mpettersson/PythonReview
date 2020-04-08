"""
    GROUP ANAGRAMS (CCI 10.2)

    Write a method to sort an array of strings so that all the anagrams are next to each other.

    Example:
        Input = ['dog', 'race', 'creative', 'care', 'reactive', 'acre', 'god']
        Output = ['dog', 'god', 'race', 'care', 'acre', 'creative', 'reactive']
"""


# Verbose Comparison Key Approach:
def sort_anagrams_verbose(anagrams):
    return sorted(anagrams, key=anagram_cmp)


def anagram_cmp(s):
    return sorted(s)


# Pythonic Comparison Key Approach:
def sort_anagrams(anagrams):
    return sorted(anagrams, key=sorted)


# Enhanced Approach (groups by len() then sorted()):
def group_anagrams(anagrams):
    return sorted(list(map(lambda s: s.lower(), anagrams)), key=lambda x: (len(x), sorted(x)))


anagrams = ["they", "race", "fights", "care", "listens", "silent", "acre", "funeral", "admirer", "married", "angered",
            "dog", "enraged", "death", "hated", "elvis", "lives", "creative", "leaf", "flea", "reactive", "god"]

print("anagrams:", anagrams)
print()

print("sort_anagrams_verbose(anagrams):", sort_anagrams_verbose(anagrams))
print("sort_anagrams(anagrams):        ", sort_anagrams(anagrams))
print("group_anagrams(anagrams):       ", group_anagrams(anagrams))


