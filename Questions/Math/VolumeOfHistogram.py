"""
    VOLUME OF HISTOGRAM

    Imagine a histogram (vertical bar graph).  Design an algorithm to compute the volume of the water it could hold if
    someone poured water across the top.. You can assume that each histogram bar has width 1.

    Example
        Input: histogram = [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0]
        Output: 26
"""


# Iterate left once recording the max left values, then iterate right computing the max right values, the minimum of the
# two max values, and the sum of the difference between the minimum and the histogram.
# The runtime is O(N).
def volume_of_histogram(l):
    left_max = [0] * len(l)
    previous = 0
    l_sum = 0
    for i, v in enumerate(l):
        left_max[i] = v if i == 0 else max(v, left_max[i - 1])
    for i in range(len(l) - 1, -1, -1):
        right_max = previous = l[i] if i == len(l) - 1 else max(l[i], previous)
        l_min = min(left_max[i], right_max)
        l_sum += l_min - l[i]
    return l_sum


histogram_one = [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0]
histogram_two = [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 8, 0, 2, 0, 5, 2, 0, 3, 0, 0]
print("histogram_one: ", histogram_one)
print("histogram_two: ", histogram_two)
print()

print("volume_of_histogram(histogram_one):", volume_of_histogram(histogram_one))
print("volume_of_histogram(histogram_two):", volume_of_histogram(histogram_two))



