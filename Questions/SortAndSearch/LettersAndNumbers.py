"""
    LETTERS AND NUMBERS

    Given an array filled with letters and numbers, find the longest sub-array with an equal number of letters and
    numbers.
"""


# Approach 1: Brute Force, O(N**2) time, where N is len(array).
def find_longest_subarray_brute_force(array):
    for length in range(len(array), 1, -1):
        for i in range(0, len(array) - length + 1):
            if has_equal_letters_and_numbers(array, i, i + length - 1):
                return array[i: i + length]


def has_equal_letters_and_numbers(array, start, end):
    counter = 0
    for i in range(start, end + 1):
        if array[i].isalpha():
            counter += 1
        elif array[i].isdigit():
            counter -= 1
    return counter == 0


# Approach 2: Optimal--Compute deltas, find max distance between pair of deltas, O(N) time, where N is len(array).
def find_longest_subarray(array):
    deltas = compute_deltas(array)
    match = find_longest_match(deltas)
    return array[match[0] + 1:match[1] + 1]


# Compute the difference between the number of letters and numbers between the beginning of the list and each index. 
def compute_deltas(array):
    deltas = [None] * len(array)
    delta = 0
    for i in range(0, len(array)):
        if array[i].isalpha():
            delta += 1
        elif array[i].isdigit():
            delta -= 1
        deltas[i] = delta
    return deltas


# Find the matching pair of values in the deltas list which the largest difference (in indices).
def find_longest_match(deltas):
    d_map = {0: -1}
    max = [0] * 2
    for i in range(0, len(deltas)):
        if deltas[i] not in d_map:
            d_map[deltas[i]] = i
        else:
            match = d_map[deltas[i]]
            distance = i - match
            longest = max[1] - max[0]
            if distance > longest:
                max[1] = i
                max[0] = match
    return max


ex_1 = ['j', '4', 'x', '4', '8', 's', 'j', '2', '5', '9', 'f', 'u', '9']
ex_2 = ['A', 'B', '1', '2', '3', 'C', 'D', 'E', 'F', '4', 'G']
ex_3 = ['a', 'a', 'a', 'a', '1', '1', 'a', '1', '1', 'a', 'a', '1', 'a', 'a', '1', 'a', 'a', 'a', 'a', 'a']

print("ex_1:", ex_1)
print("ex_2:", ex_2)
print("ex_3:", ex_3)
print()

print("find_longest_subarray_brute_force(ex_1):", find_longest_subarray_brute_force(ex_1))
print("find_longest_subarray_brute_force(ex_2):", find_longest_subarray_brute_force(ex_2))
print("find_longest_subarray_brute_force(ex_3):", find_longest_subarray_brute_force(ex_3))
print()

print("find_longest_subarray(ex_1):", find_longest_subarray(ex_1))
print("find_longest_subarray(ex_2):", find_longest_subarray(ex_2))
print("find_longest_subarray(ex_3):", find_longest_subarray(ex_3))




