"""
    FIND MAX RECTANGLE (EPI 18.8: COMPUTE THE LARGEST RECTANGLE UNDER THE SKYLINE)

    Given an integer list representing the heights (in some unit) of a sequence of adjacent buildings (where each
    building has a single unit of width) of a skyline. Write a function to compute the largest rectangular area (in the
    units used by the list) contained in the skyline (for your architect friend).

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
        - SEE: find_max_area_histogram.py
        - SEE: find_max_area_vertical_lines.py
        - Find the largest square under the skyline.
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What values can the list contain (negative, floats, etc.)?
#   - What are the size limits of the list?
#   - What are the widths (if not stated)?


# APPROACH: Brute Force
#
# For each i, j pair, find the minimum sublist l[i:j+1] and multiply it by j-i+1.
#
# Time Complexity: O(n ** 3), where n is the size of the list (or number of buildings).
# Space Complexity: O(1).
def find_max_rectangle_bf(l):
    if l is not None:
        result = 0
        for j in range(len(l)):
            for i in range(j+1):
                min_sub_list = min(l[i:j+1])
                result = max(result, min_sub_list * (j-i+1))
        return result


# APPROACH: Naive Expand From Center (Building)
#
# For each building in the skyline, expanding from the building to find the largest rectangle that maintains the
# (current) buildings height.
#
# Time Complexity: O(n ** 2), where n is the size of the list (or number of buildings).
# Space Complexity: O(1).
def find_max_rectangle_naive(l):
    if l is not None:
        max_area = 0
        for i in range(len(l)):
            lo = hi = i
            while lo - 1 >= 0 and l[lo - 1] >= l[i]:
                lo -= 1
            while hi + 1 < len(l) and l[hi + 1] >= l[i]:
                hi += 1
            height = l[i]
            width = hi - lo + 1
            max_area = max(max_area, width * height)
        return max_area


# APPROACH: Optimal
#
# This approach builds on the 'expand from center (building)' approach above; if we maintain how far to the left the
# support is, the only missing information is how far right the current rectangle goes.
# As opposed to tracking all buildings on the left (which would lead to a search like the naive approach above), the
# only buildings on the left that will be maintained are the ones that haven't been blocked yet (that is, buildings that
# have a taller building immediately following them).
# Using a STACK to track the 'non-blocked' previous heights, we can achieve the minimal running time.
#
# To elaborate on the given example above:
#
#           E  HI
#          D▒  ▒▒J
#        B ▒▒  ▒▒▒
#        ▒ ▒▒F ▒▒▒  M
#        ▒C▒▒▒G▒▒▒K ▒
#       A░░░░░░░░░░L▒
#       ▒░░░░░░░░░░▒▒
#
# buildings: A  B  C  D  E  F  G  H  I  J  K  L  M
# list l:   [1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3]
#
#   i  l[i] l[stack[-1]] stack[..., top] max_area notes
#   -- ---- ------------ --------------- -------- -----
#   0  1    None         Bottom [] Top   0        No buildings to left.
#   1  4    1            [0]             0        Building 0 isn't blocked yet, building 1 is taller.
#   2  2    4            [0, 1]          0        Building 0 and 1 aren't blocked yet.
#   3  5    2            [0, 2]          4        Building 2 is shorter than bldg 1 (at top of stack) so pop and push.
#   4  6    5            [0, 2, 3]       4        Push building 4 (it's taller).
#   5  3    6            [0, 2, 3, 4]    4        Building 5 blocks last two buildings on stack (they're popped), push 5
#   6  2    3            [0, 2, 5]       10       Building 6 is shorter than top of stack (it blocks top of stack).
#   7  6    2            [0, 6]          10       Etc....
#   8  6    6            [0, 6, 7]       10
#   9  5    6            [0, 6, 8]       10
#   10 2    5            [0, 6, 9]       12
#   11 1    2            [0, 10]         18
#   12 3    1            [11]            20
#   13 None 3            [11, 12]        20
#
# Time Complexity: O(n), where n is the number of heights in the list.
# Space Complexity:O(n), where n is the number of heights in the list.
#
# NOTE: It may appear that the time complexity is more than O(n) because there is a nested while loop in the outer for
#       loop, however, each time the nested loop runs it pops from the stack, and since there is at most n pushes to the
#       stack we will never have more than n pushes/pops.
def find_max_rectangle(l):
    if l is not None:
        stack = []                      # Left/lo endpoints still up for consideration, 'buildings' not blocked yet.
        result = 0
        for i in range(len(l)+1):       # Iterate to len(l)+1 for uniform computation.
            if len(stack) > 0 and i < len(l) and l[i] == l[stack[-1]]:
                stack.pop()                 # Replace earlier building with same height by current building; this
                stack.append(i)                 # ensures the later buildings have the correct left endpoint.
            while (len(stack) > 0 and (     # While stack is not empty AND,
                    i == len(l) or              # i is at end of heights list (so need to finish last computation), OR,
                    l[i] <= l[stack[-1]])):     # current height 'blocks' (is shorter than) top of stack:
                height = l[stack[-1]]           # Compute the area using top of stack and current building.
                stack.pop()                     # (The top of the stack is popped.)
                width = i if len(stack) == 0 else i - stack[-1] - 1
                result = max(result, height * width)
            stack.append(i)
        return result


args = [[1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3],
        [5],
        [1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1],
        [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0],
        [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 8, 0, 2, 0, 5, 2, 0, 3, 0, 0],
        [4, 2, 0, 3, 2, 5],
        [8, 5, 6],
        [8, 5, 8],
        [6, 6, 6],
        [4, 4],
        []]
fns = [find_max_rectangle_bf,
       find_max_rectangle_naive,
       find_max_rectangle]
for l in args:
    print(f"l: {l}")
    for fn in fns:
        print(f"{fn.__name__}(l): {fn(l[:])}")
    print()


