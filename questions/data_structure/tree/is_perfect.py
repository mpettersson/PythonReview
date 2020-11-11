r"""
    IS PERFECT

    Write a function, which when given the root of a binary tree, returns true if the binary tree is a perfect binary
    tree, false otherwise.  A binary tree with height h is a PERFECT BINARY TREE if it has (2**(h+1))-1 nodes, of which
    2**h are leaves. The HEIGHT of a binary tree is the maximum depth of any node in a tree. The DEPTH of a node in a
    binary tree is the number of nodes in the path from the root to the node, not including the node itself.

    The following is a perfect binary tree with height 3:

                    19              depth 0
                ⟋       ⟍
              7           23        depth 1
            ⟋  ⟍        ⟋  ⟍
           3    13      21   41     depth 2
          / \   / \    / \   / \
         2  5  11 17  20 22 29 42   depth 3

    Example:
                tree = Node(19, Node(7, Node(3, Node(2), Node(5)), Node(13, Node(11), Node(17))),
                                Node(23, Node(21, Node(20), Node(22)), Node(41, Node(29), Node(42)))))
        Input = tree  # or, the tree above
        Output = True
"""


# Recursive Approach:  Recursively check the children, ensuring that both are perfect and have the same height.  Each
# call returns a boolean indicating perfection and the max height of the node.
# Time Complexity: O(n), where n are the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree.
def is_perfect(root):

    def _is_perfect(root):
        if root:
            l_b, l_h = _is_perfect(root.left)
            r_b, r_h = _is_perfect(root.right)
            return l_b and r_b and l_h is r_h, max(l_h, r_h) + 1
        return True, -1

    if root:
        result, max_height = _is_perfect(root)
        return result


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return repr(self.value)


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
        print()
    else:
        print(None)


trees = [Node(19, Node(7, Node(3, Node(2), Node(5)), Node(13, Node(11), Node(17))),
              Node(23, Node(21, Node(20), Node(22)), Node(41, Node(29), Node(42)))),
         Node(0),
         Node(1, Node(0), Node(2)),
         Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4))),
         Node(1, Node(3, Node(4), Node(6, Node(5), Node(0))), Node(2)),
         Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), Node(6))),
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
         Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), Node(6))),
         Node(4, Node(1, Node(0), Node(2)), Node(5, Node(3), Node(6))),
         Node(0, Node(1), Node(3, Node(2), Node(4))),
         Node(27, Node(5, Node(-37, Node(-74, Node(-86), Node(-51)), Node(-7, Node(-17), Node(-8))),
                       Node(17, Node(11, Node(8), Node(13)), Node(26, Node(18), Node(27)))),
              Node(74, Node(42, Node(34, Node(28), Node(41)), Node(52, Node(47), Node(69))),
                   Node(90, Node(88, Node(86), Node(89)), Node(99, Node(95), Node(999)))))]
fns = [is_perfect]

for i, tree in enumerate(trees):
    print(f"trees[{i}]:")
    display(tree)
    for fn in fns:
        print(f"{fn.__name__}(tree): {fn(tree)}")
    print()


