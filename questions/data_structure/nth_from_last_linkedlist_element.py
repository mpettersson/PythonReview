"""
    NTH FROM LAST LINKEDLIST ELEMENT

    Write a function which accepts the head of a linked list (ll) and an int (n), then returns the nth element from the
    END of the list.

    Example:
        Input = Node(5, Node(4, Node(3, Node(2, Node(1))))), 2  (or  ll --> 5 --> 4 --> 3 --> 2 --> 1)
        Output = 2
"""


def nth_element_in_linked_list(ll, n):
    if n < 1:
        return None
    if ll:
        pr = ll
        pl = ll
        for i in range(n):
            if not pr:
                return None
            pr = pr.next

        while pr:
            pr = pr.next
            pl = pl.next
    return pl.value


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return repr(self.value) + " --> " + (repr(self.next) if self.next else "None")


ll = Node(5, Node(4, Node(3, Node(2, Node(1)))))
print("ll:", ll)
print()

print("nth_element_in_linked_list(ll, 0):", nth_element_in_linked_list(ll, 0))
print("nth_element_in_linked_list(ll, 2):", nth_element_in_linked_list(ll, 2))
print("nth_element_in_linked_list(ll, 5):", nth_element_in_linked_list(ll, 5))
print("nth_element_in_linked_list(ll, 6):", nth_element_in_linked_list(ll, 6))

















