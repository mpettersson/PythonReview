"""
    FACTORIAL ZEROS

    Write an algorithm which computes the number of trailing zeros in n factorial.

    For example, 19! = 121645100408832000, and it has 3 trailing zeros.
"""


# Approach 1: Iterate through numbers 2 through n, counting the number of times that 5 goes into each number.
def factors_of_five(i):
    print(i)
    count = 0
    while i % 5 == 0:
        count += 1
        i = i // 5
    return count


def count_factorial_zero(num):
    count = 0
    i = 2
    while i <= num:
        count += factors_of_five(i)
        i += 1
    return count


# Approach 2: More efficiently, count the factors of 5.
def count_fact_zero(num):
    count = 0
    if num < 0:
        return None
    i = 5
    while num // i > 0:
        count += num // i
        i *= 5
    return count


print(count_factorial_zero(19))
