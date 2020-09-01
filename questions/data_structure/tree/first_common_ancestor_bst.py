r"""
    FIRST COMMON ANCESTOR BST

    NOTE: If no BST ordering, or for trees with links to parents, SEE first_common_ancestor.py/"FIRST COMMON ANCESTOR".

    Design an algorithm and write code to find the first common ancestor of two nodes in a binary search tree (BST).
    Avoid storing additional nodes in a data structure.

    Consider the following BST:

              5
            /   \
           1     6
         /  \
        0    3
            / \
           2   4

    Example:
                my_bst = Node(5, Node(1, Node(4), Node(6, Node(5), Node(0))), Node(2))
                node_4 = my_bst.left.left
                node_5 = my_bst.left.right.left
        Input = my_bst, node_4, node_5      # my_bst is the BST above
        Output = 3                          # that is, the node with value three
"""


# Naive Two Path Approach:  This may, or may not, fulfil the interviewers space requirements, ask them.
# Time complexity is O(n) and space complexity is O(h1 + h2), where h1 and h2 are the heights of n1 and n2 (however, the
# worst case space could be O(n)).
def first_common_ancestor_bst_naive(t, n1, n2):
    if t and n1 and n2:
        p1 = path_to_node(t, n1)
        p2 = path_to_node(t, n2)
        if p1 and p2:
            if len(p2) > len(p1):
                p1, p2 = p2, p1
            while len(p1) > len(p2):
                p1.pop(0)
            while p1 and p1[0] != p2[0]:
                p1.pop(0)
                p2.pop(0)
            if p1 and p1[0] == p2[0]:
                return p1[0].value


def path_to_node(root, node):
    if root is node:
        return [root]
    if node.value < root.value and root.left:
        l = path_to_node(root.left, node)
        if l:
            return l + [root]
    if node.value > root.value and root.right:
        l = path_to_node(root.right, node)
        if l:
            return l + [root]


# Recursive Modified Find Approach: Using the BST property, recurse down from root,
# Time complexity is O(n) where n is the number of nodes in the tree. Space complexity is O(h), where h is the height of
# the tree ((however, the worst case space could be O(n)).
def first_common_ancestor_bst_rec(root, n1, n2):

    def wrapper(root, n1, n2):
        if root is n1 or root is n2 or n1.value <= root.value < n2.value or n2.value <= root.value < n1.value:
            return root
        if n1.value <= root.value and n2.value <= root.value:
            return wrapper(root.left, n1, n2)
        if root.value < n1.value and root.value < n2.value:
            return wrapper(root.right, n1, n2)

    if root and n1 and n2 and is_in_bst(root, n1) and is_in_bst(root, n2):
        return wrapper(root, n1, n2)


def is_in_bst(root, node):
    if root and node:
        if root is node:
            return True
        return root.right and node.value > root.value and is_in_bst(root.right, node) or \
               root.left and node.value <= root.value and is_in_bst(root.left, node)


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return repr(self.value)


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


tree = Node(5, Node(1, Node(0), Node(3, Node(2), Node(4))), Node(6))
args = [(tree.left.left, tree.left.right.left),                     # (0, 2)
        (tree.left.right.left, tree.left.left),                     # (2, 0)
        (tree.left, tree.right),                                    # (1, 6)
        (tree.right, tree.left),                                    # (6, 1)
        (tree.left.right.right, tree.right),                        # (4, 6)
        (tree.left.right.left, tree.left.right.right),              # (2, 4)
        (tree.left.right.left, Node(7)),                            # (2, 7) (7 isn't in the tree)
        (tree.right, Node(8)),                                      # (6, 8) (8 isn't in the tree)
        (Node(7), Node(8)),                                         # (7, 8) (7 and 8 isn't in the tree)
        (None, Node(7)),                                            # (None, 7) (7 isn't in the tree)
        (Node(7), None),                                            # (7, None) (7 isn't in the tree)
        (None, None)]                                               # (None, None)

print(f"display(tree):")
display(tree)
print()

for n1, n2 in args:
    print(f"first_common_ancestor_bst_naive(tree, {n1}, {n2}):", first_common_ancestor_bst_naive(tree, n1, n2))
print()

for n1, n2 in args:
    print(f"first_common_ancestor_bst_rec(tree, {n1}, {n2}):", first_common_ancestor_bst_rec(tree, n1, n2))


