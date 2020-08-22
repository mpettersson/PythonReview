r"""
    CHECK BALANCED (CCI 4.4)

    Implement a function to check if a binary tree is balanced.  For the purposes of this question, a balanced tree is
    defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.

    Consider the following tree:

             3
           /   \
          1     5
         / \   /
        0  2  4

    Example:
        Input = Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), None))  # or, the tree above
        Output = True
"""


# Recursive Approach: Recurse down from root, comparing the height of each subtree along the way, if ever unbalanced, a
# flag value of -1 is passed up.  Runtime is O(n) where n is the number of nodes in the tree and space is O(h) where h
# is the height of the tree.
def check_balanced(root):
    def get_height(node):
        if node is None:
            return 0
        l_h = get_height(node.left)
        r_h = get_height(node.right)
        if l_h is -1 or r_h is -1 or abs(l_h - r_h) > 1:
            return -1
        else:
            return max(l_h, r_h) + 1
    return False if get_height(root) < 0 else True


# Dual Return Value Approach:  This is similar to the approach above, only returning a boolean indicating balance status
# and the max height.  Runtime is O(n) where n is the number of nodes in the tree and space is O(h) where h is the
# height of the tree.
def check_balanced_alt(root):
    def wrapper(node):
        if node:
            if node.left is None and node.right is None:
                return True, 1
            if node.right is None:
                bal, h = wrapper(node.left)
                return not(h > 1) and bal, h + 1
            if node.left is None:
                bal, h = wrapper(node.right)
                return not(h > 1) and bal, h + 1
            l_bal, l_h = wrapper(node.left)
            r_bal, r_h = wrapper(node.left)
            return l_bal and r_bal and (abs(l_h - r_h) <= 1), max(l_h, r_h) + 1
    if root:
        balanced, height = wrapper(root)
        return balanced


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


trees = [Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), None)),
         Node(3, Node(1, None, Node(2)), Node(5, Node(4), None)),
         Node(3, Node(1, None, Node(2)), Node(5)),
         Node(3, Node(1, None, Node(2))),
         Node(26, Node(5, Node(-37, Node(-74, Node(-86), Node(-51)), Node(-7, Node(-17))),
                          Node( 17, Node(11, Node(5)), Node(26, Node(18)))),
                  Node(74, Node(41, Node(34, Node(28)), Node(52, Node(47))),
                           Node(90, Node(88, Node(86)), Node(99, Node(95))))),
         Node(27, Node(2, None, Node(17, Node(11, Node(5)), Node(26, Node(18)))),
                  Node(74, Node(41, Node(34, Node(28))),
                           Node(90, Node(88), Node(99, None, Node(105, None, Node(420)))))),
         Node(0),
         None]

for i, t in enumerate(trees):
    print(f"display(trees[{i}]):"); display(t)
    print(f"check_balanced(trees[{i}]):", check_balanced(t), "\n")


