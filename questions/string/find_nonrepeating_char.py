"""
    FIND NONREPEATING CHARACTER

    Write a function, which when given a string, will return the first nonrepeating character or None if all characters
    repeat.

    Example:
        Input = "aabcb"
        Output = "c"
"""


# Naive/Brute Force Approach:  For each character, check all other characters; if no duplicates, return the character.
# Time Complexity:  O(n**2), where n is the number of characters in the string.
# Space Complexity:  O(1).
def find_nonrepeating_char_naive(s):
    if s:
        for i in range(len(s)):
            has_repeat = False
            for j in range(len(s)):
                if i != j and s[i] == s[j]:
                    has_repeat = True
                    break
            if not has_repeat:
                return s[i]


# Dictionary Approach:  Use a dictionary to count the number of occurrences for each letter, then return the first
# character with a count of 1, None otherwise.
# Time Complexity:  O(n), where n is the number of characters in the string.
# Space Complexity:  O(n), where n is the number of characters in the string.
def find_nonrepeating_char(s):
    if s:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        for k in d.keys():
            if d[k] == 1:
                return k


args = ["abcab",
        "aabcb",
        "aabbbc",
        "xxyz",
        "aabbdbc",
        "abab",
        "aabb"
        "",
        None]
fns = [find_nonrepeating_char_naive, find_nonrepeating_char]

for fn in fns:
    for s in args:
        print(f"{fn.__name__}({s}):", fn(s))
    print()


