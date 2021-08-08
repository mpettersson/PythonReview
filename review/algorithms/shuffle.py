"""
    SHUFFLE

    The Fisher–Yates shuffle (1938) is an algorithm for generating a random permutation of a finite sequence.  The alg
    produces an unbiased permutation: every permutation is equally likely.

    The Durstenfeld Shuffle (1964), as popularized by Knuth's "The Art of Computer Programming", is more efficient than
    Fisher-Yates version.

    The (Modern Approach) shuffle below is often referred to as the Fisher-Yates or Knuth Shuffle.
"""
import random


# Naive Shuffle Approach (WHAT NOT TO DO): Different permutations DO NOT have the same probabilities of being generated.
def naive_shuffle(items):
    n = len(items)
    for i in range(n):
        j = random.randrange(n)                     # 0 <= j <= n-1
        items[j], items[i] = items[i], items[j]
    return items


# Modern Approach: Each permutation DO have the same probability of being generated; O(n) Time, O(1) Space complexity.
# NOTE: An element may not move positions.
def shuffle(items):
    for i in range(len(items)-1, 0, -1):
        j = random.randrange(i + 1)                 # 0 <= j <= n-1
        items[i], items[j] = items[j], items[i]
    return items


# Same as above, but works from opposite direction (lowest index to highest index).
def shuffle_opposite_direction(items):
    for i in range(len(items) - 1):
        j = random.randrange(i, len(items))         # i <= j <= len(items)
        items[i], items[j] = items[j], items[i]
    return items


# Sattolo's algorithm for generating uniformly distributed cycles of (maximal) length n.
# NOTE: A UNIQUE item WILL NEVER stay in its original position.
def sattolo_cycle(items):
    i = len(items)
    while i > 1:
        i = i - 1
        j = random.randrange(i)                     # 0 <= j <= i-1
        items[j], items[i] = items[i], items[j]
    return items


print(f"naive_shuffle({[i for i in range(10)]}): {naive_shuffle([i for i in range(10)])}")
print(f"shuffle({[i for i in range(10)]}): {shuffle([i for i in range(10)])}")
print(f"shuffle_opposite_direction({[i for i in range(10)]}): {shuffle_opposite_direction([i for i in range(10)])}")
print(f"sattolo_cycle({[i for i in range(10)]}): {sattolo_cycle([i for i in range(10)])}")


