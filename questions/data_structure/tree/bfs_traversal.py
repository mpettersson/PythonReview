r"""
    BFS (BREADTH FIRST SEARCH) TRAVERSAL (50CIQ 44: TREE LEVEL ORDER)

    Write a function which takes the root of a binary tree and returns a string of nodes values in level order, or
    breadth first search order.

    Consider the following binary tree:

             1          Level: 0
           /   \
          2     3       Level: 1
         / \   / \
        4   5 6   7     Level: 2

    Example:
        Input = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))  # or, the tree above
        Output = "1 2 3 4 5 6 7"  # A string of the BFS node values.

    Variations:
        - Write a function that accepts the root of a tree and prints out the nodes of the tree in level order.
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Implement a node class, or assume one is created (if created what names were used)?
#   - Clarify the definition of a "level order"?
#   - What should be returned if root is None?


# APPROACH: BFS Via Queue
#
# Use a queue to add the values at each depth of the tree to the result list, then join and return the results list as a
# string.
#
# Time Complexity: O(n), where n are the number of nodes in the tree.
# Space Complexity: O(n), where n are the number of nodes in the tree.
def bfs_traversal(root):
    if root:
        q = [root]
        result = []
        while q:
            node = q.pop(0)
            if node:
                q.append(node.left)
                q.append(node.right)
                result.append(node.value)
        return ' '.join(map(str, result))


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


trees = [Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7))),
         Node(1, None, Node(2, None, Node(3))),
         Node(3, Node(1, None, Node(2))),
         Node(3, Node(2, Node(1))),
         Node(0),
         Node(1, Node(3, Node(4), Node(6, Node(5), Node(0))), Node(2)),
         Node(3, Node(1, Node(0)), Node(5, None, Node(6))),
         Node(27, Node(2, None, Node(17, Node(11, Node(5)), Node(26, Node(18)))),
              Node(74, Node(41, Node(34, Node(28))),
                   Node(90, Node(88), Node(99, None, Node(105, None, Node(420)))))),
         Node(26, Node(5, Node(-37, Node(-74, Node(-86), Node(-51)), Node(-7, Node(-17))),
                       Node(17, Node(11, Node(5)), Node(26, Node(18)))),
              Node(74, Node(41, Node(34, Node(28)), Node(52, Node(47))),
                   Node(90, Node(88, Node(86)), Node(99, Node(95)))))]
fns = [bfs_traversal]

for i, tree in enumerate(trees):
    print(f"trees[{i}]:")
    display(tree)
    print()
    for fn in fns:
        print(f"{fn.__name__}(tree): {fn(tree)}")
    print()


