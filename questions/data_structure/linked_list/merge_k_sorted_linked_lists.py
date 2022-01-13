r"""
    MERGE K SORTED LINKED LISTS (leetcode.com/problems/merge-k-sorted-lists)

    Write a function, that accepts k sorted (in ascending order) linked lists, then merges (in increasing sorted order)
    and returns one sorted (in ascending order) linked list.

    Consider the following (3) linked lists:
        1 ⟶ 3 ⟶ 5 ⟶ 7
        0 ⟶ 8
        2 ⟶ 4 ⟶ 6
    The result of merging the above (3) linked lists:
        0 ⟶ 1 ⟶ 2 ⟶ 3 ⟶ 4 ⟶ 5 ⟶ 6 ⟶ 7 ⟶ 8

    Example:
                l_1 = Node(1, Node(3, Node(5, Node(7)))),   # Or, the 1st linked list (above).
                l_2 = Node(0, Node(8)),                     # Or, the 2nd linked list.
                l_3 = Node(2, Node(4, Node(6)))             # Or, the 3rd linked list.
        Input = l_1, l_2, l_3
        Output = Node(0, Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8)))))))))  # Or, the 4th/result.
"""
import copy
import heapq


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Should I modify the given lists?
#   - What are the possible number of lists?


# APPROACH: Naive Via Sort
#
# Construct a (python) list consisting of the values from all of the linked lists, then sort the (python) list, finally,
# create and return a linked list from the sorted list.
#
# Time Complexity: O(n * log(n)), where n is the total number of elements (in all k lists).
# Space Complexity: O(n), where n is the total number of elements (in all k lists).
def merge_k_sorted_linked_lists_naive(args):
    if args:
        l = [e for sl in args for e in sl]  # Can do this because Node has __iter__ method.
        l.sort()
        result = Node(l.pop(0))
        tail = result
        while l:
            tail.next = Node(l.pop(0))
            tail = tail.next
        return result


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
def merge_k_sorted_linked_lists_heapq(args):
    head = tail = None
    if args:
        min_heap = []
        for ll in args:
            min_heap.append(ll)
        heapq.heapify(min_heap)
        while min_heap:
            curr = heapq.heappop(min_heap)
            if curr.next:
                heapq.heappush(min_heap, curr.next)
                curr.next = None
            if tail is None:
                head = tail = curr
            else:
                tail.next = curr
                tail = tail.next

    return head


# APPROACH: Merge Sort
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
def merge_k_sorted_linked_lists(args):

    def _rec(l1, l2):
        temp = prev = Node(-float("inf"))  # temp.next = result
        # NOTE: The temp (Node) has a value less than any values in l1 or l2, and is used as the 'result' variable;
        #       where temp.next is the actual return value (NOT temp).  This is done to MINIMIZE the code.
        while l1 and l2:
            if l1.value <= l2.value:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 if l1 else l2        # In case either of the lists still have values.
        return temp.next                    # REMEMBER, temp.next is the result (temp is just a pointer).

    if args:
        while len(args) > 1:
            temp = []
            if len(args) % 2 == 1:
                temp.append(args.pop())
            while args:
                temp.append(_rec(args.pop(), args.pop()))
            args = temp
        return args.pop()


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    # NOTE: This is required because the naive heapq implementation will be comparing nodes.
    def __lt__(self, node):
        return self.value < node.value

    def __eq__(self, node):
        return self.value == node.value

    def __gt__(self, node):
        return self.value > node.value

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
fns = [merge_k_sorted_linked_lists_naive,
       merge_k_sorted_linked_lists_heapq,
       merge_k_sorted_linked_lists]

for args in args_list:
    print("args:")
    for a in args:
        print(f"\t{a}")
    for fn in fns:
        print(f"{fn.__name__}(args): {fn(copy.deepcopy(args))}")
    print()


