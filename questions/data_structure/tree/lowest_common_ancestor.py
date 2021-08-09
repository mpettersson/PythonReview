r"""
    LOWEST COMMON ANCESTOR (CCI 4.8: FIRST COMMON ANCESTOR,
                            EPI 10.3: COMPUTE THE LOWEST COMMON ANCESTOR IN A BINARY TREE
                            50CIQ 18: LOWEST COMMON ANCESTOR)

    Given the root of a binary tree and two nodes, write a function that returns the lowest common ancestor of the two
    nodes, None otherwise.

    NOTE: The binary tree MAY, or MAY NOT, be a binary search tree (BST).

    Consider the following binary tree:

              1
            /   \
           3     2
         /  \
        4    6
            / \
           5   0

    Example:
                my_tree = Node(1, Node(3, Node(4), Node(6, Node(5), Node(0))), Node(2))  # or, the binary tree above.
                node_4 = my_tree.left.left
                node_5 = my_tree.left.right.left
        Input = my_tree, node_4, node_5
        Output = 3  # that is, the node with value three

    Variations:
        - SEE: lowest_common_ancestor_bst.py, and lowest_common_ancestor_parent_link.py
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What type of tree (BST, n-ary, complete, full, etc.) (if any confusion exists)?
#   - Implement the tree data structure or just the function?
#   - Will the nodes be in the same tree (and other input validation questions?
#   - What type of data will the nodes contain (this may affect some languages more than others)?


# APPROACH: Naive Compare Paths To Root
#
# This may, or may not, fulfil the interviewers space requirements; ask them. Find each of the paths from root to the
# supplied nodes.  Starting at the root (of each list) pop off the nodes one at time, maintaining the previous node
# (as the lca), until the two popped nodes are not the same.  Then return the lca.
#
# Time Complexity:  O(n), where n is the number of nodes in the tree.
# Space Complexity: O(max(h_1, h_2)), where h_1 and h_2 are the heights of n_1 and n_2 (with a worst case of O(n) if n_1
#                   or n_2 is not a node in the tree).
#
# NOTE: Although this has the same time/space complexity as the other approaches, this approach visits each node TWICE
#       in the worst case.
def lowest_common_ancestor_naive(root, n_1, n_2):

    def _get_path_to_node(root, node):
        if root is node:
            return [root]
        if root.left:
            path = _get_path_to_node(root.left, node)
            if path:
                return path + [root]
        if root.right:
            path = _get_path_to_node(root.right, node)
            if path:
                return path + [root]

    if root and n_1 and n_2:
        lca = None
        p_1 = _get_path_to_node(root, n_1)
        p_2 = _get_path_to_node(root, n_2)
        while p_1 and p_2:
            m_1 = p_1.pop()
            m_2 = p_2.pop()
            if m_1 is m_2:
                lca = m_1
            else:
                return lca


# APPROACH: Optimal Recursive 3-Tuple (Node, Flag, Flag)
#
# Starting at the root of the tree, recurse down BOTH children. Where each call returns a 3-tuple indicating that
# sides status (lca, has_n_1, has_n_2).  When BOTH children have returned the tuple, collate and return the results.
#
# Time Complexity: O(n) where n is the number of nodes in the tree.
# Space Complexity: O(max(h_1, h_2)), where h_1 and h_2 are the heights of n_1 and n_2 (with a worst case of O(n) if n_1
#                   or n_2 is not a node in the tree).
#
# NOTE: Although this has the same time/space complexity as the other approaches, this approach visits each node ONCE
#       in the worst case.
def lowest_common_ancestor(root, n_1, n_2):

    def _lowest_common_ancestor(root, n_1, n_2):
        l_res = r_res = (None, False, False)
        if root.left:
            l_res = _lowest_common_ancestor(root.left, n_1, n_2)
            if l_res[1] and l_res[2]:
                return l_res
        if root.right:
            r_res = _lowest_common_ancestor(root.right, n_1, n_2)
            if r_res[1] and r_res[2]:
                return r_res
        return root, root == n_1 or l_res[1] or r_res[1], root == n_2 or l_res[2] or r_res[2]

    if root and n_1 and n_2:
        lca, has_n_1, has_n_2 = _lowest_common_ancestor(root, n_1, n_2)
        return lca if has_n_1 and has_n_2 else None


# APPROACH: Optimal Recursive 2-Tuple (num_nodes_found, Node)
#
# Same as above, just returns (num_n_found, lca), where num_n_found is an integer representing;
#   0: No nodes found.
#   1: Either n_1 or n_2 found.
#   2: Both n_1 and n_2 found.
#
# Time Complexity: O(n) where n is the  number of nodes in the tree.
# Space Complexity: O(max(h_1, h_2)), where h_1 and h_2 are the heights of n_1 and n_2 (with a worst case of O(n) if n_1
#                   or n_2 is not a node in the tree).
#
# NOTE: Although this has the same time/space complexity as the other approaches, this approach visits each node ONCE
#       in the worst case.
def lowest_common_ancestor_alt(root, n_1, n_2):

    def _lowest_common_ancestor_alt(root, n_1, n_2):
        if root is not None:
            left_res = _lowest_common_ancestor_alt(root.left, n_1, n_2)
            if left_res[0] == 2:
                return left_res
            right_res = _lowest_common_ancestor_alt(root.right, n_1, n_2)
            if right_res[0] == 2:
                return right_res
            num_n_found = left_res[0] + right_res[0] + int(root is n_1) + int(root is n_2)
            return num_n_found, root if num_n_found == 2 else None
        return 0, None

    if root and n_1 and n_2:
        _, lca = _lowest_common_ancestor_alt(root, n_1, n_2)
        return lca


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


tree = Node(1, Node(3, Node(4), Node(6, Node(5), Node(0))), Node(2))
args = [(tree.left.left, tree.left.right.left),                     # (4, 5)
        (tree.left.right.left, tree.left.left),                     # (5, 4)
        (tree.left, tree.right),                                    # (3, 2)
        (tree.right, tree.left),                                    # (2, 3)
        (tree.left.right.right, tree.right),                        # (0, 2)
        (tree.left.right.left, tree.left.right.right),              # (5, 0)
        (tree.left.right.left, Node(7)),                            # (5, 7) (7 isn't in the tree)
        (tree.right, Node(8)),                                      # (2, 8) (8 isn't in the tree)
        (Node(7), Node(8)),                                         # (7, 8) (7 and 8 isn't in the tree)
        (None, Node(7)),                                            # (None, 7) (7 isn't in the tree)
        (Node(7), None),                                            # (7, None) (7 isn't in the tree)
        (None, None)]                                               # (None, None)
fns = [lowest_common_ancestor_naive,
       lowest_common_ancestor,
       lowest_common_ancestor_alt]

print(f"tree:")
display(tree)
print()

for n_1, n_2 in args:
    for fn in fns:
        print(f"{fn.__name__}(tree, {n_1}, {n_2}):", fn(tree, n_1, n_2))
    print()


