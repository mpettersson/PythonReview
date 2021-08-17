r"""
    INORDER TRAVERSAL ITERATIVE   (EPI 10.7: IMPLEMENT AN INORDER TRAVERSAL WITHOUT RECURSION,
                                   50CIQ 6: INORDER TRAVERSAL)

    Write a function that takes the root of a binary tree and prints the inorder values of the nodes iteratively (that
    is, without recursion).

    Consider the following binary tree:

             3
           /   \
          1     5
         / \   /
        0  2  4

    Example:
        Input = Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4)))  # or, the tree above
        Output = 0 1 2 3 4 5
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What properties does the tree have (tree value data types, is it balanced, is it a BST, etc.)?
#   - Implement a node class, or assume one is created (if created what names were used)?


# APPROACH: Naive Via Visited Set
#
# Use a stack to maintain current node and a set to maintain visited nodes.
#
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(n), where n is the number of nodes in the tree.
def inorder_traversal_iterative_naive(root):
    if root is not None:
        stack = [root]      # Use a list as a stack; the 'top' will be the end of the list.
        visited = set()
        while stack:
            node = stack.pop()
            if node.left and node.left not in visited:
                stack.append(node)
                stack.append(node.left)
            else:
                print(f" {node.value}", end="")
                visited.add(node)
                if node.right:
                    stack.append(node.right)


# APPROACH: Via Helper Function
#
# In addition to a stack, use a separate helper function (which initially called with the root) to iteratively populate
# the stack with (the supplied node's) left descendants.  Then, while the stack is populated, pop off a node from the
# stack. print its value, and call the helper function with the (current) node's right child.
#
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree.
def inorder_traversal_iterative_via_helper(root):

    def _add_left_descendants_to_stack(s, n):
        while n:
            s.append(n)
            n = n.left

    if root is not None:
        stack = []
        _add_left_descendants_to_stack(stack, root)
        while stack:
            node = stack.pop()
            print(f" {node.value}", end="")
            _add_left_descendants_to_stack(stack, node.right)


# APPROACH: Inelegant Via State Flag
#
# Use a stack to maintain the current node and a pointer to the previous node, where the previous node is used to
# determine the action for the current node, and what to add to the stack.
#
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree.
def inorder_traversal_iterative_inelegant(root):
    if root is not None:
        stack = [(root, False)]
        while stack:
            node, been_left = stack.pop()
            if node.left and not been_left:
                stack.append((node, True))
                stack.append((node.left, False))
            else:
                print(f" {node.value}", end="")
                if node.right:
                    stack.append((node.right, False))


# APPROACH: Optimal & Elegant
#
# While the stack is populated or there is a 'current' node, do the following:  If the current node has is not None,
# push it on the stack and assign current to current's left child (could be None).  When the current node becomes None,
# pop a node from the stack to current, print the new value, and assign current to current's right child.
#
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree.
def inorder_traversal_iterative(root):
    if root is not None:
        stack = []
        curr = root
        while stack or curr:
            if curr:                                # Just push to stack and go left.
                stack.append(curr)
                curr = curr.left
            else:                                   # Or: Pop, print, and go right.
                curr = stack.pop()
                print(f" {curr.value}", end="")
                curr = curr.right


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


trees = [Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4))),
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
fns = [inorder_traversal_iterative_naive,
       inorder_traversal_iterative_via_helper,
       inorder_traversal_iterative_inelegant,
       inorder_traversal_iterative]

for i, tree in enumerate(trees):
    print(f"\ntrees[{i}]:")
    display(tree)
    print(f"(recursive inorder traversal:", end="")
    inorder_traversal_recursive(tree)
    print(")\n")
    for fn in fns:
        print(f"{fn.__name__}(tree):", end="")
        fn(tree)
        print()
    print()


