r"""
    VALIDATE BST (CCI 4.5)

    NOTE: The BST property in this question is DIFFERENT than the property in the is_bst.py/IS BST problem!

    Implement a function to check if a binary tree is a binary search tree (BST).  A binary search tree (BST) is a bin
    tree in which EVERY node fits a specific ordering property; 'all left descendants <= n < all right descendants'.

    Consider the following binary trees:

             3                   4                  4                 3               3         3
           /   \               /  \               /  \              /  \             /           \
          1     5             1    2            1    5             1    5           3             3
         / \   / \           / \              / \   / \           / \  / \
        0  2  4   6         0   3            0  2  3   6         0  3  3  6

    Only the first (left most) tree maintains the BST property 'all left descendants <= n < all right descendants'.

    NOTE: Because 'n < all right descendants' a basic in-order traversal WON'T work; consider the right two trees.

    NOTE: The two middle trees are tricky; 3 is less than 5 BUT 3 is not greater than the tree's root (3 or 4).

    Example:
        Input = Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), Node(6)))   # or, the first example tree above
        Output = True
"""


# Max/Min Approach (Verbose): Track max/min values at each level; min is used to check the right child and max is used
# to check the left child.  Time complexity is O(n), where n is the number of nodes in the tree, and space complexity is
# O(h) where h is the height of the tree (or O(log n) where n is the number of nodes in the tree).
def validate_bst_verbose(root):
    def wrapper(node):
        if node is None:
            return None, None, None
        if node.left is None and node.right is None:
            return True, node.value, node.value
        if node.left and node.right is None:
            b, max_l, min_l = wrapper(node.left)
            return b and (max_l <= node.value), max(max_l, node.value), min(min_l, node.value)
        if node.right and node.left is None:
            b, max_r, min_r = wrapper(node.right)
            return b and (node.value < min_r), max(max_r, node.value), min(min_r, node.value)
        b_l, max_l, min_l = wrapper(node.left)
        b_r, max_r, min_r = wrapper(node.right)
        return b_l and b_r and max_l <= node.value < min_r, max(max_l, max_r, node.value), min(min_l, min_r, node.value)

    res, _, _ = wrapper(root)
    return res


# Max/Min Approach (Enhanced):  Track max/min values at each level; min is used to check the right child and max is used
# to check the left child.  Time complexity is O(n), where n is the number of nodes in the tree, and space complexity is
# O(h) where h is the height of the tree (or O(log n) where n is the number of nodes in the tree).
def validate_bst(node, _min=None, _max=None):
    if node:
        if _min is not None and node.value <= _min or _max is not None and _max < node.value:
            return False
        if not validate_bst(node.left, _min, node.value) or not validate_bst(node.right, node.value, _max):
            return False
    return True


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

    def flatten(self):
        l = []
        q = [(self, 0)]
        while len(q) > 0:
            node, i = q.pop(0)
            if node.left:
                q.append((node.left, i + 1))
            if node.right:
                q.append((node.right, i + 1))
            if len(l) < (i + 1):
                l.append([node.value])
            else:
                l[i].append(node.value)
        return [y for x in l for y in x]


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


trees = [Node(20, Node(10, None, Node(25)), Node(30)),                                          # ISN'T a BST
         Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), Node(6))),                         # IS a BST
         Node(4, Node(1, Node(0), Node(3)), Node(2)),                                           # ISN'T a BST
         Node(3, Node(1, None, Node(2)), Node(5, Node(4))),                                     # IS a BST
         Node(3, Node(1, None, Node(2)), Node(5)),                                              # IS a BST
         Node(3, Node(1, None, Node(2))),                                                       # IS a BST
         Node(26, Node(5, Node(-37, Node(-74, Node(-86), Node(-51)), Node(-7, Node(-17))),      # ISN'T a BST
                          Node( 17, Node(11, Node(5)), Node(26, Node(18)))),
                  Node(74, Node(41, Node(34, Node(28)), Node(52, Node(47))),
                           Node(90, Node(88, Node(86)), Node(99, Node(95))))),
         Node(27, Node(2, None, Node(17, Node(11, Node(5)), Node(26, Node(18)))),               # IS a BST
                  Node(74, Node(41, Node(34, Node(28))),
                           Node(90, Node(88), Node(99, None, Node(105, None, Node(420)))))),
         Node(4, Node(1, Node(0), Node(2)), Node(5, Node(3), Node(6))),                         # ISN'T a BST
         Node(3, Node(1, Node(0), Node(3)), Node(5, Node(3), Node(6))),                         # ISN'T a BST
         Node(4, Node(1, Node(0), Node(3)), Node(2)),                                           # ISN'T a BST
         Node(4, Node(1, Node(0), Node(2)), Node(5, Node(3), Node(6))),                         # ISN't a BST
         Node(0),                                                                               # IS a BST
         None]                                                                                  # IS None

for i, t in enumerate(trees):
    print(f"display(trees[{i}]):"); display(t)
    print(f"validate_bst_verbose(trees[{i}]):", validate_bst_verbose(t), "")
    print(f"validate_bst(trees[{i}]):", validate_bst(t), "\n")


