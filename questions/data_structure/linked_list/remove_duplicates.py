"""
    REMOVE DUPLICATES (CCI 2.1: REMOVE DUPS
                       50CIQ 40: DEDUP LINKED LIST)

    Write a function that removes all nodes of a given list with duplicate values.

    Consider the following linked list:

        0 ⟶ 0 ⟶ 0 ⟶ 1 ⟶ 2 ⟶ 0 ⟶ 1 ⟶ 4 ⟶ 5

    Example:
                ll = Node(0, Node(0, Node(0, Node(1, Node(2, Node(0, Node(1, Node(4, Node(5)))))))))
        Input = ll  # Or, the linked list above.
        Output = None  # However, ll now has the form: 0 ⟶ 1 ⟶ 2 ⟶ 4 ⟶ 5
"""
import copy


# APPROACH: Naive/Brute Force
#
# Iterate over the nodes comparing each node to all following nodes, removing duplicates.
#
# Time Complexity: O(n**2), where n is the number of nodes in the linked list.
# Space Complexity: O(1).
def remove_duplicates_naive(head):
    node = head
    while node:
        runner = node
        while runner.next:
            if runner.next.value == node.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        node = node.next
    return head


# APPROACH: Via Previous Pointer & Set
#
# Traverse the linked list with a set to maintain previously seen values. Each time a new value is encountered, add the
# value to the set, update previous.next to point to the (current) node, and set previous to the (current) node.  At the
# end of each iteration, the (current) node is assigned to its next value.  Finally, (when node is None), assign
# previous.next to None and return.
#
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(u), where u is the number of unique values in the linked list.
def remove_duplicates_via_set(head):
    if head:
        prev = head
        node = head.next
        s = {head.value}
        while node:
            if node.value not in s:
                s.add(node.value)
                prev.next = node
                prev = node
            node = node.next
        prev.next = None
        return head


# APPROACH: Via Set
#
# Using a set to maintain previously seen values, traverse the linked list.  While the next node has a previously seen
# value, update the (current) nodes pointer to be next.next.  When a next value has not been seen, (current) node is
# assigned to next node, and if node is not None, the value is added to the set.
#
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(u), where u is the number of unique values in the linked list.
def remove_duplicates(head):
    node = head
    if node:
        s = {node.value}
        while node:
            while node.next and node.next.value in s:
                node.next = node.next.next
            node = node.next
            if node:
                s.add(node.value)
    return head


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
                Node(0, Node(1, Node(0, Node(1, Node(0, Node(0, Node(1, Node(1, Node(2))))))))),
                Node(6, Node(6, Node(6, Node(6, Node(6, Node(6, Node(6, Node(6, Node(6))))))))),
                Node(0, Node(1, Node(2, Node(3, Node(2, Node(1, Node(0))))))),
                Node(1, Node(1)),
                Node(1, Node(2)),
                Node(0),
                None]
fns = [remove_duplicates_naive,
       remove_duplicates_via_set,
       remove_duplicates]

for head in linked_lists:
    for fn in fns:
        print(f"{fn.__name__}({head}): {fn(copy.deepcopy(head))}")
    print()


