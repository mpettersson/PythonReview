"""
    GROUP ANAGRAMS

    Write a method to sort an array of strings so that all the anagrams are next to each other.
"""


def anagram_cmp(s):
    return sorted(s)


def sort_anagrams(a):
    return sorted(a, key=anagram_cmp)


anagrams = ["they", "race", "fights", "care", "listens", "silent", "acre", "funeral", "admirer", "married", "angered",
            "enraged", "death", "hated", "elvis", "lives", "creative", "leaf", "flea", "reactive"]





nags_a_ram = sort_anagrams(anagrams)
print(nags_a_ram)

