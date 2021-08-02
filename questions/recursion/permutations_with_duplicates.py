"""
    PERMUTATIONS WITH DUPLICATES (CCI 8.8: PERMUTATIONS WITH DUPS)

    Write a function, which accepts a string of possibly non-unique characters, then computes and returns the strings
    permutations.

    Example:
        Input = "AAAB"
        Output = ['AAAB', 'AABA', 'ABAA', 'BAAA']
"""
import itertools
import time


# Questions you should ask the interviewer (if not explicitly stated):
#   - What is the argument type?  (This may affect some languages more than others.)


# APPROACH: Via Itertools Permutations
#
# This approach simply uses Python's itertools.permutations method.
#
# Time Complexity: O(n!), where n is the length of the string.
# Space Complexity: O(n!), where n is the length of the string.
def get_itertools_perms(s):
    if s is not None:
        return list(set(map(''.join, itertools.permutations(s))))


# APPROACH: Naive Permutation
#
# This solution generates all permutations REGARDLESS if there was already one created, however, it will only add new
# permutations.
#
# Time Complexity: O(n!), where n is the length of the string.
# Space Complexity: O(n!), where n is the length of the string.
def get_perms_w_dups_naive(s):
    if s is not None:
        if len(s) <= 1:
            return [s]
        head = s[0]
        tail_perms = get_perms_w_dups_naive(s[1:])
        result = []
        for l in tail_perms:
            for i in range(len(s)):
                candidate = l[0:i] + head + l[i:len(l)]
                if candidate not in result:
                    result.append(candidate)
        return result


# APPROACH: Naive Permutation Via Set
#
# This solution generates all permutations REGARDLESS if there was already one created, however, since the result is
# first stored as a set, there will be no duplicates.
#
# Time Complexity: O(n!), where n is the length of the string.
# Space Complexity: O(n!), where n is the length of the string.
#
# NOTE: Although this solution is 'naive' (not as cleaver as the dictionary approach below), in many instances it is
# faster than the other approaches.
def get_perms_w_dups_via_set(s):
    if s is not None:
        if len(s) <= 1:
            return [s]
        head = s[0]
        tail_perms = get_perms_w_dups_via_set(s[1:])
        result = set()
        for l in tail_perms:
            for i in range(len(s)):
                result.add(l[0:i] + head + l[i:len(l)])
        return list(result)


# APPROACH: Via Dictionary
#
# This solution uses a dict, which contains each char and the number of times it appears, to only create unique
# permutations (rather than creating duplicate permutations) via building a prefix that is appended to the results when
# the index (which is initialized equal to the length of the string) reaches zero.
#
# For example, given the strings 'ABCDE' and 'AABBC':
#       Permutations('ABCDE') == 5! / (1! * 1! * 1! * 1! * 1!) == 120
#       Permutations('AABBC') == 5! / (2! * 2! * 1!) == 30
#
# Worst Case Time Complexity: O(n!), where n is the length of the string and there are NO duplicates.
# Worst Case Space Complexity: O(n!), where n is the length of the string and there are NO duplicates.
#
# HOWEVER, when there are duplicate characters in the string, AND we only want UNIQUE permutations, the time complexity
# is reduced (divided) by the product of the factorial of each character count, or is:
#   O(n!/(num_c_1! * num_c_2! * ... * num_c_m-1! * num_c_m!)
#
# Time Complexity: O(n!/(num_c_1! * num_c_2! * ... * num_c_m!), where n = len(s), and num_c is the unique char count.
# Space Complexity: O(n!/(num_c_1! * num_c_2! * ... * num_c_m!), where n = len(s), and num_c is the unique char count.
def get_perms_w_dups_vid_dict(s):

    def _get_perms_w_dups_vid_dict(d, i, prefix, result):
        if i == 0:
            result.append(prefix)
        else:
            for k in d.keys():
                if d[k] > 0:
                    d[k] -= 1
                    _get_perms_w_dups_vid_dict(d, i - 1, prefix + k, result)
                    d[k] += 1

    if s is not None:
        result = []
        d = {}
        for c in s:
            d[c] = d.setdefault(c, 0) + 1
        _get_perms_w_dups_vid_dict(d, len(s), "", result)
        return result


# NOTE: The following is the dictionary approach (above) implemented for lists.
def get_list_perms_w_dups_vid_dict(l):

    def _rec(d, i, a, result):
        if i == 0:
            result.append(a[:])
        else:
            for k in d:
                if d[k] > 0:
                    d[k] -= 1
                    a.append(k)
                    _rec(d, i - 1, a, result)
                    a.pop()
                    d[k] += 1

    if l is not None:
        result = []
        d = {}
        for c in l:
            d[c] = d.setdefault(c, 0) + 1
        _rec(d, len(l), [], result)
        return result


args = ["", "A", "AB", "ABC", "AAB", "AAAB", "AAAAB", "AABBC"]
fns = [get_itertools_perms,
       get_perms_w_dups_naive,
       get_perms_w_dups_via_set,
       get_perms_w_dups_vid_dict]

for s in args:
    for fn in fns:
        print(f"{fn.__name__}({repr(s)}): {fn(s)}")
    print()


s = "ABBCCCDDDD"
for fn in fns:
    t = time.time()
    print(f"{fn.__name__}({s!r})", end="")
    fn(s)
    print(f" took {time.time() - t} seconds")


