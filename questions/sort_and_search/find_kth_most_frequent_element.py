"""
    FIND K MOST FREQUENT ELEMENTS (50CIQ 51: KTH MOST FREQUENT STRING)

    Write a function, which accepts a list and a positive integer k, then returns the kth most frequent element.

    Example:
        Input = ["a", "b", "e", "b", "d", "c", "d", "c", "a", "d", "a", "e"], 2
        Output = "a"  # Both "a" and "d" have a frequency of 3; either would be acceptable.
"""
import collections
import heapq
import itertools
import random
import time


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What about similar items (upper/lower cased strings, 2.0/2, etc.)?
#   - What if multiple k frequent items (all, or which one gets returned)?
#   - What is the behavior for invalid k values?


# APPROACH: Naive Count & Sort
#
# Build a dictionary with the elements as the keys and the frequency as the values, then sort on the values (in
# decreasing order) and return the element associated with the kth frequency.
#
# Time Complexity: O(n + (u * log(u))), where n is the size of l and u is the number of unique elements in l.
# Space Complexity: O(u), where u is the number of unique elements in l.
def find_kth_most_frequent_element_naive(l, k):
    if isinstance(l, list):
        if isinstance(k, int) and 0 < k:
            d = {}
            for e in l:
                d[e] = d.setdefault(e, 0) + 1
            d = {k: v for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True)}
            if k <= len(d):
                return list(d.keys())[k-1]
        raise IndexError("IndexError: invalid k")
    raise TypeError("TypeError: l must be of type list")


# APPROACH: Naive Count & Sort Minimized
#
# Build a dictionary with the elements as the keys and the frequency as the values, then sort on the values (in
# decreasing order) and return the element associated with the kth frequency.
#
# Time Complexity: O(n + (u * log(u))), where n is the size of l and u is the number of unique elements in l.
# Space Complexity: O(u), where u is the number of unique elements in l.
def find_kth_most_frequent_element_min(l, k):
    if isinstance(l, list):
        if isinstance(k, int) and 0 < k:
            return list({k: v for k, v in sorted(dict(collections.Counter(l)).items(), key=lambda x: (-x[1]))}.keys())[k - 1]
        raise IndexError("IndexError: invalid k")
    raise TypeError("TypeError: l must be of type list")


# APPROACH: Heapq
#
# Build a dictionary with the elements as the keys and the frequency as the values, then use a min heap
# with size equal to k to find the k largest elements.  Once all of the values in the dictionary have been push (and
# possibly popped) from the min heap, return the key at the top of the stack as the kth most frequent element.
#
# Time Complexity: O(n + (u * log(k))), where n is the size of l and u is the number of unique elements in l.
# Space Complexity: O(u), where u is the number of unique elements in l.
#
# NOTE: This has been designed to accept mixed type lists. And since heapq compares elements in a tuple (starting at
# index 0) until a different comparable pair is found, the id of the key must be placed before the key to prevent a
# TypeError from comparing 'str' to 'NoneType'.  This happens when two different keys are not the same type, but have
# the same value.  For example, if d = {None: 3, 'l': 3}, then the tuples in min_Heap would be (3, None) and (3, 'l'),
# so when heapq attempted to compare them, a TypeError would be raised.
def find_kth_most_frequent_element_heapq(l, k):
    if isinstance(l, list):
        if isinstance(k, int) and 0 < k:
            d = {}
            min_heap = []
            for e in l:
                d[e] = d.setdefault(e, 0) + 1                               # Find frequencies FIRST.
            if k <= len(d):
                for key, val in d.items():                                  # THEN put in min_heap to prevent duplicate
                    if len(min_heap) < k:                                       # values with different counts.
                        heapq.heappush(min_heap, (val, id(key), key))       # SEE note above about id(key).
                    elif val > min_heap[0][0]:
                        heapq.heappushpop(min_heap, (val, id(key), key))    # SEE note above about id(key).
                _, _, result = heapq.heappop(min_heap)
                return result
        raise IndexError("IndexError: invalid k")
    raise TypeError("TypeError: l must be of type list")


# APPROACH: (FASTEST) Counter & Heapq
#
# This is essentially the same approach as the heapq approach above, with the following exceptions:  The Counters object
# (from collections) is used (as opposed to using a plain dictionary).  The values were returned from heapq via the
# nlargest method (as opposed to constructing a return list via popping items off of the stack).
#
# Time Complexity: O(n + (m * log(m))), where n is the size of l and m is the number of distinct elements in l.
# Space Complexity: O(m), where m is the number of distinct elements in l.
def find_kth_most_frequent_element_counter_heapq(l, k):
    if isinstance(l, list):
        if isinstance(k, int) and 0 < k:
            counter = collections.Counter(l)
            if k <= len(counter):
                return heapq.nlargest(k, counter.keys(), key=counter.get)[-1]
        raise IndexError("IndexError: invalid k")
    raise TypeError("TypeError: l must be of type list")


# APPROACH: Quick Select
#
# Build a dictionary with the elements as the keys and the frequency as the values, then using the quick select
# algorithm, return the kth largest element.
#
# Time Complexity: O(n + u) (which reduces to O(n)) average time and a worst case time of O(n**2), where n is the size
#                  of l and u is the number of unique elements in l.
# Space Complexity: O(u), where u is the number of unique elements in l.
def find_kth_most_frequent_element_quick_select(l, k):

    def _quick_select(lo, hi, l, k):
        pivot_index = _partition(lo, hi, l)
        if pivot_index - lo is k - 1:
            return l[pivot_index]
        if pivot_index - lo > k - 1:
            return _quick_select(lo, pivot_index - 1, l, k)
        return _quick_select(pivot_index + 1, hi, l, k - pivot_index + lo - 1)

    def _partition(lo, hi, l):
        pivot_val = l[hi][0]
        i = lo
        for j in range(lo, hi):
            if l[j][0] <= pivot_val:
                l[i], l[j] = l[j], l[i]
                i += 1
        l[hi], l[i] = l[i], l[hi]
        return i

    if isinstance(l, list):
        if isinstance(k, int) and 0 < k:
            d = {}
            for e in l:
                d[e] = d.setdefault(e, 0) + 1
            m = [(val, key) for key, val in d.items()]
            if k <= len(m):
                k = len(m) - (k - 1)
                return _quick_select(0, len(m)-1, m, k)[1]
        raise IndexError("IndexError: invalid k")
    raise TypeError("TypeError: l must be of type list")


# APPROACH: Bucket Sort
#
# This approach uses bucket sort (because the frequency of any element can not be more than n) to create a list of lists
# (by frequency), then flattens the list to be able to return the kth element.
#
# Time Complexity: O(n), where n is the number of elements in l.
# Space Complexity: O(n), where n is the number of elements in l.
def find_kth_most_frequent_element_bucket_sort(l, k):
    if isinstance(l, list):
        if isinstance(k, int) and 0 < k:
            bucket = [[] for _ in range(len(l) + 1)]            # Empty buckets for frequencies 1 ... k.
            counter = collections.Counter(l)                    # Get a value:frequency count.
            if k <= len(counter):
                for num, freq in counter.items():
                    bucket[freq].append(num)                    # Put each value in its corresponding frequency bucket.
                return list(itertools.chain(*bucket))[-k]       # Flatten the list (of lists) & return the kth value.
        raise IndexError("IndexError: invalid k")
    raise TypeError("TypeError: l must be of type list")


lists = [["a", "b", "e", "b", "d", "c", "d", "a", "d", "a", "e"],
         [None, 'l', 4, 0, 'e', 'l', None, 'w', 4, 'l', 2, 2, ' ', 'r', 'd', None, 'o', 'h', 'o'],
         [1],
         [],
         None]
k_vals = [0, 1, 2, 4, 100, None]
fns = [find_kth_most_frequent_element_naive,
       find_kth_most_frequent_element_min,
       find_kth_most_frequent_element_heapq,
       find_kth_most_frequent_element_counter_heapq,
       find_kth_most_frequent_element_quick_select,
       find_kth_most_frequent_element_bucket_sort]

for l in lists:
    print(f"\nl: {l!r}\nFrequencies: {str(dict(collections.Counter(l)))[1:-1]}\n")
    for k in k_vals:
        for fn in fns:
            print(f"{fn.__name__}(l, {k}): ", end='')
            try:
                print(f"{fn(l, k)!r}")
            except Exception as e:
                print(e)
        print()

l = [random.randrange(-1000, 1001) for _ in range(500)]
k = 10
print(f"\nl: {l}\nk: {k}\n")
for fn in fns:
    t = time.time()
    print(f"{fn.__name__}(l,k): ", end="")
    fn(l[:], k)
    print(f" took {time.time() - t} seconds")


