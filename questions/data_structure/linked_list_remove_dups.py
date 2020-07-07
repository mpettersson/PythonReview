"""
    LINKED LIST REMOVE DUPS (CCI 2.1)

    Write code to remove duplicates from an unsorted linked list.  How would you solve this problem if a temporary
    buffer is not allowed?

    Example:
        Input:  0 -> 1 -> 0 -> 1 -> 3 -> 0 -> None
        Output: 0 -> 1 -> 3 -> None
"""
import copy


# Set/Hashtable Approach:  O(n) time and O(n) space complexity.
def remove_dups_w_set(head):
    no_dups = copy.deepcopy(head)
    n = no_dups
    node_set = set()
    prev = None
    while n:
        if n.value in node_set:
            prev.next = n.next
        else:
            node_set.add(n.value)
            prev = n
        n = n.next
    return no_dups


# Non-Hashtable/Set Approach:  O(n^2) time and O(1) space complexity.
def remove_dups_wo_set(head):
    no_dups = copy.deepcopy(head)
    curr = no_dups
    while curr:
        runner = curr
        while runner.next:
            if runner.next.value == curr.value:
                runner.next = runner.next.next;
            else:
                runner = runner.next
        curr = curr.next
    return no_dups


class LinkedList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return repr(self.value) + " -> " + (repr(self.next) if self.next else "None")


linked_lists = [LinkedList(0, LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, LinkedList(5)))))),
                LinkedList(0, LinkedList(1, LinkedList(0, LinkedList(1, LinkedList(3, LinkedList(0)))))),
                LinkedList(0)]

for ll in linked_lists:
    print(f"remove_dups_w_set({ll}):", remove_dups_w_set(ll))
print()

for ll in linked_lists:
    print(f"remove_dups_wo_set({ll}):", remove_dups_wo_set(ll))



