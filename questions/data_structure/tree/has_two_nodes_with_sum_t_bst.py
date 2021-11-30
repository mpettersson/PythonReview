r"""
    HAS TWO NODES WITH WITH SUM T (leetcode.com/problems/two-sum-iv-input-is-a-bst)

    Given the root of a binary search tree (BST), where each node's value is an integer, and a target value t, write a
    function that returns True if two node's values sum to t, False otherwise.

    Consider the following binary search tree:

                5
              /   \
            3      6
           / \      \
          2   4      7

    Example:
                tree = Node(5, Node(3, Node(2), Node(4)), Node(6, None, Node(7)))
        Input = tree, 9
        Output = True # either 4+5, 3+6, or 2+7

"""
from collections import deque


# APPROACH: Naive Via Inorder Traversal & Two Pointers Search
#
# Compile a list of values via an inorder traversal, then check for two list values with a sum of t via the two pointer
# approach.
#
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(n), where n is the number of nodes in the tree.
def has_two_nodes_with_sum_t_bst_naive(root, t):

    def _inorder_traversal(node):
        if node is None:
            return []
        return _inorder_traversal(node.left) + [node.value] + _inorder_traversal(node.right)

    def _has_two_sum(l, t):
        lo = 0
        hi = len(l) - 1
        while lo < hi:
            if l[lo] + l[hi] == t:
                return True
            if l[lo] + l[hi] > t:
                hi -= 1
            else:
                lo += 1
        return False

    return _has_two_sum(_inorder_traversal(root), t)


# APPROACH: (Optimal) Via BFS & Set
#
# Perform a BFS, where each node's value is first checked against a set of complement values (to allow for EARLY
# TERMINATION), if not found, the complement of its value is added to the set, then both of its children are added to
# the (BFS) queue.  If a complement value is never matched, and the queue is depleted, return False.
#
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(n), where n is the number of nodes in the tree.
#
# NOTE: Despite the same asymptotic time (as the naive approach), this approach can terminate early (UNLIKE above).
def has_two_nodes_with_sum_t_bst(root, t):
    q = deque()
    q.append(root)
    complements = set()
    while q:
        node = q.popleft()
        if node.val in complements:
            return True
        complements.add(t - node.value)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
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
        for line in lines:
            print(line)


args = [([-1, 7, 9, 16], Node(5, Node(3, Node(2), Node(4)), Node(6, None, Node(7)))),
        ([-6, 7, 16, 22], Node(10, Node(5, Node(3, Node(4), Node(-2)), Node(2, None, Node(-1))),
                                   Node(-3, None, Node(7, None, Node(11)))))]
fns = [has_two_nodes_with_sum_t_bst_naive]

for t_vals, tree in args:
    print("\ndisplay(tree): ")
    display(tree)
    print()
    for t in t_vals:
        for fn in fns:
            print(f"{fn.__name__}(tree, {t}): {fn(tree, t)}")
        if len(fns) > 1:
            print()


