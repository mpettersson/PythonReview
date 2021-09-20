"""
    BINARY HEAP

    TODO:
        - Add max heap example.
        - Add root at index 0 example.
        - Add pushpop, and other helper methods.
        - Clean up the driver code.

    A binary heap is defined as a BINARY TREE with two additional constraints:
        - Shape Property: A binary heap is a complete binary tree; that is, all levels of the tree, except possibly the
          last one (deepest) are fully filled, and, if the last level of the tree is not complete, the nodes of that
          level are filled from left to right.  (This is how O(log(n)) performance is guaranteed.)
        - Heap Property: The key stored in each node is either (max-heap) greater than or equal to (≥) or (min-heap)
          less than or equal to (≤) the keys in the node's children, according to some total order.

    Binary heaps are a common way of implementing priority queues.  Efficient O(log(n) algorithms are known for the two
    operations needed to implement a priority queue on a binary heap: inserting an element, and removing the smallest or
    largest element from a min-heap or max-heap, respectively.  The binary heap was introduced by J. W. J. Williams in
    1964, as a data structure for heapsort.  SEE: https://en.wikipedia.org/wiki/Binary_heap

    Implementation:
        - The standard approach is to use a list where each item in the list corresponds to one node in the heap.
        - Indexing (for nodes in the list at index i):
            - IF root at list[1], then:
                - Left child is at list[i*2].
                - The right child is at list[(i*2)+1].
                - The parent is at list[(i//2)] OR at list[floor(i/2)].
            - IF root at list[0], then:
                - The left child is at list[(i*2)+1].
                - The right child is at list[(i*2)+2].
                - The parent is at list[(i//2)] OR at list[floor((i-1)/2)].

        - The size, or number of nodes, is required.
        - The capacity is the length of the list is optional.
        - Push/Insert:
            1. Add the element to the bottom level of the heap at the leftmost open space.
            2. Compare the added element with its parent; if they are in the correct order, stop.
            3. If not, swap the element with its parent and return to the previous step.
            NOTE: Steps 2 & 3 are called: up-heap, bubble-up, percolate-up, sift-up, trickle-up, swim-up, heapify-up, or
                  cascade-up.
        - Pop/Extract:
            1. Replace the root of the heap with the last element on the last level.
            2. Compare the new root with its children; if they are in the correct order, stop.
            3. If not, swap the element with with the smaller child in a min-heap and its larger child in a max-heap,
               return to the previous step.
            NOTE: Steps 2 & 3 are called: down-heap, bubble-down, percolate-down, sift-down, sink-down, trickle down,
                  heapify-down, cascade-down, extract-min/max, or simply the heapify operation.

    Variations:
        - Other heap implementations/data structures include; Leftist, B-heaps, Binomial, Fibonacci, Pairing, Brodal,
          Rank-pairing, Strict Fibonacci, 2-3 heap.
        - B-heaps are binary heaps that keep subtrees in a single page, reducing the number of pages accessed by up to a
          factor of ten.  For big heaps and using virtual memory, storing elements in an array according to the above
          scheme is inefficient: (almost) every level is in a different page.
        - SEE: https://en.wikipedia.org/wiki/Binary_heap#Summary_of_running_times

    Priority Queue VS Heap:
        A priority queue is an abstract data type similar to a regular queue or stack, in which each element has an
        additionally "priority" associated with it. In a priority queue, an element with high priority is served before
        an element with low priority. In some implementations, if two elements have the same priority, they are served
        according to the order in which they were enqueued, while in other implementations, ordering of elements with
        the same priority is undefined.

        While priority queues are often implemented with heaps, they are conceptually distinct from heaps. A priority
        queue is a concept like "a list" or "a map"; just as a list can be implemented with a linked list or an array, a
        priority queue can be implemented with a heap or a variety of other methods such as an unordered array.

        SEE: https://en.wikipedia.org/wiki/Priority_queue
             https://softwareengineering.stackexchange.com/questions/254947/difference-between-a-heap-and-a-priority-queue
"""


# MINIMUM BINARY HEAP EXAMPLE
# Root is at index 1.
# Flexible size/capacity.
# SEE: https://runestone.academy/runestone/books/published/pythonds/Trees/BinaryHeapImplementation.html
class BinMinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def __len__(self):
        return self.size

    def __repr__(self):
        return repr(self.heap[1:])

    def bubble_up(self, i):
        """Ensure (via swapping values) that the ancestors of i maintain the bin heap properties."""
        while i // 2 > 0:                               # While the current node (i) has a parent:
            if self.heap[i] < self.heap[i // 2]:            # If the current node.value < parent.value:
                self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2]   # Swap the nodes/values.
            i = i // 2                                      # Current node = parent node.

    def push(self, value):
        """Push, or insert, a value to the bin heap, then ensure that the binary heap properties are maintained."""
        self.heap.append(value)                         # Add value (new node) to end of list.
        self.size = self.size + 1                       # Increment size.
        self.bubble_up(self.size)                       # Bubble up the newly added node/value.

    def bubble_down(self, i):
        """Ensure (via swapping values) that the subtree rooted at i maintains the binary heap properties."""
        while (i * 2) <= self.size:                     # While the current node has a (left) child:
            mc = self.get_min_child_idx(i)                  # Get the index of the child with min value.
            if self.heap[i] > self.heap[mc]:                # If current node.value > child.value:
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]   # Swap the nodes/values.
            i = mc                                          # Current node = child with min value.

    def get_min_child_idx(self, i):
        """Helper method to find the index of node i's child with the minimum value."""
        if i * 2 + 1 > self.size:                       # If no right child:
            return i * 2                                    # Return index of left child.
        if self.heap[i * 2] < self.heap[i * 2 + 1]:     # If left.value < right.value:
            return i * 2                                    # Return index of left child.
        return i * 2 + 1                                # Else: Return index of right child.

    def pop(self):
        """Pop and return the minimum value."""
        result = self.heap[1]                           # Save the min value (to be returned).
        self.heap[1] = self.heap[self.size]             # Copy the last element to the root position.
        self.size = self.size - 1                       # Decrease size.
        self.heap.pop()                                 # Remove the last element (that moved to the root).
        self.bubble_down(1)                             # Restore order.
        return result

    def extend(self, l):
        """Adds all of the values in the list to current bin heap (aggregate)."""
        self.heap.extend(l)
        self.size = len(self.heap) - 1
        i = (self.size - 1) // 2
        while i > 0:
            self.bubble_down(i)
            i = i - 1

    def heapify(self, l):
        """Make a new bin heap from a list (replace)."""
        i = len(l) // 2
        self.size = len(l)
        self.heap = [0] + l[:]
        while i > 0:
            self.bubble_down(i)
            i = i - 1


min_heap = BinMinHeap()
for x in [99, -1, 9, 5, 6, 2, 3]:
    min_heap.push(x)

print(f"Binary Heap: {min_heap}\n")

for x in [4, 6, 3, 8, 7]:
    print(f"min_heap.push({x}): {min_heap.push(x)}")
    print(f"Binary Heap: {min_heap}\n")

while len(min_heap):
    print(f"Binary Heap: {min_heap}")
    print(f"min_heap.pop(): {min_heap.pop()}\n")

print(f"Binary Heap: {min_heap}")

print(f"min_heap.heapify([88, 99, 66]): {min_heap.heapify([88, 99, 66])}")
print(f"Binary Heap: {min_heap}")

print(f"min_heap.heap: {min_heap}")
min_heap.extend([99, -1, 9, 5, 6, 2, 3])

print(f"len(bh): {len(min_heap)}")
print(f"min_heap.heap: {min_heap.heap}")


