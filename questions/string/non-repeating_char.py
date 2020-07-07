"""
    NON-REPEATING CHARACTER

    Write a function, which when given a string, will return the first non-repeating character or None if all characters
    repeat.

    Example:
        Input = "aabcb"
        Output = "c"
"""


# This approach has O(n) time and space.
def non_repeating_char(s):
    d = {}
    for c in s:
        d[c] = d[c] + 1 if c in d.keys() else 1
    for k in d.keys():
        if d[k] == 1:
            return k


args = ["abcab", "aabcb", "aabbbc", "xxyz", "aabbdbc", "abab", "aabb"]

for s in args:
    print(f"non_repeating_char({s}):", non_repeating_char(s))











