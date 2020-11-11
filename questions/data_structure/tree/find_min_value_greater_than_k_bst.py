r"""
    FIND MIN VALUE GREATER THAN K BST  (EPI 15.2: FIND THE FIRST KEY GREATER THAN A GIVEN VALUE IN A BST)

    Write a function, which accepts the root of a bst and a value k, then returns the minimum value in the bst greater
    than k.

    Consider the following BST:

                   19
                ⟋      ⟍
              7         43
            /  \       /   \
           3   11     23   47
         /  \   \      \    \
        2   5   17     37   53
                /     /  \
               13   29   41
                     \
                     31

    Example:
                bst = Node(19, Node(7, Node(3, Node(2), Node(5)), Node(11, None, Node(17, Node(13)))),
                      Node(43, Node(23, None, Node(37, Node(29, None, Node(31)), Node(41))), Node(47, None, Node(53))))
        Input = bst, 10
        Output = 11
"""


# Naive/Inorder Traversal Generator Approach:  Perform an inorder traversal, returning the first value greater than k.
# Time Complexity: O(n), where n is the number of nodes in the tree,
# Space Complexity: O(h), where h is the height of the tree.
def find_min_value_greater_than_k_bst_naive(t, k):
    if t and k is not None:
        it = iter(t)
        for i in it:
            if i > k:
                return i


# Recursive Approach:  If k is greater than current value, recurse right.  Else, get the result from left recursion and
# return the result if it is not None, if it is None, return the current value.
# Time Complexity: O(log(n)) if balanced tree, O(n) worst case, where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree.
def find_min_value_greater_than_k_bst_rec(root, k):
    if root and k is not None:
        if k < root.value:
            res = find_min_value_greater_than_k_bst_rec(root.left, k)
            return res if res is not None else root.value
        if k >= root.value:
            return find_min_value_greater_than_k_bst_rec(root.right, k)


# Iterative Approach:  Traverse the tree depending on the relation of k to current value, while maintaining a result
# candidate.  The result candidate is used so we don't need to traverse back (up the tree) to get the best result.
# Time Complexity: O(log(n)) if balanced tree, O(n) worst case, where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree.
def find_min_value_greater_than_k_bst_iter(root, k):
    if root and k is not None:
        curr = root
        result_candidate = curr.value
        while curr:
            if k < curr.value:
                if curr.left:
                    result_candidate = curr.value
                    curr = curr.left
                else:
                    return curr.value
            else:  # k >= curr.value
                if curr.right:
                    curr = curr.right
                else:
                    break
        return result_candidate if result_candidate > k else None


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
        return repr(self.value)


def inorder_recursive(root):
    if root:
        inorder_recursive(root.left)
        print(f" {root.value}", end="")
        inorder_recursive(root.right)


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


trees = [Node(19, Node(7, Node(3, Node(2), Node(5)), Node(11, None, Node(17, Node(13)))),
                Node(43, Node(23, None, Node(37, Node(29, None, Node(31)), Node(41))), Node(47, None, Node(53)))),
         Node(27, Node(5, Node(-37, Node(-74, Node(-86), Node(-51)), Node(-7, Node(-17))),
                       Node(17, Node(11), Node(26, Node(18)))),
              Node(74, Node(41, Node(34, Node(28)), Node(52, Node(47))),
                   Node(90, Node(88, Node(86)), Node(99, Node(95))))),
         Node(0),
         Node(3, Node(1, None, Node(2)), Node(5, Node(4)))]
args = [-86, 3, 10, -3, 53, 18, 19, 17, None]
fns = [find_min_value_greater_than_k_bst_naive,
       find_min_value_greater_than_k_bst_rec,
       find_min_value_greater_than_k_bst_iter]

for i, tree in enumerate(trees):
    print(f"trees[{i}]:")
    display(tree)
    print(f"Inorder Traversal:", end="")
    inorder_recursive(tree)
    print("\n")
    for fn in fns:
        for k in args:
            print(f"{fn.__name__}(trees[{i}], {k}):", fn(tree, k))
        print()
    print()


