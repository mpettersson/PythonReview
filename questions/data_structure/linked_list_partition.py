"""
    LINKED LIST PARTITION

    Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes
    greater than or equal to x.  If x is contained within the list, the values of x only need to be after the elements
    less than x.

    Example:
        Input:  3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1, 5
        Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""


def partition(node, x):
    l_head = None
    l_tail = None
    r_head = None
    r_tail = None

    while node:
        next = node.next
        node.next = None
        if node.value < x:
            if not l_head:
                l_head = node
                l_tail = l_head
            else:
                l_tail.next = node
                l_tail = node
        else:
            if not r_head:
                r_head = node
                r_tail = r_head
            else:
                r_tail.next = node
                r_tail = node
        node = next

    if not l_head:
        return r_head

    l_tail.next = r_head
    return l_head



def partition_(node, x):
    head = None
    tail = None
    while not node:
        next = node.next
        if node.value < x:
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node
        node = next
    tail.next = None
    return head


class LinkedList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return repr(self.value) + " --> " + (repr(self.next) if self.next else "None")


linked_lists = [(LinkedList(3, LinkedList(5, LinkedList(8, LinkedList(5, LinkedList(10, LinkedList(2, LinkedList(1))))))), 5),
                (LinkedList(0, LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, LinkedList(5)))))), 3),
                (LinkedList(0, LinkedList(1, LinkedList(0, LinkedList(1, LinkedList(3, LinkedList(0)))))), 1),
                (LinkedList(0), 0)]

for (ll, i) in linked_lists:
    print(f"partition({ll},{i}):", partition(ll, i))
print()

