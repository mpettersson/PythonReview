"""
    NUMBER MAX

    Write a method that finds the maximum of two numbers.  You should not use if-else or any other comparison operators.
"""
import math


def flip_bit(bit):
    return 1 ^ bit


def is_zero(num):
    return (num**2 + (num**2 + 1) - 1) // (num**2 + 1)



def get_sign_bit(num):
    return (num >> int(math.log((num ** 2) ** .5, 2) // 1 + 2)) & 0b1


def get_max(a, b):
    k = flip_bit(get_sign_bit(a - b))
    q = flip_bit(k)
    return k * a + q * b


def get_magic_max(x, y):
    return y ^ ((x ^ y) & -(x < y))

print(flip_bit(0))
print("is_zero(-1)", is_zero(-1))
print("is_zero(0)", is_zero(0))
print("is_zero(1)", is_zero(1))

print("get_max(7, 8)", get_max(7, 8))
print("get_max(8, 7)", get_max(8, 7))
# print("get_max(8, 8)", get_max(8, 8))

print("get_magic_max(7, 8)", get_magic_max(7, 8))
print("get_magic_max(8, 7)", get_magic_max(8, 7))
print("get_magic_max(8, 8)", get_magic_max(8, 8))


# if (test)
#     output = a;
# else
#     output = b;
# output = (((test << 31) >> 31) & a) | (((test << 31) >> 31) & b);
# char  = ((((a - b) >> 31) & l) | (((b - a) >> 31) & g) | ((~((a - b) | (b - a))) >> 31) & e);

