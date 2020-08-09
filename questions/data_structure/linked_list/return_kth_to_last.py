"""
    RETURN KTH TO LAST (CCI 2.2)

    Implement an algorithm to find the kth to last element of a singly linked list.

    Example:
        Input:  0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None, 2 (where 2 means 2nd to last)
        Output: 4
"""

# Size Know Approach: If the size was known, then we simply go to the length/size - k element; but this is trivially
# easy and probably not what the interviewer wants... The time complexity of this approach (given that size is known)
# would be O(n) and space complexity would be O(1).


# Recursive Approach: Time and space complexity is O(n), where n is the number of items in the linked list.
def kth_to_last_rec(head, k):

    def wrapper(node, k):
        if not node:
            return node, 0
        n, i = wrapper(node.next, k)
        return (n, i) if i == k else (node, i+1)

    node, i = wrapper(head, k)
    return node.value if node and i is k else None


# Iterative (Running Pointer) Approach: Time complexity is O(n) and space complexity is O(1).
def kth_to_last(node, k):
    runner = node
    for _ in range(k):
        if runner is None:
            return None
        else:
            runner = runner.next
    while runner:
        node = node.next
        runner = runner.next
    return node.value if node else None


class LinkedList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return repr(self.value) + " -> " + (repr(self.next) if self.next else "None")


ll = LinkedList(0, LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, LinkedList(5))))))
args_list = [0, 1, 3, 6, 7]

for k in args_list:
    print(f"kth_to_last_rec({ll}, {k}): {kth_to_last_rec(ll,k)}")
print()

for k in args_list:
    print(f"kth_to_last({ll}, {k}): {kth_to_last(ll,k)}")


