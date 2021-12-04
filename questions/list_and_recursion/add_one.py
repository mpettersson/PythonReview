"""
    ADD ONE (leetcode.com/problems/plus-one)

    Design an algorithm that will add one to a given a list of single digits representing a number.

    Example:
        Input =  [1, 0, 0, 3]
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
# the string to an integer, adds one, converts the integer into a string, breaks the string into a list of characters,
# and finally converts all of the characters to integers.
#
# Time Complexity: O(n), where n is the number of digits in l.
# Space Complexity: O(n), where n is the number of digits in l.
def add_one_naive(l):
    return [int(c) for c in str((int(''.join(map(str, l))) + 1))]


# APPROACH: Iterative (Make New List)
#
# This approach iterates over the digits, adding the previous carry value to the digit, then dividing and moding by 10
# to get the resulting digit and carry value.  This returns a new list.
#
# Time Complexity: O(n), where n is the number of digits in l.
# Space Complexity: O(n), where n is the number of digits in l.
def add_one(l):
    carry = 1
    result = [0] * len(l)
    for i in reversed(range(len(l))):
        total = l[i] + carry
        carry, result[i] = divmod(total, 10)
    if carry == 1:
        result = [1] + result
    return result


# APPROACH: Iterative (Modify Provided List)
#
# This approach iterates over the digits, adding the previous carry value (a 1) to the digit, stopping once the carry
# value is zero.  This modifies the provided list.
#
# Time Complexity: O(n), where n is the number of digits in l.
# Space Complexity: O(n), where n is the number of digits in l.
def add_one_alt(l):
    i = len(l) - 1
    carry = 1
    while carry:
        if i == -1:
            l.insert(0, 1)
            carry = 0
        elif l[i] < 9:
            l[i] += 1
            carry = 0
        else:
            l[i] = 0
            i -= 1
    return l


args = [[1, 0, 0, 3],
        [0],
        [9],
        [9, 9, 9, 9, 9, 9]]
fns = [add_one_naive,
       add_one,
       add_one_alt]

for l in args:
    for fn in fns:
        print(f"{fn.__name__}({l}):", fn(copy.copy(l)))
    print()

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
print(f"l: {l!r}")
for fn in fns:
    print(f"{fn.__name__}(l) took ", end='')
    t = time.time()
    fn(copy.copy(l))
    print(f"{time.time() - t} seconds.")
print()


