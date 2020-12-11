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

# Known Size Approach: If the size was known, then we simply go to the length/size - k element; but this is trivially
# easy and probably not what the interviewer wants... The time complexity of this approach (given that size is known)
# would be O(n) and space complexity would be O(1).


# Recursive Approach:  Using an int as an accumulator, track the recursion depth into the list, returning the kth node.
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(n), where n is the number of nodes in the linked list.
def find_kth_to_last_node_rec(head, k):

    def _find_kth_to_last_node_rec(node, k, i):
        if i is k:
            return node
        if node is None:
            raise IndexError(f"IndexError: k out of range.")
        return _find_kth_to_last_node_rec(node.next, k, i + 1)

    if head is None:
        raise TypeError(f"TypeError: node must be of type Node")
    if k is None or k < 1:
        raise IndexError(f"IndexError: k out of range.")
    return _find_kth_to_last_node_rec(head, k, 1)


# Iterative (Running Pointer) Approach:  Using two pointers, advance one k nodes in front of the other pointer; then
# advance both (one at a time) until the advanced pointer is None and return the node pointed at by the second pointer.
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space complexity: O(1).
def find_kth_to_last_node(node, k):
    if node is None:
        raise TypeError(f"TypeError: node must be of type Node")
    if k is None or k < 1:
        raise IndexError(f"IndexError: k out of range.")
    runner = node
    for _ in range(k):
        if runner is None:
            raise IndexError(f"IndexError: k out of range.")
        runner = runner.next
    while runner:
        node = node.next
        runner = runner.next
    return node


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __iter__(self):
        yield self.value
        if self.next:
            yield from self.next

    def __repr__(self):
        return ' ⟶ '.join(map(repr, self))


linked_list = Node(0, Node(1, Node(2, Node(3, Node(4, Node(5))))))
args_list = [1, 2, 3, 6, 7, 0, -1, None]
fns = [find_kth_to_last_node_rec,
       find_kth_to_last_node]

print("linked_list:", linked_list)
for fn in fns:
    for k in args_list:
        result = None
        try:
            result = fn(linked_list, k)
        except IndexError as ie:
            result = ie
        print(f"{fn.__name__}(ll, {k}): {result}")
    print()


