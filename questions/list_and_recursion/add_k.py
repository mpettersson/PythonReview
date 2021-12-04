"""
    ADD ONE (leetcode.com/problems/add-to-array-form-of-integer)

    Write a function which accepts a list of single integer digits (representing a number) and an integer number k, then
    returns a list of single integer digits representing their sum.

    Example:
        Input =  [1, 0, 0, 3], 1
        Output = [1, 0, 0, 4]

    NOTE: Variations of this problem could be:
            - Add/Subtract a given value.
            - Add/Subtract two lists representing values.
"""
import copy
import time


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What type of characters?
#   - Are there leading zeros?
#   - What are the estimated lengths of the strings (empty string)?
#   - Negative values (in either the list or k)?


# APPROACH: Naive
#
# This probably is not what the interviewer wants...  This converts the numbers to characters, joins the chars, converts
# the string to an integer, adds k, converts the integer into a string, breaks the string into a list of characters, and
# finally converts all of the characters to integers.
#
# Time Complexity: O(n), where n is the maximum number of digits in either of the arguments.
# Space Complexity: O(n), where n is the maximum number of digits in either of the arguments.
def add_k_naive(l, k):
    # return [int(c) for c in str(sum([(10**i)*v for i, v in enumerate(reversed(l)) if v]) + k)]    # Slower
    return [int(c) for c in str((int(''.join(map(str, l))) + k))]                                   # Faster


# APPROACH: Iterative (Via divmod)
#
# Starting with the least significant digit, while there is a carry value (which is initially set to k), add the digit
# to the carry value, then divide and mod by 10 to get the carry and new value (for that digit in the list).
#
# Time Complexity: O(n), where n is the maximum number of digits in either of the arguments.
# Space Complexity: O(n), where n is the maximum number of digits in either of the arguments.
def add_k(l, k):
    i = len(l) - 1
    carry = k
    while carry:
        carry, rem = divmod(carry, 10)
        if i == -1:
            l.insert(0, rem)
        else:
            curr = l[i] + rem
            if curr > 9:
                l[i] = curr % 10
                carry += 1
            else:
                l[i] = curr
            i -= 1
    return l


args = [(0, [1, 0, 0, 3]),
        (1, [1, 0, 0, 3]),
        (9, [1, 0, 0, 3]),
        (10, [1, 0, 0, 3]),
        (0, [0]),
        (1, [0]),
        (9, [0]),
        (10, [0]),
        (0, [9]),
        (1, [9]),
        (9, [9]),
        (10, [9]),
        (0, [9, 9, 9, 9, 9, 9]),
        (1, [9, 9, 9, 9, 9, 9]),
        (9, [9, 9, 9, 9, 9, 9]),
        (10, [9, 9, 9, 9, 9, 9]),
        (9999, [9, 9, 9, 9, 9, 9])]
fns = [add_k_naive,
       add_k]

for k, l in args:
    print(f"l: {l!r}\nk: {k!r}")
    for fn in fns:
        print(f"{fn.__name__}(l, k):", fn(copy.copy(l), k))
    print()

t_args = [(0, [1]),
          (876543210000000000001, [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])]
# k = [8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
for k, l in t_args:
    print(f"l: {l!r}\nk: {k!r}")
    for fn in fns:
        print(f"{fn.__name__}(l, k) took ", end='')
        t = time.time()
        fn(copy.copy(l), copy.copy(k))
        print(f"{time.time() - t} seconds.")
    print()


