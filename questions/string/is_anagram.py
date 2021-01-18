"""
    IS ANAGRAM (50CIQ 14: ANAGRAMS)

    Write a function, which accepts two strings, and returns True if they are anagrams, False otherwise.

    Example:
        Input = 'creative', 'reactive'
        Output = True

    Variations:
        - Same question, however, the function accepts a list of strings.
"""


# Questions to ask the interviewer:
#   - What type of text; ASCII, Unicode, etc.?
#   - Spaces?
#   - Capitalization?


# Sorting Approach:  Sort the two strings and compare for equality.
# Time Complexity: O(n * log(n)), where n is the length of the two strings.
# Space Complexity: O(1).
def is_anagram_via_sort(s_1, s_2):
    if s_1 is not None and s_2 is not None and len(s_1) is len(s_2):
        s_1 = sorted(s_1.lower())   # Remember, sort() only works on lists.
        s_2 = sorted(s_2.lower())
        return s_1 == s_2           # Remember to use '=='
    return False


# Dictionary Approach:  Use a dictionary to count the number of times characters were used in the strings.
# Time Complexity: O(n_1 + n_2), where n_1 and n_2 are the number of characters in the strings.
# Space Complexity: O(max(u_1, u_2)), where u_1 and u_2 are the number of unique characters in the strings.
def is_anagram_via_dict(s_1, s_2):
    if s_1 is not None and s_2 is not None and len(s_1) is len(s_2):
        d = {}
        s_1 = s_1.lower()
        s_2 = s_2.lower()
        for c in s_1:
            d[c] = d.setdefault(c, 0) + 1
        for c in s_2:
            if c not in d:
                return False
            if d[c] > 1:
                d[c] -= 1
            else:
                d.pop(c)
        return len(d) == 0
    return False


# VARIATION: Same question, however, K number of strings.


# Sorting Approach:  Check that all strings, when sorted, are the same.
# Time Complexity: O(k * (n * log(n))), where k is the number of args and n is the length of an arg string.
# Space Complexity: O(n), where n is the length of an arg string.  This is because args is an IMMUTABLE tuple.
def is_anagram_list_via_sort(*args):
    if args is not None and len(args) > 1 and all(map(lambda e: isinstance(e, str), args)):
        args = tuple(map(lambda e: sorted(str.lower(e)), args))
        for i in range(1, len(args)):
            if not (len(args[i]) == len(args[0]) and args[i] == args[0]):
                return False
        return True
    return False


# Dictionary Approach:  Use two dictionaries to store the number of characters in a string, if any two strings have a
# different number of characters, return False.
# Time Complexity: O(k * n), where n is the number of characters in the strings.
# Space Complexity: O(u), where u is the number of unique characters in the strings.
def is_anagram_list_via_dict(*args):
    if args is not None and len(args) > 1 and all(map(lambda e: isinstance(e, str), args)):
        d = {}
        for c in args[0]:
            c = c.lower()
            d[c] = d.setdefault(c, 0) + 1
        for i in range(1, len(args)):
            temp = {}
            for c in args[i]:
                c = c.lower()
                temp[c] = temp.setdefault(c, 0) + 1
                if c not in d:
                    return False
                if d[c] > 1:
                    d[c] -= 1
                else:
                    d.pop(c)
            if not len(d) == 0:
                return False
            d = temp
        return True
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
alt_args = [('race', 'care', 'acre'),
            ('a', 'b', 'c'),
            ('', '', ''),
            ()]
fns = [is_anagram_via_sort,
       is_anagram_via_dict]
alt_fns = [is_anagram_list_via_sort,
           is_anagram_list_via_dict]

for fn in fns:
    for s_1, s_2 in args:
        print(f"{fn.__name__}({s_1!r}, {s_2!r}): {fn(s_1, s_2)}")
    print()

for fn in alt_fns:
    for t in args + alt_args:
        print(f"{fn.__name__}{t}: {fn(*t)}")
    print()


