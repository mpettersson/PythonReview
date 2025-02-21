"""
    PERMUTATIONS WITHOUT DUPLICATES (CCI 8.7: PERMUTATIONS WITHOUT DUPS,
                                     50CIQ 12: PERMUTATIONS,
                                     leetcode.com/problems/permutations/)

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
def get_perms_wo_dups_itertools(s):
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
def get_perms_wo_dups_rec_0(s):

    def _rec(s):
        if len(s) == 0:                             # Base Case: If s is empty, or a single element:
            return [s]                                  # Return it in a list.
        result = []
        for p in _rec(s[1:]):                       # For each permutation in the recursive results:
            for i in range(len(s)):                     # In each index/position:
                result.append(p[:i] + s[0] + p[i:])         # Insert the first char (head).
        return result

    if s is not None and isinstance(s, str):
        return _rec(s)


# APPROACH: Build From All Character Substring
#
# For each character in the string, recurse on the remainder of the string, then add the (missing) character to each
# permutation in the results of the recursive call.
#
# Time Complexity: O(n!), where n is the length of the string.
# Space Complexity: O(n!), where n is the length of the string.
def get_perms_wo_dups_rec_1(s):

    def _rec(s):
        if len(s) == 0:
            return [""]
        result = []
        for i in range(len(s)):                     # For each character in the string,
            for p in _rec(s[:i] + s[i+1:]):             # For each permutation of the string (w/o the char),
                result.append(s[i] + p)                     # Add the character to the head of each list.
        return result

    if s is not None and isinstance(s, str):
        return _rec(s)


# APPROACH: Push The 'Prefix' Down The Stack
#
# Push an empty string (as the 'prefix'), the original string, and the results list down the stack (via recursive call).
# At each level of the stack each character is then selected to be appended to the prefix and excluded from the next
# recursive call.  This ends when the remainder is empty, triggering the prefix to be added to the results list.
#
# Time Complexity: O(n!), where n is the length of the string.
# Space Complexity: O(n!), where n is the length of the string.
def get_perms_wo_dups_rec_2(s):

    def _rec(prefix, remainder):
        if len(remainder) == 0:                                 # Once the remainder is empty,
            result.append(prefix)                                # Add the prefix/valid permutation.
        else:
            for i in range(len(remainder)):                     # Else, for each index, add it to the prefix and recurse
                _rec(prefix + remainder[i], remainder[:i] + remainder[i + 1:])

    if s is not None:
        result = []
        _rec("", s)                  # Note the empty string accumulator.
        return result


# APPROACH: Recursive with Index Pointer
#
# Yet another recursive approach, similar to the approaches above, with one difference; this approach uses a pointer
# with the original string. The approaches above pass slices (new strings) and therefore operate with a higher overhead.
#
# Time Complexity: O(n!), where n is the length of the string.
# Space Complexity: O(n!), where n is the length of the string.
def get_perms_wo_dups_rec(s):

    def _rec(s, i):
        if i == len(s):
            return [""]
        h = s[i]
        t = _rec(s, i+1)
        results = []
        for res in t:
            for j in range(len(res)+1):
                results.append(res[:j] + h + res[j:])
        return results

    if s is not None and isinstance(s, str):
        return _rec(s, 0)


# APPROACH: Via Dictionary
#
# This solution uses a dict, which contains each char and the number of times it appears, to create permutations via
# building an accumulator that is appended to the results when the index (which is initialized equal to the length of
# the string) reaches zero.  This, although slower than the optimal solution above, it also handles question variations
# with duplicate characters in the string...
#
# Time Complexity: O(n!), where n is the length of the string (and there are NO duplicates).
# Space Complexity: O(n!), where n is the length of the string (and there are NO duplicates).
def get_perms_wo_dups_dict(s):

    def _rec(i, accumulator):
        if i == 0:
            result.append(accumulator)
        else:
            for k in d.keys():
                if d[k] > 0:
                    d[k] -= 1
                    _rec(i-1, accumulator + k)
                    d[k] += 1

    if s is not None:
        result = []
        d = {}
        for c in s:
            d[c] = d.setdefault(c, 0) + 1
        _rec(len(s), "")
        return result


args = ["A", "AB", "ABC", "1234", "", None]
fns = [get_perms_wo_dups_itertools,
       get_perms_wo_dups_rec_0,
       get_perms_wo_dups_rec_1,
       get_perms_wo_dups_rec_2,
       get_perms_wo_dups_rec,
       get_perms_wo_dups_dict]

for s in args:
    for fn in fns:
        print(f"{fn.__name__}({s!r}): {fn(s)}")
    print()


s = "ABCDEFGHIJL"
for fn in fns:
    t = time.time()
    print(f"{fn.__name__}({s!r})", end="")
    fn(s)
    print(f" took {time.time() - t} seconds")


