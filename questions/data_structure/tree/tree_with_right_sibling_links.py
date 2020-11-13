r"""
    TREE WITH RIGHT SIBLING LINKS  (EPI 10.16: COMPUTE THE RIGHT SIBLING TREE)

    Write a function, which when given the root of a binary tree (with a left, right, and value instance variable), will
    add a right sibling link to each of the nodes in the tree.  A right sibling link is a 'right' pointer to the next
    node at the same depth or None (see below).

    Consider the following binary tree with right sibling links:

                    19 -----------→ None    depth 0
                ⟋       ⟍
              7 --------→ 23 -----→ None    depth 1
            ⟋  ⟍        ⟋  ⟍
           3 -→ 13 ---→ 21 → 41 --→ None    depth 2
          / \   / \    / \   / \
         2-→5-→11→17-→20→22→29→42 → None    depth 3

    Example:
                tree = Node(19, Node(7, Node(3, Node(2), Node(5)), Node(13, Node(11), Node(17))),
                                Node(23, Node(21, Node(20), Node(22)), Node(41, Node(29), Node(42)))))
        Input = tree  # or, the tree above
        Output = None  # however, each node now has a right_sibling field.

    Variations:
        - Same question, however, the tree may not be a perfect binary tree.
"""
import copy


# Recursive Approach:  Recursively update children's right_sibling using parents right_sibling value.
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree.
def add_right_sibling_links_perfect_rec(root):

    def _add_right_sibling_links_to_children_rec(node):
        if node.right and node.left:
            node.right.right_sibling = node.right_sibling.left if node.right_sibling else None
            node.left.right_sibling = node.right
            _add_right_sibling_links_to_children_rec(node.right)
            _add_right_sibling_links_to_children_rec(node.left)

    if root:
        root.right_sibling = None
        _add_right_sibling_links_to_children_rec(root)


# BFS Approach:  First verify that the tree is a perfect binary tree.  Then using a queue and a BFS from right to left
# (this is important), while keeping track (via a counter) of the number of the nodes, link each node's right_sibling to
# either the previous node (in the queue), or None.  The counter starts at one and increases by one for each node, any
# node that has a count equal to a power of two will have a right_sibling value of None.  This is why a right to left
# BFS is important; the nodes with a power of two are the same nodes that will have a right_sibling of None.  This is
# more easily seen in a tree where the nodes values are replaced with value of the counter when reached by a left to
# right BFS:
#
#                   1
#               ⟋       ⟍
#             3           2
#           ⟋  ⟍        ⟋  ⟍
#          7     6      5     4
#         / \   / \    / \   / \
#        15 14 13 12  11 10  9 8
#
# The nodes with a count of 1, 2, 4, and 8 will have a right_sibling value of None, all others will have the previous
# node (in a left to right BFS).
# Time Complexity: O(n), where n are the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree.
def add_right_sibling_links_perfect_iter(root):

    def _is_perfect_and_max_height(root):
        if root:
            l_b, l_m_h = _is_perfect_and_max_height(root.left)
            r_b, r_m_h = _is_perfect_and_max_height(root.right)
            return l_b and r_b and l_m_h is r_m_h, max(l_m_h, r_m_h) + 1
        return True, -1

    is_perfect, height = _is_perfect_and_max_height(root)
    if root and is_perfect:
        next_power_of_two = 1                   # Start at 2**0, or 1.  Used to assign right_sibling to prev/None.
        counter = 0
        q = [root]
        prev = None
        while q:
            counter += 1
            node = q.pop(0)
            if node.left and node.right:        # Right-To-Left BFS for more elegant code.
                q.append(node.right)
                q.append(node.left)
            if counter is next_power_of_two:    # If node/counter is power of two;
                next_power_of_two <<= 1             # Double/Update the power of two.
                node.right_sibling = None           # Node's right_sibling is None.
            else:
                node.right_sibling = prev       # Else, node's right_sibling is the previous node (since right to left).
            prev = node


# Optimal Perfect Tree Approach:  Since the binary tree is perfect, at each level, iterate across the level adding
# right_sibling links to each of the children referencing the parents right_sibling (added the level before).
# Time Complexity: O(n), where n are the number of nodes in the tree.
# Space Complexity: O(1).
#
# NOTE: This ONLY works on perfect binary trees.
def add_right_sibling_links_perfect(root):

    def _add_right_sibling_links_to_perfect_children(node):     # This function is called once per depth < tree height.
        while node:
            node.left.right_sibling = node.right
            node.right.right_sibling = node.right_sibling.left if node.right_sibling else None
            node = node.right_sibling

    if root:
        root.right_sibling = None                               # root's right_sibling is None.
        node = root
        while node and node.left:                               # For each left node (that has a left child):
            _add_right_sibling_links_to_perfect_children(node)      # Update the level of children below the node.
            node = node.left                                        # Drop down one level, and repeat.


# VARIATION: Same question, however, the tree may not be a perfect binary tree.


# Variation BFS Approach:  This works on perfect and non-perfect binary trees.  Execute a right to left BFS on the tree,
# where, for each node in the queue, the node's depth is also tracked.  For each iteration, a node will have a
# right_sibling added with the value of the actual right sibling or None (depending on the depth).
#
#    ________
#       ｜               19          depth 0
#       ｜           ⟋       ⟍
#       ｜         7           23    depth 1
#    height 3    ⟋  ⟍         /
#       ｜       3   13       21     depth 2
#       ｜      / \    \     /
#       ｜     2   5   17   20       depth 3
#    ‾‾‾‾‾‾‾‾
#
# Time Complexity: O(n), where n are the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree.
def add_right_sibling_links_iter(root):
    if root:
        q = [(root, 0)]                             # Queue stores node AND depth.
        prev = None
        prev_depth = None
        while q:
            node, depth = q.pop(0)
            if node.right:                           # Need Right-To-Left BFS.
                q.append((node.right, depth + 1))
            if node.left:
                q.append((node.left, depth + 1))
            if depth is prev_depth:                 # If same depth:
                node.right_sibling = prev               # Node's right_sibling is the previous node.
            else:                                   # Else (a new depth):
                node.right_sibling = None               # right_sibling is None (for leftmost node at each depth)
                prev_depth = depth                      # Update height
            prev = node


# Variation Recursive Approach:  Recursively update children's right_sibling from RIGHT-to-LEFT, using a dictionary to
# track the leftmost node for any depth.
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree.
def add_right_sibling_links_rec(root):

    def _add_right_siblings_links_to_children_rec(node, depth, depth_dict):
        if node.right:
            node.right.right_sibling = depth_dict[depth] if depth in depth_dict else None
            depth_dict[depth] = node.right
            _add_right_siblings_links_to_children_rec(node.right, depth + 1, depth_dict)
        if node.left:
            node.left.right_sibling = depth_dict[depth] if depth in depth_dict else None
            depth_dict[depth] = node.left
            _add_right_siblings_links_to_children_rec(node.left, depth + 1, depth_dict)

    if root:
        depth_dict = {}
        root.right_sibling = None
        _add_right_siblings_links_to_children_rec(root, 1, depth_dict)


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return repr(self.value)


def get_bfs_vars(root):
    if root:
        q = [root]
        result = []
        while q:
            node = q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            result.append(vars(node))
        return result


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
        print(None)


perfect_trees = [Node(19, Node(7, Node(3, Node(2), Node(5)), Node(13, Node(11), Node(17))),
                      Node(23, Node(21, Node(20), Node(22)), Node(41, Node(29), Node(42)))),
                 Node(0),
                 Node(1, Node(0), Node(2)),
                 Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), Node(6))),
                 Node(4, Node(1, Node(0), Node(2)), Node(5, Node(3), Node(6))),
                 Node(27, Node(5, Node(-37, Node(-74, Node(-86), Node(-51)), Node(-7, Node(-17), Node(-8))),
                       Node(17, Node(11, Node(8), Node(13)), Node(26, Node(18), Node(27)))),
                      Node(74, Node(42, Node(34, Node(28), Node(41)), Node(52, Node(47), Node(69))),
                           Node(90, Node(88, Node(86), Node(89)), Node(99, Node(95), Node(999)))))]
alt_trees = [Node(19, Node(7, Node(3, Node(2), Node(5)), Node(13, None, Node(17))),
                  Node(23, Node(21, Node(20)))),
             Node(19, Node(7, Node(3, Node(2))), Node(23, None, Node(41, None, Node(42)))),
             Node(0, Node(1), Node(3, Node(2), Node(4)))]
fns = [add_right_sibling_links_perfect_rec,     # This just returns early on some non-perfect trees.
       add_right_sibling_links_perfect_iter,    # This checks if perfect tree first (returns early if non-perfect).
       add_right_sibling_links_perfect]         # Exception if non-perfect.
alt_fns = [add_right_sibling_links_iter,        # Works on perfect and non-perfect.
           add_right_sibling_links_rec]         # Works on perfect and non-perfect.
all_fns = fns + alt_fns

for i, tree in enumerate(perfect_trees):
    print(f"trees[{i}]:")
    display(tree)
    print(f"get_bfs_vars(tree): {get_bfs_vars(tree)}\n")
    for fn in all_fns:
        root = copy.deepcopy(tree)
        print(f"{fn.__name__}(tree): {fn(root)}")
        print(f"get_bfs_vars(tree): {get_bfs_vars(root)}")
    print()

for i, tree in enumerate(alt_trees):
    print(f"alt_trees[{i}]:")
    display(tree)
    print(f"get_bfs_vars(tree): {get_bfs_vars(tree)}\n")
    for fn in alt_fns:
        root = copy.deepcopy(tree)
        print(f"{fn.__name__}(tree): {fn(root)}")
        print(f"get_bfs_vars(tree): {get_bfs_vars(root)}")
    print()


