"""
    FIND MAX AREA HISTOGRAM (CCI 17.21: VOLUME OF HISTOGRAM)

    Given a list representing a histogram (or a vertical bar graph, with each bar having a width of 1), write a function
    to compute the maximum amount/area of liquid/water it could hold.

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
        - SEE: find_max_area_vertical_lines.py
        - SEE: find_max_rectangle.py
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What values can the list contain (negative, floats, etc.)?
#   - What are the size limits of the list?
#   - Can you slant the container?
#   - What about the widths of the lines?


# APPROACH: Naive/Brute Force
#
# Iterate from zero to the maximum height value.  For iteration iterate over the list adding any 'trapped' water.  After
# all iterations have been completed, return the total amount of 'trapped' water.
#
# Time Complexity: O(n), where n is the number of values in the list.
# Space Complexity: O(1).
def volume_of_histogram_naive(l):
    if l is not None and len(l) > 0:
        n = len(l)
        result = 0
        for h in range(max(l)+1):
            lo = 0
            hi = n - 1
            while lo < n and l[lo] < h:
                lo += 1
            while hi > 0 and l[hi] < h:
                hi -= 1
            for i in range(lo, hi+1):
                if l[i] < h:
                    result += 1
        return result


# APPROACH: Optimal
#
# Iterate left once recording the max left values, then iterate right computing the max right values, the minimum of the
# two max values, and the sum of the difference between the minimum and the histogram.
#
# Time Complexity: O(n), where n is the number of values in the list.
# Space Complexity: O(n), where n is the number of values in the list.
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
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
        [4, 2, 0, 3, 2, 5],
        [8, 5, 6],
        [8, 5, 8],
        [4, 4],
        [4],
        []]
fns = [volume_of_histogram_naive,
       volume_of_histogram]

for l in args:
    print(f"l: {l}")
    for fn in fns:
        print(f"{fn.__name__}(l): {fn(l)}")
    print()


