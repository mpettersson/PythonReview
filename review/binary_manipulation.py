import sys

# NOTE: The BitVector package (pip3 install BitVector) is an OTS solution.

# REMEMBER:
#   &  - Binary AND	Operator copies a bit to the result if it exists in both operands
#   |  - Binary OR	It copies a bit if it exists in either operand.
#   ^  - Binary XOR	It copies the bit if it is set in one operand but not both.
#   ~  - Binary Ones Complement	It is unary and has the effect of 'flipping' bits.
#   <<  - Binary Left Shift	The left operands value is moved left by the number of bits specified by the right operand.
#   >>  - Binary Right Shift: The left operands value is moved right by the num of bits specified by the right operand.


# NOTE: Python doesn't have the >>> binary op, so this method simulates it.
#       >>> shifts right but will replace the most significant bit with 0 (EVEN if the number was negative)
def logical_right_shift(num, i, num_bits=32):
    return (num % 0x100000000) >> i


def is_power_two(n):
    if n == 0:
        return False
    n = abs(n)                  # I want to include negative powers of two, if you don't, remove this line.
    return n & (n - 1) == 0


# SEE: https://stackoverflow.com/questions/21871829/twos-complement-of-numbers-in-python
def bin_twos_complement(num, num_bits=32):
    if num < 0:
        num = (1 << num_bits) + num
    formatstring = '{:0%ib}' % num_bits
    return formatstring.format(num)


def get_sign_bit(num):
    return -(num >> num.bit_length())   # Have to use .bit_length() bc we don't know the length of num.
    # return -(num >> 31)               # If num is 32 bit.
    # return -(num >> 63)               # If num is 64 bit.


def get_bits_as_list(n):
    if n is 0:
        return [0]
    l = [(n >> i) & 1 for i in range(n.bit_length())]   # if n != 0 then n.bit_length() == int(math.log(abs(n), 2)) + 1
    l.reverse()
    return [1] + l if n < 0 else [0] + l


def get_ith_bit(num, i):
    return 1 if (num & (1 << i)) else 0


def set_ith_bit_to_1(num, i):
    return num | (1 << i)


def set_ith_bit_to_0(num, i):
    return num & ~(1 << i)


def set_most_sig_to_ith_bit_to_0(num, i):
    return num & ((1 << i) - 1)


def set_0_to_ith_bit_to_0(num, i):
    return num & ~(logical_right_shift(-1, 31 - i))


def set_ith_bit(num, i, val):
    if val < 0 or val > 1:
        raise Exception
    return (num & ~(1 << i)) | (val << i)


def get_most_sig_one_bit_location(num):
    num = abs(num)
    position = 0
    while num > 1:
        num = num >> 1
        position += 1
    return position


def get_least_sig_one_bit_location(num):
    num = abs(num)
    position = 0
    while (num & 1) is 0:
        num = num >> 1
        position += 1
    return position


# Given an num, print the next largest number that have the same number of 1 bits in their bin rep
def get_next_larger(num):
    c0 = c1 = 0
    temp = num
    # find number of trailing zeros
    while (temp & 1) is 0 and temp is not 0:
        temp = temp >> 1
        c0 += 1
    # find number of ones after trailing zeros
    while (temp & 1) is 1:
        temp = temp >> 1
        c1 += 1
    if c0 + c1 is 0:
        return None
    # the bit we need to flip to a one
    p = c0 + c1
    num = num | 1 << p
    num = num & ~((1 << p) - 1)
    num = num | ((1 << (c1 - 1)) - 1)
    return num


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


# Given an num, print the next smaller number that have the same number of 1 bits in their bin rep
def get_next_smaller(num):
    c0 = c1 = 0
    temp = num
    while (temp & 1) is 1:                          # find number of trailing ones
        temp = temp >> 1
        c1 += 1
    if temp is 0:                                   # if the number was all ones then there is no next smallest...
        return None
    while (temp & 1) is 0 and temp is not 0:        # find number of zeros after trailing ones
        temp = temp >> 1
        c0 += 1
    p = c0 + c1                                     # the bit we need to flip to a one
    num = num & ((~0) << (p + 1))
    mask = (1 << (c1 + 1)) - 1
    num |= mask << (c0 - 1)
    return num


def num_bits_to_flip_to_convert_a_to_b(a, b):
    c = a ^ b
    num = 0
    while c > 0:
        num += 1
        c = c & (c - 1)     # Each time the least sig 1 is removed
    return num


def swap_odd_even_bin_bits(num):
    return (logical_right_shift((num & 0xaaaaaaaa), 1)) | ((num & 0x55555555) << 1)


# How to enter binary in python
print("0B1010:  ", 0B1010)
print("-0B1010:", -0B1010)
print('"{bin(9)}": ', f" {bin(9)}")                     # '0b1001'
print('"{bin(-9)}":', f"{bin(-9)}")                     # '-0b1001'
print('"{0:07b}".format(9): ', "{0:07b}".format(9))     # '0001001'
print('"{0:07b}".format(-9):', "{0:07b}".format(-9))    # '-001001'
print('"{7:b}".zfill(8): ', f"{7:b}".zfill(8))          # '00000111'
print('"{-7:b}".zfill(8):', f"{-7:b}".zfill(8))         # '-0000111'
print()

# Misc. Binary Stuff
print("sys.byteorder:", sys.byteorder)
zero = 0; print("zero:", zero)
pos_n = 8; print("pos_n:", pos_n)
neg_n = -8; print("neg_n:", neg_n)
print("zero.bit_length():", zero.bit_length())          # NOTE: This should be 1, not 0!!
print("pos_n.bit_length():", pos_n.bit_length())
print("neg_n.bit_length():", neg_n.bit_length())
print('pos_n.to_bytes(4, "big", signed=True):', pos_n.to_bytes(4, "big", signed=True))
print('neg_n.to_bytes(4, "big", signed=True):', neg_n.to_bytes(4, "big", signed=True))
print('pos_n.to_bytes(4, "little", signed=True):', pos_n.to_bytes(4, "little", signed=True))
print('neg_n.to_bytes(4, "little", signed=True):', neg_n.to_bytes(4, "little", signed=True))
steak = int.from_bytes(b'\xde\xad\xbe\xef', byteorder='big')
joe = int.from_bytes(b'\xc0\xff\xee', 'little')
hw = int.from_bytes(b"Hello World!!!", 'big')
int.to_bytes(hw, (hw.bit_length() // 8)+1, 'big')
print()

# test logical_right_shift
print("logical_right_shift(0b1010, 1):", bin(logical_right_shift(0b1010, 1)))
print("logical_right_shift(-0b1010, 1):", bin(logical_right_shift(-0b1010, 1)))
print()

# test get_bit
for n in [-0x15, 0x15, 0b1001, -0b1001, -2, 2, 128, 255, 256, -256]:
    print(f"get_bits_as_list({n}): {get_bits_as_list(n)}")
print()

# test get_sign_bit:
print("get_sign_bit(0b1010):", bin(get_sign_bit(0b1010)))
print("get_sign_bit(-0b1010):", bin(get_sign_bit(-0b1010)))
print()

# test get_ith_bit
print("get_ith_bit(0b1010, 0):", bin(get_ith_bit(0b1010, 0)))
print()

# test set_ith_bit_to_1
print("set_ith_bit_to_1(0b1010, 0):", bin(set_ith_bit_to_1(0b1010, 0)))
print("set_ith_bit_to_1(0b1010, 1):", bin(set_ith_bit_to_1(0b1010, 1)))
print()

# test set_ith_bit_to_0
print("set_ith_bit_to_0(0b1010, 0):", bin(set_ith_bit_to_0(0b1010, 0)))
print("set_ith_bit_to_0(0b1010, 1):", bin(set_ith_bit_to_0(0b1010, 1)))
print()

# test set_most_sig_to_ith_bit_to_0
print("set_most_sig_to_ith_bit_to_0(0b1010, 0):", bin(set_most_sig_to_ith_bit_to_0(0b1010, 0)))
print("set_most_sig_to_ith_bit_to_0(0b1010, 3):", bin(set_most_sig_to_ith_bit_to_0(0b1010, 3)))
print()

# test set_0_to_ith_bit_to_0
print("set_0_to_ith_bit_to_0(0b101010101010, 0):", bin(set_0_to_ith_bit_to_0(0b101010101010, 0)))
print("set_0_to_ith_bit_to_0(0b101010101010, 3):", bin(set_0_to_ith_bit_to_0(0b101010101010, 3)))
print()

# test set_ith_bit
print("set_ith_bit(0b1010, 0, 1):", bin(set_ith_bit(0b1010, 0, 1)))
print("set_ith_bit(0b1010, 3, 0):", bin(set_ith_bit(0b1010, 3, 0)))
print()

# test get_most_sig_one_bit_location
print("get_most_sig_one_bit_location(0b1010):", get_most_sig_one_bit_location(0b1010))
print("get_most_sig_one_bit_location(-0b1010)", get_most_sig_one_bit_location(-0b1010))
print()

# test get_least_sig_one_bit_location
print("get_least_sig_one_bit_location(0b1010):", get_least_sig_one_bit_location(0b1010))
print("get_least_sig_one_bit_location(0b1011):", get_least_sig_one_bit_location(0b1011))
print()

# test add_via_bit_manipulation
print("add_via_bit_manipulation(0b1010, 0b1011):", add_via_bit_manipulation(0b1010, 0b1011))
print("add_via_bit_manipulation(0b10, 0b1111):", add_via_bit_manipulation(0b10, 0b1111))
print()

# test add_via_bit_manipulation
print("kogge_stone_add(0b1010, 0b1011):", kogge_stone_add(0b1010, 0b1011))
print("kogge_stone_add(0b10, 0b1111):", kogge_stone_add(0b10, 0b1111))
print()

# test get_next_larger
print("get_next_larger(0b1011):", bin(get_next_larger(0b1011)))
print("get_next_larger(0b11011001111100):", bin(get_next_larger(0b11011001111100)))
print()

# test get_next_larger
print("get_next_smaller(0b1011):", bin(get_next_smaller(0b1011)))
print("get_next_smaller(0b1001110000011):", bin(get_next_smaller(0b1001110000011)))
print()

# test num_bits_to_flip_to_convert_a_to_b
print("num_bits_to_flip_to_convert_a_to_b(0b11101, 0b1111):", num_bits_to_flip_to_convert_a_to_b(0b11101, 0b1111))
print()

# test swap_odd_even_bin_bits
print("swap_odd_even_bin_bits(0b111000111000):", bin(swap_odd_even_bin_bits(0b111000111000)))
print("swap_odd_even_bin_bits(0b110011001):", bin(swap_odd_even_bin_bits(0b110011001)))
