r"""
    NEXT LARGER VALUE (EPI 15.2)

    Write a program that takes as input a BST and a value, and returns the first node that would appear in an in-order
    traversal which is greater than the input value.

    Consider the following BST, t:

                  -19-
                /      \
              7         43
            /  \       /   \
           3   11     23   47
         /  \   \      \    \
        2   5   17     37   53
                /     /  \
               13   29   41
                     \
                     31

    Example:
        Input = t, 10
        Output = 11

    NOTE: For a slight variation of this question, see the successor.py/"SUCCESSOR" problem.
"""


# In-Order Traversal Naive Approach: Time complexity is O(n), where n is the number of nodes in the tree, space
# complexity is O(h) where h is the height of the tree.
def next_larger_value_naive(t, v):
    if t and v is not None:
        it = iter(t)
        for i in it:
            if i > v:
                return i


# Recursive Approach: Time complexity for a balanced tree is O(log(n)), with O(n) worst case time for unbalanced trees.
# Space complexity is O(h) where h is the height of the tree.
def next_larger_value(t, v):
    if t and v is not None:
        if v < t.value:
            res = next_larger_value(t.left, v)
            return res if res is not None and res < t.value else t.value
        if t.value <= v:
            return next_larger_value(t.right, v)


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __iter__(self):
        if self.left:
            yield from self.left
        yield self.value
        if self.right:
            yield from self.right

    def __repr__(self):
        return ", ".join(map(repr, self))


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


tree = Node(19, Node(7, Node(3, Node(2), Node(5)), Node(11, None, Node(17, Node(13)))),
                Node(43, Node(23, None, Node(37, Node(29, None, Node(31)), Node(41))), Node(47, None, Node(53))))
args = [10, -3, 53, 18, 19, 17, None]

print("display(tree):")
display(tree)
print()

for i in args:
    print(f"next_larger_value_naive(tree, {i}):", next_larger_value_naive(tree, i))
print()

for i in args:
    print(f"next_larger_value(tree, {i}):", next_larger_value(tree, i))


