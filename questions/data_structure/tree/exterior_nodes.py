r"""
    EXTERIOR NODES  (EPI 10.15:  COMPUTE THE EXTERIOR OF A BINARY TREE)

    Write a function, which when given the root of a binary tree, returns a list of the exterior nodes.  Exterior nodes
    are the nodes on the path from the root to the first value of an inorder traversal, all leaves (nodes without
    children), and all nodes on the path from the root to the last value of an inorder traversal.

    Consider the following binary tree:

                   19
                ⟋     ⟍
              7         20
            ⟋  ⟍          ⟍
           3    11         43
         ⟋  ⟍    ⟍       ⟋
        2    5     17    23
                  /        ⟍
                13          37
                           ⟋ ⟍
                          29  41
                           \
                           31

    Example:
                tree = Node(19, Node(7, Node(3, Node(2), Node(5)), Node(11, None, Node(17, Node(13)))),
                                Node(20, None, Node(43, Node(23, None, Node(37, Node(29, None, Node(31)), Node(41))))))
        Input = tree  # or, the tree above
        Output = [19, 7, 3, 2, 5, 13, 31, 41, 43, 20]
"""


# Recursive Approach:  Recurse on both subtrees, tracking if the current node is on the leftmost path or the rightmost
# path (via a combination of the 'been_left' and 'been_right' flags), returning (in proper order) nodes on the path to
# the first inorder value, leaf nodes, and nodes on the path from the last inorder value up to the root.
# Time Complexity: O(n), where n are the number of nodes in the tree.
# Space Complexity: O(n), where n are the number of nodes in the tree.
def get_exterior_nodes(root):

    def _get_exterior_nodes(root, been_left, been_right):
        if root:
            if been_left and been_right and root.left is None and root.right is None:
                return [root]
            l_res = ([root] if been_left and not been_right else []) + _get_exterior_nodes(root.left, True, been_right)
            r_res = _get_exterior_nodes(root.right, been_left, True) + ([root] if not been_left and been_right else [])
            return l_res + r_res
        return []

    if root:
        l_result = _get_exterior_nodes(root.left, True, False)
        r_result = _get_exterior_nodes(root.right, False, True)
        return [root] + l_result + r_result


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


trees = [Node(19, Node(7, Node(3, Node(2), Node(5)), Node(11, None, Node(17, Node(13)))),
              Node(20, None, Node(43, Node(23, None, Node(37, Node(29, None, Node(31)), Node(41)))))),
         Node(0),
         Node(0, None, Node(1)),
         Node(1, Node(0)),
         Node(8, Node(2, Node(6), Node(5, Node(1))), Node(3, None, Node(4, None, Node(7, Node(9))))),
         Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4))),
         Node(1, Node(3, Node(4), Node(6, Node(5), Node(0))), Node(2)),
         Node(3, Node(1, None, Node(2)), Node(5, Node(4))),
         Node(3, Node(1, Node(0)), Node(5, None, Node(6))),
         Node(4, Node(1, Node(0), Node(3)), Node(2)),
         Node(4, Node(1, Node(0), Node(2)), Node(5, Node(3), Node(6))),
         Node(0, Node(1, Node(2))),
         Node(0, Node(1), Node(3, Node(2), Node(4))),
         Node(27, Node(5, Node(-37, Node(-74, Node(-86), Node(-51)), Node(-7, Node(-17))),
                       Node(17, Node(11), Node(26, Node(18)))),
              Node(74, Node(41, Node(34, Node(28)), Node(52, Node(47))),
                   Node(90, Node(88, Node(86)), Node(99, Node(95))))),
         Node(27, Node(2, None, Node(17, Node(11, Node(5)), Node(26, Node(18)))),
              Node(74, Node(41, Node(34, Node(28))),
                   Node(90, Node(88), Node(99, None, Node(105, None, Node(420)))))),
         Node(27, Node(74, Node(90, Node(99, Node(105, Node(420))), Node(88)),
                       Node(41, None, Node(34, None, Node(28)))),
              Node(2, Node(17, Node(26, None, Node(18)), Node(11, None, Node(5)))))]
fns = [get_exterior_nodes]

for i, tree in enumerate(trees):
    print(f"trees[{i}]:")
    display(tree)
    for fn in fns:
        print(f"{fn.__name__}(trees[{i}]): {fn(tree)}")
    print()


