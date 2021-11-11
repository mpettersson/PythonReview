"""
    FIND ALL SUBLISTS SUM

    Write a function, which takes an integer list l, and returns the sum of every contiguous sublist.

    Example:
        Input = [1, 2, 3, 4]
        Output = 50  # Or ((1)+(2)+(3)+(4)) + ((1+2)+(2+3)+(3+4)) + ((1+2+3)+(2+3+4)) + ((1+2+3+4))
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Sublist/Substring or Subsequence? (Don't get them confused!)
#   - What are the size limits of the list?
#   - Are the values negative & positive?
#   - Are there duplicate values in the list?
#   - The whole list can be a sublist?


# APPROACH: Naive/Brute Force
#
# Find all sublists starting and ending indexes; then sum over each of the sublists adding the values to the results.
#
# Time Complexity: O(n**3), where n is the length of the list.
# Space Complexity: O(1).
def find_all_sublists_sum_naive_bf(l):
    if isinstance(l, list) and all([isinstance(x, int) for x in l]):
        result = 0
        for i in range(len(l)):
            for j in range(i, len(l)):
                for k in range(i, j+1):
                    result += l[k]
        return result


# APPROACH: Brute Force
#
# This approach is similar to the approach above, however, the use of an additional temporary variable eliminates the
# need for one loop.
#
# Time Complexity: O(n**2), where n is the length of the list.
# Space Complexity: O(1).
def find_all_sublists_sum_bf(l):
    if isinstance(l, list) and all([isinstance(x, int) for x in l]):
        result = 0
        for i in range(len(l)):
            temp = 0
            for j in range(i, len(l)):
                temp += l[j]
                result += temp
        return result


# APPROACH: Optimal Via A Bit Of Math
#
# Consider the series of summations for the list [1, 2, 3, 4, 5]:
#
#  ((1)+(2)+(3)+(4)+(5)) + ((1+2)+(2+3)+(3+4)+(4+5)) + ((1+2+3)+(2+3+4)+(3+4+5)) + ((1+2+3+4)+(2+3+4+5)) + ((1+2+3+4+5))
#
#  or, (l[0]*5) + (l[1]*8) + (l[2]*9) + (l[3]*8) + (l[4]*5)
#
# The first element is used exactly once in each of the four iterations.  The last element is also used exactly once in
# each of the four iterations.  The middle values are also predictable.  This all points to an equation; try plugging in
# the known values and variables (i, and l[i]) to create a formula.  You may need to use a longer list
# (i.e., [1, 2, 3, 4, 5, 6, 7]) to see the patterns more clearly.  In this situation; lots of writing on the whiteboard,
# or scratch paper, will help.
#
# Time Complexity: O(n), where n is the length of the list.
# Space Complexity: O(1).
def find_all_sublists_sum(l):
    if isinstance(l, list) and all([isinstance(x, int) for x in l]):
        result = 0
        n = len(l)
        for i in range(n):
            result += l[i] * (i + 1) * (n - i)
        return result


lists = [[0, 1, 2, 3, 4],
         [1, 2, 1, 3],
         [0, 1, 2, 1, 3],
         [2, -2, 2, -2, 2, -2],
         [3, -1, 1],
         [0, 3, -1, 1, 0],
         [1, 2, 1, 0, 3],
         [1, 1, 1, 1, 1, 1, 1],
         [0, 1, 1, 1, 1, 1, 1, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 1, 1, 1, 0, 0, 1, -1, 0],
         [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0],
         [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
         [1, 2, -5, 1, 2, -1],
         [1, 2, -5, 1, 2, 0, 0, -1]]
fns = [find_all_sublists_sum_naive_bf,
       find_all_sublists_sum_bf,
       find_all_sublists_sum]

for l in lists:
    print(f"l: {l}")
    for fn in fns:
        print(f"{fn.__name__}(l): {fn(l[:])}")
    print()


