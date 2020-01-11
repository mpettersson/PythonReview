"""
    SUBTRACT WITHOUT MINUS

    Write a function that subtracts one number from another.  You should not use - or any other arithmetic operators.
"""


# NOTE: This ONLY works when both a AND b have the same sign (can be negative).
def sub_via_bit_manipulation(a, b):
    while b is not 0:
        borrow = (~a) & b
        a = a ^ b
        b = borrow << 1
    return a


print("sub_via_bit_manipulation(3, 3):", sub_via_bit_manipulation(3, 3))
print("sub_via_bit_manipulation(-3, -3):", sub_via_bit_manipulation(-3, -3))






