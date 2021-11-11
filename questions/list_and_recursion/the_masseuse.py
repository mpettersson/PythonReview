"""
    THE MASSEUSE

    A popular masseuse receives a sequence of back-to-back appointment requests and is debating which ones to accept.
    She needs a 15-minute break between appointments and therefore she cannot accept any adjacent requests.  Given a
    sequence of back-to-back appointment requests (all multiples of 15 minutes, none overlap, and none can be moved),
    find the optimal (highest total booked minutes) set the masseuse can honor.  Return the number of minutes.

    Example
        Input: [30, 15, 60, 75, 45, 15, 15, 45]
        Output: 180 [30, 60, 45, 45]

    NOTE: We must skip consecutive appointments, but we'd NEVER skip three consecutive appointments.
"""
import time


# Approach 1: Recursive solution; O(2**N) time (because each call has two recursive calls) and O(N) space.
def masseuse_schedule_recursive(requests):
    if requests is None or len(requests) <= 1:
        return requests

    accepted = [requests[0]] + masseuse_schedule_recursive(requests[2:])
    rejected = masseuse_schedule_recursive(requests[1:])

    return accepted if sum(accepted) > sum(rejected) else rejected


# Approach 2: Recursive & Memoization; O(N) runtime and O(N) space (bc recursive call stack and memo_list).
def masseuse_schedule_memoization(requests):
    if requests is None or len(requests) <= 1:
        return requests
    memo_list = [None] * (len(requests) + 1)
    return masseuse_schedule_memo(requests, memo_list)


def masseuse_schedule_memo(requests, memo_list):
    if requests is None or len(requests) <= 1:
        return requests
    if memo_list[len(requests)] is None:
        accepted = [requests[0]] + masseuse_schedule_memo(requests[2:], memo_list)
        rejected = masseuse_schedule_memo(requests[1:], memo_list)
        memo_list[len(requests)] = accepted if sum(accepted) > sum(rejected) else rejected
    return memo_list[len(requests)]


# Approach 3: Iterative & Memoization; O(N) runtime and O(N) space (bc memo_list).
# This runs slightly faster than Recursive & Memoization, but still has the same time and space complexity...
def masseuse_schedule_iterative_memo(requests):
    memo_list = [[]] * (len(requests) + 2)  # Because we skip at most 2 appointments we will add 2 positions.
    for i in range(len(requests) - 1, -1, -1):
        best_with = [requests[i]] + memo_list[i + 2]  # The first 2 iterations will check 2 added (empty) positions.
        best_without = memo_list[i + 1]
        memo_list[i] = best_with if sum(best_with) > sum(best_without) else best_without
    return memo_list[0]


# Approach 4: (Optimal) Iterative (no memoization); O(N) runtime and O(1) space!
def masseuse_schedule_iterative(requests):
    one_away = []
    two_away = []
    for i in range(len(requests) - 1, -1, -1):
        best_with = [requests[i]] + two_away  # The first 2 iterations will check 2 added (empty) positions.
        best_without = one_away
        current = best_with if sum(best_with) > sum(best_without) else best_without
        two_away = one_away
        one_away = current
    return one_away


appointment_requests = [30, 15, 60, 75, 45, 15, 15, 45, 30, 15, 60, 75, 45, 15, 15, 45, 30, 15, 60, 75, 45, 15, 15, 45]
print("appointment_requests:", appointment_requests)
print()

t = time.time()
print("masseuse_schedule_recursive(appointment_requests):     ", masseuse_schedule_recursive(appointment_requests), "(took", time.time() - t, "seconds)")
t = time.time()
print("masseuse_schedule_memoization(appointment_requests):   ", masseuse_schedule_memoization(appointment_requests), "(took", time.time() - t, "seconds)")
t = time.time()
print("masseuse_schedule_iterative_memo(appointment_requests):", masseuse_schedule_iterative_memo(appointment_requests), "(took", time.time() - t, "seconds)")
t = time.time()
print("masseuse_schedule_iterative(appointment_requests):     ", masseuse_schedule_iterative(appointment_requests), "(took", time.time() - t, "seconds)")



