r"""
    IS BALANCED (CCI  4.4: CHECK BALANCED,
                 EPI 10.1: TEST IF A BINARY TREE IS HEIGHT-BALANCED,
                 leetcode.com/problems/balanced-binary-tree)

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
#   - Implement a node class, or assume one is created (if created what names were used)?
#   - Clarify the definition of a "balanced tree" (the definition could ask for ANY branches differing in length by more
#     than one)?


# APPROACH: Naive Recursive
#
# This naive approach has a separate (recursive) function to find node height, that is called multiple (duplicate) times
# along with the actual recursive is balanced function.
#
# Time Complexity: O(n * log(n)), where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree.
def is_balanced_naive(root):

    def _height(node):
        if not node:
            return -1                           # An empty tree (node == None) has height -1
        return 1 + max(_height(node.left), _height(node.right))

    def _rec(n):
        if n is None:
            return True                         # An empty tree (node == None) is 'balanced'.
        return abs(_height(n.left) - _height(n.right)) < 2 and _rec(n.left) and _rec(n.right)

    if isinstance(root, Node):
        return _rec(root)


# APPROACH: Recursive (Via Two Return Values)
#
# This approach uses a recursive function that returns a Tuple of type (bool, int) representing a balanced tree amd the
# current height of the tree.  At each node, the function is called on both children (if the child is None, then 0 is
# returned), and the results are collated then returned up the stack.
#
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree.
def is_balanced(root):

    def _rec(n):
        if not n:
            return True, -1                 # An empty tree is balanced and has height -1
        l_res, l_height = _rec(n.left)
        if not l_res:
            return False, 0
        r_res, r_height = _rec(n.right)
        if not r_res:
            return False, 0
        return (abs(l_height - r_height) < 2), 1 + max(l_height, r_height)

    if isinstance(root, Node):
        return _rec(root)[0]


# APPROACH: Recursive (Via A Single Int Value)
#
# This approach uses a recursive function that returns an integer value representing either; and unbalanced tree (-1) or
# the height of the tree (>= 0).  At each node, both the function is called on both children (if the child is None, then
# a simple 0 is returned), and the results are collated then returned up the stack.
#
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree.
def is_balanced_alt(root):

    def _rec(n):
        if n is None:
            return 0
        l_res = _rec(n.left)
        if l_res == -1:
            return -1                               # -1 == 'unbalanced' flag
        r_res = _rec(n.right)
        if r_res == -1 or abs(l_res - r_res) > 1:
            return -1                               # -1 == 'unbalanced' flag
        return max(l_res, r_res) + 1

    if isinstance(root, Node):
        return False if _rec(root) == -1 else True


# VARIATION: Same question, however, the definition of balanced tree is now: A balanced tree is a tree such that the
#           heights of ANY two branches never differ by more than one.


# VARIATION APPROACH: Via Get Max/Min Tree Height
#
# Inorder to see if all branches, or a path from the root to a leaf, have heights that are within one of each other,
# this approach simply finds and verifies the difference of the max and min branch heights.
#
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree.
def are_all_branches_balanced(root):

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

    if isinstance(root, Node):
        max_height, min_height = get_tree_max_and_min_height(root)
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
        return '\t' + '\n\t'.join(lines) + '\n'
    else:
        return "\tNone\n"


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
fns = [is_balanced_naive,
       is_balanced,
       is_balanced_alt,
       are_all_branches_balanced]

for tree in trees:
    print(f"\ntree:\n{display(tree)}")
    for fn in fns:
        print(f"{fn.__name__}(trees): {fn(tree)}")
    print()


