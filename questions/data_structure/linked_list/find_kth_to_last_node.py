"""
    FIND KTH TO LAST NODE  (CCI 2.2: RETURN KTH TO LAST)

    Write a function, which accepts the head of a singly linked list, and returns the kth to last node in the list,
    raise IndexError for invalid values of k.

    Consider the following linked list:

        0 ⟶ 1 ⟶ 2 ⟶ 3 ⟶ 4 ⟶ 5

    Example:
                linked_list = Node(0, Node(1, Node(2, Node(3, Node(4, Node(5))))))
        Input = linked_list, 2  # Where '2' indicates the 2nd to last node.
        Output: = 4  # That is, the node in the linked list, with value 4.
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Clarify the question (what behavior for valid/invalid k values, what member variables/methods does node have,
#     single/doubly linked list, data type, etc...)?


# APPROACH: (Trivial) Compute/Given Size
#
# Use the size to iteratively traverse to the (length - k) element; this is trivially easy and probably not what the
# interviewer wants...
#
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(1).
#
# NOTE: This has the same time complexity as the other approaches, however, this takes two iterations across the list,
#       where the other approaches only need one.
def find_kth_to_last_node_trivial(head, k):
    if head is None:
        raise TypeError(f"TypeError: node must be of type Node")
    if k is None or k < 1 or k > len(head):
        raise IndexError(f"IndexError: k out of range.")
    i = len(head) - k
    node = head
    while i:
        node = node.next
        i -= 1
    return node
# NOTE: The following could be used in place of __len__:
#     def len(n):
#         length = 0
#         while n:
#             length += 1
#             n = n.next
#         return length


# APPROACH: Via Recursion
#
# Recursively continue to the end of the list, where a tuple of (node, k_level) are returned.  When the results of a
# recursive call are received, compare the k values, if the k_level is equal to k, return both of the results.  If not,
# then return the (current) node, and one plus the received k_level.  Before returning the results, the driving function
# must verify that the highest k_level is the requested k level (in which case the node is returned), else an Error is
# raised.
#
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(n), where n is the number of nodes in the linked list.
def find_kth_to_last_node_rec(head, k):

    def _find_kth_to_last_node_rec(node, k):
        if not node.next:
            return node, 1
        n_res, k_res = _find_kth_to_last_node_rec(node.next, k)
        return (n_res, k_res) if k == k_res else (node, k_res + 1)

    if head is None:
        raise TypeError(f"TypeError: node must be of type Node")
    if k and k > 0:
        node, level = _find_kth_to_last_node_rec(head, k)
        if level == k:
            return node
    raise IndexError(f"IndexError: k out of range.")


# APPROACH: Iterative/Two Pointers (Leader/Follower)
#
# Using two pointers, advance one k nodes in front of the other pointer; then advance both (one at a time) until the
# advanced pointer is None and return the node pointed at by the second pointer.
#
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space complexity: O(1).
def find_kth_to_last_node(node, k):
    if node is None:
        raise TypeError(f"TypeError: node must be of type Node")
    if k is None or k < 1:
        raise IndexError(f"IndexError: k out of range.")
    leader = follower = node
    for _ in range(k):
        if leader is None:
            raise IndexError(f"IndexError: k out of range.")
        leader = leader.next
    while leader:
        follower = follower.next
        leader = leader.next
    return follower


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __iter__(self):
        yield self.value
        if self.next:
            yield from self.next

    def __repr__(self):
        return f"{self.value} ⟶ {'None' if self.next is None else repr(self.next)}"

    def __len__(self):
        return 1 + (0 if self.next is None else len(self.next))


linked_list = Node(0, Node(1, Node(2, Node(3, Node(4, Node(5))))))
args_list = [1, 2, 3, 6, 7, 0, -1, None]
fns = [find_kth_to_last_node_trivial,
       find_kth_to_last_node_rec,
       find_kth_to_last_node]

print(f"\nlinked_list: {linked_list}\n")
for k in args_list:
    for fn in fns:
        result = None
        try:
            result = fn(linked_list, k)
        except IndexError as ie:
            result = ie
        print(f"{fn.__name__}(ll, {k}): {result}")
    print()


