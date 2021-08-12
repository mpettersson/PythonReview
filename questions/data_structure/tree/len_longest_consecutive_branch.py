r"""
    LONGEST CONSECUTIVE BRANCH (50CIQ 22: LONGEST CONSECUTIVE BRANCH)

    Write a function, which accepts the root of a binary tree, then returns the length of the longest branch of
    consecutively increasing nodes.

    Consider the following binary trees:

             0
           /   \
          1     2
         / \   / \
        1  2  1   3

    Example:
        Input = Node(0, Node(1, Node(1), Node(2)), Node(2, Node(1), Node(3)))  # or, the tree above.
        Output = 3
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Have to start at root?
#   - Have to end at a leaf?
#   - Is it monotonically increasing (can be same or greater), or is each node in the path incremented by one?


# WRONG/INCOMPLETE APPROACH: Recursive
#
# Unless the interviewer stated that a consecutive branch must start at the root and continue to a leaf, this is
# wrong.  This approach is essentially the height function with an added condition that the values must be consecutive.
# This does not continue to leaf nodes if non-consecutive values are found.  This, however, could easily be modified
# into a working solution...
#
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree.
def wrong_longest_consecutive_branch(t):
    if t is None:
        return 0
    l_res = r_res = 0
    if t.left and t.left.value - 1 == t.value:
        l_res = longest_consecutive_branch(t.left) + 1
    if t.right and t.right.value - 1 == t.value:
        r_res = longest_consecutive_branch(t.right) + 1
    return max(l_res, r_res)


# APPROACH: Recursive
#
# Observation: This question is very similar to tree height, it may help to first implement the easier solution, then
# modify it to solve the more difficult problem.  The cases are; base (None), the consecutive node value, and
# non-consecutive node value.
#
# Include the CURRENT LENGTH and PREVIOUS VALUE in the recursive call so that only a max operation is required for e
# either of the two non-base cases (either a consecutive or non-consecutive value is encountered).
#
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(log(n)), or O(h), where n is the number of noes in the tree and h is the height of the tree.
def longest_consecutive_branch(n):

    def _rec(n, prev_value, length):
        if n is None:                                       # Base Case: Return the length.
            return length
        if n.value == prev_value + 1:                       # Consecutive Value Case: Get, then return the max.
            l_len = _rec(n.left, n.value, length + 1)
            r_len = _rec(n.right, n.value, length + 1)
            return max(l_len, r_len)
        l_len = _rec(n.left, n.value, 1)                    # Non-Consecutive Value Case: Basically start over...
        r_len = _rec(n.right, n.value, 1)
        return max(l_len, r_len, length)

    if n:
        return max(_rec(n.left, n.value, 1), _rec(n.right, n.value, 1))
    return 0


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
            print("\t" + line)
    else:
        print(None)


trees = [Node(0, Node(1, Node(1), Node(2)), Node(2, Node(1), Node(3))),
         Node(0, Node(1, Node(1), Node(2)), Node(2, Node(1), Node(3))),
         Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), Node(6))),
         Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), Node(6, None, Node(7))))]
fns = [wrong_longest_consecutive_branch,
       longest_consecutive_branch]

for i, tree in enumerate(trees):
    print(f"trees[{i}]:")
    display(tree)
    for fn in fns:
        print(f"{fn.__name__}(trees[{i}]): {fn(tree)}")
    print()


