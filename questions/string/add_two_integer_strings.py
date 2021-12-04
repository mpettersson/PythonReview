"""
    ADD TWO INTEGER STRINGS (leetcode.com/problems/add-strings)

    Write a function which accepts two non-negative integer strings (consisting of character digits '0' to' 9') and
    returns a string of their SUM (without directly converting to integers).

    Example:
        Input = '999', '999'
        Output = '1998'

"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What type of characters?
#   - Can the strings have leading zeros (other than a actual zero value)?
#   - What are the estimated lengths of the strings (empty string)?
#   - Negative values, zero value?


# APPROACH: Iterative
#
# This approach is similar to the traditional addition that is taught in elementary schools; add two digits at a time.
# The two number strings are first aligned, then each corresponding digit is added along with the previous carry value.
# If there is a new carry value, it is updated.  The result is put in a list that will be converted (from ints) to
# characters, then joined, and returned.
#
# Time Complexity: O(n), where is the length of the longer of the two strings.
# Space Complexity: O(n), where is the length of the longer of the two strings.
def add_two_integer_strings(a, b):
    if len(a) < len(b):
        a, b = b, a
    n = len(a)
    b = ((n - len(b)) * '0') + b
    i = n - 1
    l = [0] * n
    carry = 0
    while i >= 0:
        temp = int(a[i]) + int(b[i]) + carry
        carry, l[i] = divmod(temp, 10)
        i -= 1
    if carry:
        l.insert(0, carry)
    return ''.join([str(e) for e in l])


args = [('999', '999'),
        ('11', '123'),
        ('123', '456'),
        ('10000', '10000'),
        ('9', '9'),
        ('123', '0'),
        ('0', '123'),
        ('0', '0'),
        ('11111', '111111')]
fns = [add_two_integer_strings]

for a, b in args:
    for fn in fns:
        print(f"{fn.__name__}({a!r}, {b!r}): {fn(a, b)!r}")
    print()


