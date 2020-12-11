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


# Iterative Approach:  Iterate over the nodes comparing each node to all following nodes, removing duplicates.
# Time Complexity: O(n**2), where n is the number of nodes in the linked list.
# Space Complexity: O(1).
def remove_duplicates(head):
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


# Set Approach:  Traverse the linked list with a set to maintain previously seen values, when a duplicate is found
# update links to bypass the node with the duplicate value.
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(u), where u is the number of unique values in the linked list.
def remove_duplicates_via_set(head):
    node = head
    s = set()
    prev = None
    while node:
        if node.value in s:
            prev.next = node.next
        else:
            s.add(node.value)
            prev = node
        node = node.next
    return head


# Alt. Set Approach:  Traverse the linked list with a set to maintain previously seen values, when a duplicate is found
# update links to bypass the node with the duplicate value.
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(u), where u is the number of unique values in the linked list.
def remove_duplicates_via_set_alt(head):
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
                Node(1, Node(1)),
                Node(1, Node(2)),
                Node(0),
                None]
fns = [remove_duplicates,
       remove_duplicates_via_set,
       remove_duplicates_via_set_alt]

for fn in fns:
    for head in linked_lists:
        print(f"{fn.__name__}({head}): {fn(copy.deepcopy(head))}")
    print()


