r"""
    REVERSED LINKED LIST (leetcode.com/problems/reverse-linked-list)

    Write a function that accepts the head of a linked list and returns the head of a linked list with the reversed
    values of the supplied linked list.

    Consider the following linked list:

        1 ⟶ 2 ⟶ 3 ⟶ 4

    Example:
        Input = Node(1, Node(2, Node(3, Node(4))))
        Output = Node(4, Node(3, Node(2, Node(1))))
"""
import copy


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What SIZE is the linked list?
#   - What is the linked list value data type?


# APPROACH: Naive Build New List
#
# Build a new linked list while traversing only once over the provided linked list.
#
# Time Complexity: O(n), where n is the number of elements in the linked list.
# Space Complexity: O(n), where n is the number of elements in the linked list.
def reversed_linked_list_naive(node):
    if node:
        result = None
        while node:
            result = Node(node.value, result)
            node = node.next
        return result


# APPROACH: Optimal Recursive
#
# Use the recursion stack to update the linked list pointers in reverse order.
#
# Time Complexity: O(n), where n is the number of elements in the linked list.
# Space Complexity: O(1).
def reversed_linked_list_rec(head):

    def _rec(node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return _rec(n, node)

    return _rec(head)


# APPROACH: Optimal Iterative
#
# Iterate over the list updating the pointers to reverse the list.
#
# Time Complexity: O(n), where n is the number of elements in the linked list.
# Space Complexity: O(1).
#
# NOTE: Only need 3 pointers to do this (iteratively); current, node/head, previous.
def reversed_linked_list(head):
    prev = None
    node = head
    while node:
        curr = node
        node = node.next
        curr.next = prev
        prev = curr
    return prev


# APPROACH: Optimal Iterative Minimized
#
# Iterate over the list updating the pointers to reverse the list.
#
# Time Complexity: O(n), where n is the number of elements in the linked list.
# Space Complexity: O(1).
#
# NOTE: Only need 3 pointers to do this (iteratively); current, node/head, previous.
def reversed_linked_list_min(head):
    cur, prev = head, None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __iter__(self):
        yield self.value
        if self.next:
            yield from self.next

    def __repr__(self):
        return " ⟶ ".join(map(repr, self))


linked_lists = [Node(1, Node(2, Node(3, Node(4)))),
                Node("f", Node("o", Node("o", Node("b", Node("a", Node("r")))))),
                Node(0, Node(1, Node(2, Node(3, Node(4, Node(5)))))),
                Node(0),
                None]
fns = [reversed_linked_list_naive,
       reversed_linked_list_rec,
       reversed_linked_list,
       reversed_linked_list_min]

for head in linked_lists:
    for fn in fns:
        print(f"{fn.__name__}({head}): {fn(copy.deepcopy(head))}")
    print()


