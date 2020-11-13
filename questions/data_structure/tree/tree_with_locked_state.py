"""
    TREE WITH LOCKED STATE  (EPI 10.17 IMPLEMENT LOCKING IN A BINARY TREE)

    Create a binary tree node class with a lock state instance variable for a single threaded environment; the
    associated variable state properties are:
        - A node cannot be locked if any of its descendants or ancestors are locked.
        - A node's state change does not change the state of any other node.

    The binary tree node class should also contain a parent instance variable and the following methods:
        - is_locked(): A method that returns a bool indicating if the node is locked (True) or not (False).
        - lock(): A method that attempts to lock the node; returns True if able to lock the node, False otherwise.
        - unlock(): A method to unlock the node.

    NOTE: This is not multi threaded; do not add concurrency constructs.

"""


# Naive/Brute Force Approach:  The naive approach would be to only add a bool locked instance variable for each node.
# This approach would have a O(1) time for both is_locked() and unlock(), however, the time for lock() would be high.
# For a node's lock method call, all of its descendants and each of its ancestors to the root, would need to be checked;
# a time of O(n + d), where n is the number of nodes in the node's subtree, and d is the depth of the node. For example,
# if lock() were to be called on the root, then all of the nodes in the entire tree would need to be checked.


# Optimal Locked Descendants Approach:  For each node, in addition to the locked bool, maintain a counter for the number
# of descendants which are locked.  This results in a O(d) time for both the lock and unlock methods.  Additional space
# complexity is O(1) for each node, or O(n) for all nodes.
class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        if self.left:
            self.left.parent = self
        self.right = right
        if self.right:
            self.right.parent = self
        self.parent = parent
        self._locked = False
        self._num_locked_descendants = 0

    def get_value_str(self):
        if self._locked:
            return f"\033[95m{self.value}\033[0m"   # Pink if locked.
        if self._num_locked_descendants > 0:
            return f"\033[96m{self.value}\033[0m"   # Cyan if unable to lock.
        return f"{self.value}"                      # Else, no formatting.

    def __repr__(self):
        return repr(self.value)

    def is_locked(self):
        return self._locked

    def lock(self):
        if self._num_locked_descendants is 0 and not self._locked:
            node = self.parent
            while node:
                if node._locked:
                    return False
                node = node.parent
            self._locked = True
            node = self.parent
            while node:
                node._num_locked_descendants += 1
                node = node.parent
            return True
        return False

    def unlock(self):
        if self._locked:
            self._locked = False
            node = self.parent
            while node:
                node._num_locked_descendants -= 1
                node = node.parent


def display(node):
    def _display(node):
        if node.right is None and node.left is None:                                        # No child.
            return [node.get_value_str()], len(str(node.value)), 1, len(str(node.value)) // 2
        if node.right is None:                                                              # Only left child.
            lines, n, p, x = _display(node.left)
            u = len(str(node.value))
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + node.get_value_str()
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        if node.left is None:                                                               # Only right child.
            lines, n, p, x = _display(node.right)
            u = len(str(node.value))
            first_line = node.get_value_str() + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        else:                                                                               # Two children.
            left, n, p, x = _display(node.left)
            right, m, q, y = _display(node.right)
            u = len(str(node.value))
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + node.get_value_str() + y * '_' + (m - y) * ' '
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


tree = Node(27, Node(5, Node(-37, Node(-74, Node(-86), Node(-51)), Node(-7, Node(-17), Node(-8))),
                     Node(17, Node(11, Node(8), Node(13)), Node(26, Node(18), Node(27)))),
            Node(74, Node(42, Node(34, Node(28), Node(41)), Node(52, Node(47), Node(69))),
                 Node(90, Node(88, Node(86), Node(89)), Node(99, Node(95), Node(999)))))
args = [(tree.right.right.right, Node.is_locked),           # 99
        (tree.right.right.right.right, Node.is_locked),     # 999
        (tree.right.right.right.right, Node.lock),          # 999
        (tree.right.right.right.right, Node.is_locked),     # 999
        (tree.right.right.right, Node.lock),                # 99
        (tree.right.right.right.right, Node.unlock),        # 999
        (tree.right.right.right, Node.lock),                # 99
        (tree.right.right.right, Node.is_locked),           # 99
        (tree.left, Node.is_locked),                        # 5
        (tree.left, Node.lock),                             # 5
        (tree.left, Node.is_locked),                        # 5
        (tree.left.left.left.left, Node.lock),              # -86
        (tree.right.right.left, Node.lock),                 # 88
        (tree.right.left.left.right, Node.lock),            # 41
        (tree.right.left.left.left, Node.lock)]             # 28

print(f"tree:")
display(tree)
print()

for node, fn in args:
    print(f"Node({node.value}).{fn.__name__}(): {fn(node)}")

print(f"\ntree:")
display(tree)
print("(pink nodes are locked, cyan nodes have a _num_locked_descendants > 0)")


