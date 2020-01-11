"""
    ADD WITHOUT PLUS

    Write a function that adds two numbers.  You should not use + or any other arithmetic operators.
"""


# NOTE: This ONLY works when both a AND b have the same sign.
def add_via_bit_manipulation(a, b):
    while b is not 0:
        sum = a ^ b
        carry = (a & b) << 1
        a = sum
        b = carry
    return a


def kogge_stone_add(a, b):
    p, g, i = a ^ b, a & b, 1
    while True:
        if (g << 1) >> i == 0:
            return a ^ b ^ (g << 1)
        if ((p | g) << 2) >> i == ~0:
            return a ^ b ^ ((p | g) << 1)
        p, g, i = p & (p << i), (p & (g << i)) | g, i << 1


print("add_via_bit_manipulation(3, 3):", add_via_bit_manipulation(3, 3))
print("add_via_bit_manipulation(-3, -3):", add_via_bit_manipulation(-3, -3))
print()

print("kogge_stone_add(3, 3):", kogge_stone_add(3, 3))
print("kogge_stone_add(-3, 3):", kogge_stone_add(-3, 3))
print("kogge_stone_add(3, -3):", kogge_stone_add(3, -3))
print("kogge_stone_add(-3, -3):", kogge_stone_add(-3, -3))


