r"""
    BST TRAVERSAL RECONSTRUCTION (EPI 15.5)

    Suppose you are given the sequence in which keys are visited in an in-order traversal of a BST, and all keys are
    distinct.  Can you reconstruct the BST from the sequence?

    If so, write a program to do so.  Solve the same problem for pre-order and post-order traversal sequences.

    Hint:
        Given three nodes with the values 1, 2, and 3, consider the possible tree and traversal combinations.
"""


# All possible BSTs with values in the range [1, 3], and without duplicate values:
#
#        1            1            2            3           3
#         \            \          / \          /           /
#          2            3        1   3        1           2
#           \          /                       \         /
#            3        2                         2       1


# In-Order Traversal:
# After constructing all possible BSTs with the values 1, 2, and 3, (as shown above) we can see that their corresponding
# in-order traversals are identical:
#
#   [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]
#
# Therefore, we CAN'T SOLVE this problem with an in-order traversal.


# Pre-Order & Post-Order Traversal:
# The corresponding pre-order and post-order traversals of the trees above are:
#
#   pre-order:  [1, 2, 3], [1, 3, 2], [2, 1, 3], [3, 1, 2], [3, 2, 1]
#   post-order: [3, 2, 1], [2, 3, 1], [1, 3, 2], [2, 1, 3], [1, 2, 3]
#
# Since each are unique, we CAN SOLVE this problem with a pre-order


# Pre-Order BST Traversal Reconstruction Approach: Time complexity is O(n), where n is the number of nodes in the tree.
# Space complexity is O(n + h) where n is the number of nodes in the tree and h is the height of the tree.
def bst_from_preorder_traversal(l, _min=None, _max=None):
    if len(l) > 0 and (_min is None or _min < l[0]) and (_max is None or l[0] <= _max):
        n = Node(l.pop(0))
        if len(l) > 0 and l[0] <= n.value:
            n.left = bst_from_preorder_traversal(l, _min, n.value)
        if len(l) > 0 and n.value < l[0]:
            n.right = bst_from_preorder_traversal(l, n.value, _max)
        return n


# Post-Order BST Traversal Reconstruction Approach: Time complexity is O(n), where n is the number of nodes in the tree.
# Space complexity is O(n + h) where n is the number of nodes in the tree and h is the height of the tree.
# NOTE: The that values are popped from END of the list, AND that left/right recursion order is SWITCHED.
def bst_from_postorder_traversal(l, _min=None, _max=None):
    if len(l) > 0 and (_min is None or _min < l[-1]) and (_max is None or l[-1] <= _max):
        n = Node(l.pop())
        if len(l) > 0 and n.value < l[-1]:
            n.right = bst_from_postorder_traversal(l, n.value, _max)
        if len(l) > 0 and l[-1] < n.value:
            n.left = bst_from_postorder_traversal(l, _min, n.value)
        return n


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __iter__(self):
        if self.left:
            yield from self.left
        yield self.value
        if self.right:
            yield from self.right

    def __repr__(self):
        return ", ".join(map(repr, self))


def is_identical(t1, t2):
    if t1 is t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    return t1.value == t2.value and is_identical(t1.left, t2.left) and is_identical(t1.right, t2.right)


def preorder_values(t):
    def wrapper(t, l):
        l.append(t.value)
        if t.left:
            wrapper(t.left, l)
        if t.right:
            wrapper(t.right, l)
    l = []
    if t:
        wrapper(t, l)
    return l


def postorder_values(t):
    def wrapper(t, l):
        if t.left:
            wrapper(t.left, l)
        if t.right:
            wrapper(t.right, l)
        l.append(t.value)
    l = []
    if t:
        wrapper(t, l)
    return l


def display(node):
    def wrapper(node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        if node.right is None and node.left is None:                                        # No child.
            return [str(node.value)], len(str(node.value)), 1, len(str(node.value)) // 2
        if node.right is None:                                                              # Only left child.
            lines, n, p, x = wrapper(node.left)
            u = len(str(node.value))
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + str(node.value)
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        if node.left is None:                                                               # Only right child.
            lines, n, p, x = wrapper(node.right)
            u = len(str(node.value))
            first_line = str(node.value) + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        else:                                                                               # Two children.
            left, n, p, x = wrapper(node.left)
            right, m, q, y = wrapper(node.right)
            u = len(str(node.value))
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + str(node.value) + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zip(left, right)]
            return lines, n + m + u, max(p, q) + 2, n + u // 2
    if node:
        lines, _, _, _ = wrapper(node)
        for line in lines:
            print(line)


trees = [Node(1, None, Node(2, None, Node(3))),
         Node(1, None, Node(3, Node(2))),
         Node(2, Node(1), Node(3)),
         Node(3, Node(1, None, Node(2))),
         Node(3, Node(2, Node(1))),
         Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), Node(6))),
         Node(3, Node(1, None, Node(2)), Node(5, Node(4), None)),
         Node(3, Node(1, Node(0), None), Node(5, None, Node(6))),
         Node(0),
         None]

for i, t in enumerate(trees):
    print(f"t = trees[{i}]:")
    display(t)
    print(f"is_identical(t, bst_from_preorder_traversal({preorder_values(t)})): {is_identical(t, bst_from_preorder_traversal(preorder_values(t)))}")
    print(f"is_identical(t, bst_from_postorder_traversal({postorder_values(t)})): {is_identical(t, bst_from_postorder_traversal(postorder_values(t)))}\n")


