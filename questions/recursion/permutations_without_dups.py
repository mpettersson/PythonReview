"""
    PERMUTATIONS WITHOUT DUPS (CCI 8.7)

    Write a method to compute all permutations of a string of unique characters.

    Example:
        Input = "ABC"
        Output = ['ABC', 'BAC', 'BCA', 'ACB', 'CAB', 'CBA']

    NOTE: Remember that for n items, the number of permutations is n! (so you can't do better than O(n!) time).
"""
import itertools
import time


# Via Itertools Permutations:
def get_itertools_perms(s):
    if s is not None:
        return list(map(''.join, itertools.permutations(s)))


# Head & Tail/Build From Permutations of Tail n-1 Chars:  For each of the tail's permutation strings, add the head
# character, and return the results.  Time and space complexity is O(n!) where n is the size of the string s.
def get_perms_wo_dups(s):
    if s is not None:
        length = len(s)
        if length <= 1:
            return [s]
        perms = []
        for t_perm in get_perms_wo_dups(s[1:]):                 # Get tail perms
            for i in range(length):                             # In each position of each tail permutation,
                perms.append(t_perm[:i] + s[0] + t_perm[i:])    # Insert the first char (head)
        return perms


# Minimised Approach:  Same as above, but minimized.  Time and space complexity is O(n!) where n is the size of s.
def get_perms_wo_dups_min(s):
    if s is not None:
        l = len(s)
        return [s] if l <= 1 else [t_perm[:i] + s[0] + t_perm[i:] for t_perm in get_perms_wo_dups_min(s[1:]) for i in range(l)]


# Build From All Character Substring Approach:  For each char i in the string, get the permutations of all of the other
# characters (before and after), then add the character to each of the permutations and return.  Time and space
# complexity is O(n!) where n is the size of the string s.
def get_perms_wo_dubs_2(s):
    if s is not None:
        if len(s) is 0:
            return [""]
        perms = []
        for i in range(len(s)):                                 # For each index, i, in the string,
            for p in get_perms_wo_dubs_2(s[:i] + s[i + 1:]):    # Get permutations of s without s[i],
                perms.append(s[i] + p)                          # And add s[i] to each of the permutations.
        return perms


# Push Prefix Down Stack Approach: Once there is no more 'remainder' add the prefix as a permutation.  Time and space
# complexity is O(n!) where n is the size of the string s.
def get_perms_wo_dubs_3(s):

    def _get_perms_wo_dubs_3(prefix, remainder, perms):
        if len(remainder) is 0:                                 # Once the remainder is empty,
            perms.append(prefix)                                # You have generated a valid permutation (as prefix).
        else:
            for i in range(len(remainder)):                     # Else, for each index, add it to the prefix and recurse
                _get_perms_wo_dubs_3(prefix + remainder[i], remainder[:i] + remainder[i + 1:], perms)

    if s is not None:
        perms = []
        _get_perms_wo_dubs_3("", s, perms)                      # Note the empty string acumulator.
        return perms


strings = ["A", "AB", "ABC", "1234", "", None]

for s in strings:
    print(f"get_itertools_perms({s!r}): {get_itertools_perms(s)}")
print()

for s in strings:
    print(f"get_perms_wo_dups({s!r}): {get_perms_wo_dups(s)}")
print()

for s in strings:
    print(f"get_perms_wo_dups_min({s!r}): {get_perms_wo_dups_min(s)}")
print()

for s in strings:
    print(f"get_perms_wo_dubs_2({s!r}): {get_perms_wo_dubs_2(s)}")
print()

for s in strings:
    print(f"get_perms_wo_dubs_3({s!r}): {get_perms_wo_dubs_3(s)}")
print()

s = "ABCDEFGHIJ"
t = time.time(); print(f"get_itertools_perms({s!r})", end=""); get_itertools_perms(s); print(f" took {time.time() - t} seconds")
t = time.time(); print(f"get_perms_wo_dups({s!r})", end=""); get_perms_wo_dups(s); print(f" took {time.time() - t} seconds")
t = time.time(); print(f"get_perms_wo_dups_min({s!r})", end=""); get_perms_wo_dups_min(s); print(f" took {time.time() - t} seconds")
t = time.time(); print(f"get_perms_wo_dubs_2({s!r})", end=""); get_perms_wo_dubs_2(s); print(f" took {time.time() - t} seconds")
t = time.time(); print(f"get_perms_wo_dubs_3({s!r})", end=""); get_perms_wo_dubs_3(s); print(f" took {time.time() - t} seconds")


