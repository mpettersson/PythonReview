"""
    STRING ROTATION (CCI 1.9)

    Assume you have a method is_substring() which checks if one word is a substring of another.  Given two strings, s1
    and s2, write code to check if s2 is a rotation of s1 using only one call to is_substring().

    Example:
        Input = "waterbottle", "erbottlewat"
        Output = True
"""


# If both strings are of the same length, then simply concatenates one string on itself will allow the is_substring()
# method to be called only once.
# The runtime depends on is_substring(), however, we can assume that it is O(n).
def is_rotation(s1, s2):
    if len(s1) == len(s2):
        s1s1 = s1 + s1
        return is_substring(s1s1, s2)


# One implementation of is_substring.
def is_substring(s1s1, s1):
    return s1 in s1s1


string_list = [("waterbottle", "erbottlewat"), ("", ""), ("abcdefg", "abcdefg"), ("nope", "nooo")]

for (s1, s2) in string_list:
    print(f"is_rotation(\"{s1}\", \"{s2}\"):", is_rotation(s1, s2), "\n")

