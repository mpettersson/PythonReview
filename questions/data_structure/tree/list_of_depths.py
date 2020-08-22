r"""
    LIST OF DEPTHS (CCI 4.3)

    Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you
    have a tree with depth D, you'll have D linked lists).

    Consider the following tree:

             3
           /   \
          1     5
         / \   /
        0  2  4

    Example:
        Input = Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), None))  # or, the tree above
        Output = [[3], [1, 5], [0, 2, 4]]
"""


# BFS/Iterative Approach:  Time and space complexity is O(n) where n is the number of nodes in the tree.
def list_of_depths_bfs(root):
    res = []
    q = [(root, 1)]
    while len(q) > 0:
        node, depth = q.pop(0)
        if node.left:
            q.append((node.left, depth + 1))
        if node.right:
            q.append((node.right, depth + 1))
        if len(res) < depth:
            res.append([node.value])
        else:
            res[depth - 1].append(node.value)
    return res


# DFS/Recursive Approach:  Time and space complexity is O(n) where n is the number of nodes in the tree.
def list_of_depths_dfs(root):
    def wrapper(node, level, l):
        if node:
            if len(l) < level:
                l.append([node.value])
            else:
                l[level - 1].append(node.value)
            if node.left:
                wrapper(node.left, level + 1, l)
            if node.right:
                wrapper(node.right, level + 1, l)
    res = []
    wrapper(root, 1, res)
    return res


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __iter__(self):
        if self.left:
            yield self.left
        yield self.value
        if self.right:
            yield self.right

    def __repr__(self):
        return ", ".join(map(str, self))


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


trees = [Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), None)),
         Node(26, Node(5, Node(-37, Node(-74, Node(-86), Node(-51)), Node(-7, Node(-17))),
                          Node( 17, Node(11, Node(5)), Node(26, Node(18)))),
                  Node(74, Node(41, Node(34, Node(28)), Node(52, Node(47))),
                           Node(90, Node(88, Node(86)), Node(99, Node(95))))),
         Node(27, Node(2, None, Node(17, Node(11, Node(5)), Node(26, Node(18)))),
                  Node(74, Node(41, Node(34, Node(28))),
                           Node(90, Node(88), Node(99, None, Node(105, None, Node(420)))))),
         Node(0)]

for i, t in enumerate(trees):
    print(f"display(trees[{i}]):"); display(t)
    print(f"list_of_depths_dfs(trees[{i}]):", list_of_depths_dfs(t))
    print(f"list_of_depths_bfs(trees[{i}]):", list_of_depths_bfs(t), "\n")


