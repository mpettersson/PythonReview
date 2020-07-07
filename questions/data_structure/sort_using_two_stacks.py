"""
    SORT USING TWO STACKS

    Write a program to sort a stack such that the smallest items are on the top.  You can use an additional temporary
    stack, but you may not copy the elements into any other data structure (such as an array).  The stack supports
    the following operations: push, pop, peek, is_empty.

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
        v = self.top.value
        self.top = self.top.next
        return v

    def peek(self):
        if not self.top:
            raise Exception
        return self.top.value

    def is_empty(self):
        return not self.top

    def print_stack(self):
        s = self.top
        print("-")
        while s:
            print(s.value)
            s = s.next
        print("-")


def sort_using_two_stacks(stack):
    # Temp stack will always have the smallest item on the bottom.
    temp_stack = Stack()
    # pop item off stack and put it in the correct place in the temp stack by returning larger items to stack
    while not stack.is_empty():
        v = stack.pop()
        while not temp_stack.is_empty() and temp_stack.peek() > v:
            stack.push(temp_stack.pop())
        temp_stack.push(v)
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())
    return stack


stack = Stack()
print(stack.is_empty())
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.print_stack()

stack = sort_using_two_stacks(stack)
stack.print_stack()
