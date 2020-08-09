"""
    PALINDROME (CCI 2.6)

    Implement a function to check if a linked list is a palindrome.

    Example:
        Input:  t -> a -> c -> o -> c -> -> a -> t -> None
        Output: True
"""


# Naive Stack Solution: Time and space complexity is O(n).
def palindrome_naive(l):
    if l:
        s = []
        n = l
        while n:
            s.insert(0, n.value)
            n = n.next
        while l:
            if l.value != s.pop(0):
                return False
            l = l.next
        return True


# Improved (Runner technique) Stack Solution: Time and space complexity is O(n) (but half of the naive solution above).
def palindrome(l):
    if l:
        fast = slow = l
        s = []
        while fast and fast.next:
            s.insert(0, slow.value)
            slow = slow.next
            fast = fast.next.next
        if fast:    # NOTE: This handles the case when l has an odd length!
            slow = slow.next
        while slow:
            if s.pop(0) != slow.value:
                return False
            slow = slow.next
        return True


# Recursive Approach: Time and space complexity is O(n).
def palindrome_rec(l):

    def wrapper(head, length):
        if not head or length <= 0:
            return head, True
        elif length == 1:
            return head.next, True
        node, res = wrapper(head.next, length - 2)
        if not node or not res:
            return node, res
        return node.next, head.value == node.value

    return wrapper(l, length(l))[1] if l else None


# Helper Function
def length(l):
    if l:
        size = 0
        while l:
            size += 1
            l = l.next
        return size


class LinkedList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return repr(self.value) + " -> " + (repr(self.next) if self.next else "None")


linked_lists = [LinkedList("t", LinkedList("a", LinkedList("c", LinkedList("o", LinkedList("c", LinkedList("a", LinkedList("t"))))))),
                LinkedList(0, LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, LinkedList(5)))))),
                LinkedList(0, LinkedList(1, LinkedList(2, LinkedList(2, LinkedList(1, LinkedList(0)))))),
                LinkedList(0, LinkedList(1, LinkedList(2, LinkedList(1, LinkedList(0))))),
                LinkedList(0),
                None]

for l in linked_lists:
    print(f"palindrome_naive({l}): {palindrome_naive(l)}")
print()

for l in linked_lists:
    print(f"palindrome({l}): {palindrome(l)}")
print()

for l in linked_lists:
    print(f"palindrome_rec({l}): {palindrome_rec(l)}")


