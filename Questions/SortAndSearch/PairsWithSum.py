"""
    PAIRS WITH SUM

    Design an algorithm to find all pairs of integers within an array which sum to a specified value.
"""


# Approach 1: Brute Force
def pairs_with_sum_bf(l, s):
    result = []
    for i, v in enumerate(l):
        j = i + 1
        while j < len(l):
            if v + l[j] == s:
                result.append((v, l[j]))
            j += 1
    return result


# Approach 2: Optimize via Set; takes O(N) time and O(N) space.
def pairs_with_sum_via_set(l, s):
    result = []
    elements = set()
    for x in l:
        complement = s - x
        if complement in elements and x not in elements:
            result.append((x, complement))
        elements.add(x)
    return result


# Approach 3: Alternate Optimization via Sort; takes O(N log N) to sort and O(N) to find pairs.
def pairs_with_sum_via_sort(l, s):
    result = []
    l.sort()
    first = 0
    last = len(l) - 1
    while first < last:
        temp = l[first] + l[last]
        if temp == s:
            result.append((l[first], l[last]))
            first += 1
            last -= 1
        else:
            if temp < s:
                first += 1
            else:
                last -= 1
    return result


input_list = [13, 0, 14, -2, -1, 7, 9, 5, 3, 6]
print("pairs_with_sum_bf(input_list, 6):", pairs_with_sum_bf(input_list, 6))
print("pairs_with_sum_via_set(input_list, 6):", pairs_with_sum_via_set(input_list, 6))
print("pairs_with_sum_via_sort(input_list, 6):", pairs_with_sum_via_sort(input_list, 6))



