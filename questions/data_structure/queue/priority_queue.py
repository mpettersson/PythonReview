"""
    PRIORITY QUEUE (50CIQ 50: PRIORITY QUEUE)

    Implement a priority queue.
"""


# NOTE: Some questions are designed to to show your problem solving process and the interviewer doesn't want you to
#       already KNOW the answer.  This question, on the other hand, is a knowledge question; you are expected to KNOW
#       how to implement a binary heap and how the push/pop/sift down functions work.


# Ask the interviewer:
#   - Max/Min Priority Queue?
#   - Fixed Size (this is more important for languages with fixed size arrays)?


# APPROACH: Binary Heap Via List
#
# The basics, or key, to this question are:
#   - Indexing: For all nodes in the list at index i, the relations are as follows:
#       - Root at list[i=0].
#       - The left child is at list[(i*2)+1].
#       - The right child is at list[(i*2)+2].
#       - The parent is at list[(i//2)] OR at list[floor((i-1)/2)].
#   - Push (Insert):
#       1. Add the element to the bottom level of the heap at the leftmost open space.
#       2. Compare the added element with its parent; if they are in the correct order, stop.   (BUBBLE UP)
#       3. If not, swap the element with its parent and return to the previous step.            (BUBBLE UP)
#   - Pop/Extract:
#       1. Replace the root of the heap with the last element on the last level.
#       2. Compare the new root with its children; if they are in the correct order, stop.
#       3. If not, swap the element with with the smaller child in a min-heap and its larger    (BUBBLE DOWN)
#          child in a max-heap, return to the previous step.                                    (BUBBLE DOWN)
#
# Time Complexity: See below.
# Space Complexity: See below.
class MaxPriorityQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.heap = [None] * self.capacity              # BIN HEAP via LIST.
        self.size = 0

    def __str__(self):
        return str(self.heap)

    def __len__(self):
        return self.size

    # Time Complexity: O(log(n)), where n is the number of elements in the queue.
    # Space Complexity: O(n), where n is the number of elements in the queue.
    def push(self, value):
        if self.size < self.capacity:
            idx = self.size
            self.heap[idx] = value

            while idx > 0:                              # "BUBBLE UP": While value > parent, swap with parent.
                parent = (idx + 1) // 2 - 1             # Get parent index
                if self.heap[parent] > self.heap[idx]:  # If parent > value then break.
                    break
                self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]   # Else: Swap with Parent.
                idx = parent

            self.size += 1
        else:
            raise Exception("Exceeded Capacity.")

    # Time Complexity: O(log(n)), where n is the number of elements in the queue.
    # Space Complexity: O(n), where n is the number of elements in the queue.
    def pop(self):
        if self.size == 0:
            raise IndexError

        result = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]     # Could leave a copy of the last item at the end AND decrement size
        self.heap[self.size - 1] = None                 # (i.e., NOT replace with None), however, for an accurate str fn
        self.size -= 1                                  # the value must be removed (updated as None).
        idx = 0

        while idx < self.size // 2:                 # "BUBBLE DOWN": Divide by 2 BC children are 2xIndex away frm parent
            l_child = idx * 2 + 1                   #
            r_child = l_child + 1                   # Might be None.
            if r_child < self.size and self.heap[l_child] < self.heap[r_child]:             # Swap with Right Child
                self.heap[idx], self.heap[r_child] = self.heap[r_child], self.heap[idx]
                idx = r_child
            else:                                                                           # Swap with Left Child
                if self.heap[idx] >= self.heap[l_child]:
                    break
                self.heap[idx], self.heap[l_child] = self.heap[l_child], self.heap[idx]
                idx = l_child

        return result

# NOTE: It may help to visualize the queue as a tree structure.
#       Consider the following:
#
#   - INIT a priority queue, 'pq = PriorityQueue(7)':
#       [None, None, None, None, None, None, None]                 None
#                                                                  /  \
#                                                                ...  ...
#   - PUSH a value 4, 'pq.push(4)':
#       [4, None, None, None, None, None, None]                     4
#                                                                 /   \
#                                                              None   None
#                                                              /  \   /  \
#                                                            ... ... ... ...
#   - PUSH a value 6, 'pq.push(6)':
#       [4, 6, None, None, None, None, None]                     4                     6
#       [6, 4, None, None, None, None, None]                  /     \               /     \
#                                                            6      None    ==>    4       None
#                                                          /  \     /  \          /  \     /  \
#                                                       None None  ... ...      None None ... ...
#   - PUSH a value 3, 'pq.push(3)':
#       [6, 4, 3, None, None, None, None]            6
#                                                 /     \
#                                                4       3
#                                              /   \    /  \
#                                            None None None None
#   - PUSH a value 8, 'pq.push(8)':
#       [6, 4, 3, 8, None, None, None]             6                        6                     8
#       [6, 8, 3, 4, None, None, None]          /     \                  /     \               /     \
#       [8, 6, 3, 4, None, None, None]         4       3        ==>     8       3     ==>     6       3
#                                            /   \    /  \            /   \    /  \         /   \    /  \
#                                           8   None None None       4   None None None     4   None None None
#   - PUSH a value 7, 'pq.push(7)':
#       [8, 6, 3, 4, 7, None, None]                  8                     8
#       [8, 7, 3, 4, 6, None, None]               /     \               /     \
#                                                6       3      ==>    7       3
#                                              /   \    /  \         /   \    /  \
#                                             4     7 None None     4     6 None None
#   - POP a value (8), 'pq.push(8)':
#       [_, 7, 3, 4, 6, None, None]                _                        6                     7
#       [6, 7, 3, 4, None, None, None]          /     \                  /     \               /     \
#       [7, 6, 3, 4, None, None, None]         7       3        ==>     7       3     ==>     6       3
#                                            /   \    /  \            /   \    /  \         /   \    /  \
#                                           4    6   None None       4   None None None    4   None None None


pq = MaxPriorityQueue(7)
print(f"Priority Queue: {pq}\n")
for x in [4, 6, 3, 8, 7]:
    print(f"pq.push({x}): {pq.push(x)}")
    print(f"Priority Queue: {pq}\n")
while len(pq):
    print(f"Priority Queue: {pq}")
    print(f"pq.pop(): {pq.pop()}\n")
print(f"Priority Queue: {pq}")


