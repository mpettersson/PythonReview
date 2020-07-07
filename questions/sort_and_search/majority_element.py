"""
    MAJORITY ELEMENT

    A majority element is an element that makes up more than half of the items in an array.  Given a positive integers
    array, find the majority element, if there is no majority element, return -1.

    Do this in O(N) time and O(1) space.

    Example
        Input:  [1, 2, 5, 9, 5, 9, 5, 5, 5]
        Output: 5

    NOTE: Running once to find a possible majority element, and a second run to validate fits the constraints (and is
    what needs to happen)...
"""


def find_majority_element(l):
    candidate = get_candidate(l)
    return candidate if validate(l, candidate) else -1


def get_candidate(l):
    majority = 0
    count = 0
    for i in l:
        if count == 0:  # No majority element in previous set.
            majority = i
        if i == majority:
            count += 1
        else:
            count -= 1
    return majority


def validate(l, majority):
    count = 0
    for i in l:
        if i == majority:
            count += 1
    return count > len(l) // 2


l1 = [1, 2, 5, 9, 5, 9, 5, 5, 5]
l2 = [3, 1, 7, 1, 3, 7, 3, 7, 1, 7, 7]
l3 = [3, 1, 7, 1, 1, 7, 7, 3, 7, 7, 7]
print("l1:", l1)
print("l2:", l2)
print("l3:", l3)
print()

print("find_majority_element(l1):", find_majority_element(l1))
print("find_majority_element(l2):", find_majority_element(l2))
print("find_majority_element(l3):", find_majority_element(l3))












