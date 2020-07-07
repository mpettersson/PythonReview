r"""
    AVG FOR EACH LEVEL

    Given a binary tree, write a function that returns a list of numbers representing the average of each level of the
    binary tree.

    Example:

            4
           / \
          7   9
         / \   \
        10  2   6
             \
             6
            /
           2

        Input =
        Output =

"""


def avg_for_each_level(root):
    depth_values_dict = {}
    res = []
    get_values_by_depth(root, depth_values_dict)

    i = 0
    while i in depth_values_dict.keys():
        res.append(sum(depth_values_dict[i]) / len(depth_values_dict[i]))
        i += 1
    return res


def get_values_by_depth(n, vals, depth=0):
    if not n:
        return

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


bin_tree = Node(4, Node(7, Node(10), Node(2, right=Node(6, left=Node(2)))), Node(9, right=Node(6)))


print(avg_for_each_level(bin_tree))


