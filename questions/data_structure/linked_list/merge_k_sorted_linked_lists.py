r"""
    MERGE K SORTED LINKED LISTS (leetcode.com/problems/merge-k-sorted-lists)

    Write a function, that accepts k sorted (in ascending order) linked lists, then merges (in increasing sorted order)
    and returns one sorted (in ascending order) linked list.

    Consider the following linked lists:
        1 ⟶ 3 ⟶ 5 ⟶ 7
        0 ⟶ 8
        2 ⟶ 4 ⟶ 6
        0 ⟶ 1 ⟶ 2 ⟶ 3 ⟶ 4 ⟶ 5 ⟶ 6 ⟶ 7 ⟶ 8

    Example:
                l_1 = Node(1, Node(3, Node(5, Node(7)))),   # Or, the 1st linked list (above).
                l_2 = Node(0, Node(8)),                     # Or, the 2nd linked list.
                l_3 = Node(2, Node(4, Node(6)))             # Or, the 3rd linked list.
        Input = l_1, l_2, l_3
        Output = Node(0, Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8)))))))))  # Or, the 4th list.

    Variations:
        - SEE: merge_k_sorted_lists.py
"""
import copy
import heapq


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Should I modify the given lists?
#   - What are the possible number of lists?


# SLOW APPROACHES:
#   - Brute Force: Construct a list, sort it, then make a linked list.  Time: O(n * log(n)), Space: O(n)
#   - One By One: While there are values; find the k list heads min value for the new list. Time: O(k * n) Space O(n).


# APPROACH: Min Heap/Heapq
#
# Use a min heap of size k, where k is the number of lists, to track the value and head of each of the first nodes in
# the lists.  While there are values in the heap, continually pop the lowest value, replacing it with the next value if
# one exists in its list, until a merged list is created.
#
# Time Complexity: O(n * log(k)), where n is the total number of elements, and k is the number of lists.
# Space Complexity: O(k), where k is the number of lists
#
# NOTE: If the Node class is already defined WITHOUT a __lt__ method, execute the following line to add a __lt__ method:
#           Node.__lt__ = lambda self, node: self.value < node.value
def merge_k_sorted_linked_lists_heapq(l):
    head = tail = None
    if l:
        min_heap = []
        for e in l:
            head = e
            while head:
                curr = head
                head = head.next
                curr.next = None
                min_heap.append(curr)
        heapq.heapify(min_heap)
        while min_heap:
            curr = heapq.heappop(min_heap)
            if tail is None:
                head = tail = curr
            else:
                tail.next = curr
                tail = tail.next
    return head


# APPROACH: Dynamic Programming/Merge Sort
#
# While there are more than two lists, merge two lists at a time; when only one list remains, return its head.  That is;
# Pair up the k lists and merge each pair, (after the first pairing, k lists are merged into k/2 lists with average of
# 2N/k length, then k/4, k/8, etc.), repeat this procedure until the final sorted list is formed, and return it.
#
# Time Complexity: O(n * log(k)), where n is the total number of elements, and k is the number of lists.
# Space Complexity: O(1).
#
# NOTE: IF the k lists were merged one at a time (for example; via merging 2 lists k-1 times, or fold(merge, args, [])),
# then the time complexity would be O(k * n) NOT O(n * log(k)).  This is because the summation of the series would be;
# the sum from 1 to k-1, of ((i * (n/k)) + (n/k)), which equals O(k * n).
def merge_k_sorted_linked_lists_dp(l):

    def _merge_two_sorted_linked_lists(a, b):
        if not a or not b:
            return a if a else b
        head = curr = None
        while a and b:
            if a.value <= b.value:
                c = a
                a = a.next
            else:
                c = b
                b = b.next
            c.next = None
            if head is None:
                head = curr = c
            else:
                curr.next = c
                curr = curr.next
        if a or b:
            curr.next = a if a else b
        return head

    if l:
        while len(l) > 1:
            temp = []
            if len(l) % 2 == 1:
                temp.append(l.pop())
            while l:
                temp.append(_merge_two_sorted_linked_lists(l.pop(), l.pop()))
            l = temp
        return l.pop()
    return l


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    # NOTE: This is required because the naive heapq implementation will be comparing nodes.
    def __lt__(self, node):
        return self.value < node.value

    def __iter__(self):
        yield self.value
        if self.next:
            yield from self.next

    def __repr__(self):
        return ' ⟶ '.join(map(repr, self))


args_list = [[Node(1, Node(3, Node(5, Node(7)))),
              Node(0, Node(8)),
              Node(2, Node(4, Node(6)))],
             [Node(1, Node(3, Node(5, Node(7, Node(9))))),
              Node(0, Node(2, Node(4, Node(6, Node(8)))))],
             [Node(0, Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9))))))))))],
             [Node(-6, Node(-3, Node(5, Node(7)))),
              Node(0, Node(8)),
              Node(2, Node(4, Node(6))),
              Node(1, Node(3, Node(5, Node(7, Node(9))))),
              Node(-8, Node(-2, Node(-4, Node(6, Node(8))))),
              Node(-9, Node(-7, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9))))))))))],
             []]
fns = [merge_k_sorted_linked_lists_dp,
       merge_k_sorted_linked_lists_heapq]

for args in args_list:
    print("args:")
    for a in args:
        print(f"\t{a}")
    for fn in fns:
        print(f"{fn.__name__}(args): {fn(copy.deepcopy(args))}")
    print()


