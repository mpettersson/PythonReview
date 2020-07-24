"""
    NUM SUBSETS WITH SUM K

    Given a list of integers and a value (k) write a function that returns the number of subsets with sum equal to k.

    Example:
        Input = [2, 4, 6, 10], 16
        Output = 2 (or the subsets {2, 4, 10} and {6, 10})

    NOTE: It is important to ask clarifying questions, for example:
            - Can there be repeating values?
            - Can there be negative values?
            - What if k is zero?
"""
import copy


# Naive Solution: Get power set, then sum each of the sets.
def num_subsets_with_sum_k(l, k):
    count = 0
    ps = power_set(set(l)) + [set()]
    valid = []
    for s in ps:
        if sum(s) == k:
            valid.append(s)
            count += 1
    return count


def power_set(s):
    if not s or len(s) <= 1:
        return [s]

    h = s.pop()
    t = power_set(s)
    temp = copy.deepcopy(t)

    for ss in temp:
        ss.add(h)

    return [{h}] + temp + t


# Recursive (Non-Powerset) Approach:
# NOTE: This assumes that the list consists of positive integers ONLY.
def num_subsets_with_sum_k_no_power_set(arr, total):
    return num_subsets_with_sum_k_no_ps(arr, total, len(arr) - 1)


def num_subsets_with_sum_k_no_ps(arr, total, i):
    if total is 0:
        return 1
    if total < 0 or i < 0:
        return 0
    if total < arr[i]:
        return num_subsets_with_sum_k_no_ps(arr, total, i - 1)
    return num_subsets_with_sum_k_no_ps(arr, total - arr[i], i - 1) + num_subsets_with_sum_k_no_ps(arr, total, i - 1)


# Top Down Dynamic Programming Approach: Runtime is O(
# NOTE: The simple memoization technique of using a LIST will NOT easily/efficiently work here; in stead, use a DICT!
def num_subsets_with_sum_k_tddp(arr, total):
    memo = {}
    return num_subsets_with_sum_k_td(arr, total, len(arr) - 1, memo)


def num_subsets_with_sum_k_td(arr, total, i, memo):
    key = str(total) + ":" + str(i)
    if total is 0:
        return 1
    if total < 0 or i < 0:
        return 0
    if key in memo:
        return memo[key]
    if total < arr[i]:
        memo[key] = num_subsets_with_sum_k_td(arr, total, i - 1, memo)
        return memo[key]
    memo[key] = num_subsets_with_sum_k_td(arr, total - arr[i], i - 1, memo) + num_subsets_with_sum_k_td(arr, total, i - 1, memo)
    return memo[key]


args = [([2, 4, 6, 10], 16),
        ([10, 6, 4, 2], 16),
        ([2, 4, 6, 10], 0),
        ([1, 2, 4, 6, 8, 10, 12, 16, 22, 25, 99], 30)]

for (l, k) in args:
    print(f"num_subsets_with_sum_k({l}, {k}):", num_subsets_with_sum_k(l, k))
print()

for (l, k) in args:
    print(f"num_subsets_with_sum_k_no_power_set({l}, {k}):", num_subsets_with_sum_k_no_power_set(l, k))
print()

for (l, k) in args:
    print(f"num_subsets_with_sum_k_tddp({l}, {k}):", num_subsets_with_sum_k_tddp(l, k))




