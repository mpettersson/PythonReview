"""
    PERMUTATIONS WITHOUT DUPS

    Write a method to compute all permutations of a string of unique characters.
"""


def perm_without_dups(s):
    if len(s) is 1:
        return [s]
    head = s[0]
    tail_perms = perm_without_dups(s[1:])
    perms_list = []
    for l in tail_perms:
        for i in range(len(s)):
            perms_list.append(l[0:i] + head + l[i:len(l)])
    return perms_list


perms = perm_without_dups("ABCDE")
print(perms)
