r"""
    LOWEST COMMON ANCESTOR BST

    Create a function takes the root of a binary search tree and two nodes, then returns the lowest common ancestor of
    the two nodes, None otherwise.  A tree is considered a BST, if for each node in the tree, the property
    "all left descendants <= node < all right descendants" is true.

    Consider the following BST:

              5
            /   \
           1     6
         /  \
        0    3
            / \
           2   4

    Example:
                my_bst = Node(5, Node(1, Node(4), Node(6, Node(5), Node(0))), Node(2))  # or, the BST above.
                node_4 = my_bst.left.left
                node_5 = my_bst.left.right.left
        Input = my_bst, node_4, node_5
        Output = 3  # that is, the node with value three

    Variations:
        - SEE: lowest_common_ancestor.py
        - Same question, however, the BST property is now: "all left descendants <= node <= all right descendants".
"""


# Naive Two Path Approach:  This may, or may not, fulfil the interviewers space requirements, ask them.
# Time Complexity: O(n), where n is the number of nodes in n_1 and n_2's tree(s).
# Space Complexity: O(max(h_1, h_2)), where h_1 and h_2 are the heights of n_1 and n_2 (O(log(n)) in the worst case).
#
# NOTE: Although this has the same time/space complexity as the other approaches, this approach visits each node in the
# paths to n_1 and n_2 TWICE, in the worst case.
def least_common_ancestor_bst_naive(root, n_1, n_2):

    def _get_path_to_node_bst_rec(root, n):
        if root is n:
            return [root]
        if n.value <= root.value and root.left:
            path = _get_path_to_node_bst_rec(root.left, n)
            if path:
                return path + [root]
        if n.value > root.value and root.right:
            path = _get_path_to_node_bst_rec(root.right, n)
            if path:
                return path + [root]

    if root and n_1 and n_2:
        lca = None
        p_1 = _get_path_to_node_bst_rec(root, n_1)
        p_2 = _get_path_to_node_bst_rec(root, n_2)
        while p_1 and p_2:
            m_1 = p_1.pop()
            m_2 = p_2.pop()
            if m_1 == m_2:
                lca = m_1
            else:
                break
        return lca


# Recursive Approach: First verify that both nodes are descendants of the root (if not, return None), then, using the
# BST property, recurse down until either: one of the two nodes is reached, OR one node's value is on the root's left
# and the other node's value is on root's right.
# Time Complexity: O(n) where n is the number of nodes in the tree.
# Space Complexity: O(max(h_1, h_2)), where h_1 and h_2 are the heights of n_1 and n_2 (O(log(n)) in the worst case).
#
# NOTE: Although this has the same time/space complexity as the other approaches, this approach visits each node in the
# paths to n_1 and n_2 TWICE, in the worst case.
def lowest_common_ancestor_bst_rec(root, n_1, n_2):

    def _is_descendant_bst_rec(root, n):
        if root is not None:
            if n is root:
                return True
            if root.left and n.value <= root.value:
                return _is_descendant_bst_rec(root.left, n)
            if root.right and n.value > root.value:
                return _is_descendant_bst_rec(root.right, n)
        return False

    def _lowest_common_ancestor_bst_rec(root, n_1, n_2):
        if root is n_1 or root is n_2 or n_1.value <= root.value < n_2.value or n_2.value <= root.value < n_1.value:
            return root
        if n_1.value <= root.value and n_2.value <= root.value:
            return _lowest_common_ancestor_bst_rec(root.left, n_1, n_2)
        if root.value < n_1.value and root.value < n_2.value:
            return _lowest_common_ancestor_bst_rec(root.right, n_1, n_2)

    if root and n_1 and n_2 and _is_descendant_bst_rec(root, n_1) and _is_descendant_bst_rec(root, n_2):
        return _lowest_common_ancestor_bst_rec(root, n_1, n_2)


# Optimal Recursive Approach: Tracking which nodes have been found in a tuple (lca_applicant, has_n_1, has_n_2), recurse
# from root, only on children that may lead to the nodes, then collate results  and return.
# Time Complexity: O(n) where n is the number of nodes in the tree.
# Space Complexity: O(max(h_1, h_2)), where h_1 and h_2 are the heights of n_1 and n_2 (with a worst case of O(n) if n_1
# or n_2 is not a node in the tree).
#
# NOTE: Although this has the same time/space complexity as the other approaches, this approach visits each node in the
# paths to n_1 and n_2 only ONCE.
def lowest_common_ancestor_bst(root, n_1, n_2):

    def _lowest_common_ancestor_bst(root, n_1, n_2):
        l_res = r_res = (None, False, False)
        if root.left and (n_1.value <= root.value or n_2.value <= root.value):
            l_res = _lowest_common_ancestor_bst(root.left, n_1, n_2)
            if l_res[1] and l_res[2]:
                return l_res
        if root.right and (root.value < n_1.value or root.value < n_2.value):
            r_res = _lowest_common_ancestor_bst(root.right, n_1, n_2)
            if r_res[1] and r_res[2]:
                return r_res
        return root, root == n_1 or l_res[1] or r_res[1], root == n_2 or l_res[2] or r_res[2]

    if root and n_1 and n_2:
        lca_applicant, has_n_1, has_n_2 = _lowest_common_ancestor_bst(root, n_1, n_2)
        return lca_applicant if has_n_1 and has_n_2 else None


# VARIATION: Same question, however, the BST property is now: "all left descendants <= node <= all right descendants".
#
# Observations:
#   - General:
#       - Could have a full bst (all nodes have two children, except leaves) with all one value.
#   - The two path approach:
#       - Same time/space complexity.
#       - Only change is in the function to build the path.
#   - The recursive case:
#       - A duplicate value is no longer guaranteed to be on the left, therefore, must check two paths.


# Alternate BST Property Naive/Two Path Approach:  Only difference from above is while path construction; the decision
# to go left or right is no longer mutually exclusive. This may, or may not, fulfil the interviewers space requirements,
# ask them.
# Time Complexity: O(n), where n is the number of nodes in n_1 and n_2's trees.
# Space Complexity: O(max(h_1, h_2)), where h_1 and h_2 are the heights of n_1 and n_2 (O(n) worst case).
def least_common_ancestor_alt_bst_property_naive(root, n_1, n_2):

    def _get_path_to_node_alt_bst_property(root, n):
        if root is n:
            return [root]
        l_path = r_path = None
        if n.value <= root.value and root.left:
            l_path = _get_path_to_node_alt_bst_property(root.left, n)
        if n.value >= root.value and root.right:
            r_path = _get_path_to_node_alt_bst_property(root.right, n)
        if l_path or r_path:
            return (l_path if l_path else r_path) + [root]

    if root and n_1 and n_2:
        lca = None
        p_1 = _get_path_to_node_alt_bst_property(root, n_1)
        p_2 = _get_path_to_node_alt_bst_property(root, n_2)
        while p_1 and p_2:
            m_1 = p_1.pop()
            m_2 = p_2.pop()
            if m_1 == m_2:
                lca = m_1
            else:
                break
        return lca


# Alternate BST Property Recursive Find Approach: Using the BST property, recurse down from root,
# Time Complexity: O(n) where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree ((however, the worst case space could be O(n)).
def lowest_common_ancestor_alt_bst_property(root, n_1, n_2):

    def _lowest_common_ancestor_alt_bst_property(root, n_1, n_2):
        l_res = r_res = (None, False, False)
        if root.left and (n_1.value <= root.value or n_2.value <= root.value):
            l_res = _lowest_common_ancestor_alt_bst_property(root.left, n_1, n_2)
            if l_res[1] and l_res[2]:
                return l_res
        if root.right and (n_1.value >= root.value or n_2.value >= root.value):
            r_res = _lowest_common_ancestor_alt_bst_property(root.right, n_1, n_2)
            if r_res[1] and r_res[2]:
                return r_res
        return root, root == n_1 or l_res[1] or r_res[1], root == n_2 or l_res[2] or r_res[2]

    if root and n_1 and n_2:
        lca_applicant, has_n_1, has_n_2 = _lowest_common_ancestor_alt_bst_property(root, n_1, n_2)
        return lca_applicant if has_n_1 and has_n_2 else None


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return repr(self.value)


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


tree = Node(5, Node(1, Node(0), Node(3, Node(2), Node(4))), Node(6))
args = [(tree.left.left, tree.left.right.left),                     # (0, 2)
        (tree.left.right.left, tree.left.left),                     # (2, 0)
        (tree.left, tree.right),                                    # (1, 6)
        (tree.right, tree.left),                                    # (6, 1)
        (tree.left.right, tree.left.right),                         # (3, 3)
        (tree.left.right.right, tree.right),                        # (4, 6)
        (tree.left.right.left, tree.left.right.right),              # (2, 4)
        (tree.left.right.left, Node(7)),                            # (2, 7) (7 isn't in the tree)
        (tree.right, Node(8)),                                      # (6, 8) (8 isn't in the tree)
        (Node(7), Node(8)),                                         # (7, 8) (7 and 8 isn't in the tree)
        (None, Node(7)),                                            # (None, 7) (7 isn't in the tree)
        (Node(7), None),                                            # (7, None) (7 isn't in the tree)
        (None, None)]                                               # (None, None)
fns = [least_common_ancestor_bst_naive,
       lowest_common_ancestor_bst_rec,
       lowest_common_ancestor_bst]

alt_tree = Node(3, Node(1, Node(0), Node(3, Node(3), Node(3))), Node(5, Node(3, Node(3), Node(3)), Node(6)))
alt_args = [(alt_tree.left.left, alt_tree.right.right),
            (alt_tree.left.left, alt_tree.left.right),
            (alt_tree.left, alt_tree.right),
            (alt_tree.right, alt_tree.left),
            (alt_tree.left.right.right, alt_tree.right.left.left),
            (alt_tree.left.right.left, alt_tree.right.left.right),
            (alt_tree.right.left.left, alt_tree.right.left.right),
            (alt_tree.left.right.right, alt_tree.left.right.right),
            (alt_tree.right.left.left, Node(7)),
            (alt_tree.left.right.left, Node(8)),
            (Node(7), Node(8)),
            (None, Node(7)),
            (Node(7), None),
            (None, None)]
alt_fns = [least_common_ancestor_alt_bst_property_naive,
           lowest_common_ancestor_alt_bst_property]

print(f"display(tree):")
display(tree)
for fn in fns:
    for n_1, n_2 in args:
        print(f"{fn.__name__}(tree, {n_1}, {n_2}):", fn(tree, n_1, n_2))
    print()

print(f"display(alt_tree):")
display(alt_tree)
for fn in alt_fns:
    for n_1, n_2 in alt_args:
        print(f"{fn.__name__}(alt_tree, {n_1}, {n_2}): {fn(alt_tree, n_1, n_2)}")
    print()


