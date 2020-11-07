r"""
    PATHS OF NUMBERS (CCI 4.12: PATHS WITH SUM)

    You are given a binary tree in which each node contains an integer value (which might be positive or negative).
    Design an algorithm to count the number of paths that sum to a given value.  The path does not need to start or end
    at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

    Consider the following binary tree:

               10
             /    \
            5     -3
           /  \     \
          3    2     7
         / \    \     \
        4  -2   -1    11

"""


# Brute Force/Naive Approach:  Recursively try all possible paths downwards.  Time complexity is O(n log(n)) on a
# balanced tree or O(n**2) in the worst case, where n is the number of nodes in the tree.  Space complexity is O(h)
# where, h is the height of the tree.
def paths_with_sum_naive(root, target_sum):

    def _paths_with_sum_naive(node, target_sum, curr_sum):
        if not node:
            return 0
        curr_sum += node.value
        paths = 0
        if curr_sum == target_sum:
            paths += 1
        paths += _paths_with_sum_naive(node.left, target_sum, curr_sum)
        paths += _paths_with_sum_naive(node.right, target_sum, curr_sum)
        return paths

    if not root:
        return 0
    root_paths = _paths_with_sum_naive(root, target_sum, 0)
    left_paths = paths_with_sum_naive(root.left, target_sum)
    right_paths = paths_with_sum_naive(root.right, target_sum)
    return root_paths + left_paths + right_paths


# Dictionary Approach:  This approach utilizes a dictionary where keys=<sums_of_all_possible_paths> and
# values=<if_key_value_is_in_current_path> (1 for yes, 0 for no).  At each level of the recursive calls the values are
# toggled, or updated, and used to check if there is a match.  Consider the following tree:
#
#           10
#         /    \
#        5     -3
#       /  \     \
#      3    2     7
#     / \    \     \
#    4  -2   -1    11
#
# For example, the dictionary of the tree above when visiting node -2, is:
#
#   path_dict: {0: 1, 10: 1, 15: 1, 18: 1, 22: 0, 16: 1}
#
# Notice that the key value 22 (or, the sum of the path [10, 5, 3, 4]) is 0 because node 4 is not in the path to -2.
# Moreover, the dictionary after visiting all of the nodes:
#
#   path_dict: {0: 1, 10: 0, 15: 0, 18: 0, 22: 0, 16: 0, 17: 0, 7: 0, 14: 0, 25: 0}
#
# In order to check if the current node is part of a matching path sum that DOESN'T start at the root, check if
# <current_path_sum> - <target_sum> is in the dictionary; if so, increment the count.
# Time and Space is O(n), where n are the number of nodes in the tree.
def paths_with_sum(root, target_sum):

    def _paths_with_sum(node, target_sum, running_sum, path_dict):
        if not node:
            return 0
        running_sum += node.value                                                   # Sum of all nodes in path from root
        path_dict[running_sum] = path_dict.setdefault(running_sum, 0) + 1           # Increment for this path
        previous_sum = running_sum - target_sum                                     # IF matching paths DON'T start at
        num_paths = path_dict[previous_sum] if previous_sum in path_dict else 0         # root, start w/ correct count
        num_paths += _paths_with_sum(node.left, target_sum, running_sum, path_dict)
        num_paths += _paths_with_sum(node.right, target_sum, running_sum, path_dict)
        path_dict[running_sum] -= 1                                                 # Decrement curr path for other path
        return num_paths

    if not root:
        return 0
    path_dict = {0: 1}
    return _paths_with_sum(root, target_sum, 0, path_dict)


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


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


sums = [7, 8, 9]
tree = Node(10, Node(5, Node(3, Node(4), Node(-2)), Node(2, None, Node(-1))), Node(-3, None, Node(7, None, Node(11))))

print("display(tree)")
display(tree)
print()

for s in sums:
    print(f"paths_with_sum_naive(tree, {s}): {paths_with_sum_naive(tree, s)}")
print()

for s in sums:
    print(f"paths_with_sum(tree, {s}): {paths_with_sum(tree, s)}")


