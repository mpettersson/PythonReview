"""
    COINS

    Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent), write
    code to calculate the number of ways of representing n cents.
"""


# Recursive solution without Memoization
def make_change_rec(n):
    denoms = [25, 10, 5, 1]
    return _make_change_rec(n, denoms, 0)


def _make_change_rec(amount, denoms, index):
    if index >= len(denoms) - 1:
        # The last denoms
        return 1
    denom_amount = denoms[index]
    ways = 0
    i = 0
    while i * denom_amount <= amount:
        amount_remaining = amount - i * denom_amount
        ways += _make_change_rec(amount_remaining, denoms, index + 1)
        i += 1
    return ways


# Recursive solution WITH Memoization
def make_change_rec_memo(n):
    denoms = [25, 10, 5, 1]
    map = [[0] * len(denoms) for _ in range(n + 1)]
    return _make_change_rec_memo(n, denoms, 0, map)


def _make_change_rec_memo(amount, denoms, index, map):
    if map[amount][index] > 0:
        return map[amount][index]
    if index >= len(denoms) - 1:
        return 1
    denom_amount = denoms[index]
    ways = 0
    i = 0
    while i * denom_amount <= amount:
        amount_remaining = amount - i * denom_amount
        ways += _make_change_rec_memo(amount_remaining, denoms, index + 1, map)
        i += 1
    map[amount][index] = ways
    return ways


import time

sm = 4
print("sm:", sm)
print("make_change_rec(", sm, "):", make_change_rec(sm))
print("make_change_rec_memo(", sm, "):", make_change_rec_memo(sm))
print()

med = 69
print("med:", med)
print("make_change_rec(", med, "):", make_change_rec(med))
print("make_change_rec_memo(", med, "):", make_change_rec_memo(med))
print()

lg = 2999
print("lg:", lg)
t = time.time(); print("make_change_rec(", lg, "):", make_change_rec(lg), end=""); print("      took:", time.time() - t)
t = time.time(); print("make_change_rec_memo(", lg, "):", make_change_rec_memo(lg), end=""); print(" took:", time.time() - t)
