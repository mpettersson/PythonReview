r"""
    TREE WITH MINIMAL HEIGHT (CCI 4.2: MINIMAL TREE)

    Create a function which accepts a list of values l, then builds and returns a binary tree with minimal height.

    NOTE: If the list is SORTED, in increasing order, and all values are UNIQUE then the a binary search tree (BST) with
    the property "all left descendants <= node < all right descendants" will be created.  If there are DUPLICATE values
    then a BST with the property "all left descendants <= node <= all right descendants" will be created.

    Consider the following BST:

             3
           /   \
          1     5
         / \   / \
        0  2  4  None

    Example:
        Input = [0, 1, 2, 3, 4, 5]
        Output = Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), None))  # or, the BST above
"""


# Recursive Approach:  Use the middle value as root, recurse on sub-lists left and right of middle for left and right
# children/subtrees.
# Time Complexity: O(n), where n is the size of the list.
# Space Complexity: O(n + log(n)), which reduces to O(n), where n is the size of the list (log(n) bc list slicing).
def tree_with_minimal_height_via_slicing(l):
    if l and len(l) > 0:
        mid = len(l) // 2
        return Node(l[mid], tree_with_minimal_height_via_slicing(l[0:mid]),
                    tree_with_minimal_height_via_slicing(l[mid + 1:]))


# Recursive Approach:  Same as above, however, uses indexing and the given list (not list slices).
# Time Complexity: O(n), where n is the size of the list.
# Space Complexity: O(n + log(n)), which reduces to O(n), where n is the size of the list (log(n) bc recursion stack).
def tree_with_minimal_height(l):

    def _tree_with_minimal_height(l, lo, hi):
        if 0 <= lo <= hi:
            mid = (lo + hi + 1) // 2    # +1 so that left fills up first.
            return Node(l[mid], _tree_with_minimal_height(l, lo, mid - 1), _tree_with_minimal_height(l, mid + 1, hi))

    if l is not None:
        return _tree_with_minimal_height(l, 0, len(l)-1)


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
    else:
        print(None)


args = [[0, 1, 2, 3, 4, 5],
        [0, 3, 3, 3, 3, 3, 3, 5],
        [-86, -74, -51, -37, -17, -7, 5, 5, 11, 17, 18, 26, 26, 28, 34, 41, 47, 52, 74, 86, 88, 90, 95, 99],
        [1, 2, 3],
        [0],
        [],
        None]
fns = [tree_with_minimal_height_via_slicing,
       tree_with_minimal_height]

for l in args:
    for fn in fns:
        print(f"display({fn.__name__}({l})):")
        display(fn(l))
        print()


