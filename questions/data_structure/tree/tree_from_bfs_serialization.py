r"""
    TREE FROM BFS SERIALIZATION

    Given a list with the values of a breadth first search (BFS) serialized binary tree, write a function that returns
    the root of a new tree with the same structure as the tree that produced the BFS serialization.

    Consider the following binary tree:

             3
           /   \
          1     5
         / \   /
        0  2  4

    Example:
        Input = [3, 1, 5, 0, 2, 4, None, None, None, None, None, None, None]
        Output = Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4)))  # or, the tree above

    Variations:
        - Is this solvable for an inorder traversal serialization?
        - Same question, however, a naive serialization was used resulting the maximum length list for any tree (a list
          of size (2 ** (h + 1)) - 1).
"""


# BFS (Queue) Approach: Create a root from the first value of the list and put it in a queue.  While the list has
# values, dequeue (the current) node, pop from the head of the list and create a left/right child (if the values are not
# None), finally, enqueue created children nodes.
# Time Complexity: O(s), where s is the size of the list.
# Space Complexity: O(n), where n is the number of non-None values in the list.
#
# NOTE: This also works for BFS serializations that have all trailing Nones removed, (i.e., [3, 1, 5, 0, 2, 4])
def tree_from_bfs_serialization(l):
    if l:
        root = Node(l.pop(0))
        q = [root]
        while l:
            node = q.pop(0)
            l_val = l.pop(0)
            if l_val is not None:
                node.left = Node(l_val)
                q.append(node.left)
            if l:
                r_val = l.pop(0)
                if r_val is not None:
                    node.right = Node(r_val)
                    q.append(node.right)
        return root


# VARIATION: Naive/MAXIMUM Length Serialization (a list of size (2 ** (h + 1)) - 1).


# Naive Serialization BFS (Queue) Approach: This approach is similar to the above approach except that None values must
# also be enqueued/tracked to maintain the alignment with the remaining list.
# Time Complexity: O(s), where s is the size of the list.
# Space Complexity: O(n), where n is the number of non-None values in the list.
def tree_from_naive_bfs_serialization(l):
    if l:
        root = Node(l.pop(0))
        q = [root]
        while l:
            node = q.pop(0)
            l_val = l.pop(0)
            r_val = l.pop(0) if l else None
            if node:
                if l_val is not None:
                    node.left = Node(l_val)
                q.append(node.left)
                if r_val is not None:
                    node.right = Node(r_val)
                q.append(node.right)
            else:
                q.extend([None, None])
        return root


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return repr(self.value)

    def equals(self, root):
        if root and root.value == self.value:
            l_equals = (self.left.equals(root.left) if root.left else False) if self.left else (root.left is None)
            r_equals = (self.right.equals(root.right) if root.right else False) if self.right else (root.right is None)
            return l_equals and r_equals
        return False


def get_bfs_serialization(root):
    if root:
        result = []
        q = [root]
        while q:
            node = q.pop(0)
            if node:
                q.append(node.left)
                q.append(node.right)
            result.append(node.value if node else None)
        return result


def get_naive_bfs_serialization(root):
    if root:
        q = [root]
        result = []
        levels_result = []
        level_num = 0
        is_valid_level = False
        while q:
            node = q.pop(0)
            if node:
                is_valid_level = True
            levels_result.append(node.value if node else None)
            if len(levels_result) is 2**level_num:
                if is_valid_level:
                    result.extend(levels_result)
                    levels_result = []
                    is_valid_level = False
                    level_num += 1
                else:
                    break
            q.append(node.left if node else None)
            q.append(node.right if node else None)
        return result


def bfs(root):
    if root:
        q = [root]
        while q:
            node = q.pop(0)
            print(f" {node.value}", end="")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


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


trees = [Node(5, Node(4, Node(3, Node(2, Node(1, Node(0)))))),
         Node(5, None, Node(4, None, Node(3, None, Node(2, None, Node(1, None, Node(0)))))),
         Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4))),
         Node(1, None, Node(2, None, Node(3))),
         Node(1, None, Node(3, Node(2))),
         Node(2, Node(1), Node(3)),
         Node(3, Node(1, None, Node(2))),
         Node(3, Node(2, Node(1))),
         Node(0),
         Node(1, Node(3, Node(4), Node(6, Node(5), Node(0))), Node(2)),
         Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), Node(6))),
         Node(3, Node(1, Node(0), Node(3)), Node(5, Node(3), Node(6))),
         Node(4, Node(1, Node(0), Node(3)), Node(2)),
         Node(4, Node(1, Node(0), Node(2)), Node(5, Node(3), Node(6))),
         Node(0, Node(1, Node(2))),
         Node(0, Node(1), Node(3, Node(2), Node(4))),
         Node(26, Node(5, Node(-37, Node(-74, Node(-86), Node(-51)), Node(-7, Node(-17))),
                       Node(17, Node(11, Node(5)), Node(26, Node(18)))),
              Node(74, Node(41, Node(34, Node(28)), Node(52, Node(47))),
                   Node(90, Node(88, Node(86)), Node(99, Node(95))))),
         Node(27, Node(2, None, Node(17, Node(11, Node(5)), Node(26, Node(18)))),
              Node(74, Node(41, Node(34, Node(28))),
                   Node(90, Node(88), Node(99, None, Node(105, None, Node(420))))))]
fn_pairs = [(tree_from_bfs_serialization, get_bfs_serialization),
            (tree_from_naive_bfs_serialization, get_naive_bfs_serialization)]   # Variation: Naive Serialization

for i, tree in enumerate(trees):
    print(f"trees[{i}]:")
    display(tree)
    print(f"(bfs order:", end="")
    bfs(tree)
    print(f")\n")
    for tree_fn, serial_fn in fn_pairs:
        print(f"{serial_fn.__name__}(tree): {serial_fn(tree)}")
        print(f"{tree_fn.__name__}({serial_fn.__name__}(tree)).equals(tree): {tree_fn(serial_fn(tree)).equals(tree)}")
        print()
    print()


