"""
    LOOP DETECTION (CCI 2.8)

    Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.

    Definition:
        Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to
        make a loop in the linked list.

    Example:
        l = A -> B -> C --> D
                       ↖   ↙
                         E
        Input: l
        Output: C (that is, the linked list node with value C)

    Variation:
        Detect if a linked list has a loop.
"""


# Time complexity is O(n), where n is the number of nodes in the list, space complexity is O(n).
# NOTE: Be careful with the if/while statements; it's VERY easy to forget a .next or .next.next check!!!
def intersection(head):
    if head and head.next and head.next.next:
        slow = head.next
        fast = head.next.next
        while fast and fast.next and slow != fast:
            slow = slow.next
            fast = fast.next.next
        if not fast or not fast.next:
            return None
        node = head
        while node != slow:
            node = node.next
            slow = slow.next
        return node
    return None


class LinkedList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return repr(self.value) + " -> " + (repr(self.next) if self.next else "None")


linked_lists = [LinkedList("A", LinkedList("B", LinkedList("C", LinkedList("D", LinkedList("E"))))),
                LinkedList(0, LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4))))),
                LinkedList(5),
                LinkedList("t", LinkedList("a", LinkedList("c", LinkedList("o", LinkedList("c", LinkedList("a", LinkedList("t"))))))),
                LinkedList(6),
                None]

# Create a few circularly linked lists:
linked_lists[0].next.next.next.next.next = linked_lists[0].next.next    # E -> C
linked_lists[1].next.next.next.next = linked_lists[1]                   # 4 -> 0
linked_lists[2].next = linked_lists[2]                                  # 5 -> 5

for i, l in enumerate(linked_lists):
    result = intersection(l)
    print(f"intersection(linked_list[{i}]): {result.value if result else result}")

