"""
    ONE AWAY (CCI 1.5)

    Write a method, which given two strings, will return True if the two strings are one edit away from each other.
    An edit can be adding, deleting, or changing a character.

    Example:
        Input = "abcde", "abfde"
        Output = True
"""


# Runtime is O(n), where n is the length of the shorter string, and space complexity is O(1).
def is_one_away(s1, s2):
    if len(s1) == len(s2):
        return is_one_away_same_len(s1, s2)
    else:
        return is_one_away_diff_len(s1, s2)


def is_one_away_same_len(s1, s2):
    num_diff = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            num_diff += 1
            if num_diff > 1:
                return False
    return True


def is_one_away_diff_len(s1, s2):
    if len(s1) + 1 == len(s2) or len(s2) + 1 == len(s1):
        if len(s2) > len(s1):
            s2, s1 = s1, s2
        num_diff = i = 0
        while i < len(s2):
            if s1[i + num_diff] == s2[i]:
                i += 1
            else:
                num_diff += 1
                if num_diff > 1:
                    return False
        return True
    return False


# Runtime is O(n), where n is the length of the shorter string, and space complexity is O(1).
# This is essentially the same as above, just combined, so might not be as easy to understand...
def one_away(first, second):
    if abs(len(first) - len(second)) > 1:
        return False
    s1 = first if len(first) < len(second) else second
    s2 = second if len(first) < len(second) else first
    i = j = 0
    has_diff = False
    while j < len(s2) and i < len(s1):
        if s1[i] != s2[j]:
            if has_diff:
                return False
            has_diff = True
            if len(s1) < len(s2):
                j += 1
            elif len(s1) == len(s2):
                i += 1
                j += 1
        else:
            i += 1
            j += 1
    return True


string_list = [("abcde", "abcd"), ("abde", "abcde"), ("a", "a"), ("a", ""), ("", ""), ("", "a"), ("abcdef", "abqdef"),
               ("abcdef", "abccef"), ("abcdef", "abcde"), ("aaa", "abc"), ("abcde", "abc"), ("abc", "abcde"),
               ("abc", "bcc")]

for (s1, s2) in string_list:
    print(f'is_one_away("{s1}", "{s2}"):', is_one_away(s1, s2))
print()

for (s1, s2) in string_list:
    print(f'one_away("{s1}", "{s2}"):', one_away(s1, s2))

