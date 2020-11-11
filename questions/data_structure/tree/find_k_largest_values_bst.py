r"""
    FIND K LARGEST VALUES BST  (EPI 15.3: FIND THE K LARGEST ELEMENTS IN A BST)

    Write a function that accepts the root of a BST, and an integer k, then returns the k largest nodes (values) of the
    BST in decreasing order.

    Consider the following BST, t:

                   19
                ⟋     ⟍
              7         43
            ⟋ ⟍        ⟋ ⟍
           3   11     23   47
         ⟋ \    \      \    \
        2   5   17     37   53
                /     /  \
               13   29   41
                     \
                     31

    Example:
        Input = t, 4
        Output = [53, 47, 43, 41]
"""


# Recursive Generator Approach:  Using a nested generator/iterator with inorder (with right-to-left) traversal function,
# create and return a result list.
# Time Complexity: O(h + k), where h is the height of the tree.
# Space Complexity: O(h + k), where h is the height of the tree.
def find_k_largest_values_bst_gen(root, k):

    def _gen_k_largest_values_bst(root):
        if root.right:
            yield from _gen_k_largest_values_bst(root.right)
        yield root.value
        if root.left:
            yield from _gen_k_largest_values_bst(root.left)

    if root and k is not None and k >= 0:
        result = []
        gen = _gen_k_largest_values_bst(root)
        for _ in range(k):
            try:
                result.append(next(gen))
            except StopIteration:
                break  # Instructions did not mention behavior if k > num nodes in bst; so just return partial list.
        return result


# Recursive Approach:  Using a nested inorder (right-to-left) traversal function, create and return a result list.
# Time Complexity: O(min(n, k)) where n is the number of nodes in the tree.
# Space is O(max(h, k)), where h is the height of the tree.
def find_k_largest_values_bst_rec(root, k):

    def _find_k_largest_values_bst_rec(t, k, result):
        if len(result) < k and t.right:
            _find_k_largest_values_bst_rec(t.right, k, result)
        if len(result) < k:
            result.append(t.value)
        if len(result) < k and t.left:
            _find_k_largest_values_bst_rec(t.left, k, result)

    if root and k is not None and k >= 0:
        result = []
        _find_k_largest_values_bst_rec(root, k, result)
        return result


# Iterator Approach:  Use a stack to implement an iterative inorder (right-to-left) traversal. While either the stack
# has a value or a pointer to the current node has a value; if the current node has a value, push it on the stack and
# update current to be the right child (could be None), if the current node doesn't have a value (is None), update the
# current node by popping from the stack, add the new current node's value to the result list then update current to
# be the left child.
# Time Complexity: O(min(n, k)) where n is the number of nodes in the tree.
# Space is O(max(h, k)), where h is the height of the tree.
def find_k_largest_values_bst_iter(root, k):
    if root and k is not None and k >= 0:
        result = []
        stack = []
        curr = root
        while (stack or curr) and len(result) < k:
            if curr:
                stack.append(curr)
                curr = curr.right
            else:
                curr = stack.pop()
                result.append(curr.value)
                curr = curr.left
        return result


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

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
         Node(3, Node(1, None, Node(2)), Node(5, Node(4)))]

args = [-5, 0, 5, 100, None]
fns = [find_k_largest_values_bst_gen,
       find_k_largest_values_bst_rec,
       find_k_largest_values_bst_iter]

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


