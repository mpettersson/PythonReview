r"""
    LEAVES  (EPI 10.14: FORM A LINKED LIST FROM THE LEAVES OF A BINARY TREE)

    Sometimes only a binary tree's leaves are useful, or needed.  Write a function, which accepts the root of a binary
    tree, and returns a list of the leaves.  A node with no descendants (or children) is a leaf node.

    Consider the following binary tree:

             3
           /   \
          1     5
         / \
        0  2

    Example:
        Input = Node(3, Node(1, Node(0), Node(2)), Node(5))  # or, the tree above
        Output = [0, 2, 5]  # or, the nodes with values 0, 2, and 5
"""


# DFS (Recursive) Approach:  Recursively return [self] if no children, else, return a combined list of the children's
# results or (in the case of a single child, the) single child's results.
# Time Complexity: O(n), where n are the number of nodes in the tree.
# Space Complexity: O(max(h, 2**h)), where h is the height of the tree.
def get_leaves_dfs(root):
    if root:
        if not root.left and not root.right:
            return [root]
        l_leaves = get_leaves_dfs(root.left)
        r_leaves = get_leaves_dfs(root.right)
        return (l_leaves if l_leaves else []) + (r_leaves if r_leaves else [])


# BFS (Iterative) Approach:  Using a queue to search all nodes, only add a node to the results if it doesn't have
# children.  Once the queue is empty, return the results.
# Time Complexity: O(n), where n are the number of nodes in the tree.
# Space Complexity: O(max(h, 2**h)), where h is the height of the tree.
def get_leaves_bfs(root):
    if root:
        result = []
        q = [root]
        while q:
            node = q.pop(0)
            if node.left or node.right:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            else:
                result.append(node)
        return result


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
        print()
    else:
        print(None)


trees = [Node(1, None, Node(2, None, Node(3))),
         Node(1, None, Node(3, Node(2))),
         Node(2, Node(1), Node(3)),
         Node(3, Node(1, None, Node(2))),
         Node(3, Node(2, Node(1))),
         Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4))),
         Node(1, Node(3, Node(4), Node(6, Node(5), Node(0))), Node(2)),
         Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), Node(6))),
         Node(3, Node(1, Node(0), Node(3)), Node(5, Node(3), Node(6))),
         Node(4, Node(1, Node(0), Node(3)), Node(2)),
         Node(4, Node(1, Node(0), Node(2)), Node(5, Node(3), Node(6))),
         Node(0, Node(1, Node(2))),
         Node(0, Node(1), Node(3, Node(2), Node(4))),
         Node(26, Node(5, Node(-37, Node(-74, Node(-86), Node(-51)), Node(-7, Node(-17))),
                       Node(17, Node(11, Node(5)), Node(26, Node(18)))),
              Node(74, Node(41, Node(34, Node(28)), Node(52, Node(47))),
                   Node(90, Node(88, Node(86)), Node(99, Node(95))))),
         Node(27, Node(2, None, Node(17, Node(11, Node(5)), Node(26, Node(18)))),
              Node(74, Node(41, Node(34, Node(28))),
                   Node(90, Node(88), Node(99, None, Node(105, None, Node(420))))))]
fns = [get_leaves_dfs,
       get_leaves_bfs]

for tree in trees:
    print(f"trees:")
    display(tree)
    for fn in fns:
        print(f"{fn.__name__}(tree): {fn(tree)}")
    print()


