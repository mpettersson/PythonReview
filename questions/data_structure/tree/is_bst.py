r"""
    IS BST

    NOTE: The BST property in this question is DIFFERENT than the property in the validate_bst.py/VALIDATE BST problem!

    Given the head of a binary tree (head), write an algorithm that returns True if the tree is a Binary Search Tree
    (BST) or false otherwise.

    For each node in a BST the property "all left descendants <= node <= all right descendants" must be true.

    Consider the following binary trees:

            3                    4                    4                 3
          /   \                /  \                 /  \              /  \
         1     5              1    2              1    5             1    5
        / \   / \            / \                / \   / \           / \  / \
       0  2  4   6          0   3              0  2  3   6         0  3  3  6

    The trees with root value 3 are BSTs, the trees with root 4 are not.

    NOTE: The third (second from right) tree is tricky; 3 is less than 5 BUT 3 is not greater than the root value of 4.

    Example:
        Input = Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), Node(6)))  # or, the first example tree above
        Output = True
"""


# In-Order Traversal:  Compare current value to previous value along the traversal.  Time complexity is O(n), where n is
# the number of nodes in the tree, and space complexity is O(h) where h is the height of the tree (or O(log n) where n
# is the number of nodes in the tree).
def is_bst_via_gen(t):
    if t:
        vals = in_order_traversal_generator(t)
        prev = next(vals)
        while True:
            curr = next(vals, None)
            if not curr:
                break
            if prev > curr:
                return False
            prev = curr
        return True


def in_order_traversal_generator(bt):
    if bt.left:
        yield from in_order_traversal_generator(bt.left)
    yield bt.value
    if bt.right:
        yield from in_order_traversal_generator(bt.right)


# Max/Min Approach:  Track max/min values at each level; min is used to check the right child and max is used to check
# the left child.  Time complexity is O(n), where n is the number of nodes in the tree, and space complexity is O(h)
# where h is the height of the tree (or O(log n) where n is the number of nodes in the tree).
def is_bst(n, lowest=None, highest=None):
    if lowest and n.value < lowest:
        return False
    if highest and highest < n.value:
        return False
    is_left_bst = is_right_bst = True
    if n.left:
        is_left_bst = is_bst(n.left, lowest, n.value)
    if is_left_bst and n.right:
        is_right_bst = is_bst(n.right, n.value, highest)
    return is_left_bst and is_right_bst


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


trees = [Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), Node(6))),     # IS a BST
         Node(3, Node(1, Node(0), Node(3)), Node(5, Node(3), Node(6))),     # IS a BST
         Node(4, Node(1, Node(0), Node(3)), Node(2)),                       # ISN'T a BST
         Node(4, Node(1, Node(0), Node(2)), Node(5, Node(3), Node(6)))]     # ISN'T a BST

for i, t in enumerate(trees):
    print(f"display(t[{i}]):"); display(t)
    print(f"is_bst_via_gen(t[{i}])", is_bst_via_gen(t))
    print(f"is_bst(t[{i}]):", is_bst(t), "\n")

