r"""
    TREE SERIALIZATION (SEE https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

    Given a tree t, design two functions; serialize_tree(t) to serialize a provided tree and deserialize_serial_tree(l)
    to deserialize the output of serialize_tree(t), or a serialized tree.

    Consider the following tree, t:

          0
         / \
        1   3
           / \
          2   4

    Example:
        serialize_tree(t)
            Input =  Node(0, Node(1), Node(3, Node(2), Node(4)))
            Output = [0, 1, 3, None, None, 2, 4]

        deserialize_serial_tree(l)
            Input =  [0, 1, 3, None, None, 2, 4]
            Output = Node(0, Node(1), Node(3, Node(2), Node(4)))

    NOTE: This can be solved via breath first search (BFS) AND via depth first search (DFS), however, the serialized
    output will be DIFFERENT.  A BFS serialization will always have the size 2**h - 1, where h is the height of the
    tree, where the DFS serialization will have the size 2n + 1, where n is the number of nodes in the tree.
    Therefore, IF a tree is a COMPLETE binary tree then BFS will produce a shorter serialized list than DFS, however,
    if the tree is very unbalanced then DFS will produce a shorter list.
"""


# BFS Approach: Time and space complexity is O(2**h) where h is the height of the tree.
def serialize_tree_bfs(t):
    if t:
        l = []
        h = get_max_height(t)
        q = [(1, t)]
        while q:
            i, n = q.pop(0)
            if i <= h:
                l.append(n.value if n else None)
                q.append((i + 1, n.left if n else None))
                q.append((i + 1, n.right if n else None))
        return l


def get_max_height(t):
    if t is None:
        return 0
    return max(get_max_height(t.left), get_max_height(t.right)) + 1


# BFS Approach: Time and space complexity is O(2**h) where h is the height of the tree.
def deserialize_serial_tree_bfs(l):
    if l:
        r = Node(l.pop(0))
        q = [r]
        while l:
            node = q.pop(0)
            if node:
                left = l.pop(0)
                right = l.pop(0)
                node.left = None if left is None else Node(left)
                node.right = None if right is None else Node(right)
                q.extend([node.left, node.right])
            else:
                q.extend([l.pop(0), l.pop(0)])
        return r


# Pre-Order DFS Traversal/Recursive Approach:  Time and space complexity is O(n), where n is the number of nodes in the
# tree.
def serialize_tree_dfs(t):

    def _serialize_tree_dfs(n):
        if n is None:
            l.append(n)
        else:
            l.append(n.value)
            _serialize_tree_dfs(n.left)
            _serialize_tree_dfs(n.right)

    l = []
    _serialize_tree_dfs(t)
    return l


# Pre-Order DFS Traversal/Recursive Approach:  Time and space complexity is O(n), where n is the number of nodes in the
# tree.
def deserialize_serial_tree_dfs(l):
    if l:
        value = l.pop(0)
        if value is not None:
            return Node(value, deserialize_serial_tree_dfs(l), deserialize_serial_tree_dfs(l))


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __iter__(self):
        if self.left:
            yield from self.left
        yield self.value
        if self.right:
            yield from self.right

    def __repr__(self):
        return ", ".join(map(repr, self))


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


trees = [Node(0, Node(1, Node(2))),
         Node(0, Node(1), Node(3, Node(2), Node(4))),
         Node(26, Node(5, Node(-37, Node(-74, Node(-86), Node(-51)), Node(-7, Node(-17))),
                       Node(17, Node(11, Node(5)), Node(26, Node(18)))),
              Node(74, Node(41, Node(34, Node(28)), Node(52, Node(47))),
                   Node(90, Node(88, Node(86)), Node(99, Node(95))))),
         Node(27, Node(2, None, Node(17, Node(11, Node(5)), Node(26, Node(18)))),
              Node(74, Node(41, Node(34, Node(28))),
                   Node(90, Node(88), Node(99, None, Node(105, None, Node(420))))))]

for t in trees:
    print(f"display(t)")
    display(t)
    print(f"serialize_tree_bfs(t): {serialize_tree_bfs(t)}")
    print(f"serialize_tree_dfs(t): {serialize_tree_dfs(t)}")
    print(f"t:                                                  [{t}]")
    print(f"deserialize_serial_tree_bfs(serialize_tree_bfs(t)): [{deserialize_serial_tree_bfs(serialize_tree_bfs(t))}]")
    print(f"deserialize_serial_tree_dfs(serialize_tree_dfs(t)): [{deserialize_serial_tree_dfs(serialize_tree_dfs(t))}]")
    print()


