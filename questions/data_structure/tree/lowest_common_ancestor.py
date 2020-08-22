"""
    LOWEST COMMON ANCESTOR

    Given the root of a binary tree (root) and two node values (n1 & n2), write a function that finds the lowest common
    ancestor of nodes with the supplied values.

    For example, given the root of the binary tree depicted below and the node values 4 and 5, the least common ancestor
    is the node with value 3.

              1
            /   \
           3     2
         /  \
        4    6
            / \
           5   0

    Example:
        Input = BTNode(1, BTNode(3, BTNode(4), BTNode(6, BTNode(5), BTNode(0))), BTNode(2)), 4, 5
        Output = 3
"""


# This takes O(n) time and O(log(n)) space (or, O(h) space, where h is the height of the tree).
def least_common_ancestor(root, n1, n2):
    path_to_n1 = path_to_node(root, n1)
    path_to_n2 = path_to_node(root, n2)

    lca_node = None

    while path_to_n1 and path_to_n2:
        m1 = path_to_n1.pop(-1)
        m2 = path_to_n2.pop(-1)
        if m1 == m2:
            lca_node = m1
        else:
            break

    return lca_node


def path_to_node(root, x):
    if root is None:
        return None
    if root.value == x:
        return [x]  # using a list as a stack.
    left_path = path_to_node(root.left, x)
    if left_path:
        return left_path + [root.value]
    right_path = path_to_node(root.right, x)
    if right_path:
        return right_path + [root.value]


class BTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


bin_tree_root = BTNode(1, BTNode(3, BTNode(4), BTNode(6, BTNode(5), BTNode(0))), BTNode(2))

print("least_common_ancestor(bin_tree_root, 4, 5):", least_common_ancestor(bin_tree_root, 4, 5))
print("least_common_ancestor(bin_tree_root, 2, 0):", least_common_ancestor(bin_tree_root, 2, 0))
print("least_common_ancestor(bin_tree_root, 20, 0):", least_common_ancestor(bin_tree_root, 20, 0))
print("least_common_ancestor(bin_tree_root, 0, -4):", least_common_ancestor(bin_tree_root, 0, -4))


