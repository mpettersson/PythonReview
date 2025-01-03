"""
    FENWICK TREE

    A Fenwick Tree, or Binary Indexed Tree, is a data structure that can efficiently compute range operations (+, *, ^).

            Average         Worst
    Search: O(log(n))       O(log(n))
    Insert: TODO            TODO
    Delete: TODO            TODO
    Space:  O(n)            O(n)

    This structure was proposed by Boris Ryabko in 1989.  It has subsequently become known under the name Fenwick Tree
    after Peter Fenwick, who described this structure in his 1994 paper.

    Fenwick trees allow updates and range operations to be performed in O(log n) time. This is achieved by representing
    the numbers in a second list (as a tree, similar to a heap), where the value of each node is the +|*|^ of the
    numbers in that subtree. Hence, the tree structure allows operations to be performed using only O(log n) node
    accesses.  The list is base one indexed (i.e., start at index 1), and is based on the least significant set bit of
    the corresponding number.

    TODO:
        Add the KEY concept of bit manipulation. And and example of how changes are propagated.

    References:
        - wikipedia.org/wiki/Fenwick_tree
        - cp-algorithms.com/data_structures/fenwick.html
        - youtu.be/uSFzHCZ4E-8
        - bitbucket.org/StableSort/play/src/master/src/com/stablesort/fenwick/FenwickTree.java
"""
import operator


# BASIC OPERATOR=SUM
class FenwickSum:
    def __init__(self, l=[]):                   # initialize the fenwick tree
        self.N = len(l)
        self.BIT = [0 for i in range(self.N)]
        for i in range(1, self.N + 1):
            self.update(i, l[i - 1])

    def update(self, i, x):                     # add x to the ith position
        while i <= self.x:
            self.BIT[i - 1] += x                # because we're working with an 1-based array
            i += i & (-i)

    def query(self, i):                         # find the ith prefix sum
        s = 0
        while i > 0:
            s += self.BIT[i - 1]
            i -= i & (-i)
        return s


# TODO TODO TODO
#   SEE: https://bitbucket.org/StableSort/play/src/master/src/com/stablesort/fenwick/FenwickTree.java
#   Can operator also be max, min?
#   SEE: https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326308/C%2B%2BPython-DP-Binary-Search-BIT-Solutions-Picture-explain-O(NlogN)
class Fenwick:
    def __init__(self, l=[], f=operator.add):   # initialize the fenwick tree
        if f is None or not (f == operator.add or f == operator.mul or f == operator.xor):
            raise TypeError("Function f must be operator.add, operator.mul, or operator.xor.")
        self.f = f
        self.size = len(l)
        self.tree = [0 for i in range(self.size)]
        for i in range(1, self.N + 1):
            self.update(i, l[i - 1])

    def __len__(self):
        return self.size

    def update(self, i, x):                     # add x to the ith position
        while i <= self.x:
            self.tree[i - 1] += x                # because we're working with an 1-based array
            i += i & (-i)

    def query(self, i):                         # Returns the f(tree[i]) from index 1 to i, inclusive
        q = None
        while i > 0:
            if q is None:
                q = self.tree[i]
            else:
                q += self.tree[i - 1]
            i -= i & (-i)
        return q


# TODO TODO TODO
#   SEE: https://www.topcoder.com/thrive/articles/Binary%20Indexed%20Trees#2d
# Fenwick Tree/BIT can be used as a multi-dimensional data structure.
#
# Suppose you have a plane with pixels/dots (using NON-NEGATIVE coordinates). Then the following methods may be useful:
#   - set a dot at (x , y)
#   - remove the dot from (x , y)
#   - count the num of dots (0,0),(x,y) – (0,0) is bottom-left, (x , y) is up-right (sides are parallel to x/y-axis).
#
# If m is the number of queries, max_x is the maximum x coordinate, and max_y is the maximum y coordinate, then this
# problem can be solved in O(m * log (max_x) * log (max_y)) time as follows. Each element of the tree will contain an
# array of dimension max_y, that is yet another BIT. Hence, the overall structure is instantiated as tree[max_x][max_y].
# Updating indices of x-coordinate is the same as before. For example, suppose we are setting/removing dot (a , b). We
# will call update(a , b , 1)/update(a , b , -1), where update is:
class Fenwick2D:
    def __init__(self, l=[]):                   # initialize the fenwick tree
        self.N = len(l)
        self.BIT = [0 for i in range(self.N)]
        for i in range(1, self.N + 1):
            self.update(i, l[i - 1])

    def update(self, i, x):                     # add x to the ith position
        while i <= self.x:
            self.BIT[i - 1] += x                # because we're working with an 1-based array
            i += i & (-i)

    # void update(int x, int y, int val) {
    #   while (x <= max_x) {
    #     updatey(x, y, val);
    #     // this function should update the array tree[x]
    #     x += (x & -x);
    #   }
    # }
    # void updatey(int x, int y, int val) {
    #   while (y <= max_y) {
    #     tree[x][y] += val;
    #     y += (y & -y);
    #   }
    # }
    # void update(int x, int y, int val) {
    #   int y1;
    #   while (x <= max_x) {
    #     y1 = y;
    #     while (y1 <= max_y) {
    #       tree[x][y1] += val;
    #       y1 += (y1 & -y1);
    #     }
    #     x += (x & -x);
    #   }
    # }

    def query(self, i):                         # find the ith prefix sum
        s = 0
        while i > 0:
            s += self.BIT[i - 1]
            i -= i & (-i)
        return s


