"""
    THE KNAPSACK PROBLEM (EPI 17.6,
                          50CIQ 2: KNAPSACK)

    A thief breaks into a clock store.  Each clock has a weight and a value, which are known to the thief.  His knapsack
    cannot hold more than a specified combined weight.  His intention is to take clocks whose total value is maximum
    subject to the knapsack's weight constraint.

    Write a program for the knapsack problem that selects a subset of items that has a maximum value and satisfies the
    weight constraint.  All items have integer weights and values.  Return the value of the subset.

    Example:
        Input = [(65, 20), (35, 8), (245, 60), (195, 55), (65, 40), (99, 10), (275, 85), (155, 25), (120, 30), (75, 75),
                 (320, 65), (40, 10), (200, 95), (100, 50), (220, 40), (150, 70)], 130  # (price, weight), total_weight
        Output = 695    # Max value set: [(155, 25), (320, 65), (220, 40)]

    Variations:
        - Solve the same problem using O(w) space, where w is the initial capacity.
        - Solve the same problem using O(c) space, where c is the number of weights between 0 and w that can be
          achieved. For example, if the weights are 100, 200, 200, 500, and w=853, then c=9, corresponding to the
          weights 0, 100, 200, 300, 400, 500, 600, 700, 800.
        - Solve the fractional knapsack problem. In this formulation, the thief can take a fractional part of an item,
          e.g., by breaking it.  Assume the value of a fraction of an item is that fraction times the value of the item.
        - In the 'divide-the-spoils-fairly' problem, two thieves who have successfully completed a burglary want to know
          how to divide the stolen items into two groups such that the difference between the value of these two groups
          is minimized. Write a program to solve the divide-the-spoils-fairly problem.
        - Solve the divide-the-spoils-fairly problem with the additional constraint that the thieves have the same
          number of items.
"""
import itertools
import sys
import time


# APPROACH: Recursive
#
# Time Complexity:
# Space Complexity:
def knapsack_rec(l, max_w):
    def _knapsack_rec(l, i, cap, value):
        if i == len(l) or cap == 0:
            return value
        included = _knapsack_rec(l, i+1, cap - l[i].weight, value + l[i].value) if cap >= l[i].weight else 0
        excluded = _knapsack_rec(l, i+1, cap, value)
        return max(included, excluded)
    if l and max_w > 0:
        return _knapsack_rec(l, 0, max_w, 0)


# APPROACH: Powerset (Via Itertools Combinations)
#
# Time Complexity: O(2**s), where s is the number of elements in items list.
# Space Complexity: O(m), where m is the size of the max value set (could be O(1) if max_price_set isn't maintained).
def knapsack_power_set(items, capacity):
    if items is not None and capacity is not None and capacity > 0:
        max_price_set = None
        max_price = -sys.maxsize
        for r in range(len(items)):
            for s in itertools.combinations(items, r):
                if sum(x.weight for x in s) <= capacity:
                    price = sum(x.value for x in s)
                    if price > max_price:
                        max_price = price
                        max_price_set = set(s)
        return max_price, max_price_set


# APPROACH: Combinatorics/Iterative
#
# Time Complexity: O(2**s), where s is the number of elements in items list.
# Space Complexity: O(m), where m is the size of the max value set (could be O(1) if max_price_set isn't maintained).
def knapsack_combinatorics(items, capacity):

    def _gen_reversed_bits(n):
        while True:
            yield n & 1
            n >>= 1

    if items is not None and capacity is not None and capacity > 0:
        max_price_set = None
        max_price = -sys.maxsize
        for i in range(2**len(items)):
            g = _gen_reversed_bits(i)
            s = {e for e, b in zip(items, g) if b}
            if sum(x.weight for x in s) <= capacity:
                price = sum(x.value for x in s)
                if price > max_price:
                    max_price = price
                    max_price_set = s
        return max_price, max_price_set


# APPROACH: Memoization/Dynamic Programming
#
# This approach is just a coded version of the following recurrence:
#       V[i][w]  =  max(V[i-1][w], V[i-1][w-i.w]+i.v)       if i.w < w
#                   V[i-1][w]                               otherwise
#   Where:
#       V is the Max Value/Price memoization table (0..i rows, 0..w columns, initialized to -1, start/end at [i][w])
#       i is the size of the items list; each item has a weight i.w and value i.v.
#       w is the weight capacity.
#
# Time and space complexity is O(sw), where s is the size of the items list.
#
# Example:
#   Items Table:
#              Val Weight
#            |-----------
#           0| $60    5oz
#           1| $50    3oz
#           2| $70    4oz
#           3| $30    2oz
#
#   Completed Knapsack (V/Max Value/Price) Table:
#                    CAPACITY
#               0   1   2   3   4   5
#            |-----------------------
#       I   0|  0   0   0   0  -1  60
#       T   1| -1   0  -1  50  -1  60
#       E   2| -1  -1  -1  50  -1  70
#       M   3| -1  -1  -1  -1  -1  80  <-- Starts/ends/returns at [3][5] OR [len(items)][capacity]
#
# NOTE: This approach ASSUMES WHOLE NUMBER/INTEGER VALUES for prices and weights!
# NOTE: This approach DOESN'T maintain the set associated with the max value!
def knapsack_memo(items, capacity):     # ASSUMES INTEGERS!  Modify with math.ceil() if real nums are wanted!

    def _knapsack_memo(items, i, cap, memo):
        if i < 0:
            return 0
        if memo[i][cap] == -1:
            without_curr_item = _knapsack_memo(items, i - 1, cap, memo)
            with_curr_item = 0 if cap < items[i].weight else items[i].value + _knapsack_memo(items, i - 1, cap - items[i].weight, memo)
            memo[i][cap] = max(without_curr_item, with_curr_item)
        return memo[i][cap]

    if items is not None and capacity is not None:
        memo = [[-1] * (capacity + 1) for _ in range(len(items))]   # memo[len(items)][capacity] has max value when done
        return _knapsack_memo(items, len(items) - 1, capacity, memo)


class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        return f"(Value: {self.value}, Weight: {self.weight})"


items = [Item(65, 20), Item(35, 8), Item(245, 60), Item(195, 55), Item(65, 40), Item(99, 10), Item(275, 85),
         Item(155, 25), Item(120, 30), Item(75, 75), Item(320, 65), Item(40, 10), Item(200, 95), Item(100, 50),
         Item(220, 40), Item(150, 70)]
weight_capacity = 130
fns = [knapsack_rec,
       knapsack_power_set,
       knapsack_combinatorics,
       knapsack_memo]

print(f"items: {items}\nweight_capacity: {weight_capacity}\n")

for fn in fns:
    t = time.time()
    print(f"{fn.__name__}(items, max_weight),", end="")
    result = fn(items, weight_capacity)
    print(f" took {time.time() - t} seconds: {result}")


