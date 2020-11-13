r"""
    TREE FROM POSTORDER SERIALIZATION

    Given a list with the values of a postorder serialized binary tree, write a function to produce the binary tree.

    Consider the following binary tree:

             3
           /   \
          1     5
         / \   /
        0  2  4

    Example:
        Input = [None, None, 0, None, None, 2, 1, None, None, 4, None, 5, 3]
        Output = Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4)))  # or, the tree above

    Variations:
        - Is this solvable for an inorder traversal serialization?
"""


# Recursive Approach:  Pop from the head of of the list, and if it's not None, recurse for the left then right children.
# Time Complexity: O(s), where s is the size of the list.
# Space Complexity: O(n), where n is the number of non-None values in the list.
def tree_from_postorder_serialization_rec(l):
    if l:
        value = l.pop()
        if value is not None:
            right_tree = tree_from_postorder_serialization_rec(l)
            left_tree = tree_from_postorder_serialization_rec(l)
            return Node(value, left_tree, right_tree)


# Iterative Approach:  Use a stack with tuples of nodes and boolean flag (that indicates the child that needs to be
# updated next; True is left, False is right) in place of recursion.
# Time Complexity: O(s), where s is the size of the list.
# Space Complexity: O(n), where n is the number of non-None values in the list.
def tree_from_preorder_serialization_iter(l):
    pass
    if l:
        root = Node(l.pop())
        stack = [(root, True)]  # (node, bool flag; True: go right, False go left), after going left, it won't be used.
        while l:
            value = l.pop()
            node, flag = stack.pop()
            if value is not None:
                if flag:
                    node.right = Node(value)
                    stack.append((node, False))
                    stack.append((node.right, True))
                else:
                    node.left = Node(value)
                    stack.append((node.left, True))
            elif flag:
                stack.append((node, False))
        return root


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return repr(self.value)

    def equals(self, root):
        if root and root.value == self.value:
            l_equals = (self.left.equals(root.left) if root.left else False) if self.left else (root.left is None)
            r_equals = (self.right.equals(root.right) if root.right else False) if self.right else (root.right is None)
            return l_equals and r_equals
        return False


def get_postorder_serialization(root):
    if root:
        return get_postorder_serialization(root.left) + get_postorder_serialization(root.right) + [root.value]
    return [None]


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


trees = [Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4))),
         Node(1, Node(3, Node(4), Node(6, Node(5), Node(0))), Node(2)),
         Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), Node(6))),
         Node(3, Node(1, Node(0), Node(3)), Node(5, Node(3), Node(6))),
         Node(4, Node(1, Node(0), Node(3)), Node(2)),
         Node(4, Node(1, Node(0), Node(2)), Node(5, Node(3), Node(6))),
         Node(0, Node(1, Node(2))),
         Node(0),
         Node(0, None, Node(1, None, Node(2))),
         Node(0, Node(1), Node(3, Node(2), Node(4))),
         Node(26, Node(5, Node(-37, Node(-74, Node(-86), Node(-51)), Node(-7, Node(-17))),
                       Node(17, Node(11, Node(5)), Node(26, Node(18)))),
              Node(74, Node(41, Node(34, Node(28)), Node(52, Node(47))),
                   Node(90, Node(88, Node(86)), Node(99, Node(95))))),
         Node(27, Node(2, None, Node(17, Node(11, Node(5)), Node(26, Node(18)))),
              Node(74, Node(41, Node(34, Node(28))),
                   Node(90, Node(88), Node(99, None, Node(105, None, Node(420))))))]
fns = [tree_from_postorder_serialization_rec,
       tree_from_preorder_serialization_iter]

for i, tree in enumerate(trees):
    print(f"trees[{i}]:")
    display(tree)
    print(f"Postorder Traversal:", end="")
    postorder_traversal_recursive(tree)
    postorder_serialization = get_postorder_serialization(tree)
    print(f"\npostorder_serialization: {postorder_serialization}\n")
    for fn in fns:
        print(f"{fn.__name__}(postorder_serialization).equals(tree): {fn(postorder_serialization[:]).equals(tree)}")
    print()


