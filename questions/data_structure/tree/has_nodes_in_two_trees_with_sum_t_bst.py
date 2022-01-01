r"""
    HAS TWO NODES WITH WITH SUM T (leetcode.com/problems/two-sum-bsts)

    Given the root of TWO binary search trees (BST) (where each node's value is an integer), and a target value t, write
    a function that returns True if there exists two nodes, ONE from each tree, with values that sum to t, False
    otherwise.

    Consider the following binary search trees:

                0              5
              /   \          /   \
            -10   10        1     7
                          /   \
                         0     2

    Example:
                tree1 = Node(0, Node(-10), Node(10))
                tree2 = Node(5, Node(1, Node(0), Node(2)), Node(7))
        Input = tree1, tree2, 12
        Output = True   # 10+2

"""
from collections import deque


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for (can you use extra space)?
#   - What properties does the tree have (balanced, is a BST, BST Definition, data types, etc.)?
#   - Implement a node class, or assume one is created (if created what names were used)?


# APPROACH: Naive Via Inorder Traversal & Has Two Sum
#
# Compile two lists of values via two inorder traversals (one for each tree), then check for two list values, where the
# values are from different lists, with a sum of t via the two pointer search approach (starting with one pointer
# pointing at the low end of one list and the other pointer pointing at the high end of the other list).
#
# Time Complexity: O(n), where n is the number of nodes in the tree with the most nodes.
# Space Complexity: O(u), where u is the number of nodes in the tree with the most unique node values.
def has_nodes_in_two_trees_with_sum_t_bst_naive(root1, root2, t):

    def _inorder_traversal(node):
        if node is None:
            return set()
        return _inorder_traversal(node.left) | {node.value} | _inorder_traversal(node.right)

    def _has_two_sum(s1, s2, t):
        if len(s2) < len(s1):
            s1, s2 = s2, s1
        for x in s1:
            if t - x in s2:
                return True
        return False

    if isinstance(root1, Node) and isinstance(root2, Node) and root1 is not root2 and isinstance(t, int):
        l1 = _inorder_traversal(root1)
        l2 = _inorder_traversal(root2)
        return _has_two_sum(l1, l2, t)
    return False


# APPROACH: (Optimal) Via BFS & Two Sets
#
# Perform a BFS, where each node's value is first checked against a set of complement values (to allow for EARLY
# TERMINATION), if not found, the complement of its value is added to the set, then both of its children are added to
# the (BFS) queue.  If a complement value is never matched, and the queue is depleted, return False.
#
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(n), where n is the number of nodes in the tree.
#
# NOTE: Despite the same asymptotic time (as the naive approach), this approach can terminate early (UNLIKE above).
def has_nodes_in_two_trees_with_sum_t_bst(root0, root1, t):
    if isinstance(root0, Node) and isinstance(root1, Node) and root0 is not root1 and isinstance(t, int):
        q = deque()
        q.extend([(0, root0), (1, root1)])              # Use an integer to distinguish the two trees.
        complements = [set(), set()]                    # Complement sets (one for each of the trees).
        while q:
            i, node = q.popleft()
            if node.value in complements[(i+1) % 2]:    # Has the complement been seen in the OTHER tree's set?
                return True
            complements[i].add(t - node.value)
            if node.left:
                q.append((i, node.left))
            if node.right:
                q.append((i, node.right))
    return False


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
        return '\t' + '\n\t'.join(lines)


trees = [Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), Node(6))),
         Node(5, Node(3, Node(2, Node(1)), Node(4)), Node(6, None, Node(8, Node(7), Node(9)))),
         Node(3, Node(1, Node(0, Node(-1)), Node(2)), Node(5, Node(4), Node(7, Node(6), Node(9)))),
         Node(10),
         None]
args = [(trees[0], trees[1], 0),
        (trees[0], trees[2], 0),
        (trees[0], trees[3], 0),
        (trees[1], trees[1], 0),
        (trees[1], trees[2], 0),
        (trees[1], trees[3], 0),
        (trees[0], trees[4], 0),
        (trees[4], trees[1], 0),
        (trees[4], trees[4], 0)]
fns = [has_nodes_in_two_trees_with_sum_t_bst_naive,
       has_nodes_in_two_trees_with_sum_t_bst]

for tree_a, tree_b, target in args:
    print(f"\ntree_a: \n{display(tree_a)}\n\ntree_b:\n{display(tree_b)}\n")
    for fn in fns:
        print(f"{fn.__name__}(tree_a, tree_b, {target}): {fn(tree_a, tree_b, target)}")
    print()


