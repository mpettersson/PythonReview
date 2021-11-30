r"""
    HAS PATH WITH SUM T (EPI 10.6: FIND A ROOT TO LEAF PATH WITH SPECIFIED SUM)

    Given the root of a binary tree, where each node's value is a number (whole or decimal, positive or negative) and
    a target sum t, write a function that returns all paths (as a list of lists of nodes) from the root to leaf, with
    downward movement only, that has the sum of t.

    Consider the following binary tree:

               10
             /    \
            5     -3
           /  \     \
          3    2     7
         / \    \     \
        4  -2   -1    11

    Example:
                tree = Node(10, Node(5, Node(3, Node(4), Node(-2)), Node(2, None, Node(-1))),
                                Node(-3, None, Node(7, None, Node(11))))
        Input = tree, 16
        Output = [[10, 5, 3, -2], [10, 5, 2, -1]]
"""


# APPROACH: Via Recursion
#
# Recurse from root, appending nodes to the path, adding the nodes to result if at a leaf and the values of the nodes in
# the path is t, then popping from the end of the path.
#
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(n), where n is the number of nodes in the tree.
def find_paths_with_sum_t(root, t):

    def _rec(root, t, path, result):
        if root:
            path.append(root)
            if root.left is None and root.right is None and sum([n.value for n in path]) is t:
                result.append(list(path))
            _rec(root.left, t, path, result)
            _rec(root.right, t, path, result)
            path.pop()

    if root and t is not None:
        result = []
        _rec(root, t, [], result)
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


tree = Node(10, Node(5, Node(3, Node(4), Node(-2)), Node(2, None, Node(-1))), Node(-3, None, Node(7, None, Node(11))))
t_vals = [-6, 7, 16, 22, 23, 24, 25, None]
fns = [find_paths_with_sum_t]

print("\ndisplay(tree)")
display(tree)
print()
for t in t_vals:
    for fn in fns:
        print(f"{fn.__name__}(tree, {t}): {fn(tree, t)}")
    if len(fns) > 1:
        print()


