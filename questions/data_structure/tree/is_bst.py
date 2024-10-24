r"""
    IS BST  (CCI 4.5: VALIDATE BST,
             leetcode.com/problems/validate-binary-search-tree,
             50CIQ 25: BINARY SEARCH TREE VERIFICATION)

    Write a function, that when given the root of a binary tree, returns True if the tree is a Binary Search Tree (BST),
    false otherwise.  For a binary tree to be a BST, the property 'all left descendants <= node < all right descendants'
    is true for each node.

    Consider the following binary trees:

             3                   4                  4                 3               3         3
           /   \               /  \               /  \              /  \             /           \
          1     5             1    2            1    5             1    5           3             3
         / \   / \           / \              / \   / \           / \  / \
        0  2  4   6         0   3            0  2  3   6         0  3  3  6

    Example:
        Input = Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), Node(6)))  # or, the first example tree above
        Output = True

    Variations:
        - Same question, however, the BST property is now: 'all left descendants <= node <= all right descendants'.
        - Same question, however, the BST property is now: 'all left descendants < node < all right descendants'.
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for (does implicit stack space count)?
#   - Clarify the BST definition (there are several variations)?
#   - What data types will the tree contain (if, for example strings, then how would they be compared)?


# APPROACH: Recursive Max/Min
#
# Recursively check the (current) nodes value with the supplied max/min value.  If at any time the current nodes value
# is greater than the max or less than or equal to the minimum value, return False.  Recurse and return the logical and
# for both children.  The base case is that the node is None; True is returned.
#
# NOTE: The key with this question is passing down a max and a min value, where the max is used for the left children
#       and the min is used for the right children.
#
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h) where h is the height of the tree (or, O(log(n)) where n is the number of nodes in the tree).
def is_bst(root):

    def _rec(n, _max=None, _min=None):
        if n is None:
            return True
        if _max is not None and n.value > _max:
            return False
        if _min is not None and n.value <= _min:
            return False
        return _rec(n.left, n.value, _min) and _rec(n.right, _max, n.value)

    if root:
        return _rec(root)


# VARIATION: Alternate BST Property: 'all left descendants <= node <= all right descendants'.


# VARIATION APPROACH: Alternate BST Property In-Order Traversal
#
# This approach simply executes an in-order traversal of the tree comparing values along the way, if a smaller value is
# ever encountered then a False is returned, True otherwise.
#
# NOTE: This approach DOESN'T work for the 'standard' def: "all left descendants <= node < all right descendants"!
#
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h) where h is the height of the tree (or, O(log(n)) where n is the number of nodes in the tree).
def is_alt_prop_bst_via_gen(root):

    def gen_inorder_values(n):
        if n.left:
            yield from gen_inorder_values(n.left)
        yield n.value
        if n.right:
            yield from gen_inorder_values(n.right)

    if root:
        vals = gen_inorder_values(root)
        prev = next(vals)
        while True:
            curr = next(vals, None)
            if curr is None:
                break
            if prev > curr:
                return False
            prev = curr
        return True


# VARIATION APPROACH: BST Property Max/Min
#
# This approach is exactly the same as the approach for the original question; only one comparison was changed.
#
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h) where h is the height of the tree (or, O(log(n)) where n is the number of nodes in the tree).
def is_alt_prop_bst(root):

    def _rec(n, _max, _min):
        if n is None:
            return True
        if _max is not None and n.value > _max:
            return False
        if _min is not None and n.value < _min:  # This is the only variation difference (original question uses <=).
            return False
        return _rec(n.left, n.value, _min) and _rec(n.right, _max, n.value)

    if root:
        return _rec(root, None, None)


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
        print()
    else:
        print(None, "\n")


trees = [Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), Node(6))),
         Node(4, Node(1, Node(0), Node(3)), Node(2)),
         Node(3, Node(1, None, Node(2)), Node(5, Node(4))),
         Node(3, Node(1, None, Node(2)), Node(5)),
         Node(3, Node(1, None, Node(2))),
         Node(3, Node(3)),
         Node(3, None, Node(3)),
         Node(3, Node(1, Node(0, None, Node(1, Node(0, None, Node(3)))))),
         Node(26, Node(5, Node(-37, Node(-74, Node(-86), Node(-51)), Node(-7, Node(-17))),
                          Node( 17, Node(11, Node(5)), Node(26, Node(18)))),
                  Node(74, Node(41, Node(34, Node(28)), Node(52, Node(47))),
                           Node(90, Node(88, Node(86)), Node(99, Node(95))))),
         Node(27, Node(2, None, Node(17, Node(11, Node(5)), Node(26, Node(18)))),
                  Node(74, Node(41, Node(34, Node(28))),
                           Node(90, Node(88), Node(99, None, Node(105, None, Node(420)))))),
         Node(4, Node(1, Node(0), Node(2)), Node(5, Node(3), Node(6))),
         Node(3, Node(1, Node(0), Node(3)), Node(5, Node(3), Node(6))),
         Node(4, Node(1, Node(0), Node(3)), Node(2)),
         Node(4, Node(1, Node(0), Node(2)), Node(5, Node(3), Node(6))),
         Node(0),
         None]
fns = [is_bst,                      # BST Prop: 'all left descendants <= node < all right descendants'
       is_alt_prop_bst_via_gen,     # Alt. BST Prop: 'all left descendants <= node <= all right descendants'
       is_alt_prop_bst]             # Alt. BST Prop: 'all left descendants <= node <= all right descendants'

for i, tree in enumerate(trees):
    print(f"\ntrees[{i}]:")
    display(tree)
    for fn in fns:
        print(f"{fn.__name__}(tree[{i}]): {fn(tree)}")
    print()


