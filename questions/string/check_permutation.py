"""
    CHECK PERMUTATION (CCI 1.2)

    Given two strings, write a method to decide if one is a permutation of the other.

    Example:
        Input = "race", "acre"
        Output = True

    NOTE: You ought to ask the interviewer for clarification on spaces, capitalization, text type (ASCII/Unicode), etc.
"""


# Via sorting, with O(n log n) time and O(1) space complexity:
def check_permutation_via_sort(s1, s2):
    if not s1 and not s2 or len(s1) == len(s2) == 0:
        return True
    if len(s1) == len(s2):
        ss1 = sorted(s1)
        ss2 = sorted(s2)
        if ss1 == ss2:
            return True
    return False


# Via two dictionaries, with O(n) time and O(n) space complexity:
def check_permutation_via_dict(s1, s2):
    if not s1 and not s2 or len(s1) == len(s2) == 0:
        return True
    if len(s1) == len(s2):
        d1 = dict()
        d2 = dict()
        for i in range(len(s1)):
            d1[s1[i]] = d1[s1[i]] + 1 if s1[i] in d1 else 1
            d2[s2[i]] = d2[s2[i]] + 1 if s2[i] in d2 else 1
        if d1.keys() == d2.keys():
            for k in d1.keys():
                if d1[k] != d2[k]:
                    return False
            return True
    return False


string_list = [("race", "acre"), ("aaaaa", "aaaa"), ("", ""), (None, None)]

for (s1, s2) in string_list:
    print(f"check_permutation_via_sort({s1}, {s2}):", check_permutation_via_sort(s1, s2))
print()

for (s1, s2) in string_list:
    print(f"check_permutation_via_dict({s1}, {s2}):", check_permutation_via_dict(s1, s2))

