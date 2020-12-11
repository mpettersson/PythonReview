"""
    SPLIT LINKED LIST (50CIQ 41: SPLIT A LINKED LIST)

    Write a function, which accepts the head of a linked list, then splits the provided linked list, returning two
    (heads of) linked lists.  The resulting linked lists should maintain the original order and the lengths must not
    differ by more than one.

    Consider the following linked list:

        0 ⟶ 0 ⟶ 0 ⟶ 1 ⟶ 2 ⟶ 0 ⟶ 1 ⟶ 4 ⟶ 5

    Example:
                ll = Node(0, Node(0, Node(0, Node(1, Node(2, Node(0, Node(1, Node(4, Node(5)))))))))
        Input = ll  # Or, the linked list above.
        Output = Node(0, Node(0, Node(0, Node(1)))), Node(2, Node(0, Node(1, Node(4, Node(5)))))
"""
import copy


# Fast/Slow Runner Approach:  Use two pointers, one moving at twice the speed of the other, to determine where the
# linked list needs to be split.
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(1).
def split_linked_list(head):
    if head and head.next:
        fast = slow = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        if prev:
            prev.next = None
        return head, slow


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __iter__(self):
        yield self.value
        if self.next:
            yield from self.next

    def __repr__(self):
        return ' ⟶ '.join(map(repr, self))


linked_lists = [Node(0, Node(0, Node(0, Node(1, Node(2, Node(0, Node(1, Node(4, Node(5))))))))),
                Node(0, Node(1, Node(2, Node(3, Node(4, Node(5)))))),
                Node(0, Node(1, Node(0, Node(1, Node(3, Node(0)))))),
                Node(6, Node(9)),
                Node(0),
                None]
fns = [split_linked_list]

for fn in fns:
    for head in linked_lists:
        print(f"{fn.__name__}({head}): {fn(copy.deepcopy(head))}")
    print()


