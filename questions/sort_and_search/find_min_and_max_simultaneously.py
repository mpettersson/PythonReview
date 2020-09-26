"""
    FIND THE MIN AND MAX SIMULTANEOUSLY (EPI 12.7)

    Given a list of comparable objects, you can find either the min or the max of the elements in the list with n - 1
    comparisons, where n is the length of the list.

    Is it possible to compute both the min and the max with less than the 2(n - 1) comparisons required to compute the
    min and max independently?  If so, design an algorithm to find the min and max elements in a list.

    Example:
        Input = [3, 2, 5, 1, 2, 4]
        Output = 1, 5

    Hint:
        Use the fact that a < b and b < c implies a < c to reduce the number of brute force comparisons.

    Variation:
        What is the least number of comparision required to find the min and the max in the worst-case?
"""


# Brute Force Approach:  This approach has 2(n - 1) comparisons.  Time complexity is O(n), where n is the number of
# elements in l.  Space complexity is O(1).
def min_and_max_brute_force(l):
    if l is not None and len(l) > 0:
        min = l[0]
        max = l[0]
        for i in l[1:]:     # For each element:
            if i < min:     # 1 Comparison
                min = i
            if i > max:     # 2 Comparison
                max = i
        return min, max


# Naive Partition Approach: Partition the elements into 'min candidates' and 'max candidates' by comparing successive
# pairs; this will yield n/2 min candidates and n/2 max candidates at the cost of n/2 comparisons. It then takes (n/2)-1
# to find the min from the min candidates and (n/2)-1 to find the max from the max candidates.  This sums to (3n/2)-2
# total comparisons.  Time and space complexity is O(n), where n is the length of the list.
# NOTE: This is naive because it uses O(n) space.
def min_and_max_naive(l):
    if l is not None and len(l) > 0:
        if len(l) is 1:
            return l[0], l[0]
        min_list = []
        max_list = []
        for i in range(1, len(l), 2):
            if l[i-1] < l[i]:
                min_list.append(l[i-1])
                max_list.append(l[i])
            else:
                min_list.append(l[i])
                max_list.append(l[i-1])
        min = min_list[0]
        max = max_list[0]
        for i in range(1, len(min_list)):
            if min_list[i] < min:
                min = min_list[i]
            if max_list[i] > max:
                max = max_list[i]
        if len(l) % 2 is 1:
            if l[-1] < min:
                min = l[-1]
            if l[-1] > max:
                max = l[-1]
        return min, max


# Partition Approach: Similar to the approach above, compare two elements at a time, then, directly compare the smaller
# element with min and the larger element with max (thus, saving space complexity).  The total number of comparisons is
# (3n/2)-2 (not including length stuff).  Time complexity is O(n), where n is the l's length. Space complexity is O(1).
def min_and_max(l):
    if l is not None and len(l) > 0:
        if len(l) is 1:
            return l[0], l[0]
        min = max = None
        if l[0] < l[1]:
            min = l[0]
            max = l[1]
        else:
            min = l[1]
            max = l[0]
        for i in range(3, len(l), 2):
            if l[i-1] < l[i]:
                if l[i-1] < min:
                    min = l[i-1]
                if max < l[i]:
                    max = l[i]
            else:
                if l[i] < min:
                    min = l[i]
                if max < l[i-1]:
                    max = l[i-1]
        if len(l) % 2 is 1:
            if l[-1] < min:
                min = l[-1]
            if max < l[-1]:
                max = l[-1]
        return min, max


lists = [[3, 2, 5, 1, 2, 4],
         [i for i in range(10)],
         ['a', 'b', 'c'],
         [0],
         [1, -1]]

for l in lists:
    print(f"min_and_max_brute_force({l}): {min_and_max_brute_force(l)}")
print()

for l in lists:
    print(f"min_and_max_naive({l}): {min_and_max_naive(l)}")
print()

for l in lists:
    print(f"min_and_max({l}): {min_and_max(l)}")


