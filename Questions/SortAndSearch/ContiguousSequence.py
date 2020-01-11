"""
    CONTIGUOUS SEQUENCE

    You are given an array of integers (both positive and negative).
    Find the contiguous sequence with the largest sum.
    Return the sum

    Example:
        input = [2, -8, 3, -2, 4, -10]
        output = 5 (i.e., [3, -2, 4])
"""


def get_max_sum(a):
    maxsum = 0
    sum = 0
    i = 0
    while i < len(a):
        sum += a[i]
        if maxsum < sum:
            maxsum = sum
        elif sum < 0:
            sum = 0
        i += 1
    return maxsum


input = [2, -8, 3, -2, 4, -10]
print(get_max_sum(input))


