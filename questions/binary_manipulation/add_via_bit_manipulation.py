"""
    ADD VIA BIT MANIPULATION (CCI 17.1: ADD WITHOUT PLUS

    Write a function that adds two numbers.  You should not use + or any other arithmetic operators.

    Example:
        Input =
        Output =
"""


# Basic/Limited Approach:
# Time Complexity:
# Space Complexity:
#
# NOTE: This ONLY works when both a AND b have the same sign.
def add_via_bit_manipulation(a, b):
    while b is not 0:
        sum = a ^ b
        carry = (a & b) << 1
        a = sum
        b = carry
    return a


# Optimal/Correct Kogge  Approach:
# Time Complexity:
# Space Complexity:
#
def kogge_stone_add(a, b):
    p, g, i = a ^ b, a & b, 1
    while True:
        if (g << 1) >> i == 0:
            return a ^ b ^ (g << 1)
        if ((p | g) << 2) >> i == ~0:
            return a ^ b ^ ((p | g) << 1)
        p, g, i = p & (p << i), (p & (g << i)) | g, i << 1


args = [                # XOR, AND, SUM, +-
        (10, 10),       #   0,  10,  20,
        # (10, -10),    #  -4,   2,   0, -b
        # (-10, 10),    #  -4,   2,   0, -a
        (-10, -10),     #   0, -10, -20,  -
        (10, 20),       #  30,   0,  30,
        (10, -20),      # -26,   8, -10, -b
        (-10, -20),     #  26, -28, -30,  -
        (20, 10),       #  30,   0,  30,
        # (20, -10),    # -30,  20,  10, -b
        (-20, 10),      # -26,   8, -10, -a
        (-20, -10),     #  26, -28, -30,  -
        ]
fns = [add_via_bit_manipulation,
       kogge_stone_add]
# import operator

# fns = [operator.xor, operator.and_]
for fn in fns:
    for a, b in args:
        print(f"{fn.__name__}({a}, {b}): {fn(a, b)}")
    print()

