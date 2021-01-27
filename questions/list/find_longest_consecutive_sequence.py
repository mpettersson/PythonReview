"""
    FIND LONGEST CONSECUTIVE SEQUENCE (50CIQ 5: CONSECUTIVE ARRAY,
                                       leetcode.com/problems/longest-consecutive-sequence)

    Write a function which accepts an unsorted list of ints, then returns the longest list composed of consecutive
    integers from the unsorted list.

    Example:
        Input = [4, 2, 1, 6, 5]
        Output = [4, 5, 6]
"""
import copy


# Naive/Brute Force Approach:  Check for the most consecutive sequences starting at each value in the list.
# Time Complexity: O(n**3), where n is the number of elements in the list.
# Space Complexity: O(r), where r is the length of the longest consecutive sequence in the list.
def find_longest_consecutive_sequence_naive(l):
    if l is None or len(l) == 0:
        return None if l is None else []
    max_len = 1
    start = l[0]
    for v in l:                                     # O(n)
        curr_val = curr_start = v
        curr_len = 1
        while curr_val + 1 in l:                    # O(n * n): O(n) for the 'while', O(n) for the 'in'.
            curr_val += 1
            curr_len += 1
        if curr_len > max_len:
            max_len = curr_len
            start = curr_start
    return list(range(start, max_len + start))


# Naive Sort Approach:  Sort the provided list, then starting at each index, build a list of consecutive values,
# returning the longest of the consecutive values lists.
# Time Complexity: O(n * log(n)), where n is the number of elements in the list.
# Space Complexity: O(r), where r is the length of the longest consecutive sequence in the list.
def find_longest_consecutive_sequence_via_sort(l):
    if l is None or len(l) == 0:
        return None if l is None else []
    l = sorted(l)
    max_len = curr_len = 1
    start = curr_start = l[0]
    for i in range(1, len(l)):
        if l[i-1] + 1 == l[i]:
            curr_len += 1
            if curr_len > max_len:
                max_len = curr_len
                start = curr_start
        else:
            curr_len = 1
            curr_start = l[i]
    return list(range(start, max_len + start))


# Optimal Set Approach:  Construct a set from the provided list, then, for each number in the set, if it is the first
# number in a consecutive sequence, construct a temporary candidate list.  If the candidate list is longer than the
# current result list, update the result with the candidate list.
# Time Complexity: O(n), where n is the number of elements in the list.
# Space Complexity: O(u), where u are the number of unique elements in the list.
#
# NOTE: This appears to have O(n**2) time (because of the nested while loop), however, the while loop will ONLY RUN n
# times.  Therefore, the time is O(n + n), or O(n), NOT O(n * n).  Furthermore, this can only be achieved via the set's
# O(1) time 'in' lookup operation.
def find_longest_consecutive_sequence_via_set(l):
    if l is not None:
        s = set(l)                                  # Need to use set for O(1) 'in' lookup time.
        result = []
        for n in s:
            if n - 1 not in s:                      # ONLY if n is the FIRST value in a sequence...
                candidate = [n]
                m = n + 1
                while m in s:                       # Build candidate list from consecutive values.
                    candidate.append(m)             # This ONLY happens n times!
                    m += 1
                if len(candidate) > len(result):
                    result = candidate
        return result


# Optimal Dictionary Approach: Use a dictionary to record the size of the consecutive subset for which the element is a
# member. Whenever a new element is found (is not in the dictionary), check if one plus/minus the element is in the
# dictionary; if it is, then update the size for the FIRST and LAST element in the consecutive sequence.
# Time Complexity: O(n), where n is the number of elements in the list.
# Space Complexity: O(u), where u are the number of unique elements in the list.
def find_longest_consecutive_sequence_via_dict(l):
    if l is not None:
        if len(l) > 0:
            max_len = 0
            start_n = None
            d = {}
            for n in l:
                if n not in d:                      # If n is in d, then nothing changes/is updated.
                    num_left = d[n - 1] if (n - 1) in d else 0
                    num_right = d[n + 1] if (n + 1) in d else 0
                    curr_total = num_left + num_right + 1
                    d[n] = curr_total
                    if curr_total > max_len:
                        max_len = curr_total
                        start_n = n - num_left
                    d[n - num_left] = curr_total     # Update first element sequence count, or n if n is first.
                    d[n + num_right] = curr_total    # Update last element sequence count, or n if n is last.
            return list(range(start_n, start_n + max_len))
        return []


lists = [[1, 2, 3, 4, 5, 6],
         [4, 2, 1, 6, 5],
         [5, 5, 3, 1],
         [100, 4, 200, 1, 3, 2],
         [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
         [-5, 8, 1, -1, -3, -2, 0],
         [2],
         [],
         None]
fns = [find_longest_consecutive_sequence_naive,
       find_longest_consecutive_sequence_via_sort,
       find_longest_consecutive_sequence_via_set,
       find_longest_consecutive_sequence_via_dict]

for l in lists:
    for fn in fns:
        print(f"{fn.__name__}({l}): {fn(copy.deepcopy(l))}")
    print()


