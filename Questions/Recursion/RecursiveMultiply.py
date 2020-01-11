"""
    RECURSIVE MULTIPLY

    Write a recursive function to multiply two numbers without using the * operator.
    You can use addition, subtraction, and bit shifting, but you should minimize the number of those operations.
"""


def rec_mult_smaller(a, b):
    if a > b:
        a, b = b, a
    return rec_mult(a, b)


def rec_mult(a, b):
    print("a:", a, "b:", b)
    if a is 0 or b is 0:
        return 0
    if a is 1:
        return b
    half_prod = rec_mult(a >> 1, b)     # Int divide a by two.
    return half_prod + half_prod + (0 if a % 2 is 0 else b)


print("rec_mult(3, 5):", rec_mult_smaller(50, 5))
