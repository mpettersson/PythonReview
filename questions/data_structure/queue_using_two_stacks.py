"""
    QUEUE USING 2 STACKS

    Implement a QueueFromTwoStacks class which implements a queue using two stacks.

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.top = None

    def push(self, value):
        n = Node(value)
        n.next = self.top
        self.top = n

    def pop(self):
        if not self.top:
            raise Exception
        n = self.top
        self.top = n.next
        return n.value

    def peek(self):
        if not self.top:
            raise Exception
        return self.top.value

    def is_empty(self):
        return not self.top

# NOTE: You can "enhance" this if, after a remove/add, you leave the items in the stack that they were last moved to
# (in case there is a duplicate call; i.e. two adds in a row) until the opposite call makes you move them back.

class QueueUsingTwoStacks:

    def __init__(self):
        self.main_stack = Stack()
        self.second_stack = Stack()

    # add
    def add(self, value):
        self.main_stack.push(value)

    # remove
    def remove(self):
        if self.main_stack.is_empty():
            raise Exception
        # pop items off to second_stack
        while not self.main_stack.is_empty():
            self.second_stack.push(self.main_stack.pop())
        # pop/return item from second_stack
        v = self.second_stack.pop()
        # pop/return items to main_stack
        while not self.second_stack.is_empty():
            self.main_stack.push(self.second_stack.pop())
        return v

    # is_empty
    def is_empty(self):
        return self.main_stack.is_empty()

    # peek
    def peek(self):
        if self.main_stack.is_empty():
            raise Exception
        # pop items off to second_stack
        while not self.main_stack.is_empty():
            self.second_stack.push(self.main_stack.pop())
        # pop/return item from second_stack
        v = self.second_stack.peek()
        # pop/return items to main_stack
        while not self.second_stack.is_empty():
            self.main_stack.push(self.second_stack.pop())
        return v



stack = Stack()
print(stack.is_empty())
stack.push(1)
stack.push(2)
print(stack.is_empty())
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.is_empty())

print("----------------------")
queue = QueueUsingTwoStacks()
print(queue.is_empty())
queue.add(1)
queue.add(2)
queue.add(3)
print(queue.is_empty())
print(queue.peek())
print(queue.remove())
print(queue.remove())
print(queue.remove())

