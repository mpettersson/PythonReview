"""
    GRAY CODE (50CIQ 35: GRAY CODE)

    Write a function which when given two integers, returns True if their binary representations differs by a single
    bit, False otherwise.

    Example:
        Input = 0, 1
        Output = True

    NOTE: Alternate phrasing may ask if two numbers are sequential numbers in a RCB/RB/gray code. Where the reflected
      binary code (RBC), also known just as reflected binary (RB) or Gray code after Frank Gray, is an ordering of
      the binary numeral system such that two successive values differ in only one bit (binary digit).

    SEE: https://en.wikipedia.org/wiki/Gray_code
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Clarify problem (same number, negative numbers, etc...)?
#   - Input Validation?


# Approach: Via Binary Operations (XOR and &)
#
# XOR the two numbers; return True if the binary representation contains a single bit, False otherwise.
#
# NOTE: The KEY to this solution, is realizing that you must FIRST XOR the two numbers.
#
# Time Complexity: O(1).
# Space Complexity: O(1).
def has_one_bit_diff(x, y):
    if x is not None and y is not None and isinstance(x, int) and isinstance(y, int):
        z = x ^ y
        return z & (z - 1) == 0 and x != y


args = [(0, 1),
        (1, 2),
        (0, 0),
        (131071, 98303),
        (1, -1),
        (-2, -3),
        (-1, -4),
        (16, 17),
        (3, 17),
        (16, 3),
        (16, 24),
        (16, 18),
        (1, None),
        (None, None)]
fns = [has_one_bit_diff]

for x, y in args:
    for fn in fns:
        print(f"{fn.__name__}({x}, {y}): {fn(x, y)}")


