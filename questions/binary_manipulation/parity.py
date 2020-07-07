"""
    PARITY OF A BINARY NUMBER (EPI 5.1)

    The parity of a binary number is 1 if the number of 1s is odd; otherwise, it is 0.
    Write a method that accepts a positive number n and returns the parity of the binary representation of the number.

    Example:
        Input = 0b1011
        Output = 1
"""


# Brute force approach: Runtime is O(n) where n is the size of the binary representation of the number.
def brute_force_parity(n):
    result = 0
    while n > 0:
        if n & 1 == 1:
            result ^= 1
        n >>= 1
    return result


# Improved approach: Runtime is O(k) where k is the number of 1s in the binary representation of the number.
def count_only_ones_parity(n):
    result = 0
    while n > 0:
        result ^= 1
        n &= (n - 1)
    return result


# If n is very large and of a fixed size (say 64 bits), this solution is more efficient (O(log n) if 64 bits).
def efficient_large_num_parity(n):
    n ^= n >> 32
    n ^= n >> 16
    n ^= n >> 8
    n ^= n >> 4
    n ^= n >> 2
    n ^= n >> 1
    return n & 1


print(brute_force_parity(0b1011))
print(brute_force_parity(0b1001))
print()

print(count_only_ones_parity(0b1011))
print(count_only_ones_parity(0b1001))
print()

print(efficient_large_num_parity(0b1011))
print(efficient_large_num_parity(0b1001))








