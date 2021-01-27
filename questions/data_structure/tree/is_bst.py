r"""
    IS BST  (CCI 4.5: VALIDATE BST)

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


# Verbose Max/Min Approach: Track max/min values at each level; min is used to check the right child and max is used
# to check the left child.
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h) where h is the height of the tree (or, O(log(n)) where n is the number of nodes in the tree).
def is_bst_verbose(root):
    def _is_bst_verbose(node):
        if node is None:
            return None, None, None
        if node.left is None and node.right is None:
            return True, node.value, node.value
        if node.left and node.right is None:
            b, max_l, min_l = _is_bst_verbose(node.left)
            return b and (max_l <= node.value), max(max_l, node.value), min(min_l, node.value)
        if node.right and node.left is None:
            b, max_r, min_r = _is_bst_verbose(node.right)
            return b and (node.value < min_r), max(max_r, node.value), min(min_r, node.value)
        b_l, max_l, min_l = _is_bst_verbose(node.left)
        b_r, max_r, min_r = _is_bst_verbose(node.right)
        return b_l and b_r and max_l <= node.value < min_r, max(max_l, max_r, node.value), min(min_l, min_r, node.value)

    res, _, _ = _is_bst_verbose(root)
    return res


# Optimal Max/Min Approach:  Track max/min values at each level; min is used to check the right child and max is used
# to check the left child.
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h) where h is the height of the tree (or, O(log(n)) where n is the number of nodes in the tree).
def is_bst(root):

    def _is_bst(node, _min=None, _max=None):
        if node:
            if _min is not None and node.value <= _min or _max is not None and _max < node.value:
                return False
            if not _is_bst(node.left, _min, node.value) or not _is_bst(node.right, node.value, _max):
                return False
        return True

    if root:
        return _is_bst(root)


# VARIATION: Alternate BST Property: 'all left descendants <= node <= all right descendants'.


# Alternate BST Property In-Order Traversal Approach:  Compare current value to previous value along the traversal.
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h) where h is the height of the tree (or, O(log(n)) where n is the number of nodes in the tree).
def is_alt_prop_bst_via_gen(root):

    def gen_inorder_values(node):
        if node.left:
            yield from gen_inorder_values(node.left)
        yield node.value
        if node.right:
            yield from gen_inorder_values(node.right)

    if root:
        vals = gen_inorder_values(root)
        prev = next(vals)
        while True:
            curr = next(vals, None)
            if not curr:
                break
            if prev > curr:
                return False
            prev = curr
        return True


# Alternate BST Property Max/Min Approach:  Track max/min values at each level; min is used to check the right child and
# max is used to check the left child.
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h) where h is the height of the tree (or, O(log(n)) where n is the number of nodes in the tree).
def is_alt_prop_bst(node, _min=None, _max=None):
    if node:
        if _min and node.value < _min:
            return False
        if _max and _max < node.value:
            return False
        is_left_bst = is_right_bst = True
        if node.left:
            is_left_bst = is_alt_prop_bst(node.left, _min, node.value)
        if is_left_bst and node.right:
            is_right_bst = is_alt_prop_bst(node.right, node.value, _max)
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
fns = [is_bst_verbose,              # BST Prop: 'all left descendants <= node < all right descendants'
       is_bst,                      # BST Prop: 'all left descendants <= node < all right descendants'
       is_alt_prop_bst_via_gen,     # Alt. BST Prop: 'all left descendants <= node <= all right descendants'
       is_alt_prop_bst]             # Alt. BST Prop: 'all left descendants <= node <= all right descendants'

for i, tree in enumerate(trees):
    print(f"trees[{i}]:")
    display(tree)
    for fn in fns:
        print(f"{fn.__name__}(tree[{i}]): {fn(tree)}")
    print()


