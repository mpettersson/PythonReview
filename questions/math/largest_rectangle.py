"""
    COMPUTE THE LARGEST RECTANGLE UNDER THE SKYLINE (EPI 18.8)

    You are given a sequence of adjacent buildings.  Each has unit width and an integer height.  These buildings form
    the skyline of a city.  An architect wants to know the area of a largest rectangle contained in this skyline.

    Let l be a list representing the heights of adjacent buildings of unit width.  Design an algorithm to compute the
    area of the largest rectangle contained in this skyline.

    Consider the following skyline and it's corresponding list l:

            E  HI
           D▒  ▒▒J
         B ▒▒  ▒▒▒
         ▒ ▒▒F ▒▒▒  M
         ▒C▒▒▒G▒▒▒K ▒
        A░░░░░░░░░░L▒
        ▒░░░░░░░░░░▒▒

        buildings: A  B  C  D  E  F  G  H  I  J  K  L  M
        list l:   [1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3]

    Example:
        Input = [1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3]
        Output = 20

    Variations:
        - SEE: get_max_trapped_water.py
        - SEE: volume_of_histogram.py
        - Find the largest square under the skyline.
"""


# Naive/Brute Force Approach: For each building height, get the low and high starting points for the width to find the
# area.
def get_largest_rectangle_naive(l):
    if l is not None:
        max_area = 0
        for i in range(len(l)):
            lo = hi = i
            while lo - 1 > 0 and l[lo - 1] >= l[i]:
                lo -= 1
            while hi + 1 < len(l) and l[hi + 1] >= l[i]:
                hi += 1
            height = l[i]
            width = hi - lo + 1
            max_area = max(max_area, width * height)
        return max_area


# Optimal Approach: Using a STACK to track the relevant previous heights, we can achieve the minimal running time. Time
# and space complexity is O(n), where n is the number of heights in the list.
#
# NOTE: It may appear that the time complexity is more than O(n) because there is a nested while loop in the outer for
# loop, however, each time the nested loop runs it pops from the stack, and since there is at most n pushes to the stack
# we will never have more than n pushes/pops.
#
# Function state for each iteration of the algorithm, when l = [1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3], is:
#       i   l[i]    stack[top, ...]     max_area
#       --  ----    ---------------     --------
#       0   1       []                  0
#       1   4       [0]                 0
#       2   2       [1, 0]              0
#       3   5       [2, 0]              4
#       4   6       [3, 2, 0]           4
#       5   3       [4, 3, 2, 0]        4
#       6   2       [5, 2, 0]           10
#       7   6       [6, 0]              10
#       8   6       [7, 6, 0]           10
#       9   5       [8, 6, 0]           10
#       10  2       [9, 6, 0]           12
#       11  1       [10, 0]             18
#       12  3       [11]                20
#       13  None    [12, 11]            20
def get_largest_rectangle(l):

    def is_new_pillar_or_reach_end(l, curr_idx, last_idx):
        return l[curr_idx] <= l[last_idx] if curr_idx < len(l) else True

    if l is not None:
        stack = []
        max_area = 0
        for i in range(len(l)+1):
            if len(stack) > 0 and i < len(l) and l[i] == l[stack[0]]:
                stack.pop(0)
                stack.insert(0, i)
            while len(stack) > 0 and is_new_pillar_or_reach_end(l, i, stack[0]):
                height = l[stack[0]]
                stack.pop(0)
                width = i if len(stack) is 0 else i - stack[0] - 1
                max_area = max(max_area, height * width)
            stack.insert(0, i)
        return max_area


args = [[1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3],
        [1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1],
        [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0],
        [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 8, 0, 2, 0, 5, 2, 0, 3, 0, 0]]

for l in args:
    print(f"l: {l}")
    print(f"get_largest_rectangle_naive(l): {get_largest_rectangle_naive(l)}")
    print(f"get_largest_rectangle(l): {get_largest_rectangle(l)}")
    print()


