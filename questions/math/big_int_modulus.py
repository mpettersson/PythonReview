"""
    BIG INT MODULES (50CIQ 33: BIG INT MODULES)

    Write a function, which accepts an iterable of bytes (representing a very large integer) and an integer n, then
    compute the modulus of iterable % n.

    Example:
        Input = bytearray(b'\x03\xed'), 10
        Output = 5
"""


# Questions you should ask the interviewer:
#   - How long can the byte array be?
#   - Can you use the modulus operator?
#   - Can you use any big int/number classes?


# Observations:
# This question is more about handling large amounts of information; if the iterable was small, then you could just read
# in the whole number convert it to an int and mod it.
# Think of this like long division; divide the most significant digits first, adding the remainders along the way.


# Approach:  Similar to long division, for each byte, align the previous result with the new byte, sum then mod.
# Time Complexity: O(n), where n is the length of the byte iterable.
# Space Complexity: O(1).
def mod_bytes(iterable, n):
    if iterable is not None:
        mod_result = 0
        for byte in iterable:
            mod_result <<= 8                # Align to the next byte.
            mod_result += (byte & 0xFF)     # Add with the next byte (ensuring the byte has the correct size).
            mod_result %= n                 # Mod.
        return mod_result


bytearrays = [bytes(b'\x03\xed'),
              bytearray(b'\xe0\xdc\xd4\xb7\xe4\xc9\xce\xd9\xd8\xbe\xf8\xc2\xee\xb6\xcf\xdd\xe8\xc4\xc0\xe6\xd6\xca\xfb'
                        b'\xb3\xdc\xe2\xba\xbf\xe4\xd9\xb5\xc4\xf7\xdb\xe1\xdd\xf8\xdb\xd4\xed\xe3\xc7\xca\xbc\xfa\xd6'
                        b'\xd9\xe8\xc5\xac\xcb\xb8\xf2\xc7\xd0\xb0\xf3\xef\xc5\xf8\xf6\xf2\xd3\xc0\xde\xf7\xb4\xe5\xbf'
                        b'\xf7\xf9\xcd\xd3\xc0\xce\xc3\xf5\xaa\xd5\xd6\xbe\xc6\xf7\xc7\xf2\xc7\xda\xe5\xe3\xd8\xd7\xd0'
                        b'\xb9\xd8\xd6\xe5\xce\xbf\xaf\xb6'),
              None]
mod_values = [-12, -2, 2, 5, 10, 12, 40, 100]
fns = [mod_bytes]

for i_bytes in bytearrays:
    print(f"i_bytes: {i_bytes}")
    for fn in fns:
        for m in mod_values:
            print(f"{fn.__name__}(i_bytes, {m}): {fn(i_bytes, m)}")
        print()


