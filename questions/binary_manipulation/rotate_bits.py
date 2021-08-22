"""
    ROTATE BITS (50CIQ 36: ROTATE BITS)

    Write a function, which accepts two integers n and k, then rotates (i.e., circular shifts) the bits in n by k number
    of places.

    Example:
        Input = 0b00000000000000000000000000011111, 3
        Output = 0b11100000000000000000000000000011
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Clarify problem (NEGATIVE NUMBERS, num bit length, right/left/clockwise/counter clockwise, etc...)?
#   - Input Validation?


# NOTE: The combination of Pythons internal int representation (unbounded length ints), with the properties of binary
#       manipulation on twos complement numbers, makes this (normally easy question) quit tricky.  With any luck, your
#       interviewer will allow the limitation/assumption of positive integers and you can sidestep the complications.
#       If not, then FIRST solve the problem with the assumption that only positive integers are provided, then, attempt
#       to solve it for negative numbers as well.


# APPROACH: Via Binary Manipulation
#
# This approach uses binary manipulation to combine a shifted left n with a shifted right n, thus 'rotating' the bits
# via the joining two opposite direction shifts.
#
# Time Complexity: O(b), where b is the maximum number of bits (num_bits).
# Space Complexity: O(b), where b is the maximum number of bits (num_bits).
def rotate_bits_right_via_bit_manipulation(n, k, num_bits=32):
    if isinstance(n, int) and isinstance(k, int) and isinstance(num_bits, int) and num_bits > 0 and k > 0:
        k = k % num_bits
        # return n >> k | n << (num_bits - k)           # IFF POSITIVE NUMBERS ONLY!
        return ((n & (2 ** num_bits - 1)) >> k) | (n << (num_bits - k) & (2 ** num_bits - 1))


# APPROACH: Via Binary Manipulation
#
# This approach uses binary manipulation to combine a shifted left n with a shifted right n, thus 'rotating' the bits
# via the joining two opposite direction shifts.
#
# Time Complexity: O(b), where b is the maximum number of bits (num_bits).
# Space Complexity: O(b), where b is the maximum number of bits (num_bits).
def rotate_bits_left_via_bit_manipulation(n, k, num_bits=32):
    if isinstance(n, int) and isinstance(k, int) and isinstance(num_bits, int) and num_bits > 0 and k > 0:
        k = k % num_bits
        # return n << k | n >> (num_bits - k)       # IFF POSITIVE NUMBERS ONLY!
        return (n << k) & (2 ** num_bits - 1) | ((n & (2 ** num_bits - 1)) >> (num_bits - k))


# APPROACH: (Right Shift) Via String Manipulation
#
# This approach simply converts the binary representation of the integer to a string, then returns two slices as the
# result. The first slice starts at index num_bits-k and goes to the end of the converted string, the second slice (that
# is concatenated with the first) starts at the beginning of the converted string and goes to, but doesn't include,
# index num_bits-k.
#
# Time Complexity: O(b), where b is the maximum number of bits (num_bits).
# Space Complexity: O(b), where b is the maximum number of bits (num_bits).
def rotate_bits_right_via_str_manipulation(n, k, num_bits=32):
    if isinstance(n, int) and isinstance(k, int) and isinstance(num_bits, int) and num_bits > 0 and k > 0:
        s = f"{(2 ** num_bits - 1) & n:b}".zfill(num_bits)
        k = k % num_bits
        return s[num_bits-k:] + s[:num_bits-k]


# APPROACH: (Left Shift) Via String Manipulation
#
# This approach simply converts the binary representation of the integer to a string, then returns two slices as the
# result. The first slice is from k to the end of the converted string, the second slice (that is concatenated with the
# first) starts at the beginning of the converted string and goes to (but doesn't include) k.
#
# Time Complexity: O(b), where b is the maximum number of bits (num_bits).
# Space Complexity: O(b), where b is the maximum number of bits (num_bits).
def rotate_bits_left_via_str_manipulation(n, k, num_bits=32):
    if isinstance(n, int) and isinstance(k, int) and isinstance(num_bits, int) and num_bits > 0 and k > 0:
        s = f"{(2 ** num_bits - 1) & n:b}".zfill(num_bits)
        k = k % num_bits
        return s[k:] + s[:k]


def bin_twos_complement(num, num_bits=32):
    if num < 0:
        num = (1 << num_bits) + num
    formatstring = '{:0%ib}' % num_bits
    return formatstring.format(num)


def _bin(n, num_bits=32):
    return f"{(2 ** num_bits - 1) & n:b}".zfill(num_bits)


args = [(31, 3),
        (1, 31),
        (1, 32),
        (1, 33),
        (15, 4),
        (15, 5),
        (15, 6),
        (119, 2),
        (119, 3),
        (119, 4),
        (-8, 10),
        (-8, 11),
        (-8, 12),
        (65535, 8),
        (65535, 16)]
fns = [rotate_bits_right_via_bit_manipulation,
       rotate_bits_right_via_str_manipulation,
       rotate_bits_left_via_bit_manipulation,
       rotate_bits_left_via_str_manipulation]

for n, k in args:
    print(f"bin_twos_complement({n}): {bin_twos_complement(n)}")
    for fn in fns:
        print(f"{fn.__name__}({n}, {k}): {fn(n, k)}")
    print()


