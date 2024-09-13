"""
    ADD VIA BIT MANIPULATION (CCI 17.1: ADD WITHOUT PLUS,
                              leetcode.com/problems/sum-of-two-integers,
                              50CIQ 19: SUM)

    Given two integers, write a function that returns the integers sum via bit manipulation (no arithmetic operators).

    Example:
        Input = 1, 1
        Output = 2
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Specifically, what operators can't be used?
#   - Input Validation?
#   - What values will the integers have (will be negative)?  (This AFFECTS Python!)
#   - Integer overflow? (This might affect some languages more than others...)


# APPROACH:  Recursive Bitwise Sum & Carry
#
# Use a combination of binary XORs, ANDs, and SHIFTs to sum two numbers.  That is, XOR the numbers to get a partial
# sum (with no carry applied--this will be one of the numbers in the next recursive call), then AND the two numbers (to
# find the carry value for the next call) and continue while b is valid.
#
# NOTE: Since Python integer implementation is dynamic, a mask is needed (in some negative value cases) to prevent
#       infinite loops.
#
# Time Complexity: O(log2(n)), where n is the maximum number of bits needed to represent a or b.
# Space Complexity: O(log2(n)), where n is the maximum number of bits needed to represent a or b.
def add_via_bit_manipulation_rec(a, b):
    mask = 0xffffffff
    if b & mask <= 0:
        return a & mask if b > 0 else a
    xor_sum = a ^ b
    carry = (a & b) << 1
    return add_via_bit_manipulation_rec(xor_sum, carry)
# NOTE: If only positive numbers are considered, this becomes very simple:
# def add_via_bit_manipulation_rec(a, b):
#     if b == 0:
#         return a
#     xor_sum = a ^ b
#     carry = (a & b) << 1
#     return add_via_bit_manipulation_rec(xor_sum, carry)


# APPROACH:  Iterative Bitwise Sum & Carry
#
# This approach uses the same concepts as the recursive approach above, however, this is done in an (iterative) while
# loop, and therefore doesn't add any stack overhead.
#
# Time Complexity: O(log2(N)), where n is the maximum number of bits needed to represent a or b.
# Space Complexity: O(1).
def add_via_bit_manipulation(a, b):
    mask = 0xffffffff
    while b & mask > 0:
        xor_sum = a ^ b
        carry = (a & b) << 1
        a, b = xor_sum, carry
    return a & mask if b > 0 else a
# NOTE: If only positive numbers are considered, this becomes very simple:
# def add_via_bit_manipulation(a, b):
#     while b != 0:
#         xor_sum = a ^ b
#         carry = (a & b) << 1
#         a = xor_sum
#         b = carry
#     return a


# APPROACH: Kogge Stone Adder
#
# This is based on the Kogge-Stone (KSA/KS) look-ahead adder.  This is optimal.
# SEE: en.wikipedia.org/wiki/Kogge-Stone_adder
#
# Time Complexity: O(1).
# Space Complexity: O(1).
def kogge_stone_add(a, b):
    p, g, i = a ^ b, a & b, 1
    while True:
        if (g << 1) >> i == 0:
            return a ^ b ^ (g << 1)
        if ((p | g) << 2) >> i == ~0:
            return a ^ b ^ ((p | g) << 1)
        p, g, i = p & (p << i), (p & (g << i)) | g, i << 1


args = [(1, 0),
        (0, 1),
        (1, 1),
        (2, 3),
        (3, 2),
        (256, 64),
        (10, 1),
        (1, 10),
        (10, 10),
        (10, 20),
        (20, 10),
        (10, -10),
        (-10, 10),
        (-10, -10),
        (10, -20),
        (-10, -20),
        (20, -10),
        (-20, 10),
        (-20, -10)]

fns = [add_via_bit_manipulation_rec,
       add_via_bit_manipulation,
       kogge_stone_add]

for a, b in args:
    for fn in fns:
        print(f"{fn.__name__}({a}, {b}): {fn(a, b)}")
    print()


