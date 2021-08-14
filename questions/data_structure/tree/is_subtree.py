r"""
    IS SUBTREE (CCI 4.10: CHECK SUBTREE)

    Write a function, which accepts two trees (t1 and t2), then returns True if t2 is a subtree of t1, False otherwise.
    A tree t2 is a subtree of tree t1 if there exists a node n in t1 such that the subtree of n is identical to t2.
    That is, if you cut off the tree at node n, the two trees would be identical.

    Consider the following trees t1 (left), t2 (middle), and t3 (right):

              1             6            6
            /   \          / \          / \
           3     2        5   0        5   0
         /  \                               \
        4    6                               1
            / \
           5   0

    NOTE: According to the given definition, tree t2 (middle) is NOT a subtree of tree t3 (right) because "if you cut
    off the tree at node n", the two trees would NOT be identical.

    Example:
                t1 = Node(1, Node(3, Node(4), Node(6, Node(5), Node(0))), Node(2))
                t2 = Node(6, Node(5), Node(0))
        Input = t1, t2     # or, the trees above
        Output = True
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Clarify the subtree definition (there are several variations)?
#   - What if t1 is t2?
#   - What data types will the tree contain (if, for example strings, then how would the be compared)?


# Pre-Order Traversal List Approach
#
# This simple approach builds a list node values via preorder tree traversal, then the lists are compared.
#
# Time Complexity: O(n + m), where n and m are the number of nodes in trees t1 and t2.
# Space Complexity: O(n + m), where n and m are the number of nodes in trees t1 and t2.
#
# NOTE: If the definition of subtree was changed, such that the the sub tree (t2) could be anywhere in the larger tree
#       (t1) then this approach would NOT work.
# NOTE: The None marker on links without children is necessary for meaningful tree description (if no None markers, then
#       it is possible for different shaped trees (with the same values) to have the same traversal values.
def check_subtree_preorder(t1, t2):

    def _get_preorder_values(root):
        return [root.value] + _get_preorder_values(root.left) + _get_preorder_values(root.right) if root else [None]

    def _is_list_in_list(l1, l2):
        len1 = len(l1)
        len2 = len(l2)
        if len1 >= len2:
            for i in range(len1 - len2 + 1):
                for j in range(len2):
                    if l1[i + j] != l2[j]:
                        break
                    elif j is len2 - 1:
                        return True
        return False

    if t1 and t2:
        l1 = _get_preorder_values(t1)
        l2 = _get_preorder_values(t2)
        return _is_list_in_list(l1, l2)
    return False


# Naive Recursive Approach
#
# This recursively checks any of t1's nodes is identical to t2.
#
# Time Complexity: O(nm), where n and m are the number of nodes in t1 and t2.
# Space Complexity: O(h1 + h2) space, where h1 and h2 are the height of t1 and t2.
def check_subtree_naive(t1, t2):
    if t1 and t2:
        return is_identical(t1, t2) or check_subtree_naive(t1.left, t2) or check_subtree_naive(t1.right, t2)
    return False


# Improved Recursive Approach
#
# This recursive approach only compares nodes in t1 that have a same height as t2, and fails upon first non-match.
#
# Time Complexity: O(2**h1 * h2), where h1 and h2 are the heights of the trees t1 and t2.
# Space complexity: O(h1 + h2), where h1 and h2 are the heights of the trees t1 and t2.
def check_subtree(t1, t2):

    def wrapper(n, t2, h):
        if not n:
            return 0, False
        lh, lb = wrapper(n.left, t2, h)
        rh, rb = wrapper(n.right, t2, h)
        return max(lh, rh) + 1, lb or rb or (max(lh, rh) is h and is_identical(n, t2))

    if t1 and t2:
        h1 = get_max_height(t1)
        h2 = get_max_height(t2)
        if h2 > h1:
            return False
        return wrapper(t1, t2, h2)[1]
    return False


def is_identical(t1, t2):
    if t1 is t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    # print(f"t1: {t1.value}, t2: {t2.value}")
    return t1.value == t2.value and is_identical(t1.left, t2.left) and is_identical(t1.right, t2.right)


def get_max_height(n):
    if not n:
        return -1
    return max(get_max_height(n.left), get_max_height(n.right)) + 1


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
        return ", ".join(map(str, self))


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
        print()
    else:
        print(None, "\n")


trees = [Node(1, Node(3, Node(4), Node(6, Node(5), Node(0))), Node(2)),
         Node(6, Node(5), Node(0)),
         Node(26, Node(5, Node(-37, Node(-74, Node(-86), Node(-51)), Node(-7, Node(-17), Node(50))),
                       Node(17, Node(11, Node(27)), Node(90, Node(84), Node(99, Node(6, Node(5), Node(0, Node(42))))))),
                  Node(74, Node(41, Node(34, Node(28)), Node(52, Node(47), Node(9))),
                       Node(90, Node(88, Node(86)), Node(99, Node(95), Node(-7))))),
         Node(42),
         Node(0),
         None,
         Node(0)]
args = [(4, 6),
        (1, 4),
        (0, 1),
        (1, 0),
        (2, 1),
        (2, 3),
        (2, 4),
        (0, 4),
        (0, 5)]
fns = [check_subtree_preorder,
       check_subtree_naive,
       check_subtree]

for i, j in args:
    print(f"\ndisplay(trees[{i}]):")
    display(trees[i])
    print(f"display(trees[{j}]):")
    display(trees[j])

    for fn in fns:
        print(f"{fn.__name__}(trees[{i}], trees[{j}]): {fn(trees[i], trees[j])}")
    print()


