"""
    SWAP (CCI 16.1: NUMBER SWAPPER,
          50CIQ 34: SWAP VARIABLES)

    Write a function which accepts a list of integers and two indices, then swaps the values at the two indices without
    using additional variables?

    Example:
                l = [1, 2, 3]
        Input = l, 0, 2
        Output = [3, 2, 1]
"""
import copy


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What is the expected output (i.e., in c we could pass by reference, and this would make sense)?


# APPROACH: Addition/Subtraction
#
# Use one addition operation, followed by two subtraction operations, to reverse the variables values.  For example:
#   x = 6
#   y = 9
#   x = x + y = 6 + 9 = 15
#   y = x - y = 15 - 9 = 6
#   x = x - y = 15 - 6 = 9
#
# Time Complexity: O(1).
# Space Complexity: O(1).
def swap_via_add_and_sub(l, x, y):
    if isinstance(l, list) and -len(l) <= x < len(l) and -len(l) <= y < len(l):
        l[x] = l[x] + l[y]
        l[y] = l[x] - l[y]
        l[x] = l[x] - l[y]
        return l


# APPROACH: XOR (^)
#
# Use three XOR operations to reverse the variables values.  For Example:
#   x = 6     = 0110
#   y = 9     = 1001
#   x = x ^ y = 1111
#   y = x ^ y = 0110
#   x = x ^ y = 1001
#
# Time Complexity: O(1).
# Space Complexity: O(1).
def swap_via_xor(l, x, y):
    if isinstance(l, list) and -len(l) <= x < len(l) and -len(l) <= y < len(l):
        l[x] = l[x] ^ l[y]       # 1111
        l[y] = l[x] ^ l[y]       # 0110
        l[x] = l[x] ^ l[y]       # 1001
        return l


# APPROACH: Pythonic
#
# Do it the python way.
#
# Time Complexity: O(1).
# Space Complexity: O(1).
def swap(l, x, y):
    if isinstance(l, list) and -len(l) <= x < len(l) and -len(l) <= y < len(l):
        l[x], l[y] = l[y], l[x]
        return l


l = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
indices_tuples = [(1, 2), [0, -1], [4, 4]]
fns = [swap_via_add_and_sub,
       swap_via_xor,
       swap]
print(f"\nl: {l}\n")

for x, y in indices_tuples:
    for fn in fns:
        print(f"{fn.__name__}(l, {x}, {y}): {fn(copy.deepcopy(l), x, y)}")
    print()

