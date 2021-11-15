"""
    THE 01 FRACTIONAL (OR CONTINUOUS) KNAPSACK PROBLEM

    Given a set of items that each have a value, and a weight, determine the set of fractional items to select to
    maximize the total value, constrained by the given knapsack's capacity.

    Example:
                          # name         weight        value
                items = [('beef',           3.8,        36.0),
                         ('pork',           5.4,        43.0),
                         ('ham',            3.6,        90.0),
                         ('greaves',        2.4,        45.0),
                         ('flitch',         4.0,        30.0),
                         ('brawn',          2.5,        56.0),
                         ('welt',           3.7,        67.0),
                         ('salami',         3.0,        95.0),
                         ('sausage',        5.9,        98.0)]
                capacity = 15
        Input = items, capacity
        Output = 1287, 13.0, (99, 10)   # Or, the value is 1287, for 13x, of item (99, 10).
"""
import copy


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
# This approach sorts the list items (from high to low) according to their value:weight ratio, then, then greedily
# fills the knapsack.
#
# Time Complexity: O(n * log(n)), where n is the length of the items list.
# Space Complexity: O(1).
def knapsack_01_fractional(items, capacity):
    items.sort(key=lambda x: x.value/x.weight, reverse=True)
    result_value = 0
    result_set = []
    for item in items:
        curr_weight = min(capacity, item.weight)                # curr_weight = how much of this item can be used.
        capacity -= curr_weight                                 # Update capacity.
        curr_value = curr_weight * item.value/item.weight       # curr_value = the value for curr_weight's of this item.
        result_value += curr_value                              # Update the resulting value.
        result_set += [(curr_weight, curr_value, item)]         # Return whatever your interviewer wants...
        if capacity == 0:                                       # Terminate once the knapsack is full.
            break
    return result_value, result_set                             # Again, return whatever your interviewer wants.


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


args = [(15, [Item(36.0, 3.8, 'beef'), Item(43.0, 5.4, 'pork'), Item(90.0, 3.6, 'ham'), Item(45.0, 2.4, 'greaves'),
              Item(30.0, 4.0, 'flitch'), Item(56.0, 2.5, 'brawn'), Item(67.0, 3.7, 'welt'), Item(95.0, 3.0, 'salami'),
              Item(98.0, 5.9, 'sausage')]),
        (130, [Item(65, 20), Item(35, 8), Item(245, 60), Item(195, 55), Item(65, 40), Item(99, 10), Item(275, 85),
               Item(155, 25), Item(120, 30), Item(75, 75), Item(320, 65), Item(40, 10), Item(200, 95), Item(100, 50),
               Item(220, 40), Item(150, 70)]),
        (10, [Item(10, 5), Item(40, 4), Item(30, 6), Item(60, 3)])]
fns = [knapsack_01_fractional]

for capacity, items in args:
    print(f"\nitems: {items}\ncapacity: {capacity}")
    for fn in fns:
        print(f"{fn.__name__}(items, capacity): {fn(copy.deepcopy(items), capacity)}")
    print()


