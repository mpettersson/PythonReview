r"""
    FIND AVG FOR EACH LEVEL (leetcode.com/problems/average-of-levels-in-binary-tree)

    Given a binary tree, write a function that returns a list of numbers representing the average of each level of the
    binary tree.

    Consider the following tree:

              4
            /  \
           7    9
         /  \    \
        10   2    6
              \
               6
              /
             2

    Example:
        Input = Node(4, Node(7, Node(10), Node(2, right=Node(6, left=Node(2)))), Node(9, right=Node(6)))    # tree above
        Output = [4.0, 8.0, 6.0, 6.0, 2.0]
"""
from collections import deque


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for (can you use extra space)?
#   - What properties does the tree have (is it balanced, is it a BST, data types, etc.)?
#   - Implement a node class, or assume one is created (if created what names were used)?


# APPROACH: Naive/DFS & Lists Of Values Per Depths
#
# This approach uses depth first search to populate a list of lists with the values for each level of the tree, then
# once all of the values have been added to the lists, each level's average is computed (and returned in a list).
#
# Time Complexity: O(n) where n is the number of nodes in the tree.
# Space Complexity: O(n) where n is the number of nodes in the tree.
def find_avg_for_each_level_dfs_naive(root):

    def _rec(n, vals, lvl=0):
        if len(vals) < lvl+1:
            vals.append([])
        vals[lvl].append(n.value)
        if n.left:
            _rec(n.left, vals, lvl + 1)
        if n.right:
            _rec(n.right, vals, lvl + 1)

    vals = []
    if root:
        _rec(root, vals)
    return [sum(vals[i])/len(vals[i]) for i in range(len(vals))]


# APPROACH: Naive/BFS & Lists Of Values Per Depths
#
# This approach uses breadth first search to populate a list of lists with the values for each level of the tree, then
# once all of the values have been added to the lists, each level's average is computed (and returned in a list).
#
# Time Complexity: O(n) where n is the number of nodes in the tree.
# Space Complexity: O(n) where n is the number of nodes in the tree.
def find_avg_for_each_level_bfs_naive(root):
    vals = []
    if root:
        q = deque()
        q.append((0, root))
        while q:
            lvl, n = q.popleft()
            if len(vals) < lvl+1:
                vals.append([])
            vals[lvl].append(n.value)
            if n.left:
                q.append((lvl+1, n.left))
            if n.right:
                q.append((lvl+1, n.right))
    return [sum(vals[i])/len(vals[i]) for i in range(len(vals))]


# APPROACH: DFS & List Of [Depth Sum, Depth Count]
#
# This approach uses depth first search to populate a list of level sum and level count pairs for each level of the
# tree, then once all of the values have been added to the lists, each levels sum is divided by the count (and returned
# in a list).
#
# Time Complexity: O(n) where n is the number of nodes in the tree.
# Space Complexity: O(h) where n is the height of the tree.
def find_avg_for_each_level_dfs(root):

    def _rec(n, vals, lvl=0):
        if len(vals) < lvl+1:
            vals.append([0, 0])
        vals[lvl][0] += n.value
        vals[lvl][1] += 1
        if n.left:
            _rec(n.left, vals, lvl + 1)
        if n.right:
            _rec(n.right, vals, lvl + 1)

    vals = []
    if root:
        _rec(root, vals)
    return [v[0]/v[1] for v in vals]


# APPROACH: BFS & Lists Of Values Per Depths
#
# This approach uses breadth first search to populate a list of lists with the values for each level of the tree, then
# once all of the values have been added to the lists, each level's average is computed (and returned in a list).
#
# Time Complexity: O(n) where n is the number of nodes in the tree.
# Space Complexity: O(h) where n is the height of the tree.
def find_avg_for_each_level_bfs(root):
    vals = []
    if root:
        q = deque()
        q.append((0, root))
        while q:
            lvl, n = q.popleft()
            if len(vals) < lvl+1:
                vals.append([0, 0])
            vals[lvl][0] += n.value
            vals[lvl][1] += 1
            if n.left:
                q.append((lvl+1, n.left))
            if n.right:
                q.append((lvl+1, n.right))
    return [v[0]/v[1] for v in vals]


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def display(node):
    def _rec(node):
        if node.right is None and node.left is None:                                        # No child.
            return [str(node.value)], len(str(node.value)), 1, len(str(node.value)) // 2
        if node.right is None:                                                              # Only left child.
            lines, n, p, x = _rec(node.left)
            u = len(str(node.value))
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + str(node.value)
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        if node.left is None:                                                               # Only right child.
            lines, n, p, x = _rec(node.right)
            u = len(str(node.value))
            first_line = str(node.value) + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        else:                                                                               # Two children.
            left, n, p, x = _rec(node.left)
            right, m, q, y = _rec(node.right)
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
        lines, _, _, _ = _rec(node)
        for line in lines:
            print(f"\t{line}")
    else:
        print(f"\tNone")
    print()


trees = [Node(4, Node(7, Node(10), Node(2, right=Node(6, left=Node(2)))), Node(9, right=Node(6))),
         Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), None)),
         Node(3, Node(1, None, Node(2)), Node(5, Node(4), None)),
         Node(3, Node(1, None, Node(2)), Node(5)),
         Node(3, Node(1, None, Node(2))),
         Node(26, Node(5, Node(-37, Node(-74, Node(-86), Node(-51)), Node(-7, Node(-17))),
                          Node( 17, Node(11, Node(5)), Node(26, Node(18)))),
                  Node(74, Node(41, Node(34, Node(28)), Node(52, Node(47))),
                           Node(90, Node(88, Node(86)), Node(99, Node(95))))),
         Node(27, Node(2, None, Node(17, Node(11, Node(5)), Node(26, Node(18)))),
                  Node(74, Node(41, Node(34, Node(28))),
                           Node(90, Node(88), Node(99, None, Node(105, None, Node(420)))))),
         Node(0),
         None]
fns = [find_avg_for_each_level_dfs_naive,
       find_avg_for_each_level_bfs_naive,
       find_avg_for_each_level_dfs,
       find_avg_for_each_level_bfs]

for tree in trees:
    print(f"\ntree:")
    display(tree)
    for fn in fns:
        print(f"{fn.__name__}(trees):", fn(tree))
    print()


