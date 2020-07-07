"""
    BINODE

    Consider a simple data structure called BiNode, which has pointers to two other nodes.

    class BiNode:
        def __init__ (self, data, node_one=None, node_two=None):
            self.data = data
            self.node_one = node_one
            self.node_two = node_two

    The data structure BiNode could be used to represent both a binary tree (where node_one is the left node and
    node_two is the right node) or a doubly linked list (where node_one is the previous node and node_two is the next
    node).  Implement a method to convert a binary search tree (implemented with BiNode) into a doubly linked list.
    The values should be kept in order and the operation should be performed in place (that is, on the original data
    structure).
"""


def convert_to_dll(node):
    if node is None:
        return None, None

    l_start, l_end = convert_to_dll(node.node_one)
    if l_start is None:
        l_start = node
    else:
        l_end.node_two = node
        node.node_one = l_end

    r_start, r_end = convert_to_dll(node.node_two)
    if r_start is None:
        r_end = node
    else:
        r_start.node_one = node
        node.node_two = r_start

    return l_start, r_end


def bst_pre_order_print(node):
    if node is not None:
        none = "None"
        print(f"Data = {node.data:>2},  Left = {none if node.node_one is None else node.node_one.data:>4},  Right = {none if node.node_two is None else node.node_two.data:>4}")
        bst_pre_order_print(node.node_one)
        bst_pre_order_print(node.node_two)


def dll_print(node):
    while node is not None:
        none = "None"
        print(f"Data = {node.data:>2},  Previous = {none if node.node_one is None else node.node_one.data:>4},  Next = {none if node.node_two is None else node.node_two.data:>4}")
        node = node.node_two


class BiNode:
    def __init__(self, data, node_one=None, node_two=None):
        self.data = data
        self.node_one = node_one
        self.node_two = node_two


# This is the BST that this example uses:
#      8
#    /   \
#   3     10
#  / \      \
# 1   6      14
#    / \    /
#   4   7  13
binode_bst = BiNode(8, BiNode(3, BiNode(1), BiNode(6, BiNode(4), BiNode(7))), BiNode(10, None, BiNode(14, BiNode(13), None)))
print("Pre-Order Traversal (of binode_bst):")
bst_pre_order_print(binode_bst)
print()

start, end = convert_to_dll(binode_bst)
print("Converted Doubly Linked List (from binode_bst ")
dll_print(start)



