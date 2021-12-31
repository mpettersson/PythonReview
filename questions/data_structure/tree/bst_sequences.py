r"""
    BST SEQUENCES (CCI 4.9: BST SEQUENCES)

    Given the root of a binary search tree (BST) with n distinct elements, which was created by inserting each of the n
    elements one at a time, write a function to enumerate all possible insertion permutations.

    Consider the following tree:

            2
          /  \
        1     3

    Example:
        Input = Node(2, Node(1), Node(3))   # or, the tree above.
        Output = [[2, 1, 3], [2, 3, 1]]
"""
import copy


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for (can you use extra space)?
#   - Should the existing tree be modified?
#   - What properties does the tree have (is it balanced, is it a BST, data types, etc.)?
#   - Implement a node class, or assume one is created (if created what names were used)?


# APPROACH: TODO
#
# TODO
#
# Time Complexity: TODO
# Space Complexity: TODO
def bst_sequences(root):    # TODO: Add comments...

    def _weave_lists(first, second, result, prefix):
        if not first or not second:
            result.append(prefix + first + second)
        else:
            prefix.append(first.pop(0))
            _weave_lists(first, second, result, prefix)
            first.insert(0, prefix.pop())

            prefix.append(second.pop(0))
            _weave_lists(first, second, result, prefix)
            second.insert(0, prefix.pop())

    result = []
    if root is None:
        return [[]]
    l_seq = bst_sequences(root.left)
    r_seq = bst_sequences(root.right)
    for left in l_seq:
        for right in r_seq:
            weaved = []
            _weave_lists(left, right, weaved, [root.value])
            print(weaved)
            result.extend(weaved)
    return result


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def display(node):
    def _rec(node):
        if node.right is None and node.left is None:    # No child.
            return [str(node.value)], len(str(node.value)), 1, len(str(node.value)) // 2
        if node.right is None:                          # Only left child.
            lines, n, p, x = _rec(node.left)
            u = len(str(node.value))
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + str(node.value)
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        if node.left is None:                           # Only right child.
            lines, n, p, x = _rec(node.right)
            u = len(str(node.value))
            first_line = str(node.value) + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        else:                                           # Two children.
            left, n, p, x = _rec(node.left)
            right, m, q, y = _rec(node.right)
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
        lines, _, _, _ = _rec(node)
        for line in lines:
            print(f"\t{line}")
    else:
        print(f"\tNone")
    print()


trees = [Node(2, Node(1), Node(3)),
         Node(2, Node(1, Node(-1)), Node(3)),
         Node(3, Node(1, Node(0), Node(2)), Node(5)),
         Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4))),
         Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), Node(6))),
         Node(3, Node(1, Node(0, Node(-1)), Node(2)), Node(5, Node(4), Node(6))),
         Node(3, Node(1, Node(0, Node(-1)), Node(2)), Node(5, Node(4), Node(6, None, Node(9)))),
         Node(3, Node(1, Node(0, Node(-1)), Node(2)), Node(5, Node(4), Node(7, Node(6), Node(9)))),
         Node(0),
         None]
fns = [bst_sequences]

for tree in trees:
    print(f"\ntree:")
    display(tree)
    for fn in fns:
        print(f"{fn.__name__}(tree): {fn(copy.deepcopy(tree))}")
    print()


