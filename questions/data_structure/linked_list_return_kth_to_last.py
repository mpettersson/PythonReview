"""
    LINKED LIST RETURN KTH TO LAST (CCI 2.2)

    Implement an algorithm to find the kth to last element of a singly linked list.

    For example, the 2nd to last element of the linked list 0 --> 1 --> 2 --> 3 --> 4 --> 5 --> None is 4.
"""


# Recursive Approach:
def print_kth_to_last(head, k):
    if not head:
        return 0
    index = print_kth_to_last(head.next, k) + 1
    if index == k:
        print(head.value)
    return index


class LinkedList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return repr(self.value) + " --> " + (repr(self.next) if self.next else "None")


linked_lists = [LinkedList(0, LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, LinkedList(5)))))),
                LinkedList(0, LinkedList(1, LinkedList(0, LinkedList(1, LinkedList(3, LinkedList(0)))))),
                LinkedList(0)]

for ll in linked_lists:
    print(f"print_kth_to_last({ll}): ", end=""); print_kth_to_last(ll, 2)
print()

