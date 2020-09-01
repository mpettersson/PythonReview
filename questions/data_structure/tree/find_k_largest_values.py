r"""
    FIND K LARGEST VALUES (EPI 15.3)

    Write a program that takes as input a BST and an integer k, and returns the k largest elements in the BST in
    decreasing order.

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
        Input = t, 4
        Output = [53, 47, 43, 41]
"""


# Iterator Approach:  Time and space is O(h + k), where h is the height of the tree.
def k_largest_values_iter(t, k):

    def wrapper(t):
        if t.right:
            yield from wrapper(t.right)
        yield t.value
        if t.left:
            yield from wrapper(t.left)

    l = []
    for i in wrapper(t):
        if len(l) is k:
            return l
        l.append(i)


# Recursive Approach:  Time is O(min(n, k)) where n is the number of nodes in the tree.  Space is O(max(h, k)), where h
# is the height of the tree.
def k_largest_values(t, k):

    def wrapper(t, k, l):
        if len(l) < k and t.right:
            wrapper(t.right, k, l)
        if len(l) < k:
            l.append(t.value)
        if len(l) < k and t.left:
            wrapper(t.left, k, l)

    if t and k is not None and k >= 0:
        l = []
        wrapper(t, k, l)
        return l


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
args = [-5, 0, 5, None]

print("display(tree):")
display(tree)
print()

for i in args:
    print(f"k_largest_values_iter(tree, {i}):", k_largest_values_iter(tree, i))
print()

for i in args:
    print(f"k_largest_values(tree, {i}):", k_largest_values(tree, i))


