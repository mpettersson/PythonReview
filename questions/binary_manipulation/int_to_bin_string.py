"""
    INT TO BINARY STRING

    Given an int i, convert it to a binary string using only bitwise ops and int division.
"""


def int_to_bin_string(i):
    if i == 0:
        return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i //= 2
    return s


def to_binary(n):
    return ''.join(str(1 & int(n) >> i) for i in range(64)[::-1])


print("int_to_bin_string(100):", int_to_bin_string(100))
print("to_binary(100):", to_binary(100))


