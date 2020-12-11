r"""
    BREADTH FIRST SEARCH (BFS) SERIALIZATION

    Write a function which takes the root of a binary tree and returns a breadth first search serialization of the
    binary tree.  Use None to denote, or mark, an empty child node.

    Consider the following binary tree:

             3
           /   \
          1     5
         / \   /
        0  2  4

    Example:
        Input = Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4)))  # or, the tree above
        Output = [3, 1, 5, 0, None, None, 6, None, None, None, None]

    Variations:
        - Same question, however, create a minimal serialization.
        - Same question, however, create a maximum serialization, or a list of length 2**(h+1) - 1.
"""


# BFS (Queue) Approach:  Use a queue to add the values at each depth of the tree to the result list.
# Time Complexity: O(n), where n are the number of nodes in the tree.
# Space Complexity: O(n), where n are the number of nodes in the tree.
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


# VARIATION:  Create a MINIMAL serialization.


# MINIMAL Serialization Naive/Get Height Approach:  Find the the tree's height first and track the depth of each node
# in the queue.  Once a depth value is greater than height is dequeue, break (that level will have nothing but Nones).
# Time Complexity: O(n), where n are the number of nodes in the tree.
# Space Complexity: O(n), where n are the number of nodes in the tree.
#
# NOTE: Despite the same time complexity as the next approach, this approach traverses over all nodes twice.
def get_bfs_min_serialization_naive(root):

    def _get_tree_height(root):
        if root:
            return max(_get_tree_height(root.left), _get_tree_height(root.right)) + 1
        return -1

    if root:
        result = []
        h = _get_tree_height(root)
        q = [(root, 0)]
        while q:
            node, depth = q.pop(0)
            if depth > h:
                break
            if node:
                result.append(node.value)
                q.append((node.left, depth + 1))
                q.append((node.right, depth + 1))
            else:
                result.append(None)
        return result


# MINIMAL Serialization Optimal Approach:  Perform a 'normal' BFS serialization, then once the result list is assembled
# pop from the result tail until a non-None value is last.
# Time Complexity: O(n), where n are the number of nodes in the tree.
# Space Complexity: O(n), where n are the number of nodes in the tree.
#
# NOTE: This approach traverses over all nodes once; hence, is better (unless root is a perfect binary tree, which would
# effectively be the same as above).
def get_bfs_min_serialization(root):
    if root:
        result = []
        q = [root]
        while q:
            node = q.pop(0)
            if node:
                q.append(node.left)
                q.append(node.right)
            result.append(node.value if node else None)
        while result[-1] is None:
            result.pop()
        return result


# VARIATION: Create a MAXIMUM serialization, or a list of length 2**(h+1) - 1.


# MAXIMUM Serialization Naive/Get Height Approach:  Find the the tree's height first and track the depth of each node
# in the queue.  Continue to add the values (or None) for each possible node in the level (this is the difference from
# the standard question). Once a depth value is greater than height is dequeue, break (that level will have nothing but
# None values).
# Time Complexity: O((2 ** (h + 1)) - 1), or O(2**h), where h is the height of the tree.
# Space Complexity: O((2 ** (h + 1)) - 1), or O(2**h), where h is the height of the tree.
#
# NOTE: Despite the same time complexity as the next approach, this approach traverses over all nodes twice.
def get_bfs_max_serialization_naive(root):

    def _get_tree_height(node):
        if node is None:
            return -1
        return max(_get_tree_height(node.left), _get_tree_height(node.right)) + 1

    if root:
        result = []
        tree_height = _get_tree_height(root)
        q = [(root, 0)]
        while q:
            node, depth = q.pop(0)
            if depth <= tree_height:
                result.append(node.value if node else None)
                q.append((node.left if node else None, depth + 1))
                q.append((node.right if node else None, depth + 1))
        return result


# MAXIMUM Serialization Approach:  In place of obtaining the tree's height (as the approach above), keep a list of
# values (or None) for each level, when a full levels worth is accumulated, add it to results (if it contains a non_None
# value, else break).
# Time Complexity: O((2 ** (h + 1)) - 1), or O(2**h), where h is the height of the tree.
# Space Complexity: O((2 ** (h + 1)) - 1), or O(2**h), where h is the height of the tree.
#
# NOTE: This approach traverses over all nodes once.
def get_bfs_max_serialization(root):
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


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return repr(self.value)


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


trees = [Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4))),
         Node(1, None, Node(2, None, Node(3))),
         Node(1, None, Node(3, Node(2))),
         Node(2, Node(1), Node(3)),
         Node(3, Node(1, None, Node(2))),
         Node(3, Node(2, Node(1))),
         # None,
         Node(0),
         Node(6, Node(5, Node(4, Node(3, Node(2, Node(1, Node(0))))))),
         Node(1, Node(3, Node(4), Node(6, Node(5), Node(0))), Node(2)),
         Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), Node(6))),
         Node(3, Node(1, Node(0)), Node(5, None, Node(6))),
         Node(4, Node(1, Node(0), Node(3)), Node(2)),
         Node(4, Node(1, Node(0), Node(2)), Node(5, Node(3), Node(6))),
         Node(0, Node(1, Node(2))),
         Node(0, Node(1), Node(3, Node(2), Node(4))),
         Node(27, Node(2, None, Node(17, Node(11, Node(5)), Node(26, Node(18)))),
              Node(74, Node(41, Node(34, Node(28))),
                   Node(90, Node(88), Node(99, None, Node(105, None, Node(420)))))),
         Node(26, Node(5, Node(-37, Node(-74, Node(-86), Node(-51)), Node(-7, Node(-17))),
                       Node(17, Node(11, Node(5)), Node(26, Node(18)))),
              Node(74, Node(41, Node(34, Node(28)), Node(52, Node(47))),
                   Node(90, Node(88, Node(86)), Node(99, Node(95)))))]
fns = [get_bfs_serialization,               # Original Problem
       get_bfs_min_serialization_naive,     # Variation: Min Serialization
       get_bfs_min_serialization,           # Variation: Min Serialization
       get_bfs_max_serialization_naive,     # Variation: Max Serialization
       get_bfs_max_serialization]           # Variation: Max Serialization

for i, tree in enumerate(trees):
    print(f"trees[{i}]:")
    display(tree)
    print(f"(bfs order:", end="")
    bfs(tree)
    print(")\n")
    for fn in fns:
        print(f"{fn.__name__}(tree): {fn(tree)}")
    print()


