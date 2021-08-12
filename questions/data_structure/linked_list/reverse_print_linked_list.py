r"""
    REVERSED LINKED LIST (50CIQ 23: PRINT REVERSED LINKED LIST)

    Write a function that accepts the head of a linked list and prints the linked list in reversed order.

    Consider the following linked list:

        1 ⟶ 2 ⟶ 3 ⟶ 4

    Example:
        Input = Node(1, Node(2, Node(3, Node(4))))
        Output = 4 ⟶ 3 ⟶ 2 ⟶ 1  # This would be printed.
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What SIZE is the linked list?
#   - What is the linked list value data type?
#   - What output formatting do you want?


# APPROACH: Naive Build List & Print
#
# Build a list of the linked list value, then print it backwards.
#
# Time Complexity: O(n), where n is the number of elements in the linked list.
# Space Complexity: O(n), where n is the number of elements in the linked list.
def reverse_print_linked_list_naive(head):
    if head:
        l = []
        node = head
        while node:
            l.append(node.value)
            node = node.next
        print(" -> ".join(list(map(str, reversed(l)))))
    else:
        print()


# APPROACH: Reverse List, Print, Reverse List (For Long List)
#
# This approach utilizes an additional function to reverse the list, then prints the list, and finally re-reverses the
# list.
#
# Time Complexity: O(n), where n is the number of elements in the linked list.
# Space Complexity: O(1).
#
# NOTE: This approach is intended for the specific use case where the LENGTH of the list is too long for a recursion
#       stack to be used to reverse the order.  The tradeoff, is additional passes are required (to reverse and the
#       un-reverse the list order).
def reverse_print_reverse_linked_list(head):

    def _reverse_linked_list(head):
        prev = None
        node = head
        while node:
            curr = node
            node = node.next
            curr.next = prev
            prev = curr
        return prev

    if head:
        head = _reverse_linked_list(head)
        print(head)
        _reverse_linked_list(head)
    else:
        print()


# APPROACH: Optimal Via Recursion Stack
#
# Use the recursion stack to reverse the printing order.
#
# Time Complexity: O(n), where n is the number of elements in the linked list.
# Space Complexity: O(1).
#
# NOTE: This approach is intended for smaller lists, or lists that can easily be pushed to the (recursion) stack.
def reverse_print_linked_list(head):

    def _rec(node):
        if node:
            _rec(node.next)
            print((" ⟶ " if node.next else "") + f"{node.value}", end="")

    if head:
        _rec(head)
        print()


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
fns = [reverse_print_linked_list_naive,
       reverse_print_reverse_linked_list,
       reverse_print_linked_list]

for head in linked_lists:
    for fn in fns:
        print(f"{fn.__name__}({head}): ", end="")
        fn(head)
    print()


