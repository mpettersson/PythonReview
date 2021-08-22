"""
    NUM ONES IN BIN NUM (50CIQ 36: NUMBER OF ONES IN A BINARY NUMBER)

    Write a function, which accepts an integer n, and returns the number of '1' bits in the binary representation of n.

    Example:
        Input = 31
        Output = 5

    Variation:
        - Write a function, which accepts an integer n, and returns the number of '1' non-sign bits in the binary
          representation of n.
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Clarify problem (NEGATIVE NUMBERS/SIGN BITS, num bit length, etc...)?
#   - Input Validation?


# APPROACH: Naive Shift And Compare
#
# While n is not zero and the number of bits compared so far is less than the total bit length/num_bits, iteratively add
# one to the result if the lowest bit (of the binary representation) is a one, then return the result.
#
# Time Complexity: O(log(n)) or, O(b), where b is the number of bits in the binary representation of n.
# Space Complexity: O(1).
def num_ones_in_bin_num_naive(n, num_bits=32):
    if isinstance(n, int):
        count = i = 0                       # i is only used if n was negative.
        while n != 0 and i < num_bits:
            count += n & 1
            n >>= 1
            i += 1
        return count


# APPROACH: Kernighan's Algorithm
#
# This approach repetitively clears the least significant set bit, adding one to count for each iteration, and
# (normally) ends when n is zero, or (because of Pythons integer implementation,) when n is less than or equal to
# -2 ** bit length.
#
# SEE: https://en.wikipedia.org/wiki/Brian_Kernighan for more on Brian.
#
# Time Complexity: O(log(n)) or, O(b), where b is the number of bits in the binary representation of n.
# Space Complexity: O(1).
def num_ones_in_bin_num_kernighan(n, num_bits=32):
    if isinstance(n, int):
        count = 0
        while n > 0 or -2 ** num_bits < n < 0:
            count += 1
            n &= (n - 1)
        return count
# NOTE: If Python used a 32bit integer implementation, Kernighan's algorithm would be:
#           def kernighan(n):
#               count = 0
#               while n != 0:
#                   count += 1
#                   n &= (n - 1)
#               return count


# VARIATION: Write a function, which accepts an integer n, and returns the number of '1' non-sign bits in the binary
#            representation of n.

# NOTE: Similar to each positive power of having a single 1 bit count, all negative powers of two, when excluding sign
#       bits, will have a 1 bit count of zero.


# VARIATION APPROACH: Shift And Compare (Exclude Sign Bits)
#
# While n is not zero or negative one, iteratively add one to the result if the lowest bit (of the binary
# representation) is a one, then return the result.
#
# Time Complexity: O(log(n)) or, O(b), where b is the number of bits in the binary representation of n.
# Space Complexity: O(1).
def num_ones_in_bin_num_naive_exclude_sign_bits(n, num_bits=32):
    if isinstance(n, int):
        count = 0
        while n != 0 and n != -1:       # If n was negative, then n will converge to -1 (not 0, like positive nums).
            count += n & 1
            n >>= 1
        return count


# VARIATION APPROACH: Kernighan's Algorithm (Exclude Sign Bits)
#
# This approach repetitively clears the least significant set bit, adding one to count for each iteration, and
# (normally) ends when n is zero, or (because of Pythons integer implementation,) when n is less than or equal to
# -2 ** bit length.
#
# SEE: https://en.wikipedia.org/wiki/Brian_Kernighan for more on Brian.
#
# Time Complexity: O(log(n)) or, O(b), where b is the number of bits in the binary representation of n.
# Space Complexity: O(1).
def num_ones_in_bin_num_kernighan_exclude_sign_bits(n, num_bits=32):
    if isinstance(n, int):
        count = 0
        while n > 0 or n < 0 and not -n & (-n - 1) == 0:
            count += 1
            n &= (n - 1)
        return count


def bin_twos_complement(num, num_bits=32):
    if num < 0:
        num = (1 << num_bits) + num
    formatstring = '{:0%ib}' % num_bits
    return formatstring.format(num)


args = [0, 1, 31, 32, 33, 64, 65, -1, -0, -2, -32, -33, -64, -65 -31, -35]
fns = [num_ones_in_bin_num_naive,
       num_ones_in_bin_num_kernighan,
       num_ones_in_bin_num_naive_exclude_sign_bits,         # Variation: Exclude sign bits.
       num_ones_in_bin_num_kernighan_exclude_sign_bits]     # Variation: Exclude sign bits.

for n in args:
    print(f"bin_twos_complement({n}): {bin_twos_complement(n)}")
    for fn in fns:
        print(f"{fn.__name__}({n}): {fn(n)}")
    print()


