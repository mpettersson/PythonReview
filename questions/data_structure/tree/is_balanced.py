r"""
    IS BALANCED (CCI  4.4: CHECK BALANCED,
                 EPI 10.1: TEST IF A BINARY TREE IS HEIGHT-BALANCED)

    Write a function that accepts a binary tree root and returns True if the tree is balanced, False otherwise.  A
    balanced tree is a tree such that the heights of two subtrees of any node never differ by more than one.

    Consider the following tree:

             3
           /   \
          1     5
         / \   /
        0  2  4

    Example:
        Input = Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), None))  # or, the tree above
        Output = True

    Variations:
        - Same question, however, the definition of balanced tree is now: A balanced tree is a tree such that the
          heights of ANY two branches never differ by more than one.
        - Write a function that returns the size of the largest complete subtree.
        - Write a function is_k_balanced, that takes a root and a positive integer k, and returns True if the tree is
          k balanced, False otherwise.  A k balanced tree is a tree such that the heights of the two subtrees of any
          node never differ by more than k.
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Clarify the definition of a "balanced tree" (the definition could ask for ANY branches differing in lenght by more
#     than one)?


# APPROACH: Recursive (Via Dual Return Value)
#
# This approach uses a recursive function that returns a Tuple of type (bool, int) representing a balanced tree amd the
# current height of the tree.  At each node, the function is called on both children (if the child is None, then 0 is
# returned), and the results are collated then returned up the stack.
#
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree.
def is_balanced_tree(root):

    def _rec(node):
        if node is None:
            return True, 0
        lb, lh = _rec(node.left)
        rb, rh = _rec(node.right)
        return lb and rb and (abs(lh - rh) <= 1), max(lh, rh) + 1

    if root is not None:
        balanced, height = _rec(root)
        return balanced


# APPROACH: Recursive (Via Int Value)
#
# This approach uses a recursive function that returns an integer value representing either; and unbalanced tree (-1) or
# the height of the tree (>= 0).  At each node, both the function is called on both children (if the child is None, then
# a simple 0 is returned), and the results are collated then returned up the stack.
#
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree.
def is_balanced(root):

    def _is_balanced(n):
        if n is None:
            return 0
        l = _is_balanced(n.left)
        r = _is_balanced(n.right)
        if l == -1 or r == -1 or abs(l - r) > 1:
            return -1                                       # -1 == unbalanced flag
        return max(l, r) + 1

    if root is not None:
        return False if _is_balanced(root) == -1 else True


# VARIATION: Same question, however, the definition of balanced tree is now: A balanced tree is a tree such that the
#           heights of ANY two branches never differ by more than one.


# VARIATION APPROACH: Via Get Max/Min Tree Height
#
# Inorder to see if all branches, or a path from the root to a leaf, have heights that are within one of each other,
# this approach simply finds and verifies the difference of the max and min branch heights.
#
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree.
def are_all_branches_balanced(r):

    def get_tree_max_and_min_height(n):
        def _rec(n):
            if n is None:
                return 0, 0
            lmax, lmin = _rec(n.left)
            rmax, rmin = _rec(n.right)
            if n.left and not n.right:                          # Case: left child only.
                return lmax + 1, lmin + 1
            if n.right and not n.left:                          # Case: right child only
                return rmax + 1, rmin + 1
            return max(lmax, rmax) + 1, min(lmin, rmin) + 1     # Case: 0 or 2 children.
        return _rec(n)

    if r:
        max_height, min_height = get_tree_max_and_min_height(r)
        return max_height - min_height <= 1


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
        print()


trees = [Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), None)),
         Node(3, Node(1, None, Node(2)), Node(5, Node(4), None)),
         Node(3, Node(1, None, Node(2)), Node(5)),
         Node(3, Node(1, None, Node(2))),
         Node(26, Node(5, Node(-37, Node(-74, Node(-86), Node(-51)), Node(-7, Node(-17))),
                          Node( 17, Node(11, Node(5)), Node(26, Node(18)))),
                  Node(74, Node(41, Node(34, Node(28)), Node(52, Node(47))),
                           Node(90, Node(88, Node(86)), Node(99, Node(95))))),
         Node(26, Node(5, Node(-37, Node(-74, Node(-86), Node(-51))),
                       Node(17, Node(11, Node(5)), Node(26, Node(18)))),
              Node(74, Node(41, Node(34, Node(28)), Node(52, Node(47))),
                   Node(90, Node(88, Node(86)), Node(99, Node(95))))),
         Node(27, Node(2, None, Node(17, Node(11, Node(5)), Node(26, Node(18)))),
                  Node(74, Node(41, Node(34, Node(28))),
                           Node(90, Node(88), Node(99, None, Node(105, None, Node(420)))))),
         Node(0),
         None]
fns = [is_balanced_tree,
       is_balanced,
       are_all_branches_balanced]

for i, t in enumerate(trees):
    print(f"\ndisplay(trees[{i}]):")
    display(t)
    print()
    for fn in fns:
        print(f"{fn.__name__}(trees[{i}]): {fn(t)}")
    print()


