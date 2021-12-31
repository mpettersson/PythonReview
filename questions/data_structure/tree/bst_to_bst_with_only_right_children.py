r"""
    BST TO BST WITH ONLY RIGHT CHILDREN (leetcode.com/problems/increasing-order-search-tree)

    Given a binary search tree, write a function that reorders/rearranges the provided bst such that each node only has
    a right child (all left children links point to None), then returns the root (of the newly reordered bst).

    Consider the following tree:

               5
            /    \
           3      6
         /  \      \
        2    4      8
      /           /  \
     1           7    9

    Example:
        Input = Node(5, Node(3, Node(2, Node(1)), Node(4)), Node(6, None, Node(8, Node(7), Node(9))))
        Output =
"""
import copy
import time


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for (can you use extra space)?
#   - Should the existing tree be modified?
#   - What properties does the tree have (is it balanced, is it a BST, data types, etc.)?
#   - Implement a node class, or assume one is created (if created what names were used)?


# APPROACH: Via List/Two Passes
#
# This approach first creates a list of inorder nodes, then iterates over the list to update each of the affected nodes
# pointers.
#
# Time Complexity: O(n), where n is the number of nodes in the bst.
# Space Complexity: (Always) O(n), where n is the number of nodes in the bst.
def bst_to_bst_with_only_right_children_via_list(root):

    def _rec(node):
        if node:
            _rec(node.left)
            l.append(node)
            _rec(node.right)

    if isinstance(root, Node):
        l = []
        _rec(root)
        for n in range(len(l)-1):
            l[n].left = None
            l[n].right = l[n+1]
        l[-1].left = None
        l[-1].right = None
        return l[0]


# APPROACH: Via Recursion
#
# This approach uses a single recursive pass over all off the nodes.  Each node returns the leftmost and rightmost nodes
# after the update so that the calling node (it's parent) can update accordingly.
#
# Time Complexity: O(n), where n is the number of nodes in the bst.
# Space Complexity: O(n) (worst case), and O(log(n)) if balanced tree, where n is the number of nodes in the bst.
def bst_to_bst_with_only_right_children(root):

    def rec(node):
        left_most = node
        right_most = node
        if node.left:
            ll, lr = rec(node.left)
            left_most = ll
            lr.right = node
            node.left = None
        if node.right:
            rl, rr = rec(node.right)
            node.right = rl
            right_most = rr
        return left_most, right_most

    if isinstance(root, Node):
        return rec(root)[0]


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def display(node):
    def wrapper(node):
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


trees = [Node(5, Node(3, Node(2, Node(1)), Node(4)), Node(6, None, Node(8, Node(7), Node(9)))),
         None]
fns = [bst_to_bst_with_only_right_children_via_list,
       bst_to_bst_with_only_right_children]

for tree in trees:
    print(f"tree:")
    display(tree)
    for fn in fns:
        t = time.time()
        print(f"{fn.__name__}(trees):")
        display(fn(copy.deepcopy(tree)))
        print(f"took: {time.time() - t} seconds.")
    print()


