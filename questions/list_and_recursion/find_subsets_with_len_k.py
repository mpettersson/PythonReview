"""
    FIND SUBSETS WITH LENGTH K (EPI 16.5: GENERATE ALL SUBSETS OF SIZE K)

    Write a function that takes a set s and size k, and returns all subsets of s with a length, or size, of k.

    Example:
        Input = {1, 2, 3, 4, 5}, 2
        Output = [{1, 2}, {1, 3}, {1, 4}, {1, 5}, {2, 3}, {2, 4}, {2, 5}, {3, 4}, {3, 5}, {4, 5}]
"""
import copy
import itertools
import time


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Verify subsets (or combinations, not permutations)?
#   - What type of data structure is provided?
#   - What are the size limits of the data structure?
#   - What are the data types in the provided data structure?
#   - Are the elements ordered?
#   - Are there duplicate values in the data structure (multiset)?
#   - Should the output contain only unique sets?
#   - Can the input be modified?


# NOTE: The following are listed in order of FASTEST TO SLOWEST (for an input with length 18):


# APPROACH: Via Itertools Combinations
#
# This approach uses the itertools combinations function.
#
# Time complexity: between O(n * (n choose k)) and O(2**n), where n is the number of elements in s.
# Space complexity: between O(n * (n choose k)) and O(2**n), where n is the number of elements in s.
def find_subsets_with_len_k_via_itertools_combinations(s, k):
    if s is not None and k is not None and 0 <= k:
        return list(itertools.combinations(s, k))


# APPROACH: Via Recursion/DFS
#
# This approach recursively builds a set (accumulator), where each recursion uses the set difference of the calling
# functions supplied set and most recently added value to the accumulated set.  Once the accumulated set has a size of
# k, the set is added to the result list.
#
# Time complexity: between O(n * (n choose k)) and O(2**n), where n is the number of elements in s.
# Space complexity: between O(n * (n choose k)) and O(2**n), where n is the number of elements in s.
def find_subsets_with_len_k_via_dfs(s, k):

    def _rec(i, path):              # path == accumulator.
        if len(path) == k:
            result.append(path)
            return
        for j in range(i, len(l)):
            _rec(j+1, path + [l[j]])

    if s is not None and k is not None and 0 <= k:
        result = []
        l = list(s)
        _rec(0, [])
        return result


# APPROACH: Via Recursive Sets
#
# This approach recursively builds a set (accumulator), where each recursion uses the set difference of the calling
# functions supplied set and most recently added value to the accumulated set.  Once the accumulated set has a size of
# k, the set is added to the result list.
#
# Time complexity: between O(n * (n choose k)) and O(2**n), where n is the number of elements in s.
# Space complexity: between O(n * (n choose k)) and O(2**n), where n is the number of elements in s.
def find_subsets_with_len_k_via_sets_rec(s, k):

    def _rec(s, k, accumulator, result):
        if k == 0:
            if accumulator not in result:
                result.append(accumulator)
        else:
            for i in s:
                _rec(s.difference({i}), k-1, accumulator.union({i}), result)

    if s is not None and k is not None and 0 <= k:
        result = []
        _rec(set(s), k, set(), result)
        return result


# APPROACH: Combinatorics/Bit Masking
#
# Using the fact that there are 2**n sets in a power set, we can use the set bits of the binary representation of the
# numbers (in the range 0 to 2**n - 1) to generate the subsets of the given set s.
#
# Time Complexity: O(2**n), where n is the number of set s items (since we must check EACH of the 2**n sets).
# Space Complexity: O(n choose k), where n is the number of elements in s.
def find_subsets_with_len_k_via_combinatorics(s, k):

    def _has_k_set_bits(n, k):
        count = 0
        while n:
            n &= (n - 1)
            count += 1
        return count is k

    def _gen_reversed_bits(n):
        while True:
            yield n & 1
            n >>= 1

    if s is not None and k is not None and 0 <= k:
        result = []
        for i in range(2**len(s)):
            if _has_k_set_bits(i, k):
                g = _gen_reversed_bits(i)
                result.append(set(itertools.compress(s, g)))  # Same as :result.append({x for b, x in zip(g, s) if b})
        return result


# APPROACH: Alternate Combinatorics/Bit Masking
#
# This approach, although implemented differently, has the same logic and theory as the combinatorics approach above.
#
# Time Complexity: O(2**n), where n is the number of set s items (since we must check EACH of the 2**n sets).
# Space Complexity: O(n choose k), where n is the number of elements in s.
def find_subsets_with_len_k_via_combinatorics_alt(s, k):

    def _has_k_set_bits(n, k):
        count = 0
        while n:
            n &= (n-1)
            count += 1
        return count == k

    if s is not None and k is not None and 0 <= k:
        result = []
        length = len(s)
        for i in range(2**length):
            if _has_k_set_bits(i, k):
                result.append({x for b, x in zip([int(c) for c in f"{i:b}".zfill(length)], s) if b})
        return result


# APPROACH: Naive/Brute Force Via Power Set
#
# This approach naively creates a power set, or all unique subsets of the set, of the provided set.  Once the power set
# is created, any sub-sets with a size not equal to k are removed.  The remaining sets are then returned.
#
# Time Complexity: O(2**n), where n is the number of set s items.
# Space Complexity: O(2**n), where n is the number of set s items.
def find_subsets_with_len_k_via_naive_power_set(s, k):

    def _power_set(s):
        if s is not None:
            if len(s) == 0:
                return [set()]
            h = s.pop()
            t = _power_set(s)
            ht = copy.deepcopy(t)
            for i in ht:
                i.add(h)
            return t + ht

    if s is not None and k is not None and 0 <= k:
        result = _power_set(set(copy.deepcopy(s)))
        i = 0
        while i < len(result):
            if len(result[i]) != k:
                result.pop(i)
            else:
                i += 1
        return result


iterables = [{'A', 'B', 'C'},
             [0, 1, 2, 4],
             "abc",
             range(5),
             set(),
             []]
k_vals = [2, 3, 4]
fns = [find_subsets_with_len_k_via_itertools_combinations,
       find_subsets_with_len_k_via_dfs,
       find_subsets_with_len_k_via_sets_rec,
       find_subsets_with_len_k_via_combinatorics,
       find_subsets_with_len_k_via_combinatorics_alt,
       find_subsets_with_len_k_via_naive_power_set]

for iterable in iterables:
    print(f"\niterable: {iterable}")
    for k in k_vals:
        for fn in fns:
            print(f"{fn.__name__}(iterable, {k}): {fn(iterable, k)}")
        print()

s = set(range(18))
k = 2
print(f"s: {s}\nk: {k}")
for fn in fns:
    t = time.time()
    print(f"{fn.__name__}(s,k)", end="")
    fn(s.copy(), k)
    print(f" took {time.time() - t} seconds")


