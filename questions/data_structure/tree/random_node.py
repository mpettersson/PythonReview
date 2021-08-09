"""
    RANDOM NODE (CCI 4.11: RANDOM NODE,
                 50CIQ 17: RANDOM BINARY TREE)

    Implementing a binary tree class with the methods; insert, find, delete, and get_random_node.  The get_random_node
    method should return a random node from the tree, where all nodes have the same probability of being chosen.
"""
import random


# Questions you should ask the interviewer (if not explicitly stated):
#   - Implement the tree data structure or just the method (maybe the provided question is ambiguous)?
#   - What time/space complexity are you looking for?
#   - What type of data will the nodes contain (this may affect some languages more than others)?


# APPROACH: Convert to List
#
# When the method is called, perform an inorder DFS traversal of the tree, adding each of the nodes to a list.  When the
# list is composed, return a random node.  This, however, is slow and probably not what the interviewer wants...
#
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(n), where n is the number of nodes in the tree.
#
# SEE:  Node.values() and BTree.get_random_node_from_list() below.


# APPROACH: Maintain List (NOT Implemented)
#
# Akin to the above approach, (as an alternate to converting a tree to a list) maintain a list of all of the nodes (as
# well as the actual tree), then when the method is called, return a random node from the maintained list.
#
# Get Time Complexity: O(1).
# Delete Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(n), where n is the number of nodes in the tree.


# APPROACH: Random Tree Traversal
#
# At each level, select left traversal, current node, or right traversal, with EVENLY distributed probabilities.
# As a reminder, the following are some probability properties of a binary tree:
#   - The probability of of selecting a node from a tree is 1/n.
#   - The probability of selecting a node from a left subtree, tree.left, is 1/n * tree.left.size.
#   - The probability of selecting a node from a right subtree, tree.right, is 1/n * tree.right.size.
# Therefore, at any node n in the tree generate a random value r, recurse left if r is less than the size of the left
# tree, return node if r is the same as the size of the left tree, or recurse right.
#
# Time Complexity: O(log(n)), where n is the number of nodes in the tree (or, O(h), where h is the max tree height).
# Space Complexity: O(log(n)), where n is the number of nodes in the tree (or, O(h), where h is the max tree height).
#
# SEE:  Node.get_random_node() and BTree.get_random_node() below.


# APPROACH: Random Node (Optimal)
#
# Randomly select a random value r in the range of the size of the tree, then recurse to the node (subtracting the left
# size, or node.left.size, from the value r IF recursing down the right side, or tree.right).
#
# Time Complexity: O(log(n)), where n is the number of nodes in the tree (or, O(h), where h is the max tree height).
# Space Complexity: O(log(n)), where n is the number of nodes in the tree (or, O(h), where h is the max tree height).
#
# NOTE: Although the time/space complexities are the same as the approach above, there are fewer costly random calls!!!
#
# SEE:  Node.get_ith_node(i) and BTree.get_random_ith_node(), and BNodeMin.get_random_node() below.
class BNodeMin:     # Minimized Solution.
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __len__(self):
        num_left = 0 if self.left is None else len(self.left)
        num_right = 0 if self.right is None else len(self.right)
        return num_left + num_right + 1

    def __repr__(self):
        return f"({self.value}, {self.left}, {self.right})"

    def _get_ith_node(self, i):
        left_size = 0 if self.left is None else len(self.left)
        if i < left_size:
            return self.left._get_ith_node(i)
        if i == left_size:
            return self
        return self.right._get_ith_node(i - (left_size + 1))

    def get_random_node(self):
        return self._get_ith_node(random.randrange(0, len(self)))


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.size = 1

    def __iter__(self):
        if self.left:
            yield from self.left
        yield self.value
        if self.right:
            yield from self.right

    def __repr__(self):
        return ", ".join(map(repr, self))

    def __len__(self):
        return self.size

    def __getitem__(self, item):
        if item is self.value:
            return self
        elif item <= self.value and self.left:
            return self.left.__getitem__(item)
        elif item > self.value and self.right:
            return self.right.__getitem__(item)
        else:
            raise IndexError(f"{item} is not in tree")

    def insert(self, value):
        if value <= self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = Node(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value)
        self.size += 1

    def find(self, value):
        if self.value == value:
            return self
        if self.value > value and self.left:
            return self.left.find(value)
        elif self.value < value and self.right:
            return self.right.find(value)
        raise ValueError(f"{value} is not in tree")

    def delete(self, value):
        if self.value == value:
            if self.left is None and self.right is None:
                return None
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            node = self.right
            prev = None
            while node.left:
                prev = node
                node = node.left
            if prev:
                prev.left = node.right
                prev.size -= node.size
                node.right = self.right
            node.left = self.left
            node.size = node.left.size + node.right.size
            return node
        elif self.left and value < self.value:
            self.left = self.left.delete(value)
            self.size -= 1
            return self
        elif self.right and value > self.value:
            self.right = self.right.delete(value)
            self.size -= 1
            return self
        else:
            raise ValueError(f"{value} is already in tree")

    def update_sizes(self):
        def update_size(node):
            if not node:
                return 0
            node.size = update_size(node.left) + update_size(node.right) + 1
            return node.size
        self.size = update_size(self)

    # APPROACH: Convert to List
    def values(self):
        def in_order_add_to_list(n, l):
            if n:
                if n.left:
                    in_order_add_to_list(n.left, l)
                l.append(n)
            if n.right:
                in_order_add_to_list(n.right, l)
        l = []
        in_order_add_to_list(self, l)
        return l

    # APPROACH: Random Tree Traversal
    def get_random_node(self):
        left_size = 0 if self.left is None else self.left.size
        index = random.randint(0, self.size - 1)
        if index < left_size:
            return self.left.get_random_node()
        elif index == left_size:
            return self
        else:
            return self.right.get_random_node()

    # APPROACH: Random Node (Optimal)
    def get_ith_node(self, i):
        left_size = 0 if self.left is None else self.left.size
        if i < left_size:
            return self.left.get_ith_node(i)
        elif i == left_size:
            return self
        else:
            return self.right.get_ith_node(i - (left_size + 1))


class BTree:
    def __init__(self, *args):
        self.root = None
        if args:
            self.root = Node(args[0])
            for i in args[1:]:
                self.root.insert(i)

    def __len__(self):
        return self.root.size if self.root else 0

    def __iter__(self):
        return self.root

    def __repr__(self):
        return f"[{self.root}]"

    def __getitem__(self, item):
        if self.root is None:
            raise IndexError("root is None")
        else:
            return self.root.__getitem__(item)

    def insert(self, *args):
        for i in args:
            self.root.insert(i)

    def populate_tree_from_list(self, l):
        def create_nodes(l):
            if l:
                mid = len(l) // 2
                return Node(l[mid], create_nodes(l[:mid]), create_nodes(l[mid + 1:]))
        self.root = create_nodes(sorted(l))
        self.root.update_sizes()

    def find(self, value):
        return self.root.find(value)

    def delete(self, value):
        if self.root is None:
            raise ValueError("root is None")
        else:
            self.root = self.root.delete(value)

    # APPROACH: Convert to List
    def get_random_node_from_list(self):
        if self.root:
            l = self.root.values()
            return random.choice(l)

    # APPROACH: Random Tree Traversal
    def get_random_node(self):
        if self.root:
            return self.root.get_random_node()

    # APPROACH: Random Node (Optimal)
    def get_random_ith_node(self):
        if self.root:
            return self.root.get_ith_node(random.randint(0, self.root.size - 1))

    def values(self):
        if self.root is None:
            raise ValueError("root is None")
        else:
            return self.root.values()


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


tree = BTree()
n = 100
tree.populate_tree_from_list(list(range(n)))
fns = [tree.get_random_node_from_list,
       tree.get_random_node,
       tree.get_random_ith_node]

print("\ntree:")
display(tree.root)
print(f"n: {n}\n")


for fn in fns:
    for _ in range(5):
        print(f"{fn.__name__}().value", fn().value)
    print()


