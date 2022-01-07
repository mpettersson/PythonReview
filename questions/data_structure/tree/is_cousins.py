r"""
    ARE/IS COUSINS (leetcode.com/problems/cousins-in-binary-tree)

    Write a function that accepts the root of a binary tree and two (binary tree) nodes n1 and n1, then return True if
    the nodes (n1 and n2) are cousins in the tree, False otherwise.  Two nodes of a binary tree are said to be cousins
    IFF they have the same depth with different parents.

    Consider the following tree:

             3
           /   \
          1     5
         / \   /
        0  2  4

    Example:
                root = Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), None))  # Or, the tree above
                x = root.left.left  # Or, the node with value 0.
                y = root.right.left  # Or, the node with value 4.
        Input = root, x, y
        Output = True
"""
from collections import deque


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What are the properties of the tree; is it binary, a BST, Complete, Balanced, Perfect, etc.?
#   - Implement a node class, or assume one is created (if created what names were used)?
#   - Do nodes have a link to their parent?
#   - Clarify the definition of "cousins"!!!


# APPROACH: Via DFS
#
# This approach uses depth first search (DFS) to find the nodes.  The calling function has a local variable (that is a
# nonlocal variable in the nested _dfs function) of type list, which contains the end result and the depth at which the
# first of the two nodes was found.  The depth of the first found node is used to limit searches (after one node is
# found) and for distinguishing siblings from cousins.
#
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(n), where n is the number of nodes in the tree.
def are_cousins_dfs(root, n1, n2):

    def _dfs(node, depth, n1, n2):
        nonlocal result
        if node is None:
            return False
        if result[1] and depth > result[1]:             # Don't go past first found node's depth.
            return False
        if node == n1 or node == n2:
            if result[1] is None:
                result[1] = depth                       # Save depth for the first node.
            return result[1] == depth                   # True IFF the second node is found at same depth.
        left = _dfs(node.left, depth+1, n1, n2)
        right = _dfs(node.right, depth+1, n1, n2)
        if left and right and result[1] != depth+1:     # result[1] != depth+1 checks n1 & n2 are cousins, NOT siblings.
            result[0] = True
        return left or right

    result = [False,                                    # result[0] == bool result (is cousin).
              None]                                     # result[1] == depth of the first found node.
    if isinstance(root, Node) and isinstance(n1, Node) and isinstance(n2, Node):
        _dfs(root, 0, n1, n2)
    return result[0]


# APPROACH: Via BFS
#
# Perform a breadth first search (BFS), where each level is searched for the two nodes; if both nodes are found in a
# level then return True, however, if only one is found return False.  If all nodes in the tree is searched, with
# neither of the nodes being found, then return False.
#
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(w), where w is the max width of the tree (or, the num of nodes at the depth with the most nodes).
def are_cousins(root, n1, n2):
    if isinstance(root, Node) and isinstance(n1, Node) and isinstance(n2, Node):
        q = deque()
        q.append(root)
        num_nodes_found = 0
        parent = {root: None}
        while len(q) > 0:
            for _ in range(len(q)):                 # Nested loop to loop over all nodes at a single depth:
                node = q.popleft()
                if node == n1 or node == n2:
                    num_nodes_found += 1
                if num_nodes_found == 2:
                    if parent[n1] == parent[n2]:
                        return False
                    return True
                if node.left:
                    parent[node.left] = node
                    q.append(node.left)
                if node.right:
                    parent[node.right] = node
                    q.append(node.right)
            if num_nodes_found == 1:
                return False
    return False


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.val = value
        self.left = left
        self.right = right

    def __iter__(self):
        if self.left:
            yield from self.left
        yield self.value
        if self.right:
            yield from self.right

    def __repr__(self):
        return ", ".join(map(str, self))


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
        return '\t' + '\n\t'.join(lines) + '\n'
    else:
        return "\tNone\n"


trees = [Node(26, Node(5, Node(-37, Node(-74, Node(-86), Node(-51)), Node(-7, Node(-17))),
                          Node( 17, Node(11, Node(5)), Node(26, Node(18)))),
                  Node(74, Node(41, Node(34, Node(28)), Node(52, Node(47))),
                           Node(90, Node(88, Node(86)), Node(99, Node(95))))),
         Node(33),
         Node(44)]
args = [(trees[0], trees[0], trees[0]),
        (trees[0], trees[0].left, trees[0].left),
        (trees[0], trees[0].left, trees[0].right),
        (trees[0], trees[0].left.left, trees[0].right.right),
        (trees[0], trees[0].left.left.left.right, trees[0].right.right.right.left),
        (trees[0], trees[0].left.right, trees[0].right.right),
        (trees[0], trees[1], trees[0].left.left.left.left),
        (trees[1], trees[2], trees[0].left.left.left.left),
        (trees[0], trees[1], trees[2])]
fns = [are_cousins_dfs,
       are_cousins]

for root, n1, n2 in args:
    print(f"\ntree:\n{display(root)}")
    for fn in fns:
        print(f"{fn.__name__}(root, {n1.value if n1 else None}, {n2.value if n2 else None}): {fn(root, n1, n2)}")
    print()


