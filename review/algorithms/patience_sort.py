"""
    PATIENCE SORT

    Patience sort is a sorting algorithm with two main parts; first, greedily distributing the elements into 'piles' of
    non-increasing values, then, merging the sorted piles into a single sorted sequence. The algorithm's name derives
    from a version of the patience card game.

    Average Runtime:    TODO O(n * log(n))
    Worst Runtime:      TODO O(n * log(n))
    Best Runtime:       O(n)    (elements are already sorted)
    Space Complexity:   O(n)
    Alg Paradigm:       TODO
    Sorting In Place:   TODO
    Stable:             No      (the relative order of elements with equal keys are changed)
    Online:             TODO      (can sort a list as it receives it)

    Patience Card Game Rules:
        1.  Initially, there are no piles. The first card dealt forms a new pile consisting of the single card.
        2.  Each subsequent card is placed on the leftmost existing pile whose top card has a value greater than or
            equal to the new card's value, or to the right of all of the existing piles, thus forming a new pile.
        3.  When there are no more cards remaining to deal, the game ends.

    References:
        - wikipedia.org/wiki/Patience_sorting
"""
from functools import total_ordering
from bisect import bisect_left
from heapq import merge


# O(NlogK) where N is the total number of elements and K are the items fed into the minheap for comparison.
# The space complexity is O(K) because the minheap has K items at any given point in time during the execution.
def patience_sort(n):
    piles = []
    for x in n:
        new_pile = Pile([x])
        i = bisect_left(piles, new_pile)
        if i != len(piles):
            piles[i].append(x)
        else:
            piles.append(new_pile)

    n[:] = merge(*[reversed(pile) for pile in piles])       # use a heap-based merge to merge piles efficiently
    return n


@total_ordering
class Pile(list):
    def __lt__(self, other): return self[-1] < other[-1]
    def __eq__(self, other): return self[-1] == other[-1]


lists = [[4, 65, 2, -31, 0, 99, 83, 782, 1],
         [44, 77, 59, 39, 41, 69, 72, 72, 41, 37, 11, 72, 16, 22, 33],
         [170, 45, 2, 75, 90, 802, 24, 2, 66, 0, -1],
         [44, 77, 59, 39, 41, 69, 68, 10, 72, 99, 72, 11, 41, 37, 11, 72, 16, 22, 10, 100],
         [44, 77, 59, 39, 41, 69, 68, 10, 72, 99, 72, 11, 41, 37, 11, 72, 16, 22, 10, 33],
         []]
fns = [patience_sort]

for l in lists:
    print(f"l: {l}")
    for fn in fns:
        print(f"{fn.__name__}(l): {fn(l[:])}")
    print()


