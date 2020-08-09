"""
    DELETE MIDDLE NODE (CCI 2.3)

    Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.

    Example:
        Input:  c (of the linked list a -> b -> c -> d -> e -> None)
        Output: None (however, the linked list will be a -> b -> d -> e -> None)
"""


# Time and space complexity is O(1).
def delete_middle_node(node):
    if node:
        next = node.next
        if next:
            node.value = next.value
            node.next = next.next
        else:
            node.value = None


# Helper Function
def return_middle_node(head):
    """Given the head of a linked list, returns a reference to a middle node."""
    runner = head
    while runner and runner.next:
        runner = runner.next.next
        head = head.next
    return head


class LinkedList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return repr(self.value) + " -> " + (repr(self.next) if self.next else "None")


linked_lists = [LinkedList("a", LinkedList("b", LinkedList("c", LinkedList("d", LinkedList("e"))))),
                LinkedList(0, LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, LinkedList(5)))))),
                LinkedList(0)]  # NOTE: Due to the questions constraints the best we can do is update 0 to None....

for ll in linked_lists:
    middle_node = return_middle_node(ll)
    print(f"Before: {ll}")
    print(f"delete_middle_node({middle_node.value})"); delete_middle_node(middle_node)
    print(f"After:  {ll}\n")


