r"""
    SUM OF PATHS AS BINARY NUMBERS  (EPI 10.5: SUM THE ROOT-TO-LEAF PATHS IN A BINARY TREE)

    When given the root of a binary tree, where each path from root to leaf represents a binary number, write a function
    that returns the sum of all the binary numbers encoded in the root to leaf paths.

    Consider the following BST:

                   1
               ⟋      ⟍
             0           1
           ⟋  ⟍       ⟋  ⟍
          0     1     0     0
         ⟋⟍      ⟍    ⟍     ⟍
        0   1      1     0     0
                  /     ⟋⟍
                 0     1  0
                        \
                         1

    NOTE: The tree above encode the following binary numbers (with decimal values): 1000 (8), 1001 (9), 10110 (22),
    110011 (51), 11000 (24), 1100 (12)

    Example:
                tree = Node(1, Node(0, Node(0, Node(0), Node(1)), Node(1, None, Node(1, Node(0)))),
                               Node(1, Node(0, None, Node(0, Node(1, None, Node(1)), Node(0))), Node(0, None, Node(0))))
        Input = tree
        Output = 126
"""


# Recursive Approach:  Recurse from root, multiplying by two then adding node value as a partial sum until a leaf is
# reached, then return the sum (to the calling recursive call).
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree.
def sum_of_paths_as_bin_num(root):

    def _sum_of_paths_as_bin_num(root, partial_path_sum):
        if root is None:
            return 0
        partial_path_sum = partial_path_sum * 2 + root.value
        if root.left is None and root.right is None:
            return partial_path_sum
        return _sum_of_paths_as_bin_num(root.left, partial_path_sum) + \
               _sum_of_paths_as_bin_num(root.right, partial_path_sum)

    if root:
        return _sum_of_paths_as_bin_num(root, 0)


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


tree = Node(1, Node(0, Node(0, Node(0), Node(1)), Node(1, None, Node(1, Node(0)))),
            Node(1, Node(0, None, Node(0, Node(1, None, Node(1)), Node(0))), Node(0, None, Node(0))))

print(f"display(tree):")
display(tree)

print(f"sum_of_paths_as_bin_num(tree):", sum_of_paths_as_bin_num(tree))


