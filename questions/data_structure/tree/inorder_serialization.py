r"""
    INORDER SERIALIZATION

    A meaningful inorder serialization, or a serialization which can be used to reconstruct a unique binary tree,
    requires MORE THAN the node values and marked empty children.  That is, if only the node values and empty children
    were used then all permutations of a tree with the same set of node values would have the same serialization.

    Consider the following binary trees:

        1            1            2            3           3
         \            \          / \          /           /
          2            3        1   3        1           2
           \          /                       \         /
            3        2                         2       1

    If only node values and None (for empty children) are used for serialization, then each of the above would have the
    serialization of: [None, 1, None, 2, None, 3, None]

    Write a function which takes the root of a binary tree and returns a non-unique inorder serialization of the binary
    tree.  Use None to denote, or mark, an empty child node.

    Consider the following binary tree:

             3
           /   \
          1     5
         / \   /
        0  2  4

    Example:
        Input = Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4)))  # or, the tree above
        Output = [None, 0, None, 1, None, 2, None, 3, None, 4, None, 5, None]
"""


# Recursive Approach: Recursively append node values, or None if no Node, to a result list.
# Time Complexity: O(n) best case, O(2**(h+1)) worst case, where n & h are the number of nodes & height of the tree.
# Space Complexity: O(n) best case, O(2**(h+1)) worst case, where n & h are the number of nodes & height of the tree.
def get_inorder_serialization_rec_verbose(root):

    def _get_inorder_serialization_rec_verbose(root, result):
        if root:
            _get_inorder_serialization_rec_verbose(root.left, result)
            result.append(root.value)
            _get_inorder_serialization_rec_verbose(root.right, result)
        else:
            result.append(None)

    if root:
        result = []
        _get_inorder_serialization_rec_verbose(root, result)
        return result


# Recursive Approach: Recursively build a result list of node values, or None if no Node.
# Time Complexity: O(n) best case, O(2**(h+1)) worst case, where n & h are the number of nodes & height of the tree.
# Space Complexity: O(n) best case, O(2**(h+1)) worst case, where n & h are the number of nodes & height of the tree.
def get_inorder_serialization_rec(root):

    def _get_inorder_serialization_rec(root):
        if root:
            return _get_inorder_serialization_rec(root.left) + [root.value] + _get_inorder_serialization_rec(root.right)
        return [None]

    if root:
        return _get_inorder_serialization_rec(root)


# Iterative Approach: Using a stack in place of a recursion stack; build and return the preorder nodes, using None as a
# marker for empty children.
# Time Complexity: O(n) best case, O(2**(h+1)) worst case, where n & h are the number of nodes & height of the tree.
# Space Complexity: O(n) best case, O(2**(h+1)) worst case, where n & h are the number of nodes & height of the tree.
#
# NOTE: There are 3 DIFFERENCES in this iterative inorder traversal due to the None for empty children.
def get_inorder_serialization_iter(root):
    if root:
        result = []
        stack = []
        curr = root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                result.append(curr)     # DIFFERENCE 1: Added to 'mark' an empty child node with None.
                curr = stack.pop()
                result.append(curr)
                if curr:                # DIFFERENCE 2: Check if None marker (if it is, then just continue).
                    curr = curr.right
        result.append(None)             # DIFFERENCE 3: BC while condition, the loop exits without last/trailing None.
        return result


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return repr(self.value)


def inorder_traversal_recursive(root):
    if root:
        inorder_traversal_recursive(root.left)
        print(f" {root.value}", end="")
        inorder_traversal_recursive(root.right)


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
    else:
        print(None)


trees = [Node(1, None, Node(2, None, Node(3))),     # The first five trees have the same inorder traversal...
         Node(1, None, Node(3, Node(2))),           # The first five trees have the same inorder traversal...
         Node(2, Node(1), Node(3)),                 # The first five trees have the same inorder traversal...
         Node(3, Node(1, None, Node(2))),           # The first five trees have the same inorder traversal...
         Node(3, Node(2, Node(1))),                 # The first five trees have the same inorder traversal...
         None,
         Node(0),
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
fns = [get_inorder_serialization_rec_verbose,
       get_inorder_serialization_rec,
       get_inorder_serialization_iter]

for i, tree in enumerate(trees):
    print(f"trees[{i}]:")
    display(tree)
    print(f"(recursive inorder traversal:", end="")
    inorder_traversal_recursive(tree)
    print(")\n")
    for fn in fns:
        print(f"{fn.__name__}(tree): {fn(tree)}")
    print()


