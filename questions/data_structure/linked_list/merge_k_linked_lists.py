r"""
    MERGE K SORTED LINKED LISTS (50CIQ 8: MERGE K ARRAYS)

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
"""
import copy
import heapq


# Dynamic Programming/Merge Sort Approach:  While there are more than two lists, merge two lists at a time; when only
# one list remains, return it's head.
# Time Complexity: O(n * log(n)), where n is the total number of elements in the linked lists.
# Space Complexity: O(1).
def merge_k_sorted_linked_lists_dyn_prog(l):

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
            if len(l) % 2 is 1:
                temp.append(l.pop())
            while l:
                temp.append(_merge_two_sorted_linked_lists(l.pop(), l.pop()))
            l = temp
        return l.pop()
    return l


# Heapq Approach:
# Time Complexity: O(n * log(n)), where n is the total number of elements in the linked lists.
# Space Complexity: O(1).
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
fns = [merge_k_sorted_linked_lists_dyn_prog,
       merge_k_sorted_linked_lists_heapq]

for args in args_list:
    print("args:")
    for a in args:
        print(f"\t{a}")
    for fn in fns:
        print(f"{fn.__name__}(args): {fn(copy.deepcopy(args))}")
    print()


