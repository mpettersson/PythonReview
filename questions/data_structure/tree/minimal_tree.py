r"""
    MINIMAL TREE (CCI 4.2)

    Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search
    tree with minimal height.

    Consider the following BST:

             3
           /   \
          1     5
         / \   / \
        0  2  4  None

    Example:
        Input = [0, 1, 2, 3, 4, 5]
        Output = Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), None))     # or, the BST above
"""


# Recursive Approach: Time and space complexity is O(n) where n is the size of the array (list).
def minimal_tree(l):
    if l and len(l) > 0:
        mid = len(l) // 2
        return Node(l[mid], minimal_tree(l[0:mid]), minimal_tree(l[mid+1:]))


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __iter__(self):
        if self.left:
            yield self.left
        yield self.value
        if self.right:
            yield self.right

    def __repr__(self):
        return ", ".join(map(str, self))


# Helper Function
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


list_of_lists = [[0, 1, 2, 3, 4, 5],
                 [-86, -74, -51, -37, -17, -7, 5, 5, 11, 17, 18, 26, 26, 28, 34, 41, 47, 52, 74, 86, 88, 90, 95, 99],
                 [1, 2, 3],
                 [0],
                 []]

for i, l in enumerate(list_of_lists):
    minimal_bst = minimal_tree(l)
    print(f"display(minimal_tree(list_of_lists[{i}])):"); display(minimal_bst)
    print()


