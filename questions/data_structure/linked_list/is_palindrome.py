"""
    IS PALINDROME (CCI 2.6: PALINDROME,
                   50CIQ 30: PALINDROMES)

    Write a function, which accepts the head of a linked list, and returns True if the linked list is a palindrome,
    False otherwise.

    Example:
        Input:  t -> a -> c -> o -> c -> -> a -> t -> None
        Output: True
"""


# Naive (Whole) Stack Solution: Reverse the WHOLE list, via a stack, then compare.
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(n), where n is the number of nodes in the linked list.
def is_palindrome_naive(l):
    if l:
        s = []
        n = l
        while n:
            s.append(n.value)
            n = n.next
        while l:
            if l.value != s.pop():
                return False
            l = l.next
        return True


# Recursive Approach:  This approach makes use of the call stack to store the values to compare.  Note that this version
# stores HALF the list in the call stack at the cost of first finding the length of the list.
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(n), where n is the number of nodes in the linked list.
def is_palindrome_rec(l):

    def _get_length(l):                                 # Find length so only half the list is stored.
        size = 0
        while l:
            size += 1
            l = l.next
        return size

    def _is_palindrome_rec(head, length):
        if not head or length <= 0:
            return head, True
        elif length == 1:
            return head.next, True
        node, res = _is_palindrome_rec(head.next, length - 2)
        if not node or not res:
            return node, res
        return node.next, head.value == node.value

    return _is_palindrome_rec(l, _get_length(l))[1] if l else None


# Improved (Half) Stack Solution:  Use a fast/slow pointer to find half the list, then just add half of the list to a
# stack to compare.  Although this has the same Big O complexities as above, the space is half of the first approach,
# and the length is not needed (like the second approach).
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(n/2), which reduces to O(n), where n is the number of nodes in the linked list.
def is_palindrome(l):
    if l:
        fast = slow = l
        s = []
        while fast and fast.next:
            s.append(slow.value)
            slow = slow.next
            fast = fast.next.next
        if fast:                        # NOTE: This handles the case when l has an odd length!
            slow = slow.next
        while slow:
            if s.pop() != slow.value:
                return False
            slow = slow.next
        return True


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return repr(self.value) + " ⟶ " + (repr(self.next) if self.next else "None")


linked_lists = [Node("t", Node("a", Node("c", Node("o", Node("c", Node("a", Node("t"))))))),
                Node(0, Node(1, Node(2, Node(3, Node(4, Node(5)))))),
                Node(0, Node(1, Node(2, Node(2, Node(1, Node(0)))))),
                Node(0, Node(1, Node(2, Node(1, Node(0))))),
                Node(0),
                None]
fns = [is_palindrome_naive,
       is_palindrome_rec,
       is_palindrome]

for fn in fns:
    for l in linked_lists:
        print(f"{fn.__name__}({l}): {fn(l)}")
    print()


