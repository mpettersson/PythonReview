"""
    HAS ONE BIT DIFF (50CIQ 35: GRAY CODE)

    Write a function which when given two integers, returns True if their binary representations differs by a single
    bit, False otherwise.

    Example:
        Input = 0, 1
        Output = True
"""


# Approach:  XOR the two numbers; return True if the binary representation contains a single bit, False otherwise.
# Time Complexity: O(1).
# Space Complexity: O(1).
def has_one_bit_diff(x, y):
    if x is not None and y is not None and isinstance(x, int) and isinstance(y, int):
        z = x ^ y
        return z & (z - 1) is 0 and x != y


args = [(0, 1),
        (1, 2),
        (0, 0),
        (131071, 98303),
        (1, -1),
        (0, -1),
        (-1, -2),
        (1, None),
        (None, 1),
        (None, None)]
fns = [has_one_bit_diff]

for fn in fns:
    for x, y in args:
        print(f"{fn.__name__}({x}, {y}): {fn(x, y)}")
    print()


