r"""
    LOWEST COMMON ANCESTOR (CCI 4.8: FIRST COMMON ANCESTOR,
                            EPI 10.3: COMPUTE THE LOWEST COMMON ANCESTOR IN A BINARY TREE))

    Create a function takes the root of a binary tree and two nodes, then returns the lowest common ancestor of the two
    nodes, None otherwise.

    NOTE: The binary tree may, or may NOT, be a binary search tree (BST).

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
        - SEE: lowest_common_ancestor_bst.py
        - Same question, however, nodes also have links to parent nodes.
"""


# Naive Two Path Approach:  This may, or may not, fulfil the interviewers space requirements, ask them.
# Time Complexity:  O(n), where n is the number of nodes in the tree.
# Space Complexity: O(max(h_1, h_2)), where h_1 and h_2 are the heights of n_1 and n_2 (with a worst case of O(n) if n_1
# or n_2 is not a node in the tree).
#
# NOTE: Although this has the same time/space complexity as the other approaches, this approach visits each node TWICE
# in the worst case.
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


# Recursive Optimal Approach: Recurse down each side returning a tuple indicating the sides status, or returning
# (lca, has_n_1, has_n_2), then collate results from both children and return.
# Time Complexity: O(n) where n is the number of nodes in the tree.
# Space Complexity: O(max(h_1, h_2)), where h_1 and h_2 are the heights of n_1 and n_2 (with a worst case of O(n) if n_1
# or n_2 is not a node in the tree).
#
# NOTE: Although this has the same time/space complexity as the other approaches, this approach visits each node ONCE
# in the worst case.
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


# Alternate Recursive Optimal Approach: Same as above, just returns (num_n_found, lca), where num_n_found is an int with
# values 0: None, 1: n_1 or n_2 found, and 2: both n_1 and n_2 found.
# Time Complexity: O(n) where n is the  number of nodes in the tree.
# Space Complexity: O(max(h_1, h_2)), where h_1 and h_2 are the heights of n_1 and n_2 (with a worst case of O(n) if n_1
# or n_2 is not a node in the tree).
#
# NOTE: Although this has the same time/space complexity as the other approaches, this approach visits each node ONCE
# in the worst case.
def lowest_common_ancestor_alt(root, n_1, n_2):

    def _lowest_common_ancestor_alt(root, n_1, n_2):
        if root is not None:
            left_res = _lowest_common_ancestor_alt(root.left, n_1, n_2)
            if left_res[0] is 2:
                return left_res
            right_res = _lowest_common_ancestor_alt(root.right, n_1, n_2)
            if right_res[0] is 2:
                return right_res
            num_n_found = left_res[0] + right_res[0] + int(root is n_1) + int(root is n_2)
            return num_n_found, root if num_n_found is 2 else None
        return 0, None

    if root and n_1 and n_2:
        _, lca = _lowest_common_ancestor_alt(root, n_1, n_2)
        return lca


# VARIATION: Same question, however, nodes also have links to parent nodes.


# Variation Parent Link Naive Approach:  Check each of the n_1 and n_2 ancestor combinations, returning when matched.
# Time Complexity: O(h_1 * h_2), where h_1 and h_2 are the heights of the nodes in their trees.
# Space Complexity: O(1)
def lowest_common_ancestor_parent_link_naive(root, n_1, n_2):
    while n_1:
        n = n_2
        while n:
            if n_1 is n:
                return n
            n = n.parent
        n_1 = n_1.parent


# Variation Parent Link Approach:  Check each of n_1's ancestors to n_2's ancestors, returning once a match is found.
# Time complexity: O(max(h_1, h_2)) where h_1 and h_2 are the heights of the nodes in their trees.
# Space complexity: O(n), where n is the number of nodes in the n_1 and n_2 tree(s).
def lowest_common_ancestor_parent_link_set(root, n_1, n_2):
    s = set()   # Set containing visited nodes.
    while n_1:
        s.add(n_1)
        n_1 = n_1.parent
    while n_2:
        if n_2 in s:
            return n_2
        n_2 = n_2.parent


# Variation Parent Link Optimal Approach: Going up the tree, check if a node or it's sibling is a descendant of the
# other node.
# Time complexity: O(t) time, where t is the size of the subtree for the first common ancestor, with a worst case time
# of O(n), where n is the number of nodes in n_1's tree.
# Space complexity: O(1).
def lowest_common_ancestor_parent_link(root, n_1, n_2):

    def _is_descendant(root, node):
        if root:
            while node:
                if node == root:
                    return True
                node = node.parent
        return False

    def _get_sibling(node):
        if node and node.parent:
            return node.parent.left if node.parent.left != node else node.parent.right

    if root and n_1 and n_2:
        if _is_descendant(n_1, n_2):
            return n_1
        if _is_descendant(n_2, n_1):
            return n_2
        n_1_sibling = _get_sibling(n_1)
        n_1_parent = n_1.parent
        while n_1_parent and not _is_descendant(n_1_sibling, n_2):
            n_1_sibling = _get_sibling(n_1_parent)
            n_1_parent = n_1_parent.parent
        return n_1_parent


# Variation Optimal Parent Link Alternate Approach: Get the heights of the nodes, climb the tree until both nodes are at
# the same height, then compare nodes until they are the same or are None, at which point the result is returned.
# Time complexity: O(max(h_1, h_2)), where h_1 and h_2 are the heights of the nodes in their trees.
# Space complexity: O(1).
def lowest_common_ancestor_parent_link_alt(root, n_1, n_2):

    def _get_depth(node):
        i = 0
        while node.parent:
            node = node.parent
            i += 1
        return node, i

    if root and n_1 and n_2:
        root_1, depth_1 = _get_depth(n_1)
        root_2, depth_2 = _get_depth(n_2)
        if root_1 is root_2:
            depth_diff = abs(depth_1 - depth_2)
            if depth_2 > depth_1:
                n_1, n_2 = n_2, n_1
            while depth_diff:
                n_1 = n_1.parent
                depth_diff -= 1
            while n_1 != n_2:
                n_1 = n_1.parent
                n_2 = n_2.parent
            return n_1


class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        if self.left:
            self.left.parent = self
        self.right = right
        if self.right:
            self.right.parent = self
        self.parent = parent

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
       lowest_common_ancestor_alt,
       lowest_common_ancestor_parent_link_naive,                    # Parent Link Variation
       lowest_common_ancestor_parent_link_set,                      # Parent Link Variation
       lowest_common_ancestor_parent_link,                          # Parent Link Variation
       lowest_common_ancestor_parent_link_alt]                      # Parent Link Variation

print(f"display(tree):")
display(tree)
print()

for fn in fns:
    for n_1, n_2 in args:
        print(f"{fn.__name__}(tree, {n_1}, {n_2}):", fn(tree, n_1, n_2))
    print()


