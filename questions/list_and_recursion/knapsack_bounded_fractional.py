"""
    THE BOUNDED FRACTIONAL (OR CONTINUOUS) KNAPSACK PROBLEM

    Given a set of items that each have a value, a weight, and a number of units, determine the set of fractional items
    to select as to maximize the total value, constrained by the given knapsack's capacity.

    Example:
                items = (("map",                9,     150,     1),
                         ("compass",           13,      35,     1),
                         ("water",            153,     200,     3),
                         ("sandwich",          50,      60,     2),
                         ("candy",             15,      60,     2),
                         ("canned food",       68,      45,     3),
                         ("banana",            27,      60,     3),
                         ("apple",             39,      40,     3),
                         ("cheese",            23,      30,     1),
                         ("beer",              52,      10,     3),
                         ("sunscreen",         11,      70,     1),
                         ("camera",            32,      30,     1),
                         ("t-shirt",           24,      15,     2),
                         ("pants",             48,      10,     2),
                         ("umbrella",          73,      40,     1),
                         ("waterproof pants",  42,      70,     1),
                         ("waterproof jacket", 43,      75,     1),
                         ("notes",             22,      80,     1),
                         ("sunglasses",         7,      20,     1),
                         ("towel",             18,      12,     2),
                         ("socks",              4,      50,     1),
                         ("book",              30,      10,     2))
                         # name             weight    value  units
                capacity = 400
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
def knapsack_bounded_fractional(items, capacity):
    items.sort(key=lambda x: x.value / x.weight, reverse=True)
    result_value = 0
    result_set = []
    for item in items:
        curr_weight = min(capacity, item.weight * item.units)   # curr_weight = how much of this item can be used.
        # NOTE: The only difference from (regular) fractional knapsack is multiplying by 'item.units'!!!
        capacity -= curr_weight                                 # Update capacity.
        curr_value = curr_weight * item.value / item.weight     # curr_value = the value for curr_weight's of this item.
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


args = [(400, [Item(150, 9, 'map', 1), Item(35, 13, 'compass', 1), Item(200, 153, 'water', 3),
               Item(60, 50, 'sandwich', 2), Item(60, 15, 'candy', 2), Item(45, 68, 'canned food', 3),
               Item(60, 27, 'banana', 3), Item(40, 39, 'apple', 3), Item(30, 23, 'cheese', 1), Item(10, 52, 'beer', 3),
               Item(70, 11, 'sunscreen', 1), Item(30, 32, 'camera', 1), Item(15, 24, 't-shirt', 2),
               Item(10, 48, 'pants', 2), Item(40, 73, 'umbrella', 1), Item(70, 42, 'waterproof pants', 1),
               Item(75, 43, 'waterproof jacket', 1), Item(80, 22, 'notes', 1), Item(20, 7, 'sunglasses', 1),
               Item(12, 18, 'towel', 2), Item(50, 4, 'socks', 1), Item(10, 30, 'book', 2)])]
fns = [knapsack_bounded_fractional]

for capacity, items in args:
    print(f"\nitems: {items}\ncapacity: {capacity}")
    for fn in fns:
        print(f"{fn.__name__}(items, capacity): {fn(copy.deepcopy(items), capacity)}")
    print()


