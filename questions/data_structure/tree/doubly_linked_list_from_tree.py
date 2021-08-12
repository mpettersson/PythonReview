r"""
    DOUBLY LINKED LIST FROM TREE (CCI 17.12: BINODE,
                                  50CIQ 21: TREE TO DOUBLY LINKED LIST)

    Write a function to modify the pointers of a given binary tree such that it is converted, from left to right, into a
    circular doubly linked list.  Return the leftmost node as the head of the 'list'.

    Consider the following binary tree, and a doubly linked list version of the tree:

             1
           /   \
          2     3       ⟷ 4 ⟷ 2 ⟷ 5 ⟷ 1 ⟷ 6 ⟷ 3 ⟷ 7 ⟷
         / \   / \
        4  5  6  7

    Example:
        Input = BiNode(1, BiNode(2, BiNode(4), BiNode(5)), BiNode(3, BiNode(6), BiNode(7)))
        Output = None  # However, printing the tree will now show a doubly linked list.
"""
import copy
import time


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Clarify problem:
#       + What output?
#       + What direction (in-order, pre-order, post-order)?
#       + Circular?
#   - Input Validation?
#   - What happens with a single node tree?


# APPROACH: Recursive (Verbose)
#
# Recursively update the left and right child (pointers) in a DFS fashion to form a doubly linked list.
#
# NOTE: The key to this question is to visualize the tree to list transformation (draw it; see it'll essentially be
#       flattened, or that a DFS traversal is what you want), then to realize that each recursive call must return the
#       START & END of its sublist, finally, to carefully account for each case (no children, one child, two children).
#
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree.
def dll_from_tree_verbose(r):
    def _rec(n):
        if n.left and n.right:
            l_first, l_last = _rec(n.left)
            l_last.right = n
            n.left = l_last
            r_first, r_last = _rec(n.right)
            r_first.left = n
            n.right = r_first
            return l_first, r_last
        if n.left:
            l_first, l_last = _rec(n.left)
            l_last.right = n
            n.left = l_last
            return l_first, n
        if n.right:
            r_first, r_last = _rec(n.right)
            r_first.left = n
            n.right = r_first
            return n, r_last
        return n, n
    if isinstance(r, BiNode):
        first, last = _rec(r)
        first.left = last
        last.right = first
        return first


# APPROACH: Recursive
#
# This approach is the same as above, however, duplicate code has been combined and removed.
#
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree.
def dll_from_tree(r):
    def _rec(n):
        first = last = n
        if n.left:
            first, l_last = _rec(n.left)
            l_last.right = n
            n.left = l_last
        if n.right:
            r_first, last = _rec(n.right)
            r_first.left = n
            n.right = r_first
        return first, last
    if isinstance(r, BiNode):
        first, last = _rec(r)
        first.left = last
        last.right = first
        return first


# APPROACH: Via DFS Generator
#
# This approach utilizes a DFS generator to update the links.
#
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree.
def dll_from_tree_via_gen(node):

    def gen_dfs(node):
        if node.left:
            yield from gen_dfs(node.left)
        yield node
        if node.right:
            yield from gen_dfs(node.right)

    if node:
        g = gen_dfs(node)
        head = prev = None
        for n in g:
            if head is None:
                head = n
            n.left = prev
            if prev:
                prev.right = n
            prev = n
        head.left = prev
        prev.right = head
        return head


class BiNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def is_binary_tree(self):
        q = [self]
        seen = set(q)
        while q:
            curr = q.pop(0)
            if curr.left:
                if curr.left in seen:
                    return False
                seen.add(curr.left)
                q.append(curr.left)
            if curr.right:
                if curr.right in seen:
                    return False
                seen.add(curr.right)
                q.append(curr.right)
        return True

    def is_circular_doubly_linked_list(self, timeout=1):
        if isinstance(timeout, int) and timeout > 0:
            t = time.time() + timeout
            node = self.right
            prev = self
            while time.time() < t and node and node.left == prev:
                if node is self:
                    return True
                prev = node
                node = node.right
            return False
        raise ValueError

    def __repr__(self):
        if self.is_circular_doubly_linked_list():
            return self._display_list()
        else:
            return self._display_tree()

    def _display_list(self):
        node = self.left
        result = f"⟷ {self.value} ⟷"
        while node and node != self:
            result += f" {node.value} ⟷"
            node = node.left
        return result

    def _display_tree(self):
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

        if self.is_binary_tree():
            lines, _, _, _ = _display(self)
            return '\n\t' + '\n\t'.join(lines)
        else:
            raise ValueError("Configured as circular doubly linked list not binary tree.")


trees = [BiNode(1, BiNode(2, BiNode(4), BiNode(5)), BiNode(3, BiNode(6), BiNode(7))),
         BiNode(5, BiNode(4, BiNode(3, BiNode(2, BiNode(1, BiNode(0)))))),
         BiNode(5, None, BiNode(4, None, BiNode(3, None, BiNode(2, None, BiNode(1, None, BiNode(0)))))),
         BiNode(3, BiNode(1, BiNode(0), BiNode(2)), BiNode(5, BiNode(4))),
         BiNode(1, None, BiNode(2, None, BiNode(3))),
         BiNode(1, None, BiNode(3, BiNode(2))),
         BiNode(2, BiNode(1), BiNode(3)),
         BiNode(3, BiNode(1, None, BiNode(2))),
         BiNode(3, BiNode(2, BiNode(1))),
         BiNode(0),
         BiNode(1, BiNode(3, BiNode(4), BiNode(6, BiNode(5), BiNode(0))), BiNode(2)),
         BiNode(3, BiNode(1, BiNode(0), BiNode(2)), BiNode(5, BiNode(4), BiNode(6))),
         BiNode(3, BiNode(1, BiNode(0), BiNode(3)), BiNode(5, BiNode(3), BiNode(6))),
         BiNode(4, BiNode(1, BiNode(0), BiNode(3)), BiNode(2)),
         BiNode(4, BiNode(1, BiNode(0), BiNode(2)), BiNode(5, BiNode(3), BiNode(6))),
         BiNode(0, BiNode(1, BiNode(2))),
         BiNode(0, BiNode(1), BiNode(3, BiNode(2), BiNode(4))),
         BiNode(26, BiNode(5, BiNode(-37, BiNode(-74, BiNode(-86), BiNode(-51)), BiNode(-7, BiNode(-17))),
                           BiNode(17, BiNode(11, BiNode(5)), BiNode(26, BiNode(18)))),
                BiNode(74, BiNode(41, BiNode(34, BiNode(28)), BiNode(52, BiNode(47))),
                       BiNode(90, BiNode(88, BiNode(86)), BiNode(99, BiNode(95))))),
         BiNode(27, BiNode(2, None, BiNode(17, BiNode(11, BiNode(5)), BiNode(26, BiNode(18)))),
                BiNode(74, BiNode(41, BiNode(34, BiNode(28))),
                       BiNode(90, BiNode(88), BiNode(99, None, BiNode(105, None, BiNode(420))))))]
fns = [dll_from_tree_verbose,
       dll_from_tree,
       dll_from_tree_via_gen]


for i, tree in enumerate(trees):
    print(f"trees[{i}]: {tree}")
    for fn in fns:
        print(f"{fn.__name__}(trees[{i}]): {fn(copy.deepcopy(tree))}")
    print()


