r"""
    POSTORDER KTH NODE

    Given the root of a tree and an integer k, write a function which returns the kth node in an postorder traversal
    from the root.  Nodes have a left, right, value, and size field; where size is the number of nodes in the subtree
    rooted at the node.

    Consider the following binary tree:

             3
           /   \
          1     5
         / \   /
        0  2  4

    Example:
        Input = Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4))), 4  # or, the tree above
        Output = 4
"""


# Recursive Approach: There are three cases:
#   (1) Recurse left if k <= left.size,
#   (2) Return root if k - left size - right size == 1 and,
#   (3) Recurse right if k - left.size <= right size.
# Time Complexity: O(h), where h is the height of the tree.
# Space Complexity: O(h), where h is the height of the tree.
def get_kth_postorder_node(root, k):

    def _get_kth_postorder_node(root, k):
        left_size = root.left.size if root.left else 0
        right_size = root.right.size if root.right else 0
        if k <= left_size:                                          # (1)  k <= left_size
            return _get_kth_postorder_node(root.left, k)
        if k - left_size - right_size is 1:                         # (2)  k - left_size - right_size == 1
            return root
        return _get_kth_postorder_node(root.right, k - left_size)  # (3)  k - left_size <= right_size

    if root and k is not None and 0 < k <= root.size:
        return _get_kth_postorder_node(root, k)


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.size = 0
        self.update_size()

    def __repr__(self):
        return repr(self.value)

    def update_size(self):
        self.size = (self.left.size if self.left else 0) + (self.right.size if self.right else 0) + 1


def postorder_traversal_recursive(root):
    if root:
        postorder_traversal_recursive(root.left)
        postorder_traversal_recursive(root.right)
        print(f" {root.value}", end="")


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


trees = [Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4))),
         Node(1, Node(3, Node(4), Node(6, Node(5), Node(0))), Node(2)),
         Node(0, Node(1, Node(2))),
         Node(26, Node(5, Node(-37, Node(-74, Node(-86), Node(-51)), Node(-7, Node(-17))),
                       Node(17, Node(11, Node(5)), Node(26, Node(18)))),
              Node(74, Node(41, Node(34, Node(28)), Node(52, Node(47))),
                   Node(90, Node(88, Node(86)), Node(99, Node(95))))),
         Node(27, Node(2, None, Node(17, Node(11, Node(5)), Node(26, Node(18)))),
              Node(74, Node(41, Node(34, Node(28))),
                   Node(90, Node(88), Node(99, None, Node(105, None, Node(420))))))]
ks = [-1, 1, 3, 4, 5, 10]
fns = [get_kth_postorder_node]

for i, tree in enumerate(trees):
    print("tree:")
    display(tree)
    print(f"(postorder traversal:", end="")
    postorder_traversal_recursive(tree)
    print(")")
    for fn in fns:
        print()
        for k in ks:
            print(f"{fn.__name__}(tree, {k}):", fn(tree, k))
    print()


