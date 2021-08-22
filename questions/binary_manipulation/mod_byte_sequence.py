"""
    MOD BYTE SEQUENCE (50CIQ 33: BIG INT MODULES)

    Given an integer 'b', and an iterable of big-endian bytes 'i', which are the bytes of a much larger integer 'a',
    compute and return 'a' % 'b'.

    Example:
        Input = 10, [0x03, 0xED]
        Output = 5
"""
from collections.abc import Iterable


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Clarify problem (big/small-endian, what type is in the list, can the list fit in memory, etc.)?
#   - Input Validation?


# APPROACH: Naive Construct Large Int & Mod
#
# Leveraging Pythons rather flexible integers, build a large integer from the iterable, then return the result from the
# large integer mod b.
#
# Time Complexity: O(n), where n is the length of i.
# Space Complexity: O(m), where m is the number of bits in a.
def mod_byte_sequence_naive(b, i):
    if isinstance(b, int) and isinstance(i, Iterable):
        a = 0
        shift = 0
        for bytes in reversed(i):
            a += (bytes << shift)
            shift += 8
        return a % b


# APPROACH: Mod Byte By Byte
#
# This approach simply mods each byte of the iterable (plus the shifted previous bytes result) at a time, and returns
# the end result.
#
# Time Complexity: O(n), where n is the length of i.
# Space Complexity: O(1).
def mod_byte_sequence(b, i):
    if isinstance(b, int) and isinstance(i, Iterable):
        result = 0
        for value in i:
            result <<= 8
            result += value
            result %= b
        return result


args = [(10, [0x03, 0xED]),
        (3, [0xDE, 0xAD, 0xBE, 0xEF]),
        (10, [0xba, 0xba, 0xba, 0xba, 0xBA, 0xBA]),
        (2, [0x70, 0x7, 0xB0, 0x0B, 0x5]),
        (1, None),
        (None, [0xDE, 0xAD, 0xBE, 0xEF]),
        (None, None)]
fns = [mod_byte_sequence_naive,
       mod_byte_sequence]

for b, i in args:
    for fn in fns:
        pretty_print = i if not isinstance(i, Iterable) else f"[{', '.join(hex(x) for x in i)}]"
        print(f"{fn.__name__}({b}, {pretty_print}): {fn(b, i)}")
    print()


