r"""
    FIRST COMMON ANCESTOR (CCI 4.8)

    NOTE: For same question, but with BST ordering, SEE first_common_ancestor_bst.py/"FIRST COMMON ANCESTOR BST".

    Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree.  Avoid storing
    additional nodes in a data structure.

    NOTE: This is not necessarily a binary search tree (BST).

    Consider the following tree:

              1
            /   \
           3     2
         /  \
        4    6
            / \
           5   0

    Example:
                my_tree = Node(1, Node(3, Node(4), Node(6, Node(5), Node(0))), Node(2))
                node_4 = my_tree.left.left
                node_5 = my_tree.left.right.left
        Input = my_tree, node_4, node_5     # my_tree is the binary tree above
        Output = 3                          # that is, the node with value three
"""

# REMEMBER: On a balanced tree the height O(h) is O(log n) where n is the number of nodes in the tree; however, on an
#           unbalanced tree the worst case could be O(n).


# Parent Link Min Space Approach:  Check each of the n1 and n2 ancestor combinations, returning once a match is found.
# This has a minimal space complexity of O(1), and a time complexity of O(h1 * h2), where h1 and h2 are the heights of
# the nodes in the tree.
def first_common_ancestor_parent_link_min_space(n1, n2):
    while n1:
        n = n2
        while n:
            if n1 is n:
                return n
            n = n.parent
        n1 = n1.parent


# Parent Link Min Time Approach:  Check each of n1's ancestors to n2's ancestors, returning once a match is found.
# This has a space complexity of O(n), where n is the number of nodes in the tree, and a time complexity of O(h1 + h2),
# where h1 and h2 are the heights of the nodes in the tree.
def first_common_ancestor_parent_link_min_time(n1, n2):
    s = set()   # Set containing visited nodes.
    while n1:
        s.add(n1)
        n1 = n1.parent
    while n2:
        if n2 in s:
            return n2
        n2 = n2.parent


# Parent Link Optimal Approach: Going up the tree, check if a node, or it's sibling, covers the other node.
# This approach takes O(t) time, where t is the size of the subtree for the first common ancestor, with a worst case
# time of O(n), where n is the number of nodes in the tree.  Space complexity is O(1).
def first_common_ancestor_parent_link_optimal(root, n1, n2):
    if not covers(root, n1) or not covers(root, n2):
        return None
    elif covers(n1, n2):
        return n1
    elif covers(n2, n1):
        return n2
    sibling = get_sibling(n1)
    parent = n1.parent
    while not covers(sibling, n2):
        sibling = get_sibling(parent)
        parent = parent.parent
    return parent


def covers(root, node):
    if root:
        if root is node:
            return True
        return covers(root.left, node) or covers(root.right, node)
    return False


def get_sibling(node):
    if node and node.parent:
        return node.parent.left if node.parent.left != node else node.parent.right


# Naive (No Parent Link) Two Path Approach:  This may, or may not, fulfil the interviewers space requirements, ask them.
# Time complexity is O(n) and space complexity is O(h1 + h2), where h1 and h2 are the heights of n1 and n2 (however, the
# worst case space could be O(n)).
def first_common_ancestor_naive(root, n1, n2):
    if root and n1 and n2:
        p1 = path_to_node(root, n1)
        if p1:
            p2 = path_to_node(root, n2)
            if p2:
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
    if root.left:
        l = path_to_node(root.left, node)
        if l:
            return l + [root]
    if root.right:
        l = path_to_node(root.right, node)
        if l:
            return l + [root]


# Recursive (Non-Parent Link) Optimal Approach: Recurse down each side returning a tuple indicating the sides status, or
# returning (ancestor_node, has_n1, has_n2), then collate results from both children and return.
# Time complexity is O(n) where n is the number of nodes in the tree. Space complexity is O(h), where h is the height of
# the tree ((however, the worst case space could also be O(n)).
def first_common_ancestor(root, n1, n2):

    def wrapper(node, n1, n2):
        l_res = r_res = (None, False, False)
        if node.left:
            l_res = wrapper(node.left, n1, n2)
            if l_res[1] and l_res[2]:
                return l_res
        if node.right:
            r_res = wrapper(node.right, n1, n2)
            if r_res[1] and r_res[2]:
                return r_res
        return node, node == n1 or l_res[1] or r_res[1], node == n2 or l_res[2] or r_res[2]

    if root and n1 and n2:
        ancestor, has_n1, has_n2 = wrapper(root, n1, n2)
        return ancestor if has_n1 and has_n2 else None


class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return repr(self.value)


# Helper Function
def link_parents(t):
    if t:
        if t.left:
            t.left.parent = t
            link_parents(t.left)
        if t.right:
            t.right.parent = t
            link_parents(t.right)


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


tree = Node(1, Node(3, Node(4), Node(6, Node(5), Node(0))), Node(2))
link_parents(tree)
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

print(f"display(tree):")
display(tree)
print()

for n1, n2 in args:
    print(f"first_common_ancestor_parent_link_min_space({n1}, {n2}):", first_common_ancestor_parent_link_min_space(n1, n2))
print()

for n1, n2 in args:
    print(f"first_common_ancestor_parent_link_min_time({n1}, {n2}):", first_common_ancestor_parent_link_min_time(n1, n2))
print()

for n1, n2 in args:
    print(f"first_common_ancestor_parent_link_optimal(tree, {n1}, {n2}):", first_common_ancestor_parent_link_optimal(tree, n1, n2))
print()

for n1, n2 in args:
    print(f"first_common_ancestor_naive(tree, {n1}, {n2}):", first_common_ancestor_naive(tree, n1, n2))
print()

for n1, n2 in args:
    print(f"first_common_ancestor(tree, {n1}, {n2}):", first_common_ancestor(tree, n1, n2))


