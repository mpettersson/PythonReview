"""
    ADD VIA BIT MANIPULATION (CCI 17.1: ADD WITHOUT PLUS,
                              leetcode.com/problems/sum-of-two-integers)

    Write a function which accepts two integers, then returns their sum via bit manipulation (no arithmetic operators).

    Example:
        Input = 1, 1
        Output = 2
"""


# Basic/Limited Approach: TODO
# Time Complexity: TODO
# Space Complexity: O(1).
#
# NOTE: This DOESN'T work for some combinations of positive and negative values.
def add_via_bit_manipulation(a, b):
    while b != 0:
        sum = a ^ b
        carry = (a & b) << 1
        a = sum
        b = carry
    return a


# Optimal (Correct) Kogge Stone Adder Approach:  This is based on the Kogge-Stone (KSA/KS) look-ahead adder.
# SEE: en.wikipedia.org/wiki/Kogge-Stone_adder
# Time Complexity: TODO
# Space Complexity: O(1).
def kogge_stone_add(a, b):
    p, g, i = a ^ b, a & b, 1
    while True:
        if (g << 1) >> i == 0:
            return a ^ b ^ (g << 1)
        if ((p | g) << 2) >> i == ~0:
            return a ^ b ^ ((p | g) << 1)
        p, g, i = p & (p << i), (p & (g << i)) | g, i << 1


                        # XOR, AND, SUM, +-
args = [(1, 1),
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

for fn in fns:
    for a, b in args:
        print(f"{fn.__name__}({a}, {b}): {fn(a, b)}")
    print()


