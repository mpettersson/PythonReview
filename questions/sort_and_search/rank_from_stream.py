"""
    RANK FROM STREAM (CCI 10.10)

    Image you are reading in a stream of integers.  Periodically, you wish to be able to look up the rank of a number x
    (the number of values less than or equal to x).  Implement the data structures and algorithms to support these
    operations.  That is, implement the method track(x), which is called when each number is generated, and the method
    get_rank_of_number(x), which returns the number of values less than or equal to x (not including x itself).

    Example:
        stream (in order of appearance) = 20, 15, 10, 25, 5, 23, 13, 24
        stream.get_rank_of_number(20) = 4
        stream.get_rank_of_number(10) = 1
        stream.get_rank_of_number(25) = 2
        stream.get_rank_of_number(23) = 0
"""


# Binary Search Tree Approach:  Incidentally, a BST that ONLY tracks the number of left sub-children perfectly solves
# this problem. The following is the example stream as a BST (with the number of left sub children in parenthesis):
#
#             20(4)
#            /     \
#          15(3)   25(2)
#         /       /
#        10(1)   23(0)
#       /   \     \
#      5(0) 13(0)  24(0)
#
# The time complexity for track and get_rank_of_number is O(h), where h is the max height of the tree.
class RankTracker:
    def __init__(self):
        self.root = None

    def __iter__(self):
        if self.root is not None:
            q = [self.root]
            while len(q) > 0:
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                yield node.value

    def __repr__(self):
        return "[" + ', '.join(map(repr, self)) + "]"

    def track(self, x):
            node = self.root
            prev = None
            while node is not None:
                prev = node
                if x <= node.value:
                    node = node.left
                    prev.num_left_children += 1
                else:
                    node = node.right
            if prev is None:
                self.root = Node(x)
            else:
                if x <= prev.value:
                    prev.left = Node(x)
                else:
                    prev.right = Node(x)

    def get_rank_of_number(self, x):
        if x is not None:
            node = self.root
            while node is not None:
                if node.value is x:
                    return node.num_left_children
                elif x <= node.value:
                    node = node.left
                else:
                    node = node.right


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.num_left_children = 0


stream = [20, 15, 10, 25, 5, 23, 13, 24]
extra_args = [-20, 0, None]

print(f"rank_tracker = RankTracker()\n")
rank_tracker = RankTracker()

for i in stream:
    print(f"rank_tracker.track({i})")
    rank_tracker.track(i)
print()

for i in stream + extra_args:
    print(f"rank_tracker.get_rank_of_number({i}): {rank_tracker.get_rank_of_number(i)}")


