r"""
    AVG FOR EACH LEVEL

    Given a binary tree, write a function that returns a list of numbers representing the average of each level of the
    binary tree.

    Consider the following tree:

              4
            /  \
           7    9
         /  \    \
        10   2    6
              \
               6
              /
             2

    Example:
        Input = Node(4, Node(7, Node(10), Node(2, right=Node(6, left=Node(2)))), Node(9, right=Node(6)))    # tree above
        Output = [4.0, 8.0, 6.0, 6.0, 2.0]
"""


# List of Depths Approach: Time and space complexity is O(n) where n is the number of nodes in the tree.
def avg_for_each_level(root):
    depth_values_dict = {}
    res = []
    get_values_by_depth(root, depth_values_dict)

    for k in depth_values_dict.keys():
        res.append(sum(depth_values_dict[k]) / len(depth_values_dict[k]))
    return res


def get_values_by_depth(n, vals, depth=0):
    if n:
        if depth not in vals.keys():
            vals[depth] = []
        vals[depth].append(n.value)
        get_values_by_depth(n.left, vals, depth + 1)
        get_values_by_depth(n.right, vals, depth + 1)


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Helper Function
def display(node):
    def wrapper(node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
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


trees = [Node(4, Node(7, Node(10), Node(2, right=Node(6, left=Node(2)))), Node(9, right=Node(6))),
         Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), None)),
         Node(3, Node(1, None, Node(2)), Node(5, Node(4), None)),
         Node(3, Node(1, None, Node(2)), Node(5)),
         Node(3, Node(1, None, Node(2))),
         Node(26, Node(5, Node(-37, Node(-74, Node(-86), Node(-51)), Node(-7, Node(-17))),
                          Node( 17, Node(11, Node(5)), Node(26, Node(18)))),
                  Node(74, Node(41, Node(34, Node(28)), Node(52, Node(47))),
                           Node(90, Node(88, Node(86)), Node(99, Node(95))))),
         Node(27, Node(2, None, Node(17, Node(11, Node(5)), Node(26, Node(18)))),
                  Node(74, Node(41, Node(34, Node(28))),
                           Node(90, Node(88), Node(99, None, Node(105, None, Node(420)))))),
         Node(0),
         None]

for i, t in enumerate(trees):
    print(f"display(trees[{i}]):"); display(t)
    print(f"avg_for_each_level(trees[{i}]):", avg_for_each_level(t), "\n")


