"""
    THE UNBOUNDED FRACTIONAL (OR CONTINUOUS) KNAPSACK PROBLEM

    Given a set of items that each have a value, a weight, and an unlimited (unbounded) number of units, determine the
    set of fractional items to select to maximize the total value, constrained by the given knapsack's capacity.

    Example:
                items = [(65, 20), (35, 8), (245, 60), (195, 55), (65, 40), (99, 10), (275, 85), (155, 25), (120, 30),
                         (75, 75), (320, 65), (40, 10), (200, 95), (100, 50), (220, 40), (150, 70)] # (price, weight)
                capacity = 130
        Input = items, capacity
        Output = 1287, 13.0, (99, 10)   # Or, the value is 1287, for 13x, of item (99, 10).
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What are the possible values for capacity (int, None, negative, etc.)?
#   - Does the full capacity need to be used (what should happen if can't use total capacity)?
#   - What should be returned (total, or list of items, what should happen if failure)?
#   - What are the possible sizes of the list (empty, max size)?
#   - What are the possible values in the list (int/float/None/negative)?
#   - Can the list have unique/duplicate values?
#   - Will the list be sorted?
#   - Can the list be modified?


# APPROACH: Greedy
#
# This is perhaps the easiest of the knapsack variations; simply find the maximum value:weight ratio (from each of the
# provided items), then multiply it (best ratio) with the provided capacity.
#
# Time Complexity: O(n), where n is the number of items.
# Time Complexity: O(1).
def knapsack_unbounded_fractional(items, capacity):
    n = len(items)
    max_ratio_index = None
    max_ratio = -float('inf')
    for i in range(n):                                  # Find the item with the highest value:weight ratio;
        curr_ratio = items[i].value / items[i].weight       # once found, use all the knapsacks capacity for it.
        if curr_ratio > max_ratio:
            max_ratio_index = i
            max_ratio = curr_ratio
    if max_ratio_index is not None:                     # Return whatever the interviewer wants:
        return (max_ratio * capacity,                       # The max value.
                capacity / items[max_ratio_index].weight,   # How many of the items were selected.
                items[max_ratio_index])                     # The item with the best (value:weight) ratio.


class Item:
    def __init__(self, value, weight, name=None, units=1):
        self.value = value
        self.weight = weight
        self.name = name
        self.units = units

    def __repr__(self):
        return ((f"(Name: {self.name}, " if self.name else "(") +
                f"Value: {self.value}, Weight: {self.weight}" +
                (f", Units: {self.units})" if self.units > 1 else ")"))


args = [(130, [Item(65, 20), Item(35, 8), Item(245, 60), Item(195, 55), Item(65, 40), Item(99, 10), Item(275, 85),
               Item(155, 25), Item(120, 30), Item(75, 75), Item(320, 65), Item(40, 10), Item(200, 95), Item(100, 50),
               Item(220, 40), Item(150, 70)]),
        (15, [Item(36.0, 3.8, 'beef'), Item(43.0, 5.4, 'pork'), Item(90.0, 3.6, 'ham'), Item(45.0, 2.4, 'greaves'),
              Item(30.0, 4.0, 'flitch'), Item(56.0, 2.5, 'brawn'), Item(67.0, 3.7, 'welt'), Item(95.0, 3.0, 'salami'),
              Item(98.0, 5.9, 'sausage')]),
        (10, [Item(10, 5), Item(40, 4), Item(30, 6), Item(60, 3)])]
fns = [knapsack_unbounded_fractional]

for capacity, items in args:
    print(f"\nitems: {items}\ncapacity: {capacity}")
    for fn in fns:
        print(f"{fn.__name__}(items, capacity): {fn(items, capacity)}")


