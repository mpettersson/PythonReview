"""
    CIRCUS TOWER

    A circus is designing a tower routine consisting of people standing atop one another's shoulders.  For practical and
    aesthetic reasons, each person must be both shorter and lighter than the person below him or her.  Given the heights
    and weights of each person in the circus, write a method to compute the largest possible number of people in such a
    tower.

    Example
        Input: [(65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)]
        Output: [(56, 90), (60, 95), (65, 100), (68, 110), (70, 150), (75, 190)] (len == 6)
"""
import copy


# Approach 1: Recursive, runtime is O(2**N)
def longest_increasing_seq_recursive(items):
    htwt_items = [HtWt(x, y) for x, y in items]
    htwt_items.sort(key=lambda x: (x.height, x.weight))
    return [(x.height, x.weight) for x in best_seq_at_index_rec(htwt_items, [], 0)]


def best_seq_at_index_rec(array, sequence, index):
    if index >= len(array):
        return sequence
    value = array[index]
    best_with = None
    if can_append(sequence, value):
        sequence_with = copy.deepcopy(sequence)
        sequence_with.append(value)
        best_with = best_seq_at_index_rec(array, sequence_with, index + 1)
    best_without = best_seq_at_index_rec(array, sequence, index + 1)
    if best_with is None or len(best_without) > len(best_with):
        return best_without
    else:
        return best_with


def can_append(solution, value):
    if solution is None:
        return False
    if len(solution) == 0:
        return True
    last = solution[len(solution) - 1]
    return last.is_before(value)


class HtWt:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def is_before(self, other):
        if self.height < other.height and self.weight < other.weight:
            return True
        else:
            return False


# Approach 2:  Iterative, runtime is O(n**2).
def longest_increasing_seq_iterative(items):
    htwt_items = [HtWt(x, y) for x, y in items]
    htwt_items.sort(key=lambda x: (x.height, x.weight))
    solutions = []
    best_sequence = None
    for i in range(len(htwt_items)):
        longest_at_index = best_seq_at_index(htwt_items, solutions, i)
        solutions.append(longest_at_index)
        best_sequence = max(best_sequence, longest_at_index)
    return [(x.height, x.weight) for x in best_sequence]


def best_seq_at_index(array, solutions, index):
    value = array[index]
    best_sequence = []
    for i in range(index):
        solution = solutions[i]
        if can_append(solution, value):
            best_sequence = max(solution, best_sequence)
    best = copy.deepcopy(best_sequence)
    best.append(value)
    return best


def max(seq1, seq2):
    if seq1 is None:
        return seq2
    if seq2 is None:
        return seq1
    return seq1 if len(seq1) > len(seq2) else seq2


height_and_weights = [(65, 100), (70, 150), (56, 99), (56, 90), (75, 190), (60, 95), (68, 110)]
print("height_and_weights:", height_and_weights)
print()

print("longest_increasing_seq_recursive(height_and_weights):", longest_increasing_seq_recursive(height_and_weights))
print("longest_increasing_seq_iterative(height_and_weights):", longest_increasing_seq_iterative(height_and_weights))




