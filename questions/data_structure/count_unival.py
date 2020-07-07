r"""
    COUNT UNIVAL

    Given a binary tree, count the number of uni-value subtrees.

    A Uni-value subtree means all nodes of the subtree have the same value

    Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

    Output: 4

    Variations of this problem could include:
        - A different sized n-ary tree (i.e., with 5 children).
        - Semi-Unival Trees; where one of the childrens values must be the same as the root.

"""


# First Approach: O(n^2) time complexity.
def count_univals_mk_1(root):
    if not root:
        return 0

    total_count = count_univals(root.left) + count_univals(root.right)

    if is_unival(root):
        total_count += 1

    return total_count


def is_unival(root):
    if not root:
        return True
    if root.left and root.left.value != root.value:
        return False
    if root.right and root.right.value != root.value:
        return False
    if is_unival(root.left) and is_unival(root.right):
        return True


# Improved Approach: O(n) time complexity.
def count_univals(root):
    total_count, is_unival = count_univals_rec(root)
    return total_count


def count_univals_rec(root):
    if not root:
        return 0, True

    left_count, is_left_unival = count_univals_rec(root.left)
    right_count, is_right_unival = count_univals_rec(root.right)
    is_unival = True

    if not is_left_unival or not is_right_unival:
        is_unival = False
    if not root.left and root.left.value != root.value:
        is_unival = False
    if not root.right and root.right.value != root.value:
        is_unival = False
    if is_unival:
        return left_count + right_count + 1, True
    else:
        return left_count + right_count, False




