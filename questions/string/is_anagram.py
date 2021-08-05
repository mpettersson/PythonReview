"""
    IS ANAGRAM (50CIQ 14: ANAGRAMS)

    Write a function, which accepts two strings, and returns True if they are anagrams, False otherwise.

    Example:
        Input = 'creative', 'reactive'
        Output = True

    Variations:
        - is_anagram_list.py
"""


# Questions to ask the interviewer:
#   - What type of text; ASCII, Unicode, etc.?
#   - Spaces?
#   - Capitalization?


# APPROACH: Via Sort
#
# Sort the two strings and compare for equality.
#
# Time Complexity: O(n * log(n)), where n is the combined length of the two strings.
# Space Complexity: O(n), where n is the combined length of the two strings.
def is_anagram_via_sort(s_1, s_2):
    if isinstance(s_1, str) and isinstance(s_2, str) and len(s_1) == len(s_2):
        return sorted(s_1.lower()) == sorted(s_2.lower())
    return False


# APPROACH: Via Dictionary
#
# Use a dictionary to count the number of times characters were used in the strings.
#
# Time Complexity: O(n_1 + n_2), where n_1 and n_2 are the number of characters in the strings.
# Space Complexity: O(max(u_1, u_2)), where u_1 and u_2 are the number of unique characters in the strings.
def is_anagram_via_dict(s_1, s_2):
    if isinstance(s_1, str) and isinstance(s_2, str) and len(s_1) == len(s_2):
        d = {}
        for c in s_1:
            k = c.lower()
            d[k] = d.setdefault(k, 0) + 1
        for c in s_2:
            k = c.lower()
            if k not in d:
                return False
            if d[k] > 1:
                d[k] -= 1
            else:
                d.pop(k)
        return len(d) == 0
    return False


args = [('', ""),
        ("A", "A"),
        ("A", "a"),
        ("A", "B"),
        ("Ab", "Ba"),
        ("foo", "bar"),
        ("hello ", "hello"),
        ('dog', 'god'),
        ('creative', 'reactive'),
        (None, None)]
fns = [is_anagram_via_sort,
       is_anagram_via_dict]

for s_1, s_2 in args:
    for fn in fns:
        print(f"{fn.__name__}({s_1!r}, {s_2!r}): {fn(s_1, s_2)}")
    print()


