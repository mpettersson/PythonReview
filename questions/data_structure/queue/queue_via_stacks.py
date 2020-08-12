"""
    QUEUE VIA STACKS (CCI 3.4)

    Implement a MyQueue class which implements a queue using two stacks.
"""


# Approach:  Using two stacks, one with the newest element on the top, the other (reversed) with the oldest element on
# the top, we can reproduce a queues ordering.  Time and space complexity is O(n) where n are the number of elements.
# NOTE: The elements are only moved from one stack to another if the operation requires the move, thus allowing for a
# more optimized 'lazy' approach.
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return repr(self.value)


class Stack:
    def __init__(self, *args):
        self.top = None
        for a in args:
            self.push(a)

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.top:
            value = self.top.value
            self.top = self.top.next
            return value
        raise IndexError("pop from empty stack")

    def empty(self):
        return self.top is None

    def __iter__(self):
        n = self.top
        while n:
            yield n.value
            n = n.next

    def __repr__(self):
        return f"{', '.join(map(repr, self))}"


class MyQueue:
    def __init__(self, *args):
        self.in_stack = Stack()        # Top of in_stack is tail (newest element) of queue.
        self.out_stack = Stack()       # Top of out_stack is head (oldest element) of queue.
        for a in args:
            self.enqueue(a)

    def enqueue(self, value):
        while not self.out_stack.empty():
            self.in_stack.push(self.out_stack.pop())
        self.in_stack.push(value)

    def dequeue(self):
        while not self.in_stack.empty():
            self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self):
        while not self.in_stack.empty():
            self.out_stack.push(self.in_stack.pop())
        if not self.out_stack.empty():
            return self.out_stack.top.value
        raise IndexError("peek from empty queue")

    def empty(self):
        return self.in_stack.empty() and self.out_stack.empty()

    def __repr__(self):
        return f"\n\tin_stack: [{', '.join(map(repr, self.in_stack))}]\n\tout_stack:[{', '.join(map(repr, self.out_stack))}]"


my_queue = MyQueue(0, 1, 2, 3, 4, 5)
print(f"my_queue: {my_queue}")
print(f"my_queue.dequeue(): {my_queue.dequeue()}")
print(f"my_queue.peek(): {my_queue.peek()}")
print(f"my_queue.dequeue(): {my_queue.dequeue()}")
print(f"my_queue.dequeue(): {my_queue.dequeue()}")
print(f"my_queue.enqueue(99): {my_queue.enqueue(99)}")
print(f"my_queue: {my_queue}")
print(f"my_queue.peek(): {my_queue.peek()}")
print(f"my_queue.dequeue(): {my_queue.dequeue()}")
print(f"my_queue: {my_queue}")



