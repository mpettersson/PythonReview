r"""
    IS SYMMETRIC (EPI 10.2: TEST IF A BINARY TREE IS SYMMETRIC)

    Write a function, which accepts the root of a binary tree, and returns True if the tree is symmetric, False
    otherwise.  A binary tree is symmetric if the root's left subtree structure and values are a mirror of the right
    subtree structure and values.

    Consider the following symmetric (left) and asymmetric (right) binary trees:

                420                 420                 420                420
             ⟋      ⟍           ⟋      ⟍           ⟋      ⟍           ⟋      ⟍
           6          6        6          6        6          6        6          6
            \        /          \        /          \        /          \        /
             2      2            2      2           516     2           516    516
              \    /            / \    / \            \    /              \
               3  3            0   3  3   0            3  1                3

    Example:
        Input = Node(420, Node(6, None, Node(2, None, Node(3))), Node(6, Node(2, Node(3))))
        Output = True
"""


# Recursive Approach:  Recursively compare a nodes, starting at the root;
#   (1) If no children, return True.
#   (2) If both children have the same value, recursively compare the mirrored children.
#   (3) Return False otherwise.
# Time Complexity: O(n), where n are the number of nodes in the tree.
# Space Complexity is O(h), where h is the height of the tree.
#
# NOTE: By definition, a BST cannot be symmetric.
def is_symmetric(root):

    def _is_symmetric(left, right):
        if left is None and right is None:
            return True
        if left and right and left.value == right.value:
            return _is_symmetric(left.right, right.left) and _is_symmetric(left.left, right.right)
        return False

    if root is not None:
        return _is_symmetric(root.left, root.right)


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
        return ", ".join(map(str, self))


def display(node):
    def _display(node):
        if node.right is None and node.left is None:                                        # No child.
            return [str(node.value)], len(str(node.value)), 1, len(str(node.value)) // 2
        if node.right is None:                                                              # Only left child.
            lines, n, p, x = _display(node.left)
            u = len(str(node.value))
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + str(node.value)
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        if node.left is None:                                                               # Only right child.
            lines, n, p, x = _display(node.right)
            u = len(str(node.value))
            first_line = str(node.value) + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        else:                                                                               # Two children.
            left, n, p, x = _display(node.left)
            right, m, q, y = _display(node.right)
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
        lines, _, _, _ = _display(node)
        for line in lines:
            print(line)


trees = [Node(420, Node(6, None, Node(2, None, Node(3))), Node(6, Node(2, Node(3)))),
         Node(420, Node(6, None, Node(2, Node(0), Node(3))), Node(6, Node(2, Node(3), Node(0)))),
         Node(420, Node(6, None, Node(516, None, Node(3))), Node(6, Node(2, Node(1)))),
         Node(420, Node(6, None, Node(516, None, Node(3))), Node(6, Node(516))),
         Node(0),
         None]

for tree in trees:
    print(f"display(tree):")
    display(tree)
    print(f"is_symmetric(tree): {is_symmetric(tree)}\n")


