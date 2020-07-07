r"""
    IS BST

    Given the head of a binary tree (head), write an algorithm that returns True if the tree is a Binary Search Tree
    (BST) or false otherwise.

    For each node in a BST the property "all left descendants <= node <= all right descendants" must be true.

    Consider the following binary trees:

            3                    4                    4
          /   \                /  \                 /  \
         1     5              1    2              1    5
        / \   / \            / \                / \   / \
       0  2  4   6          0   3              0  2  3   6

    The tree with root value 3 is a BST, the trees with root 4 are not.

    NOTE: The third (right) tree is tricky; 3 is less than 5 BUT 3 is not greater than the root 4 (two levels up).

    Example:
        Input = BTNode(3, BTNode(1, BTNode(0), BTNode(2)), BTNode(5, BTNode(4), BTNode(6)))
        Output = True

"""


def is_bst_via_gen(t):
    if t:
        vals = in_order_traversal_generator(t)
        prev = next(vals)
        while True:
            curr = next(vals, None)
            if not curr:
                break
            if prev > curr:
                return False
            prev = curr
        return True


def in_order_traversal_generator(bt):
    if bt.left:
        yield from in_order_traversal_generator(bt.left)
    yield bt.value
    if bt.right:
        yield from in_order_traversal_generator(bt.right)


def is_bst(n, lowest=None, highest=None):
    if lowest and n.value < lowest:
        return False
    if highest and highest < n.value:
        return False
    is_left_bst = True
    is_right_bst = True
    if n.left:
        is_left_bst = is_bst(n.left, lowest, n.value)
    if is_left_bst and n.right:
        is_right_bst = is_bst(n.right, n.value, highest)
    return is_left_bst and is_right_bst


class BTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


trees = [BTNode(3, BTNode(1, BTNode(0), BTNode(2)), BTNode(5, BTNode(4), BTNode(6))),   # IS a BST
         BTNode(3, BTNode(1, BTNode(0), BTNode(3)), BTNode(5, BTNode(3), BTNode(6))),   # IS a BST
         BTNode(4, BTNode(1, BTNode(0), BTNode(3)), BTNode(2)),                         # ISN'T a BST
         BTNode(4, BTNode(1, BTNode(0), BTNode(2)), BTNode(5, BTNode(3), BTNode(6)))]   # ISN'T a BST

for t in trees:
    print("is_bst_via_gen(t)", is_bst_via_gen(t))
    print("is_bst(t):", is_bst(t))

