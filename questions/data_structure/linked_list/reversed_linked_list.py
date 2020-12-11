r"""
    REVERSED LINKED LIST (50CIQ 23: PRINT REVERSED LINKED LIST)

    Write a function that accepts the head of a linked list and returns the head of a new linked list with the reversed
    values of the supplied linked list.

    Consider the following linked list:

        1 ⟶ 2 ⟶ 3 ⟶ 4

    Example:
        Input = Node(1, Node(2, Node(3, Node(4))))
        Output = Node(4, Node(3, Node(2, Node(1))))
"""


# Naive/Queue Approach:  Traverse the linked list once, putting the values in a queue, then build a linked list from the
# queue.
# Time Complexity: O(n), where n is the number of elements in the linked list.
# Space Complexity: O(n), where n is the number of elements in the linked list.
#
# NOTE: This traverses over the values twice; see below for 'better' times.
def reversed_linked_list_naive(l):
    if l:
        q = []
        result = None
        while l:
            q.append(l.value)
            l = l.next
        while q:
            result = Node(q.pop(0), result)
        return result


# Optimal/Traversal Approach:  Build a new linked list while traversing only once over the provided linked list.
# Time Complexity: O(n), where n is the number of elements in the linked list.
# Space Complexity: O(n), where n is the number of elements in the linked list.
def reversed_linked_list(l):
    if l:
        result = None
        while l:
            result = Node(l.value, result)
            l = l.next
        return result


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
                Node(0, Node(1, Node(2, Node(2, Node(1, Node(0)))))),
                Node(0),
                None]
fns = [reversed_linked_list_naive,
       reversed_linked_list]

for fn in fns:
    for l in linked_lists:
        print(f"{fn.__name__}({l}): {fn(l)}")
    print()


