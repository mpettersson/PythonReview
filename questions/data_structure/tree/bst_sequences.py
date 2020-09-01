r"""
    BST SEQUENCES (CCI 4.9)

    A binary search tree was created by traversing through an array from left to right and inserting each element.
    Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.

    Consider the following tree:

            2
          /  \
        1     3

    Example:
        Input = Node(2, Node(1), Node(3))   # or, the tree above.
        Output = [[2, 1, 3], [2, 3, 1]]
"""


def bst_sequences(root):
    result = []
    if root is None:
        return [[]]

    l_seq = bst_sequences(root.left)
    r_seq = bst_sequences(root.right)

    for left in l_seq:
        for right in r_seq:
            weaved = []
            weave_lists(left, right, weaved, [root.value])
            result.extend(weaved)

    return result


def weave_lists(first, second, result, prefix):
    if not first or not second:
        l = prefix[:]
        l.extend(first)
        l.extend(second)
        result.append(l)
        return

    prefix.append(first.pop(0))
    weave_lists(first, second, result, prefix)
    first.insert(0, prefix.pop())

    prefix.append(second.pop(0))
    weave_lists(first, second, result, prefix)
    second.insert(0, prefix.pop())


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Helper Function
def display(node):
    def wrapper(node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        if node.right is None and node.left is None:  # No child.
            return [str(node.value)], len(str(node.value)), 1, len(str(node.value)) // 2
        if node.right is None:  # Only left child.
            lines, n, p, x = wrapper(node.left)
            u = len(str(node.value))
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + str(node.value)
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        if node.left is None:  # Only right child.
            lines, n, p, x = wrapper(node.right)
            u = len(str(node.value))
            first_line = str(node.value) + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        else:  # Two children.
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


trees = [Node(2, Node(1), Node(3)),
         Node(2, Node(1, Node(-1)), Node(3)),
         Node(3, Node(1, Node(0), Node(2)), Node(5)),
         Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4))),
         Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), Node(6))),
         Node(3, Node(1, Node(0, Node(-1)), Node(2)), Node(5, Node(4), Node(6))),
         Node(3, Node(1, Node(0, Node(-1)), Node(2)), Node(5, Node(4), Node(6, None, Node(9)))),
         Node(3, Node(1, Node(0, Node(-1)), Node(2)), Node(5, Node(4), Node(7, Node(6), Node(9)))),
         Node(0),
         None]

for i, t in enumerate(trees):
    print(f"display(trees[{i}]):"); display(t)
    sequences = bst_sequences(t)
    print(f"bst_sequences(trees[{i}]): {sequences}")
    print(f"len(bst_sequences(trees[{i}])): {len(sequences)}\n")


