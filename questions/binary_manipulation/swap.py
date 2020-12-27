"""
    SWAP (CCI 16.1: NUMBER SWAPPER,
          50CIQ 34: SWAP VARIABLES)

    How do you swap two variables containing booleans, or integers, without using additional variables?
"""


# Addition/Subtraction Approach.
# Time Complexity: O(1).
# Space Complexity: O(1).
x = 6
y = 9
print(f"x: {x}, y: {y}")
x = x + y       # 6 + 9 = 15
y = x - y       # 15 - 9 = 6
x = x - y       # 15 - 6 = 9
print(f"x: {x}, y: {y}, After Addition/Subtraction Approach.\n")


# XOR (^) Approach.
# Time Complexity: O(1).
# Space Complexity: O(1).
x = 6           # 0110
y = 9           # 1001
print(f"x: {x}, y: {y}")
x = x ^ y       # 1111
y = x ^ y       # 0110
x = x ^ y       # 1001
print(f"x: {x}, y: {y}, After XOR (^) Approach.\n")


# Pythonic Approach.
# Time Complexity: O(1).
# Space Complexity: O(1).
x = 6           # 0110
y = 9           # 1001
print(f"x: {x}, y: {y}")
x, y = y, x
print(f"x: {x}, y: {y}, After Pythonic Approach.\n")


