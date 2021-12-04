"""
    ADD TWO BINARY STRINGS (leetcode.com/problems/add-binary)

    Write a function which accepts two binary strings (consisting of '0's and '1's), and returns a string of their sum.

    Example:
        Input = '1111', '1'
        Output = '10000'

"""
import time


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What type of characters?
#   - What are the estimated lengths of the strings (empty string)?
#   - Negative values?


# APPROACH: Pythonic Approach
#
# NOTE: This approach is generally faster than the approach below.
#
# Use pythons (built in) int method to add the two numbers, then pythons (built in) bin method to convert the result to
# a string (slicing off the '0b' prefix).
#
# Time Complexity: O(n), where n is the maximum number of characters in the two strings.
# Space Complexity: O(n), where n is the maximum number of characters in the two strings.
def add_two_binary_strings_pythonic(a, b):
    result = int(a, base=2) + int(b, base=2)
    return bin(result)[2:] if result > 0 else bin(result)[3:]


# APPROACH: Iterative
#
# This approach manually pads the strings (if they are not the same size), then performs binary addition, appending to
# a result list, that is then reversed, joined, and returned.
#
# Time Complexity: O(n), where n is the maximum number of characters in the two strings.
# Space Complexity: O(n), where n is the maximum number of characters in the two strings.
def add_two_binary_strings(a, b):
    result = []
    if len(a) < len(b):
        a, b = b, a
    n = len(a)
    b = (n - len(b)) * '0' + b
    i = n - 1
    carry = 0
    while 0 <= i:
        if b[i] == a[i] == '1':
            if carry:
                result.append('1')
            else:
                result.append('0')
            carry = 1
        elif b[i] == a[i] == '0':
            if carry:
                result.append('1')
            else:
                result.append('0')
            carry = 0
        else:
            if carry:
                result.append('0')
            else:
                result.append('1')
        i -= 1
    if carry:
        result.append('1')
    return ''.join(reversed(result))


args = [('1111', '1'),
        ('11', '1'),
        ('1', '11'),
        ('1010', '1011'),
        ('0', '11111'),
        ('11111', '111111')]
fns = [add_two_binary_strings_pythonic,
       add_two_binary_strings]

for a, b in args:
    for fn in fns:
        print(f"{fn.__name__}({a!r}, {b!r}): {fn(a, b)!r}")
    print()

t_args = [('1', '1'),
          ('11111', '11111'),
          ('1111111111', '1111111111'),
          ('11111111111111111111', '11111111111111111111')]
for a, b in t_args:
    for fn in fns:
        print(f"{fn.__name__}({a}, {b}) took ", end='')
        t = time.time()
        fn(a, b)
        print(f"{time.time() - t} seconds.")
    print()


