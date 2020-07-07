"""
    DIVING BOARD

    You are building a diving board by placing a bunch of planks of wood end-to-end.  There are two types of planks,
    one of length shorter and one of length longer.  You must use exactly K planks of wood.  Write a method to generate
    all possible lengths for the diving board.

    NOTE: You are given the number K, and two whole numbers representing the lengths of the two boards.
"""
import time


def get_lengths_recursive(k, a, b):
    l = set()
    if k <= 0 or a <= 0 or b <=0:
        return None;
    if k == 1:
        return [a, b]
    if k > 1:
        c = get_lengths_recursive(k - 1, a, b)
        for i in c:
            l.add(i + a)
            l.add(i + b)
    return l


def get_lengths_mem(k, a, b):
    if k <= 0 or a <= 0 or b <=0:
        return None;
    l = [None] * (k + 1)
    l[1] = set({a, b})
    return get_lengths_memoization(k, a, b, l)


def get_lengths_memoization(k, a, b, l):
    if k == 1:
        return set({a, b})
    if l[k] is None:
        l[k-1] = get_lengths_memoization(k - 1, a, b, l)
        l[k] = set()
        for i in l[k-1]:
            l[k].add(i + a)
            l[k].add(i + b)
    return l[k]


# Tabulation, or bottom up.
def get_lengths_tabulation(k, a, b):
    if k == 0:
        return set({0})
    if k == 1:
        return set({a, b})

    l = [None] * (k + 1)
    l[1] = set({a, b})
    i = 2

    while i <= k:
        l[i] = set()
        for j in l[i - 1]:
            l[i].add(j + a)
            l[i].add(j + b)
        i += 1

    return l[k]


# OPTIMAL SOLUTION
# If you look at the problem mathematically, you'll see that a series arises:
# Lengths = ((k - 0) * shorter + 0 * longer) +
#           ((k - 1) * shorter + 1 * longer) +
#                       ....
#           ((k - k) * shorter + k * longer)
# Knowing this, you can simply iterate over k.
def get_all_lengths(k, shorter, longer):
    lengths = set()
    number_shorter = 0
    while number_shorter <= k:
        number_longer = k - number_shorter
        length = number_shorter * shorter + number_longer * longer
        lengths.add(length)
        number_shorter += 1
    return lengths


k = 5
print(f"k = {k}")
board_one = 3
print(f"board_one = {board_one}")
board_two = 10
print(f"board_two = {board_two}")

t = time.time()
print("\nRecursive Solution:  ", sorted(get_lengths_recursive(k, board_one, board_two)))
print(f"Time: {time.time() - t}")

t = time.time()
print("\nMemoization Solution:", sorted(get_lengths_mem(k, board_one, board_two)))
print(f"Time: {time.time() - t}")

t = time.time()
print("\nTabulation Solution: ", sorted(get_lengths_tabulation(k, board_one, board_two)))
print(f"Time: {time.time() - t}")

t = time.time()
print("\nOptimal Solution:    ", sorted(get_all_lengths(k, board_one, board_two)))
print(f"Time: {time.time() - t}")






