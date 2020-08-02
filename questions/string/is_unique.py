"""
    IS UNIQUE (CCI 1.1)

    Implement an algorithm to determine if a string has all unique characters.

    Example:
        Input = "abcdefgh)h(ijk-limopqr'stuvwxyz_/#@!"
        Output = False

    What if you cannot use additional data structures?
"""


# A naive approach would be to compare every character to every other char in the string, this would have a runtime of
# O(n^2) and a space complexity of O(1).
def is_unique_naive(string):
    if string:
        i = 0
        while i < len(string) - 1:
            j = i + 1
            while j < len(string):
                if string[i] == string[j]:
                    return False
                j += 1
            i += 1
    return True


# Runtime is O(n), space complexity is O(n)
# NOTE: If you knew the size of the alphabet (for example extended ASCII with 256 char) then you can improve performance
# and drop the space complexity to O(1) (a fixed size).
def is_unique_with_extra_ds(string):
    if string is not None:
        s = set()
        for c in string:
            if c in s:
                return False
            s.add(c)
    return True


# Runtime is O(n log n), space complexity is O(1)
# NOTE: Some sorting algorithms use extra space (thus rendering the additional data structure constraint moot).
def is_unique_sorted(string):
    if string is not None and len(string) > 0:
        s = sorted(string)
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                return False
    return True


str_list = ["abcdefgh)(ijk-limopqr'stuvwxyz_/#@!", "abcdefg)h(ijk-lmopqr'stuvwxyz_/#@!", "Hello\t \nWorld",
            "HeIlo\t \nWOrLd", "", None]

for s in str_list:
    print(f"is_unique_naive({s!r}):", is_unique_naive(s))
print()

for s in str_list:
    print(f"is_unique_with_extra_ds({s!r}):", is_unique_with_extra_ds(s))
print()

for s in str_list:
    print(f"is_unique_sorted({s!r}):", is_unique_sorted(s))
