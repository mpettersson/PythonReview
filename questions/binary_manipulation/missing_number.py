"""
    MISSING NUMBER

    An array A contains all the integers form 0 through n, except for one number which is missing.  In this problem,
    we cannot access an entire integer in A with a single operation.  The elements of A are represented in binary, and
    the only operation we can use to access them is "fetch the jth bit of A[i]", which takes constant time.  Write code
    to find the missing integer.  Can you do it in O(n) time?

    A similar problem is: Given a list of numbers from 0 to n, with exactly one removed, find the missing number.  This
    can be solved by adding the numbers and comparing it to the actual sum of 0 through n, which is n(n + 1) / 2.
    If that approach was used (computing the sum of the numbers based on binary representation) on this problem the
    runtime would be O(n log(n)), which isn't good enough...
"""


def find_missing(array):
    return find_missing_in_column(array, 0)


def find_missing_in_column(array, column):
    zero_bits = []
    one_bits = []

    if len(array) == 0:
        return 0

    for i in array:
        if fetch_jth_bit(i, column) == 0:
            zero_bits.append(i)
        else:
            one_bits.append(i)

    if len(zero_bits) <= len(one_bits):
        v = find_missing_in_column(zero_bits, column + 1)
        return (v << 1) | 0
    else:
        v = find_missing_in_column(one_bits, column + 1)
        return (v << 1) | 1


# This is the "only operation we can use", j starts at 0.
def fetch_jth_bit(num, j):
    return (num >> j) & 1


a_4 = [0, 1, 3, 4]
a_11 = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11]
print(find_missing(a_4))
print(find_missing(a_11))

