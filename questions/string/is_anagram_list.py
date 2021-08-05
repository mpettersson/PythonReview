"""
    IS ANAGRAM LIST

    Write a function, which accepts a list of strings, and returns True if they are all anagrams of each other, False
    otherwise.

    Example:
        Input = ['race', 'care', 'acre']
        Output = True

    Variations:
        - is_anagram.py
"""


# Questions to ask the interviewer:
#   - What type of text; ASCII, Unicode, etc.?
#   - Spaces?
#   - Capitalization?


# APPROACH: Via Sorting
#
# Check that all strings, when sorted, are the same.
#
# Time Complexity: O(k * (n * log(n))), where k is the number of args and n is the length of an arg string.
# Space Complexity: O(s), where s is the length of a single list string.
def is_anagram_list_via_sort(l):
    if isinstance(l, list) and len(l) > 1 and all(map(lambda e: isinstance(e, str), l)):
        s_0 = sorted(l[0].lower())
        for i in range(1, len(l)):
            if not s_0 == sorted(l[i].lower()):
                return False
        return True
    return False


# APPROACH: Dictionary
#
# Build up a dictionary from the lowercase character count of the first word in the list.  Then iterate over the
# remaining strings, with each iteration also creating a second dictionary that will be swapped with the previous
# dictionary (to maintain a copy), where the lower case count of characters in the current string is compared to the
# first string.  If at any point a character is found that isn't in the first dictionary, or the first dictionary had a
# character not in the current dictionary, return False.  If at the end all of the strings lower case character counts
# match, return True.
#
# Time Complexity: O(t), where t is the total number of characters in the list.
# Space Complexity: O(u), where u is the number of unique characters in the strings.
def is_anagram_list_via_dict(l):
    if isinstance(l, list) and len(l) > 1 and all(map(lambda e: isinstance(e, str), l)):
        d = {}
        for c in l[0]:
            k = c.lower()
            d[k] = d.setdefault(k, 0) + 1
        for i in range(1, len(l)):
            temp = {}
            for c in l[i]:
                k = c.lower()
                temp[k] = temp.setdefault(k, 0) + 1
                if k not in d:
                    return False
                if d[k] > 1:
                    d[k] -= 1
                else:
                    d.pop(k)
            if not len(d) == 0:
                return False
            d = temp
        return True
    return False


lists = [['', ""],
         ["A", "A"],
         ['Races', 'Cares', 'Acres', 'Scare'],
         ["A", "a"],
         ["A", "B"],
         ["Ab", "Ba"],
         ["foo", "bar", 'dog', 'god'],
         ['creative', 'reactive'],
         [None, None]]
fns = [is_anagram_list_via_sort,
       is_anagram_list_via_dict]

for l in lists:
    for fn in fns:
        print(f"{fn.__name__}({l!r}): {fn(l)}")
    print()


