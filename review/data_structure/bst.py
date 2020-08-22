import random


class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

    def set_key(self, key):
        self.key = key

    def insert(self, key):
        if self.key == key:
            return
        elif self.key < key:
            if self.right is None:
                self.right = Node(key)
            else:
                self.right.insert(key)
        else: # self.key > key
            if self.left is None:
                self.left = Node(key)
            else:
                self.left.insert(key)

    def display(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2



class BST:
    def __init__(self, list):
        self.root = self.make_BST(list)

    def make_BST(self, list):
        if len(list) == 1:
            return Node(list[0])
        else:
            partition = len(list) // 2
            left_node = self.make_BST(list[0:partition])
            if len(list) >= 3:
                right_node = self.make_BST(list[partition + 1:])
            else:
                right_node = None
            return Node(list[partition], left_node, right_node)

    def get_node(self, root, key):
        if root is None:
            return None
        if root.key == key:
            return root
        l = self.get_node(root.left, key)
        if l is not None and l.key == key:
            return l
        r = self.get_node(root.right, key)
        if r is not None and r.value == key:
            return r

    def get_random_node(self, node):
        if node is None:
            return None;
        size = self.get_size(node)
        return self.get_ith_node(node, random.randint(1, size))

    def get_ith_node(self, node, i):
        l_size = self.get_size(node.left)
        if i <= l_size:
            return self.get_ith_node(node.left, i)
        if l_size + 1 == i:
            return node
        return self.get_ith_node(node.right, i - (l_size + 1))

    def get_size(self, node):
        if node is None:
            return 0
        return self.get_size(node.right) + self.get_size(node.left) + 1

    def common_ancestor(self, root, p, q):
        if not self.covers(root, p) or not self.covers(root, q):
            return None
        return self.ancestor_helper(root, p, q)

    def covers(self, root, p):
        if root is None:
            return False
        if root is p:
            return True
        return self.covers(root.left, p) or self.covers(root.right, p)

    def ancestor_helper(self, root, p, q):
        if root is None:
            return None
        if root is p:
            return p
        if root is q:
            return q

        is_p_on_left = self.covers(root.left, p)
        is_q_on_left = self.covers(root.left, q)
        if is_p_on_left != is_q_on_left:
            return root
        child_side = root.left if is_p_on_left else root.right
        return self.ancestor_helper(child_side, p, q)

    # The naive way would be to do in-order traversal then check that it is sorted, this ONLY works if no duplicates
    # are allowed. If duplicates are allowed then a two node tree with 10 on it's root and 10 on it's right child would
    # be sorted, BUT, it wouldn't be a BST.  So you need to pass the max and min value down both sides.
    def is_bst(self, node, min=None, max=None):
        if not node:
            return True
        if (min and node.value <= min) or (max and node.value > max):
            return False
        if (not self.is_bst(node.left, min, node.value)) or (not self.is_bst(node.right, node.value, max)):
            return False
        return True

    def in_order_traversal(self, node):
        if not node:
            return []
        return self.in_order_traversal(node.left) + [node.value] + self.in_order_traversal(node.right)

    def is_balanced(self, node):
        if not node:
            return True
        if self.get_height_balanced(node) == -1:
            return False
        else:
            return True

    def get_height_balanced(self, node):
        if not node:
            return 0
        l_height = self.get_height_balanced(node.left)
        if l_height == -1:
            return -1
        r_height = self.get_height_balanced(node.right)
        if r_height == -1:
            return -1
        diff = abs(l_height - r_height)
        if diff > 1:
            return -1
        else:
            return max(l_height, r_height) + 1

    def get_height(self, node):
        if not node:
            return 0
        return max(self.get_height(node.right), self.get_height(node.left)) + 1

    def height(self, node):
        if not node or (not node.left and not node.right):
            return 0
        if node.left is None:
            return self.height(node.right) + 1
        elif node.right is None:
            return self.height(node.left) + 1
        else:
            return max(self.height(node.left), self.height(node.right)) + 1

    def insert(self, key):
        self.root.insert(key)

    def display(self):
        self.root.display()

    def count_paths_with_sum(self, node, target_sum):
        if node is None:
            return 0

        paths_from_root = self.count_paths_with_sum_from_root(node, target_sum, 0)

        paths_on_left = self.count_paths_with_sum(node.left, target_sum)
        paths_on_right = self.count_paths_with_sum(node.right, target_sum)

        return paths_from_root + paths_on_left + paths_on_right

    def count_paths_with_sum_from_root(self, node, target_sum, curr_sum):
        if node is None:
            return 0

        curr_sum += node.key

        total_paths = 0;
        if curr_sum == target_sum:
            total_paths += 1

        total_paths += self.count_paths_with_sum_from_root(node.left, target_sum, curr_sum)
        total_paths += self.count_paths_with_sum_from_root(node.right, target_sum, curr_sum)

        return total_paths

    def flatten(self):
        l = []
        q = [(self.root, 0)]
        while len(q) > 0:
            node, i = q.pop(0)
            if node.left:
                q.append((node.left, i + 1))
            if node.right:
                q.append((node.right, i + 1))
            if len(l) < (i + 1):
                l.append([node.key])
            else:
                l[i].append(node.key)
        return [y for x in l for y in x]





bst1 = BST([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
bst1.display()
print(bst1.flatten())
print(bst1.is_balanced(bst1.root))


print(bst1.count_paths_with_sum(bst1.root, 15))


node1 = bst1.get_node(bst1.root, 1)
node2 = bst1.get_node(bst1.root, 2)
node8 = bst1.get_node(bst1.root, 8)

ancestor = bst1.common_ancestor(bst1.root, node2, node1)
print("common ancestor of {} and {} is:".format(node2.key, node1.key), ancestor.key)

ancestor = bst1.common_ancestor(bst1.root, node2, node8)
print("common ancestor of {} and {} is:".format(node2.key, node8.key), ancestor.key)

print(bst1.is_bst(bst1.root))

bstInsert = BST([8])
for x in [3, 10, 1, 6, 14, 4, 7, 13]:
    bstInsert.insert(x)

bstInsert.display()

print("covers:", bstInsert.covers(bstInsert.root, node1))

print("\n")

bst2 = BST([50])
for _ in range(20):
    bst2.insert(random.randint(0, 100))
bst2.display()
print(bst2.is_balanced(bst2.root))
print("\n")
print(bst2.is_balanced(bst2.root))
