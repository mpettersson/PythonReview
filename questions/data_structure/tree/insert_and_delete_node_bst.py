r"""
    INSERT AND DELETE BST (EPI 15.10: INSERTION AND DELETION IN A BST)

    Create an insert and delete class method for a binary search tree (BST) node.  In addition to the BST property,
    the tree should maintain the property that all nodes have distinct values.

    Consider the following BSTs, t, u, and v:

                  -19-                                -19-                                -23-
                /      \                            /      \                            /      \
              7         43                        7         43                        7         43
            /  \       /   \                    /  \       /   \                    /  \       /   \
           3   11     23   47                  3   11     23   47                  3   11     37   47
         /  \   \      \    \                /  \   \      \    \                /  \   \    /  \    \
        2   5   17     37   53              2   5   17     37   53              2   5   17  29  41   53
               /      / \                      /   /      / \                      /   /      \
              13    29  41                    4   13    29  41                    4   13      31
                      \                                   \
                      31                                  31

    Example:
        insert:
            Input = t, 4
            Output = u      # or, the middle graph above

        delete:
            Input = u, 19
            Output = v      # or, the right graph above

    Variations:
        - Same question, however, nodes may have duplicate values.
        - Same question, with the added constraint; you can only change links (can't change values).
"""


# Insert Approach:  Recurse left or right, adhering to the BST property, until either the value is present (and raise a
# ValueError) or create a node with the value.
# Time Complexity: O(h) where h is the height of the tree.
# Space Complexity: O(h) where h is the height of the tree.
#
# SEE Node.insert() below.


# Delete Approach:  Recurse left or right, adhering to the BST property, until there are no more nodes (and raise a
# ValueError) or the current nodes value matches the value and return the appropriate value.  If there is no left or
# right subtree return None, if there is only one subtree return it, or if there are two subtrees find the left most
# node in the right subtree return it with updated children (and it's previous parent's children updated).
# Time Complexity: O(h) where h is the height of the tree.
# Space Complexity: O(h) where h is the height of the tree.
#
# SEE: Node.delete() below.


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
        return ", ".join(map(repr, self))

    # Insert Approach:
    def insert(self, value):
        if value is self.value:
            raise ValueError(f"{value} is already in tree")
        elif value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = Node(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value)

    # Delete Approach:
    # NOTE: Find either the smallest value on the nodes the right subtree, or the largest node on the nodes left subtree
    # to replace the deleted node (then update all of the affected links).
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
                node.right = self.right
            node.left = self.left
            return node
        elif self.left and value < self.value:
            self.left = self.left.delete(value)
            return self
        elif self.right and value > self.value:
            self.right = self.right.delete(value)
            return self
        else:
            raise ValueError(f"{value} is not in the tree.")


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


tree = Node(19, Node(7, Node(3, Node(2), Node(5)), Node(11, None, Node(17, Node(13)))),
                Node(43, Node(23, None, Node(37, Node(29, None, Node(31)), Node(41))), Node(47, None, Node(53))))

print(f"display(tree)"); display(tree); print("\n")
print(f"tree.insert(4): {tree.insert(4)}")
print(f"display(tree)"); display(tree); print("\n")
print(f"tree = tree.delete(19)"); tree = tree.delete(19)
print(f"display(tree)"); display(tree); print("\n")
print(f"tree.insert(20): {tree.insert(20)}")
print(f"tree.insert(6): {tree.insert(6)}")
try:
    print(f"tree.insert(13): {tree.insert(13)}")
except ValueError as e:
    print(f"ValueError", e.args)
print(f"display(tree)"); display(tree); print("\n")
print(f"tree = tree.delete(5)"); tree = tree.delete(5)
print(f"display(tree)"); display(tree); print("\n")
print(f"tree = tree.delete(47)"); tree = tree.delete(47)
print(f"display(tree)"); display(tree); print("\n")
print(f"tree = tree.delete(7)"); tree = tree.delete(7)
print(f"display(tree)"); display(tree); print("\n")
print(f"tree = tree.delete(43)"); tree = tree.delete(43)
print(f"display(tree)"); display(tree)


