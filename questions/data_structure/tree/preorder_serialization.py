r"""
    PREORDER SERIALIZATION

    Write a function which takes the root of a binary tree and returns a preorder serialization of the binary tree.  Use
    None to denote, or mark, an empty child node.

    Consider the following binary tree:

             3
           /   \
          1     5
         / \   /
        0  2  4

    Example:
        Input = Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4)))  # or, the tree above
        Output = [3, 1, 0, None, None, 2, None, None, 5, 4, None, None, None]
"""


# Recursive Approach: Recursively append node values, or None if no Node, to a result list.
# Time Complexity: O(n), where n are the number of nodes in the tree.
# Space Complexity: O(n), where n are the number of nodes in the tree.
def get_preorder_serialization_rec_verbose(root):

    def _get_preorder_serialization_rec_verbose(root, result):
        if root:
            result.append(root.value)
            _get_preorder_serialization_rec_verbose(root.left, result)
            _get_preorder_serialization_rec_verbose(root.right, result)
        else:
            result.append(None)

    if root:
        result = []
        _get_preorder_serialization_rec_verbose(root, result)
        return result


# Recursive Approach: Recursively build a result list of node values, or None if no Node.
# Time Complexity: O(n), where n are the number of nodes in the tree.
# Space Complexity: O(n), where n are the number of nodes in the tree.
def get_preorder_serialization_rec(root):

    def _get_preorder_serialization_rec(n):
        if n:
            return [n.value] + _get_preorder_serialization_rec(n.left) + _get_preorder_serialization_rec(n.right)
        return [None]

    if root:
        return _get_preorder_serialization_rec(root)


# Iterative Approach: Using a stack (initialized with only the root) in place of recursion; pop a value and push
# whatever its children links point to (left first, to maintain normal order).
# Time Complexity: O(n), where n are the number of nodes in the tree.
# Space Complexity: O(n), where n are the number of nodes in the tree.
def get_preorder_serialization_iter(root):
    if root:
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.right)
                stack.append(node.left)
            result.append(node)
        return result


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return repr(self.value)


def preorder_traversal_recursive(root):
    if root:
        print(f" {root.value}", end="")
        preorder_traversal_recursive(root.left)
        preorder_traversal_recursive(root.right)


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
    else:
        print(None)


trees = [Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4))),
         Node(1, None, Node(2, None, Node(3))),
         Node(1, None, Node(3, Node(2))),
         Node(2, Node(1), Node(3)),
         Node(3, Node(1, None, Node(2))),
         Node(3, Node(2, Node(1))),
         None,
         Node(0),
         Node(6, Node(5, Node(4, Node(3, Node(2, Node(1, Node(0))))))),
         Node(1, Node(3, Node(4), Node(6, Node(5), Node(0))), Node(2)),
         Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), Node(6))),
         Node(3, Node(1, Node(0)), Node(5, None, Node(6))),
         Node(4, Node(1, Node(0), Node(3)), Node(2)),
         Node(4, Node(1, Node(0), Node(2)), Node(5, Node(3), Node(6))),
         Node(0, Node(1, Node(2))),
         Node(0, Node(1), Node(3, Node(2), Node(4))),
         Node(27, Node(2, None, Node(17, Node(11, Node(5)), Node(26, Node(18)))),
              Node(74, Node(41, Node(34, Node(28))),
                   Node(90, Node(88), Node(99, None, Node(105, None, Node(420)))))),
         Node(26, Node(5, Node(-37, Node(-74, Node(-86), Node(-51)), Node(-7, Node(-17))),
                       Node(17, Node(11, Node(5)), Node(26, Node(18)))),
              Node(74, Node(41, Node(34, Node(28)), Node(52, Node(47))),
                   Node(90, Node(88, Node(86)), Node(99, Node(95)))))]
fns = [get_preorder_serialization_rec_verbose,
       get_preorder_serialization_rec,
       get_preorder_serialization_iter]

for i, tree in enumerate(trees):
    print(f"trees[{i}]:")
    display(tree)
    print(f"(recursive preorder traversal:", end="")
    preorder_traversal_recursive(tree)
    print(")\n")
    for fn in fns:
        print(f"{fn.__name__}(tree): {fn(tree)}")
    print()


