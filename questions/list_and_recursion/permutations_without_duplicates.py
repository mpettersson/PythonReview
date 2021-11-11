"""
    PERMUTATIONS WITHOUT DUPLICATES (CCI 8.7: PERMUTATIONS WITHOUT DUPS,
                                     50CIQ 12: PERMUTATIONS)

    Write a function, which accepts a string of unique characters, and returns a list of all the strings permutations.

    Example:
        Input = "ABC"
        Output = ['ABC', 'BAC', 'BCA', 'ACB', 'CAB', 'CBA']

    NOTE: Remember that for n items, the number of permutations is n! (so you can't do better than O(n!) time).
"""
import itertools
import time


# Questions you should ask the interviewer (if not explicitly stated):
#   - What is the argument type?  (This may affect some languages more than others.)
#   - Are there duplicate elements?

# APPROACH: Via Itertools Permutations
#
# This approach simply uses Python's itertools.permutations method.
#
# Time Complexity: O(n!), where n is the length of the string.
# Space Complexity: O(n!), where n is the length of the string.
def get_itertools_perms(s):
    if isinstance(s, str):
        return list(map(''.join, itertools.permutations(s)))


# APPROACH: Head & Tail/Build From Permutations of Tail n-1 Chars
#
# A string is divided into a head (the first character) and the tail (the remaining characters).  The results of calling
# the function with the tail is then used to construct a new result; where the head (character) is inserted in all
# positions of each string of the recursive call (with the tail).  The results are then returned.
#
# Time Complexity: O(n!), where n is the length of the string.
# Space Complexity: O(n!), where n is the length of the string.
def get_perms_wo_dups_ht(s):
    if s is not None:
        n = len(s)
        if n <= 1:                                              # Base Case: If s is empty, or a single element:
            return [s]                                              # Return it in a list.
        result = []
        for t_perm in get_perms_wo_dups_ht(s[1:]):              # For each list in the recursive result:
            for i in range(n):                                      # In each index/position:
                result.append(t_perm[:i] + s[0] + t_perm[i:])           # Insert the first char (head)
        return result


# APPROACH: Minimised
#
# Same as above, but minimized.
#
# Time Complexity: O(n!), where n is the length of the string.
# Space Complexity: O(n!), where n is the length of the string.
def get_perms_wo_dups_ht_min(s):
    if isinstance(s, str):
        l = len(s)
        return [s] if l <= 1 else [t_perm[:i] + s[0] + t_perm[i:] for t_perm in get_perms_wo_dups_ht_min(s[1:]) for i in range(l)]


# APPROACH: Build From All Character Substring
#
# For each character in the string, recurse on the the remainder of the string, then add the (missing) character to each
# permutation in the results of the recursive call.
#
# Time Complexity: O(n!), where n is the length of the string.
# Space Complexity: O(n!), where n is the length of the string.
def get_perms_wo_dubs(s):
    if s is not None:
        if len(s) == 0:
            return [""]
        result = []
        for i in range(len(s)):                                 # For each character in the string,
            for p in get_perms_wo_dubs(s[:i] + s[i + 1:]):          # For each permutation of the string (w/o the char),
                result.append(s[i] + p)                                 # Add the character to the head of each list.
        return result


# APPROACH: Push The 'Prefix' Down The Stack
#
# Push an empty string (as the 'prefix'), the original string, and the results list down the stack (via recursive call).
# At each level of the stack each character is then selected to be appended to the prefix and excluded from the next
# recursive call.  This ends when the remainder is empty, triggering the prefix to be added to the results list.
#
# Time Complexity: O(n!), where n is the length of the string.
# Space Complexity: O(n!), where n is the length of the string.
def get_perms_wo_dubs_prefix(s):

    def _get_perms_wo_dubs_prefix(prefix, remainder, perms):
        if len(remainder) == 0:                                 # Once the remainder is empty,
            perms.append(prefix)                                # Add the prefix/valid permutation.
        else:
            for i in range(len(remainder)):                     # Else, for each index, add it to the prefix and recurse
                _get_perms_wo_dubs_prefix(prefix + remainder[i], remainder[:i] + remainder[i + 1:], perms)

    if s is not None:
        perms = []
        _get_perms_wo_dubs_prefix("", s, perms)                  # Note the empty string accumulator.
        return perms


args = ["A", "AB", "ABC", "1234", "", None]
fns = [get_itertools_perms,
       get_perms_wo_dups_ht,
       get_perms_wo_dups_ht_min,
       get_perms_wo_dubs,
       get_perms_wo_dubs_prefix]

for s in args:
    for fn in fns:
        print(f"{fn.__name__}({s!r}): {fn(s)}")
    print()


s = "ABCDEFGHIJ"
for fn in fns:
    t = time.time()
    print(f"{fn.__name__}({s!r})", end="")
    fn(s)
    print(f" took {time.time() - t} seconds")


