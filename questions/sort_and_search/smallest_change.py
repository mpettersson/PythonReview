"""
    SMALLEST CHANGE (EPI CH4)

    Given a list of ints representing a set of coins, what is the smallest amount that can't be made with the change?
    That is, write a program which takes a list of positive ints and returns the smallest number greater than zero,
    which is not a sum of a subset of elements of the list.

    Example:
        input = [1, 10, 1, 5, 1, 1, 1, 25]
        output = 21
        input = [12, 2, 1, 15, 2, 4]
        output = 10
"""


# Time complexity is O(n log n), space complexity is O(1).
def smallest_change(l):
    l.sort()
    curr_max = 0
    for i in l:
        if i > curr_max + 1:
            break
        curr_max += i
    return curr_max + 1


lists = [[1,2,3,4,5],
         [1, 10, 1, 5, 1, 1, 1, 25]]

for l in lists:
    print(f"smallest_change({l}):", smallest_change(l))


