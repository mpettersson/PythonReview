"""
    PERMUTATIONS WITH DUPS

    Write a method to compute all permutations of a string of non-unique characters.
"""


# This generates all perm REGARDLESS if there was already one created, it then will only add it if it's new.
# This is always O(n!) time.
def perm_with_dups_slow(s):
    if len(s) is 1:
        return [s]
    head = s[0]
    tail_perms = perm_with_dups_slow(s[1:])
    perms_list = []
    for l in tail_perms:
        for i in range(len(s)):
            if l[0:i] + head + l[i:len(l)] not in perms_list:
                perms_list.append(l[0:i] + head + l[i:len(l)])
    return perms_list


# This creates a dict with number of each character in the string.
def perm_with_dups(s):
    results = []
    s_map = {}
    for c in s:
        if c not in s_map.keys():
            s_map[c] = 0
        s_map[c] = s_map[c] + 1
    _perm_with_dups(s_map, "", len(s), results)
    return results


def _perm_with_dups(s_map, prefix, remaining, results):
    if remaining is 0:
        results.append(prefix)
    for k in s_map.keys():
        v = s_map[k]
        if v > 0:
            s_map[k] = v - 1
            _perm_with_dups(s_map, prefix + k, remaining - 1, results)
            s_map[k] = v


string_to_perm = "AAAAAADAAAAAAAABAAAC"
print("string_to_perm:", string_to_perm)
print("len(perm_with_dups(string_to_perm)):", len(perm_with_dups(string_to_perm)))
print("len(perm_with_dups_slow(string_to_perm)):", len(perm_with_dups_slow(string_to_perm)))
exit()
