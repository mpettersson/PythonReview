"""
    SWAP BITS (EPI 5.2)

    Write a method that when given a number (num) and two indexes (i & j), swaps the ith and jth bit in the number num
    (where the LSB is at index 0).

    Example:
        Input =  0b010001001, 1, 7
        Output = 0b000001011

    NOTE: Python will truncate this to 0b1011
"""


# The runtime is O(1).
def swap_bits(num, i, j):
    if num >> i & 1 != num >> j & 1:
        num ^= 1 << i | 1 << j
    return num


print("swap_bits(0b010001001, 1, 7):", bin(swap_bits(0b010001001, 1, 7)))
print("swap_bits(0b010001001, 6, 0):", bin(swap_bits(0b010001001, 6, 0)))


