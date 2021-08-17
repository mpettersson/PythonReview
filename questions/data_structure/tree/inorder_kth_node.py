r"""
    INORDER KTH NODE (EPI 10.9: COMPUTE THE KTH NODE IN AN INORDER TRAVERSAL)

    Given the root of a tree and an integer k, write a function which returns the kth node in an inorder traversal from
    the root.  Nodes have a left, right, value, and size field; where size is the number of nodes in the subtree
    rooted at the node.

    Consider the following binary tree:

             3
           /   \
          1     5
         / \   /
        0  2  4

    Example:
        Input = Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4))), 4  # or, the tree above
        Output = 3  # that is, the node with value 3.
"""


# NOTE: Without additional information, the kth node is TRIVIAL IN O(N) TIME; if the SIZE field wasn't expressly
#       mentioned, ask about it!!!

# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What properties does the tree have (value data types, is it balanced, is it a BST, etc.)?
#   - Are sizes, or number of children, known?
#   - Implement a node class, or assume one is created (if created what names were used)?


# APPROACH: Recursive
#
# Recursively navigate to the node the tree using the size of each of the nodes along the way. If a valid k was
# provided, there are three cases to find it:
#   (1) Recurse left if k <= left.size,
#   (2) Return root if k - left.size == 1 and,
#   (3) Recurse right if k > left.size + 1.
#
# Time Complexity: O(h), where h is the height of the tree.
# Space Complexity: O(h), where h is the height of the tree.
def get_kth_inorder_node_rec(root, k):

    def _rec(root, k):
        left_size = root.left.size if root.left else 0                  # (this'll make things easier)
        if root.left and k <= left_size:                                # (1)  k <= left.size
            return _rec(root.left, k)
        if k - left_size == 1:                                          # (2)  k - left.size == 1
            return root
        return _rec(root.right, k - left_size - 1)                      # (3)  k > left.size + 1

    if root and k is not None and 0 < k <= root.size:
        return _rec(root, k)


# APPROACH: Iterative
#
# Iteratively navigate to the node the tree using the size of each of the nodes along the way. If a valid k was
# provided, there are three cases to find it:
#   (1) Go left if k <= left.size,
#   (2) Return root if k - left.size == 1 and,
#   (3) Go right if k > left.size + 1.
#
# Time Complexity: O(h), where h is the height of the tree.
# Space Complexity: O(h), where h is the height of the tree.
def get_kth_inorder_node_iter(root, k):
    if root and k is not None and 0 < k <= root.size:
        curr = root
        while curr:
            left_size = curr.left.size if curr.left else 0              # (this'll make things easier)
            if curr.left and k <= left_size:                            # (1)  k <= left.size
                curr = curr.left
            elif k - left_size == 1:                                    # (2)  k - left.size == 1
                return curr
            else:                                                       # (3)  k > left.size + 1
                curr = curr.right
                k = k - left_size - 1


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.size = 0
        self.update_size()

    def __repr__(self):
        return repr(self.value)

    def update_size(self):
        self.size = (self.left.size if self.left else 0) + (self.right.size if self.right else 0) + 1


def inorder_traversal_recursive(root):
    if root:
        inorder_traversal_recursive(root.left)
        print(f" {root.value}", end="")
        inorder_traversal_recursive(root.right)


def display(node):
    def wrapper(node):
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


trees = [Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4))),
         Node(1, Node(3, Node(4), Node(6, Node(5), Node(0))), Node(2)),
         Node(0, Node(1, Node(2))),
         Node(26, Node(5, Node(-37, Node(-74, Node(-86), Node(-51)), Node(-7, Node(-17))),
                       Node(17, Node(11, Node(5)), Node(26, Node(18)))),
              Node(74, Node(41, Node(34, Node(28)), Node(52, Node(47))),
                   Node(90, Node(88, Node(86)), Node(99, Node(95))))),
         Node(27, Node(2, None, Node(17, Node(11, Node(5)), Node(26, Node(18)))),
              Node(74, Node(41, Node(34, Node(28))),
                   Node(90, Node(88), Node(99, None, Node(105, None, Node(420))))))]
ks = [-1, 1, 3, 4, 5, 10]
fns = [get_kth_inorder_node_rec,
       get_kth_inorder_node_iter]

for i, tree in enumerate(trees):
    print("tree:")
    display(tree)
    print(f"(inorder traversal:", end="")
    inorder_traversal_recursive(tree)
    print(")")
    for fn in fns:
        print()
        for k in ks:
            print(f"{fn.__name__}(tree, {k}):", fn(tree, k))
    print()


