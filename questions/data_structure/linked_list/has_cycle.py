"""
    HAS CYCLE (CCI 2.8: LOOP DETECTION)

    Write a function, which accepts the head of a circular linked list, then checks if the linked list is circular; if
    the linked list is circular, the function returns the node at the beginning of the loop.

    A circular linked list is a 'corrupt' linked list in which a node's next pointer points to an earlier node, so as to
    make a loop in the linked list.

    Example:
        l = A -> B -> C --> D
                       ↖   ↙
                         E

               l = LinkedList("A", LinkedList("B", LinkedList("C", LinkedList("D", LinkedList("E")))))
               l.next.next.next.next.next = l.next.next
        Input: l
        Output: C   # That is, the linked list node with value C.

    Variations:
        - Detect if a linked list has a loop.
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Clarify the question (single/doubly linked list, can nodes be marked, can have duplicate values, is a repeated
#     value a cycle)?
#   - What will the data type be (floats, ints)?


# APPROACH: Naive Visited Set
#
# Beginning at the head, iterate over the nodes adding them to a seen/visited set, return the first repeat (seen) node,
# or None if the end of the list is encountered.
#
# Time Complexity: O(n), where n is the number of nodes in the list.
# Space Complexity: O(n), where n is the number of nodes in the list.
def has_cycle_naive(head):
    if head:
        node = head
        seen = set()
        while node:
            if node in seen:
                return node
            seen.add(node)
            node = node.next


# APPROACH: Two Pointer
#
# This approach uses the two pointer, or runner approach.  For each iteration of the loop, a 'fast' pointer advances by
# two nodes and a 'slow' pointer advances by one. If the fast pointer encounters the end of the list, or a None value,
# then there exists no loop.  If, however, the pointers land on the same node (on a single iteration), then the 'fast'
# pointer is set to the head of the list and advances one node at a time (the 'slow' pointer does not change, and starts
# at its last location).  The two pointers advance (both one node per iteration) until they both point at a node; this
# is the first node of the loop and is the return value.
#
# Time Complexity: O(n), where n is the number of nodes in the list.
# Space Complexity: O(1).
def has_cycle(head):
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
        node = self
        visited = set()
        result = ""
        while node:
            result += f"{node.value} -> "
            visited.add(node)
            if node.next is None:
                return result + "None"
            if node.next and node.next in visited:
                return result + f"(loop){node.next.value}"
            node = node.next


linked_lists = [LinkedList("A", LinkedList("B", LinkedList("C", LinkedList("D", LinkedList("E"))))),
                LinkedList(0, LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4))))),
                LinkedList(5),
                LinkedList("t", LinkedList("a", LinkedList("c", LinkedList("o", LinkedList("c", LinkedList("a", LinkedList("t"))))))),
                LinkedList(6),
                LinkedList("Alfa", LinkedList("Bravo", LinkedList("Charlie", LinkedList("Delta", LinkedList("Echo"))))),
                None]                                                   # Create a few circularly linked lists:
linked_lists[0].next.next.next.next.next = linked_lists[0].next.next    # E -> C
linked_lists[1].next.next.next.next = linked_lists[1]                   # 4 -> 0
linked_lists[2].next = linked_lists[2]                                  # 5 -> 5
fns = [has_cycle_naive,
       has_cycle]

for l in linked_lists:
    print(f"l: {l}")
    for fn in fns:
        print(f"{fn.__name__}(l): {fn(l)}")
    print()


