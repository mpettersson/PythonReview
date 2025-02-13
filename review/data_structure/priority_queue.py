"""
    PRIORITY QUEUE

    A priority queues is defined as a ... TODO
        - ...

    Implementations Show Below:
        - Via list - TODO...
        - Via heapq (Module) - TODO...
        - Via queue.PriorityQueue - TODO...

    Variations:
        - TODO

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




# IMPLEMENTATION: list (and sort)
#
# TODO: Description....
class PriorityQueueViaList:
    def __init__(self):
        self.queue = []

    def push(self, item, priority):
        self.queue.append((priority, item))
        self.queue.sort(key=lambda x: x[0])  # Sort based on priority

    def pop(self):
        if not self.is_empty():
            return self.queue.pop(0)[1]  # Return the item, ignoring priority
        raise IndexError("pop from an empty priority queue")

    def peek(self):
        if not self.is_empty():
            return self.queue[0][1]  # Return the item, ignoring priority
        raise IndexError("peek from an empty priority queue")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


# IMPLEMENTATION: heapq
#
# TODO: Description....
import heapq

class PriorityQueueViaHeapq:
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        if not self.is_empty():
            return heapq.heappop(self.heap)[1]  # Return the item, ignoring priority
        raise IndexError("pop from an empty priority queue")

    def peek(self):
        if not self.is_empty():
            return self.heap[0][1]  # Return the item, ignoring priority
        raise IndexError("peek from an empty priority queue")

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)


# IMPLEMENTATION: queue.PriorityQueue
#
# TODO: Description....
from queue import PriorityQueue

class PriorityQueueViaPriorityQueue:
    def __init__(self):
        self.queue = PriorityQueue()

    def push(self, item, priority):
        self.queue.put((priority, item))

    def pop(self):
        if not self.is_empty():
            return self.queue.get()[1]  # Return the item, ignoring priority
        raise Exception("pop from an empty priority queue")

    def peek(self):
        if not self.is_empty():
            temp = self.queue.get()
            self.queue.put(temp)
            return temp[1]  # Return the item, ignoring priority
        raise Exception("peek from an empty priority queue")

    def is_empty(self):
        return self.queue.empty()

    def size(self):
        return self.queue.qsize()


# TODO....
# Example Usage:
pq = PriorityQueueViaList()
pq.push("task1", 3)
pq.push("task2", 1)  # Higher priority (lower value)
pq.push("task3", 2)

print("Next task to process:", pq.peek())  # Should be 'task2'
print("Processing:", pq.pop())  # Removes 'task2'
print("Processing:", pq.pop())  # Removes 'task3'
print("Processing:", pq.pop())  # Removes 'task1'
