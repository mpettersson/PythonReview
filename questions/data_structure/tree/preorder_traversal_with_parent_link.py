r"""
    PREORDER WITH PARENT LINK

    Given the root to a binary tree, where nodes have a link to value, left, right, and parent, write a function that
    prints an preorder traversal with O(1) space complexity.  Without a link to the parent node, preorder traversal
    requires O(h) space, where h is the height of the tree.

    Consider the following binary tree:

             3
           /   \
          1     5
         / \   /
        0  2  4

    Example:
        Input = Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4)))  # or, the tree above
        Output = 3 1 0 2 5 4
"""


# NOTE: O(1) space rules out all recursive solutions.


# Iterative Approach:  While there are nodes; print the value, if there is a left or right child, go left or right, else
# ascend until there is a right child not on the visited (on the ascension path) or None.
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(1).
def preorder_with_parent_link_iterative(root):
    if root is not None:
        curr = root
        while curr:
            print(f" {curr.value}", end="")                         # Print node value.
            if curr.left or curr.right:                             # If left or right child, go left or right.
                curr = curr.left if curr.left else curr.right
            else:                                                   # Else go to right child of nearest ancestor with
                while curr:
                    parent = curr.parent
                    if parent and parent.right and parent.right is not curr:
                        curr = parent.right
                        break
                    curr = parent


class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        if self.left:
            self.left.parent = self
        self.right = right
        if self.right:
            self.right.parent = self
        self.parent = parent

    def __repr__(self):
        return repr(self.value)


def preorder_recursive(root):
    if root:
        print(f" {root.value}", end="")
        preorder_recursive(root.left)
        preorder_recursive(root.right)


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


trees = [Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4))),
         Node(1, Node(3, Node(4), Node(6, Node(5), Node(0))), Node(2)),
         Node(3, Node(1, None, Node(2)), Node(5, Node(4))),
         Node(3, Node(1, Node(0)), Node(5, None, Node(6))),
         Node(3, Node(1, Node(0), Node(3)), Node(5, Node(3), Node(6))),
         Node(4, Node(1, Node(0), Node(3)), Node(2)),
         Node(4, Node(1, Node(0), Node(2)), Node(5, Node(3), Node(6))),
         Node(0, Node(1, Node(2))),
         Node(0, Node(1), Node(3, Node(2), Node(4))),
         Node(26, Node(5, Node(-37, Node(-74, Node(-86), Node(-51)), Node(-7, Node(-17))),
                       Node(17, Node(11, Node(5)), Node(26, Node(18)))),
              Node(74, Node(41, Node(34, Node(28)), Node(52, Node(47))),
                   Node(90, Node(88, Node(86)), Node(99, Node(95))))),
         Node(27, Node(2, None, Node(17, Node(11, Node(5)), Node(26, Node(18)))),
              Node(74, Node(41, Node(34, Node(28))),
                   Node(90, Node(88), Node(99, None, Node(105, None, Node(420)))))),
         Node(27, Node(74, Node(90, Node(99, Node(105, Node(420))), Node(88)),
                       Node(41, None, Node(34, None, Node(28)))),
              Node(2, Node(17, Node(26, None, Node(18)), Node(11, None, Node(5)))))]
fns = [preorder_with_parent_link_iterative]

for i, tree in enumerate(trees):
    print(f"trees[{i}]:")
    display(tree)
    print(f"(recursive preorder traversal:", end="")
    preorder_recursive(tree)
    print(")\n")
    for fn in fns:
        print(f"{fn.__name__}(tree):", end="")
        fn(tree)
        print()
    print()


