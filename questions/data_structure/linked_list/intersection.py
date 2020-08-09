"""
    INTERSECTION (CCI 2.7)

    Given two (singly) linked lists, determine if the two lists intersect.  Return the intersecting node.  Note that the
    intersection is defined based on reference, not value.  That is, if the kth node of the first linked list is the
    exact same node (by reference) as the jth node of the second linked list, then they are intersecting.

    Example:
        l1 = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None
        l2 =      4 -> 5 -↗

        Input: l1, l2
        Output: 3 (that is, the linked list node with value 3)
"""


# Time complexity is O(n) and space complexity is O(1).
def intersection(l1, l2):
    if l1 and l2:
        len1, t1 = length_and_tail(l1)
        len2, t2 = length_and_tail(l2)
        if t1 is t2:
            if len1 > len2:
                for _ in range(len1 - len2):
                    l1 = l1.next
            elif len2 > len1:
                for _ in range(len2 - len1):
                    l2 = l2.next
            while l1 and l2:
                if l1 is l2:
                    return l1
                l1 = l1.next
                l2 = l2.next


# Helper Function
def length_and_tail(node):
    if node:
        size = 1
        while node.next:
            size += 1
            node = node.next
        return size, node
    return None, None


class LinkedList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return repr(self.value) + " -> " + (repr(self.next) if self.next else "None")


l0 = LinkedList(3, LinkedList(4, LinkedList(5)))
l1 = LinkedList(0, LinkedList(1, LinkedList(2, l0)))    # References l0
l2 = LinkedList(4, LinkedList(5, l0))                   # References l0
l3 = LinkedList(1)
l4 = LinkedList(0)
l5 = None

args = (l0, l0), (l0, l1), (l1, l2), (l1, l3), (l1, l5), (l3, l4), (l4, l5), (l5, l5)

for (a1, a2) in args:
    print(f"intersection({a1}, {a2}) = {intersection(a1, a2)}")


