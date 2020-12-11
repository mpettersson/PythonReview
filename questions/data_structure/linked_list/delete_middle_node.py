"""
    DELETE MIDDLE NODE (CCI 2.3: DELETE MIDDLE NODE)

    Write a function, which accepts a middle node of a linked list, then deletes the provided node.

    Consider the following linked list:

        a ⟶ b ⟶ c ⟶ d ⟶ e ⟶ None

    Example:
                linked_list = LinkedList("a", LinkedList("b", LinkedList("c", LinkedList("d", LinkedList("e")))))
        Input:  linked_list.next.next  # Or, the 'c' node above.
        Output: None  # However, the linked list will be a ⟶ b ⟶ d ⟶ e ⟶ None
"""
import copy


# Update And Delete Next Approach:  Update the provided node with the next nodes value and 'next' link.
# Time Complexity: O(1).
# Space Complexity: O(1).
def delete_middle_node(node):
    if node:
        next_node = node.next
        if next_node:
            node.value = next_node.value
            node.next = next_node.next
        else:
            node.value = None


class LinkedList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return repr(self.value) + " ⟶ " + (repr(self.next) if self.next else "None")


def get_middle_node(head):
    """Given the head of a linked list, returns a reference to a middle node."""
    runner = head
    while runner and runner.next:
        runner = runner.next.next
        head = head.next
    return head


linked_lists = [LinkedList("a", LinkedList("b", LinkedList("c", LinkedList("d", LinkedList("e"))))),
                LinkedList(0, LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, LinkedList(5))))))]
fns = [delete_middle_node]

for linked_list in linked_lists:
    print(f"linked_list: {linked_list}\n")
    for fn in fns:
        linked_list_copy = copy.deepcopy(linked_list)
        print(f"{fn.__name__}(get_middle_node(link_list)): {fn(get_middle_node(linked_list_copy))}", end="")
        print(f" (linked_list: {linked_list_copy})\n")


