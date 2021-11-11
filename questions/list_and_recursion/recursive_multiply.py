"""
    RECURSIVE MULTIPLY (CCI 8.5)

    Write a recursive function to multiply two numbers without using the * operator (or / operator).  You can use
    addition, subtraction, and bit shifting, but you should minimize the number of those operations.

    Example:
        Input = 50, 6
        Output = 300
"""


# Naive/Brute Force Approach:  Time and space is O(s), where s is the smaller number.
def recursive_multiply_naive(a, b):
    def _recursive_multiply_naive(a, b):
        if a is 0 or b is 0:
            return 0
        if a is 1:
            return b
        return b + _recursive_multiply_naive(a - 1, b)

    neg = False
    if a < 0 <= b or b < 0 <= a:
        neg = True
    a, b = abs(a), abs(b)
    if a > b:
        a, b = b, a
    res = _recursive_multiply_naive(a, b)
    return -res if neg else res


# Optimal Approach: The enhancements are; (1) the function only calls itself once (then doubles the result) and (2) it
# only calls with even a values (then adds the remainder in the return).  The second enhancement can be shown with a
# counter example, if an odd value was used, i.e., recursive_multiply(31, 35), then  recursive_multiply(15, 35) and
# recursive_multiply(16, 35) would also be called (as opposed to adding the result twice and the remainder).
# Time and space is O(log s), where s is the smaller number.
def recursive_multiply(a, b):

    def _recursive_multiply(a, b):
        if a is 0 or b is 0:
            return 0
        if a is 1:
            return b
        half_prod = _recursive_multiply(a >> 1, b)  # Int divide a by two.
        return half_prod + half_prod + (0 if a % 2 is 0 else b)

    if a is not None and b is not None:
        neg = False
        if a < 0 <= b or b < 0 <= a:
            neg = True
        a, b = abs(a), abs(b)
        if a > b:
            a, b = b, a
        res = _recursive_multiply(a, b)
        return -res if neg else res


args = [(3, 5), (-3, 5), (3, -5), (-3, -5),
        (50, 6), (-50, 6), (50, -6), (-50, -6),
        (1, 10), (-1, 10), (1, -10), (-1, -10), (1, 1),
        (0, 12), (-0, 12), (0, -12), (-0, -12), (0, 0)]

for a, b in args:
    print(f"recursive_multiply_naive({a:3}, {b:3}): {recursive_multiply_naive(a, b):4}")
    print(f"recursive_multiply_naive({b:3}, {a:3}): {recursive_multiply_naive(b, a):4}")
print()

for a, b in args:
    print(f"recursive_multiply({a:3}, {b:3}): {recursive_multiply(a, b):4}")
    print(f"recursive_multiply({b:3}, {a:3}): {recursive_multiply(b, a):4}")


