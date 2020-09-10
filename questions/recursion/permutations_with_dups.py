"""
    PERMUTATIONS WITH DUPS (CCI 8.8)

    Write a method to compute all permutations of a string of non-unique characters.

    Example:
        Input = "AAAB"
        Output = ['AAAB', 'AABA', 'ABAA', 'BAAA']
"""
import itertools
import time


# Itertools Permutations Approach:  Time and space is O(n!), where n is the size of the string s.
def get_itertools_perms(s):
    if s is not None:
        return list(set(map(''.join, itertools.permutations(s))))


# Naive Approach: This solution generates all permutations REGARDLESS if there was already one created, however, it will
# only add new permutations. Time and space is O(n!), where n is the size of the string s.
def get_perms_w_dups_naive(s):
    if s is not None:
        if len(s) <= 1:
            return [s]
        head = s[0]
        tail_perms = get_perms_w_dups_naive(s[1:])
        perms_list = []
        for l in tail_perms:
            for i in range(len(s)):
                if l[0:i] + head + l[i:len(l)] not in perms_list:
                    perms_list.append(l[0:i] + head + l[i:len(l)])
        return perms_list


# Dictionary Approach: This solution uses a dict, which contains each char and the number of times it appears, to only
# create unique permutations (rather than creating duplicate permutations).
#
# The WORST CASE time and space is still O(n!), where n is the size of the string s. HOWEVER, when there are duplicate
# characters in the string, AND we only want UNIQUE permutations, the time complexity is reduced (divided) by the
# product of the factorial of each character count, or is: O(n!/(num_c_1! * num_c_2! * ... * num_c_m-1! * num_c_m!)
#
# For example, given the strings 'ABCDE' and 'AABBC':
#       Permutations('ABCDE') == 5! / (1! * 1! * 1! * 1! * 1!) == 120
#       Permutations('AABBC') == 5! / (2! * 2! * 1!) == 30
def get_perms_w_dups(s):

    def _get_perms_w_dups(d, i, prefix, results):
        if i is 0:
            results.append(prefix)
        else:
            for k in d.keys():
                if d[k] > 0:
                    d[k] -= 1
                    _get_perms_w_dups(d, i - 1, prefix + k, results)
                    d[k] += 1

    if s is not None:
        results = []
        d = {}
        for c in s:
            d[c] = d.setdefault(c, 0) + 1
        _get_perms_w_dups(d, len(s), "", results)
        return results


args = ["", "A", "AB", "ABC", "AAB", "AAAB", "AAAAB", "AABBC"]

for s in args:
    print(f"get_itertools_perms({repr(s)}): {get_itertools_perms(s)}")
print()

for s in args:
    print(f"perm_with_dups_naive({repr(s)}): {get_perms_w_dups_naive(s)}")
print()

for s in args:
    print(f"perm_with_dups({repr(s)}): {get_perms_w_dups(s)}")
print()

s = "ABBCCCDDDD"
t = time.time(); print(f"get_itertools_perms({s!r})", end=""); get_itertools_perms(s); print(f" took {time.time() - t} seconds")
t = time.time(); print(f"perm_with_dups_naive({s!r})", end=""); get_perms_w_dups_naive(s); print(f" took {time.time() - t} seconds")
t = time.time(); print(f"perm_with_dups({s!r})", end=""); get_perms_w_dups(s); print(f" took {time.time() - t} seconds")


