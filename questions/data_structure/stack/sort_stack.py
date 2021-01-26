"""
    SORT STACK (CCI 3.5)

    Write a program to sort a stack such that the smallest items are on the top.  You can use an additional temporary
    stack, but you may not copy the elements into any other data structure (such as a list).  The stack supports the
    following operations: push, pop, peek, is_empty.

    Variations:
        - Same question, however, temporary stacks are NO longer allowed.
"""


# Sort with Two Stacks Approach:  Use a second stack that always maintains a reverse sorted order.
# Time Complexity: See below.
# Space Complexity: O(n), where n is the number of elements in the stack.
class Stack:
    # Time Complexity: O(a), where a are the number of elements in args.
    def __init__(self, *args):
        self.top = None
        for a in args:
            self.push(a)

    # Time Complexity: O(1).
    def push(self, value):
        self.top = Node(value, self.top)

    # Time Complexity: O(1).
    def empty(self):
        return self.top is None

    # Time Complexity: O(1).
    def pop(self):
        if not self.empty():
            value = self.top.value
            self.top = self.top.next
            return value
        raise IndexError("pop from empty stack")

    # Time Complexity: O(1).
    def peek(self):
        if not self.empty():
            return self.top.value
        raise IndexError("peek from empty stack")

    # Time Complexity: O(n**2), where n is the number of elements in the stack.
    def sort(self):
        if not self.empty():
            temp_stack = Stack()            # Second/temp stack ALWAYS has highest value on top.
            while not self.empty():
                temp = self.pop()
                while not temp_stack.empty() and temp_stack.peek() > temp:
                    self.push(temp_stack.pop())
                temp_stack.push(temp)
            while not temp_stack.empty():
                self.push(temp_stack.pop())

    # Time Complexity: O(1) (for the iterator object, or a single next call).
    def __iter__(self):
        node = self.top
        while node:
            yield node.value
            node = node.next

    # Time Complexity: O(n), where n is the number of elements in the stack.
    def __repr__(self):
        return f"[{', '.join(map(repr, self))}]"


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return repr(self.value)


my_stack = Stack(3, 2, 1, 0, 10, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19)
print(f"my_stack: {my_stack}")
print(f"my_stack.push(99): {my_stack.push(-99)}")
print(f"my_stack.push(99): {my_stack.push(99)}")
print(f"my_stack.push(99): {my_stack.push(-1)}")
print(f"my_stack: {my_stack}")
print(f"my_stack.sort(): {my_stack.sort()}")
print(f"my_stack: {my_stack}")
print(f"my_stack.pop(): {my_stack.pop()}")
print(f"my_stack.pop(): {my_stack.pop()}")
print(f"my_stack.pop(): {my_stack.pop()}")
print(f"my_stack: {my_stack}")


