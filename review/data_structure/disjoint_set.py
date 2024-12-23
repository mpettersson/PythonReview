"""
    DISJOINT SET, DISJOINT-SET, UNION-FIND, DATA STRUCTURE (OR MERGE-FIND SET)

    A disjoint-set is a data structure that stores a collection of disjoint (or, non-overlapping) sets; or, a partition
    of a set into disjoint subsets.  Notably, it can EFFICIENTLY determine if any two elements are in the same or
    different sets.

     To perform a sequence of m addition, union, or find operations on a disjoint-set forest with n nodes requires total
     time O(mα(n)), where α(n) is the extremely slow-growing inverse Ackermann function. Disjoint-set forests do not
     guarantee this performance on a per-operation basis. Individual union and find operations can take longer than a
     constant times α(n) time, but each operation causes the disjoint-set forest to adjust itself so that successive
     operations are faster. Disjoint-set forests are both asymptotically optimal and practically efficient.

    Example Problems:
        - Given two user IDs (say from Facebook), can you check if they belong to the same group of friends?
        - What is the size of the largest group of friends (on say, Facebook)?

    General Rules & Notes:
        - Methods/Operations:
            - Adding new sets,
            - Merging Sets (Replacing by their union)
            - Finding the representative member, or root, of a set (e.g., If any two elements are in the same/diff set).
        - Disjoint-Set Forest:
            - A common implementation which performs unions and finds in near constant amortized time
        -

    Variations:
        -

    Applications:
        - Graph Connectivity
        - Kruskal's Algorithm
        - 'Social Networks'
        - Symbolic Computation
        - Compilers
        - Register Allocation Problems

    History:


    References:
        -
        - bitbucket.org/StableSort/play/src/master/src/com/stablesort/djset/DisjointSet.java
        - nayuki.io/res/disjoint-set-data-structure/disjointset.py

"""


class DisjointSet:
    def __init__(self, size):
        if size < 0:
            raise ValueError("size must be non-negative")
        self.ar = [-1] * size
        self.max_set_index = 0

    def find(self, i):
        k = i
        while self.ar[i] > 0:
            i = self.ar[i]      # Walk up to the parent.
        while k != i:           # Path Compression: Take a second pass assigning all to root.
            temp = self.ar[k]
            self.ar[k] = i
            k = temp
        return i                # Returns the root (or, a non-neg index in self.list) of the tree to which i belongs.

    def union(self, i, k):
        iParentIdx = self.find(i)
        kParentIdx = self.find(k)
        if iParentIdx == kParentIdx:    # If the two parent indices are the same, i and k are already in the same set...
            return
        isize = self.ar[iParentIdx]     # REMEMBER: Sizes are stored as a NEGATIVE number.
        ksize = self.ar[kParentIdx]
        if isize < ksize:               # Always merge the smaller set into the big one.
            self.ar[iParentIdx] += ksize
            self.ar[kParentIdx] = iParentIdx
            if -self.ar[self.max_set_index] < -self.ar[iParentIdx]:
                self.max_set_index = iParentIdx
        else:
            self.ar[kParentIdx] += isize
            self.ar[iParentIdx] = kParentIdx
            if -self.ar[self.max_set_index] < -self.ar[kParentIdx]:
                self.max_set_index = kParentIdx

    def max_set_size(self):
        return -1 * self.ar[self.max_set_index]

    def min_set_size(self):
        result = -float('inf')
        for i in range(len(self.ar)):   # smallest number, less than -1 will be the size of the biggest set
            if -1 > self.ar[i] > result:
                result = self.ar[i]     # this is the biggest size set
        return -result

    def select_max_set(self):
        return self.select_set(self.max_set_index)

    def select_set(self, k):
        result = set()
        root = self.find(k)
        for i in range(len(self.ar)):
            if self.find(i) == root:
                result.add(i)
        return result

    def __repr__(self):
        return repr(self.ar)


class DisjointSetNayuki:
    def __init__(self, size):
        if size < 0:
            raise ValueError("size must be non-negative")
        self.num_sets = 0
        self.parents = []       # The index of the parent element. An ele is a representative iff its parent is itself.
        self.sizes = []         # Positive number if the element is a representative, otherwise zero.
        for _ in range(size):
            self.add_set()

    def __repr__(self):
        return f"\n\tparents: {self.parents}\n\tsizes:   {self.sizes}"

    def get_num_elements(self):                     # Returns the number of elements among the set of disjoint sets.
        return len(self.parents)

    def get_num_sets(self):                         # Returns the total number of disjoint sets.
        return self.num_sets                        # 0 <= result <= get_num_elements()

    def find(self, el_idx):                         # Get 'representative' ele for the set (containing el_idx).
        if not (0 <= el_idx < len(self.parents)):
            raise IndexError()
        parent = self.parents[el_idx]
        while True:                                 # Follow parent pointers until we reach a 'representative'
            grandparent = self.parents[parent]
            if grandparent == parent:
                return parent
            self.parents[el_idx] = grandparent      # Partial path compression
            el_idx = parent
            parent = grandparent

    def get_size_of_set(self, el_idx):              # Returns the size of the set that the given element is a member of
        return self.sizes[self.find(el_idx)]        # 1 <= result <= get_num_elements()

    def are_in_same_set(self, el_idx_0, el_idx_1):  # Tests if 2 elements (non-ordered) are members of the same set.
        return self.find(el_idx_0) == self.find(el_idx_1)

    def add_set(self) -> int:                       # Adds a new singleton set
        el_idx = self.get_num_elements()
        self.parents.append(el_idx)                 # This increments get_num_elements()
        self.sizes.append(1)
        self.num_sets += 1
        return el_idx                               # Returns new element idx (or, the prev get_num_elements() value).

    def union(self, el_idx_0, el_idx_1):            # NOTE: The arguments are orderless.
        rep_0 = self.find(el_idx_0)
        rep_1 = self.find(el_idx_1)
        if rep_0 == rep_1:                          # IF in SAME set; don't do anything, return False...
            return False
        if self.sizes[rep_0] < self.sizes[rep_1]:   # NOTE: Always merge smaller into larger...
            rep_0, rep_1 = rep_1, rep_0             # We choose rep_0 to be larger.
        self.parents[rep_1] = rep_0                 # Graft repr1's subtree onto node repr0
        self.sizes[rep_0] += self.sizes[rep_1]
        self.sizes[rep_1] = 0
        self.num_sets -= 1
        return True                                 # Merge (from two different sets) done; return True...


ds = DisjointSet(10)
ds.union(1, 6)
ds.union(2, 7)
ds.union(3, 8)
ds.union(4, 9)
ds.union(2, 6)
print(ds)
print(f'root index: {ds.find(6)}')
print(f'biggest set size: {ds.max_set_size()}')
print(f'smallest set size: {ds.min_set_size()}')
print(f'max set: {ds.select_max_set()}')
print()

# Constructs a new set containing the given number of singleton sets.
# For example, DisjointSet(3) --> {{0}, {1}, {2}}.
dsn = DisjointSetNayuki(10)
print('dsn:', dsn)
dsn.union(1, 6)
print('dsn:', dsn)
dsn.union(2, 7)
dsn.union(3, 8)
dsn.union(4, 9)
dsn.union(2, 6)
print('dsn:', dsn)

