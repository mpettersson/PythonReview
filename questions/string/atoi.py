"""
    ATOI (leetcode.com/problems/string-to-integer-atoi)

    Write a function to converts a given string to a 32-bit signed integer (similar to C/C++'s atoi function), with the
    following rules:
        1.  Read in and ignore any leading whitespace.
        2.  Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in
            if it is either. This determines if the final result is negative or positive respectively. Assume the result
            is positive if neither is present.
        3.  Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest
            of the string is ignored.
        4.  Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the
            integer is 0. Change the sign as necessary (from step 2).
        5.  If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it
            remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater
            than 2**31 - 1 should be clamped to 2**31 - 1.
        6.  Return the integer as the final result.

    Example:
        Input = "  -42"
        Output = -42
"""
import re


# APPROACH: Via List Of Characters
#
# This approach builds a list of characters (which match the rules), then convert the list to a string, then to an int,
# then limits the range (if needed), and finally returns the value (as an int).
#
# Time Complexity: O(n), where n is the length of the string.
# Space Complexity: O(n), where n is the length of the string.
def atoi(s):
    result = ["0"]
    n = len(s)
    neg_flag = False
    i = 0
    while i < n and s[i] == ' ':
        i += 1
    if i < n and s[i] == '-':
        i += 1
        neg_flag = True
    elif i < n and s[i] == '+':
        i += 1
    while i < n and s[i].isnumeric():
        result.append(s[i])
        i += 1
    result = int(''.join(result)) * (-1 if neg_flag else 1)
    if result < -2 ** 31:
        return -2 ** 31
    if result > 2 ** 31 - 1:
        return 2 ** 31 - 1
    return result


# APPROACH: Via RE
#
# This approach uses a regular expression to isolate the string prefix that starts with a plus or minus (optional), that
# is followed by digits.  The prefix is converted to an integer, then reduced to the proper range (if needed) and
# returned.
#
# Time Complexity: O(n), where n is the length of the string.
# Space Complexity: O(n), where n is the length of the string.
def atoi_via_re(s: str) -> int:
    s = s.strip()
    s = re.findall("^[\+\-]?\d+", s)
    try:
        res = int("".join(s))
        MIN = -2 ** 31
        MAX = 2 ** 31 - 1
        if res > MAX:
            return MAX
        if res < MIN:
            return MIN
        return res
    except:
        return 0


args = ["42",                       # Returns: 42
        "  -42",                    # Returns: -42
        "12.34",                    # Returns: 12
        "-12.34",                   # Returns: -12
        "+12.34",                   # Returns: 12
        "1982 in born",             # Returns: 1984
        "born in 1984",             # Returns: 0
        "bornin1984",               # Returns: 0
        "-90123456789",             # Returns: -2147483648  (or -2**31)
        "90123456789",              # Returns: 2147483647   (or 2**31-1)
        ""]                         # Returns: 0
fns = [atoi,
       atoi_via_re]

for s in args:
    print(f"s: {s!r}")
    for fn in fns:
        print(f"{fn.__name__}(s): {fn(s)!r}")
    print()


