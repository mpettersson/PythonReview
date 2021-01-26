r"""
    TREE FROM INORDER AND POSTORDER TRAVERSAL

    Write a function that can build and return a binary tree when given the inorder and postorder traversal values of
    the binary tree.  Assume that there are no duplicate values in the binary tree.

    Consider the following binary tree:

              8
            /   \
           2     3
         /  \     \
        6    5     4
            /       \
           1         7
                    /
                   9

    Example:
                inorder_values =  [6, 2, 1, 5, 8, 3, 4, 9, 7]
                postorder_values = [6, 1, 5, 2, 9, 7, 4, 3, 8]
        Input = inorder_values, postorder_values
        Output = Node(8, Node(2, Node(6), Node(5, Node(1))), Node(3, None, Node(4, None, Node(7, Node(9)))))

    Variations:
        - Given l, a list of n distinct ints where the index of the max element of l is m, write a function max_tree(l)
          that builds and returns a binary tree on the elements of l in which the root contains the max element of l,
          the left child is the max_tree(l[:m]) and the right child is max_tree(l[m+1:n]).
"""


# Brute Force Approach:  For each permutations of a tree with the given values; return True if an inorder and postorder
# traversals equal the provided traversals.
# Time Complexity: O((2n choose n)/(n+1)), where n is the number of distinct values.
# Space Complexity: Depends on implementation.
#
# NOTE:  The number of permutations of a binary tree with n distinct nodes is (2n choose n)/(n+1); this is impractical
# to code.


# Recursive Slice Approach:  Create a node with the first value of the postorder values, set the right/left children
# equal to the result of calling the (recursive) function on the corresponding slices/portions of the inorder and
# postorder value lists.
# Time Complexity: O(n**2), where n is the number of values in the tree (due to the .index() calls).
# Space Complexity: O(2h), which reduces to O(h), where h is the height of the tree (2h bc slicing/duplicating lists).
def tree_from_inorder_and_postorder_list_vals_naive_slice(inorder_vals, postorder_vals):
    if inorder_vals and postorder_vals and len(inorder_vals) is len(postorder_vals):
        idx = inorder_vals.index(postorder_vals[-1])
        l_tree = tree_from_inorder_and_postorder_list_vals_naive_slice(inorder_vals[:idx], postorder_vals[:idx])
        r_tree = tree_from_inorder_and_postorder_list_vals_naive_slice(inorder_vals[idx + 1:], postorder_vals[idx:-1])
        return Node(postorder_vals[-1], l_tree, r_tree)


# NOTE: When using referenced indexes it is VERY easy to be off; using a left/right SIZE var/offset really helps!!!


# Recursive Approach: This is similar to above, with the only difference being list reuse (not slicing).
# Time Complexity: O(n**2), where n is the number of values in the tree (due to the .index() calls).
# Space Complexity: O(h), where h is the height of the tree.
def tree_from_inorder_and_postorder_list_values_naive(inorder_values, postorder_values):

    def _tree_from_inorder_and_postorder_list_values_naive(i_values, i_start, i_end, p_values, p_start, p_end):
        if p_start is p_end and i_start is i_end:
            return Node(p_values[p_end])
        if p_start < p_end and i_start < i_end:
            idx = i_values.index(p_values[p_end])
            r_size = i_end - idx
            l_tree = _tree_from_inorder_and_postorder_list_values_naive(i_values, i_start, idx - 1,
                                                                        p_values, p_start, p_end - r_size - 1)
            r_tree = _tree_from_inorder_and_postorder_list_values_naive(i_values, idx + 1, i_end,
                                                                        p_values, p_end - r_size, p_end-1)
            return Node(p_values[p_end], l_tree, r_tree)

    if inorder_values and postorder_values and len(inorder_values) is len(postorder_values):
        return _tree_from_inorder_and_postorder_list_values_naive(inorder_values, 0, len(inorder_values) - 1,
                                                                  postorder_values, 0, len(postorder_values) - 1)


# Optimal Recursive W/ Dict. Approach: This is further enhanced via the use of a dictionary to decrease time complexity.
# Time Complexity: O(n), where n is the number of values in the tree.
# Space Complexity: O(n + h), where n and h are the number of values and the height of the tree (n is due to the dict).
def tree_from_inorder_and_postorder_list_values_w_dict(inorder_values, postorder_values):

    def _tree_from_inorder_and_postorder_list_values_w_dict(i_values, i_start, i_end, i_dict, p_values, p_start, p_end):
        if p_start is p_end and i_start is i_end:
            return Node(p_values[p_end])
        if p_start < p_end and i_start < i_end:
            idx = i_dict[p_values[p_end]]
            r_size = i_end - idx
            l_tree = _tree_from_inorder_and_postorder_list_values_w_dict(i_values, i_start, idx - 1, i_dict,
                                                                         p_values, p_start, p_end - r_size - 1)
            r_tree = _tree_from_inorder_and_postorder_list_values_w_dict(i_values, idx + 1, i_end, i_dict,
                                                                         p_values, p_end - r_size, p_end-1)
            return Node(p_values[p_end], l_tree, r_tree)

    if inorder_values and postorder_values and len(inorder_values) is len(postorder_values):
        inorder_map = {k: i for i, k in enumerate(inorder_values)}
        return _tree_from_inorder_and_postorder_list_values_w_dict(inorder_values, 0, len(inorder_values) - 1,
                                                                   inorder_map,
                                                                   postorder_values, 0, len(postorder_values) - 1)


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return repr(self.value)

    def equals(self, root):
        if root and root.value == self.value:
            left_equals = (self.left.equals(root.left) if root.left else False) if self.left else (not root.left)
            right_equals = (self.right.equals(root.right) if root.right else False) if self.right else (not root.right)
            return left_equals and right_equals
        return False


def get_inorder_traversal_values(root):
    def _get_inorder_traversal_values(root, result):
        if root:
            _get_inorder_traversal_values(root.left, result)
            result.append(root.value)
            _get_inorder_traversal_values(root.right, result)
    if root:
        result = []
        _get_inorder_traversal_values(root, result)
        return result


def get_postorder_traversal_values(root):
    def _get_postorder_traversal_values(root, result):
        if root:
            _get_postorder_traversal_values(root.left, result)
            _get_postorder_traversal_values(root.right, result)
            result.append(root.value)
    if root:
        result = []
        _get_postorder_traversal_values(root, result)
        return result


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


trees = [Node(0),
         Node(0, None, Node(1)),
         Node(1, Node(0)),
         Node(8, Node(2, Node(6), Node(5, Node(1))), Node(3, None, Node(4, None, Node(7, Node(9))))),
         Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4))),
         Node(1, Node(3, Node(4), Node(6, Node(5), Node(0))), Node(2)),
         Node(3, Node(1, None, Node(2)), Node(5, Node(4))),
         Node(3, Node(1, Node(0)), Node(5, None, Node(6))),
         Node(4, Node(1, Node(0), Node(3)), Node(2)),
         Node(4, Node(1, Node(0), Node(2)), Node(5, Node(3), Node(6))),
         Node(0, Node(1, Node(2))),
         Node(0, Node(1), Node(3, Node(2), Node(4))),
         Node(27, Node(5, Node(-37, Node(-74, Node(-86), Node(-51)), Node(-7, Node(-17))),
                       Node(17, Node(11), Node(26, Node(18)))),
              Node(74, Node(41, Node(34, Node(28)), Node(52, Node(47))),
                   Node(90, Node(88, Node(86)), Node(99, Node(95))))),
         Node(27, Node(2, None, Node(17, Node(11, Node(5)), Node(26, Node(18)))),
              Node(74, Node(41, Node(34, Node(28))),
                   Node(90, Node(88), Node(99, None, Node(105, None, Node(420)))))),
         Node(27, Node(74, Node(90, Node(99, Node(105, Node(420))), Node(88)),
                       Node(41, None, Node(34, None, Node(28)))),
              Node(2, Node(17, Node(26, None, Node(18)), Node(11, None, Node(5)))))]
fns = [tree_from_inorder_and_postorder_list_vals_naive_slice,
       tree_from_inorder_and_postorder_list_values_naive,
       tree_from_inorder_and_postorder_list_values_w_dict]

for i, tree in enumerate(trees):
    print(f"trees[{i}]:")
    display(tree)
    inorder_values = get_inorder_traversal_values(tree)
    postorder_values = get_postorder_traversal_values(tree)
    print(f"inorder_values: {inorder_values}")
    print(f"postorder_values: {postorder_values}\n")
    for fn in fns:
        print(f"{fn.__name__}(inorder_values, postorder_values).equals(tree):",
              fn(inorder_values, postorder_values).equals(tree))
    print()


