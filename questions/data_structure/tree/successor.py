r"""
    SUCCESSOR (CCI 4.6)

    Write an algorithm to find the 'next' node (i.e., in-order successor) of a given node in a binary search tree.  You
    may assume that each node has a link to its parent.

    Consider the following BST, tree:

             3
           /   \
          1     5
         / \   / \
        0  2  4   6

    Example:
        Input = tree[0] # or, the node with value 0 in the BST (tree) above
        Output = 1      # or, the node with value 1

    NOTE: For a slight variation of this question, see find_first_greater_than_k.py/"FIND FIRST GREATER THAN K".
"""


# Time is O(1) and space is O(log n) where n is the number of nodes or O(h) where h is the height of the tree.
def successor(node):                        # Successor can only be:
    if node:
        if node.right:                      # 1: (IFF node.right) The leftmost node on right subtree.
            node = node.right
            while node.left:
                node = node.left
            return node
        while node.parent:
            if node is node.parent.left:    # 2: The first/closest ancestor that has the node as a left descendant.
                return node.parent
            node = node.parent
    return None                             # 3: None.


class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def insert(self, value):
        if value <= self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = Node(value, parent=self)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value, parent=self)

    def __getitem__(self, item):
        if item is self.value:
            return self
        elif item <= self.value and self.left:
            return self.left.__getitem__(item)
        elif item > self.value and self.right:
            return self.right.__getitem__(item)

    def __iter__(self):
        if self.left:
            yield from self.left
        yield self.value
        if self.right:
            yield from self.right

    def __repr__(self):
        return repr(self.value)


# Helper Function
def make_bst(l):
    if l and len(l) > 0:
        n = Node(l[0])
        for v in l[1:]:
            n.insert(v)
        return n


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


tl1 = [3, 1, 5, 0, 2, 4, 6]
t1 = make_bst(tl1)
print(f"display(t1):"); display(t1)
print(f"successor(t1[0]):", successor(t1[0]))
print(f"successor(t1[3]):", successor(t1[3]))
print(f"successor(t1[6]):", successor(t1[6]), "\n")

tl2 = [27, 2, 74, 17, 41, 90, 11, 26, 34, 88, 99, 5, 18, 28, 105, 420]
t2 = make_bst(tl2)
print(f"display(t2):"); display(t2)
print(f"successor(t2[2]):", successor(t2[2]))
print(f"successor(t2[5]):", successor(t2[5]))
print(f"successor(t2[26]):", successor(t2[26]))
print(f"successor(t2[27]):", successor(t2[27]))
print(f"successor(t2[74]):", successor(t2[74]))
print(f"successor(t2[99]):", successor(t2[99]))
print(f"successor(t2[420]):", successor(t2[420]), "\n")

tl3 = [0]
t3 = make_bst(tl3)
print(f"display(t3):"); display(t3)
print(f"successor(t3[0]):", successor(t3[0]), "\n")

t4 = None
print(f"display(t4):"); display(t4)
print(f"successor(t4):", successor(t4))


