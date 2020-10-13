"""
    VOLUME OF HISTOGRAM (CCI 17.21)

    Imagine a histogram (vertical bar graph).  Design an algorithm to compute the volume of the water it could hold if
    someone poured water across the top.. You can assume that each histogram bar has width 1.

    Consider the following histograms generated from list l:

             ▒                       ▒
             ▒    ▒                  ▒░░░░▒
          ▒  ▒    ▒               ▒░░▒░░░░▒
          ▒  ▒  ▒ ▒               ▒░░▒░░▒░▒
          ▒  ▒  ▒ ▒               ▒░░▒░░▒░▒
          ▒  ▒  ▒ ▒ ▒             ▒░░▒░░▒░▒░▒
        ABCDEFGHIJKLMNOP        ABCDEFGHIJKLMNOP

        Histogram: A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P
        List l:   [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0]

    Example:
        Input = [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0]
        Output = 26  # the ░ blocks above.

    Variations:
        - SEE: get_max_trapped_water.py
        - SEE: largest_rectangle.py
"""


# Optimal Approach:  Iterate left once recording the max left values, then iterate right computing the max right values,
# the minimum of the two max values, and the sum of the difference between the minimum and the histogram. Time and space
# complexity is O(n), where n is the number of values in the list.
def volume_of_histogram(l):
    if l is not None and len(l) > 0:
        left_max = [l[0]] + [0] * (len(l) - 1)
        previous = 0
        l_sum = 0
        for i in range(1, len(l)):
            left_max[i] = max(l[i], left_max[i - 1])
        for i in range(len(l) - 1, -1, -1):
            right_max = previous = l[i] if i == len(l) - 1 else max(l[i], previous)
            l_min = min(left_max[i], right_max)
            l_sum += l_min - l[i]
        return l_sum


args = [[0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0],
        [1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1],
        [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 8, 0, 2, 0, 5, 2, 0, 3, 0, 0],
        [1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3],
        [8, 5, 6],
        [8, 5, 8],
        [4, 4],
        [4],
        []]

for l in args:
    print(f"l: {l}")
    print(f"volume_of_histogram(l): {volume_of_histogram(l)}")
    print()


