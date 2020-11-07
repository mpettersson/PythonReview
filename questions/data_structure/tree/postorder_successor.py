r"""
    POSTORDER SUCCESSOR

    Design a function that accepts a node and returns the postorder successor, or next node, of the supplied node if one
    exists, None otherwise.  In addition to left and right child node links, a node has a link to its parent node.

    Consider the following binary tree:

             3
           /   \
          1     5
         / \   /
        0  2  4

    Example:
                tree = Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4)))  # or, the tree above
        Input = tree.left
        Output = 3  # that is, the node with value 3
"""


# Iterative Parent Link Approach: The successor can be ONE of three possible values:
#   (1) Return None if the node does not have a parent.
#   (2) Return the node's parent if the node is the right child or if there is no right child.
#   (3) Return the lowest left child or lowest right child (if no left children).
# Time Complexity: O(h), where h is the height of the tree.
# Space complexity: O(1).
def get_postorder_successor(node):
    if node and node.parent:
        if not node.parent.right or node is node.parent.right:
            return node.parent
        node = node.parent.right
        while True:
            if node.left:
                while node.left:
                    node = node.left
                return node
            elif node.right:
                node = node.right
            else:
                return node


class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        if self.left:
            self.left.parent = self
        self.right = right
        if self.right:
            self.right.parent = self
        self.parent = parent

    def __repr__(self):
        return repr(self.value)


def postorder_traversal_recursive(root):
    if root:
        postorder_traversal_recursive(root.left)
        postorder_traversal_recursive(root.right)
        print(f" {root.value}", end="")


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


bin_tree = Node(26, Node(5, Node(-37, Node(-74, Node(-86), Node(-51)), Node(-7, Node(-17))),
                         Node(17, Node(11, Node(5)), Node(26, Node(18)))),
                Node(74, Node(41, Node(34, Node(28)), Node(52, Node(47))),
                         Node(90, Node(88, Node(86)), Node(99, Node(95)))))
bin_tree_nodes = [bin_tree,
                  bin_tree.left.left.left.left,
                  bin_tree.left,
                  bin_tree.right,
                  bin_tree.right.left.right,
                  bin_tree.right.right.right,
                  bin_tree.right.right.right.left,
                  bin_tree.parent]
bst = Node(27, Node(2, None, Node(17, Node(11, Node(5)), Node(26, Node(18)))),
               Node(74, Node(41, Node(34, Node(28))), Node(90, Node(88), Node(99, None, Node(105, None, Node(420))))))
bst_nodes = [bst,
             bst.left,
             bst.right,
             bst.left.right.right,
             bst.left.right.left.left,
             bst.right.left,
             bst.right.right.right.right.right,
             bst.right.right.left,
             bst.parent]
args = [(bin_tree, bin_tree_nodes), (bst, bst_nodes)]
fns = [get_postorder_successor]

for tree, nodes in args:
    print("tree:")
    display(tree)
    print(f"(postorder traversal:", end="")
    postorder_traversal_recursive(tree)
    print(")")
    for fn in fns:
        print()
        for node in nodes:
            print(f"{fn.__name__}({node}):", fn(node))
    print()


