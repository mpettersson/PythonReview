"""
    STACK OF PLATES (CCI 3.3)

    Image a (literal) stack of plates.  If the stack gets too high, it might topple.  Therefore, in real life, we would
    likely start a new stack when the previous stack exceeds some threshold.  Implement a data structure SetOfStacks
    that mimics this.  SetOfStacks should be composed of several stacks and should create a new stack once the previous
    one exceeds capacity.  SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that
    is, pop() should return the same values as it would if there were just a single stack).

    Follow Up:
        Implement a function pop_at(index) which performs a pop operation on a specific sub-stack.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return repr(self.value)


class Stack:
    def __init__(self, *args, next=None):
        self.next = next
        self.top = None
        self.size = 0
        for a in args:
            self.push(a)

    def push(self, value):
        self.top = Node(value, self.top)
        self.size += 1

    def pop(self):
        if self.size >= 1:
            return self.pop_at(0)
        raise IndexError("pop from empty stack")

    def pop_at(self, index):
        if 0 <= index < self.size:
            i = 0
            n = self.top
            p = None
            while i < index:
                p = n
                n = n.next
                i += 1
            value = n.value
            if p:
                p.next = n.next
            else:
                self.top = n.next
            self.size -= 1
            return value
        raise IndexError(f"invalid index ({index}); index must be in range [0, {self.size})")

    def peek(self, index=0):
        if 0 <= index < self.size:
            i = 0
            n = self.top
            while i < index:
                n = n.next
                i += 1
            return n
        raise IndexError(f"invalid index ({index}); index must be in range [0, {self.size})")

    def __iter__(self):
        n = self.top
        while n:
            yield n.value
            n = n.next

    def __repr__(self):
        return f"[{', '.join(map(repr, self))}]"


class SetOfStacks:
    def __init__(self, *args, threshold=5):
        self._threshold = threshold
        self.top = None
        self.total = 0
        for a in args:
            self.push(a)

    def push(self, value):
        if not self.top:
            self.top = Stack()
        if self.top.size >= self._threshold:
            self.top = Stack(next=self.top)
        self.top.push(value)
        self.total += 1

    def pop(self):
        if self.total > 0:
            return self.pop_at(0)
        raise IndexError("pop from empty stack")

    def pop_at(self, index):
        if 0 <= index < self.total:
            s = self.top
            while s.size <= index:
                index -= s.size
                s = s.next
            return s.pop_at(index)
        raise IndexError(f"invalid index ({index}); index must be in range [0, {self.total})")

    def __iter__(self):
        n = self.top
        while n:
            yield n
            n = n.next

    def __repr__(self):
        return f"[{', '.join(map(repr, self))}]"


set_of_stacks = SetOfStacks(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"set_of_stacks: {set_of_stacks}")
print(f"set_of_stacks.pop(): {set_of_stacks.pop()}")
print(f"set_of_stacks: {set_of_stacks}")
print(f"set_of_stacks.pop_at(5): {set_of_stacks.pop_at(5)}")
print(f"set_of_stacks: {set_of_stacks}")
print(f"set_of_stacks.push(97): {set_of_stacks.push(97)}")
print(f"set_of_stacks.push(98): {set_of_stacks.push(98)}")
print(f"set_of_stacks.push(99): {set_of_stacks.push(99)}")
print(f"set_of_stacks: {set_of_stacks}")
print(f"set_of_stacks.pop(): {set_of_stacks.pop()}")
print(f"set_of_stacks.pop(): {set_of_stacks.pop()}")
print(f"set_of_stacks: {set_of_stacks}")
print(f"set_of_stacks.push(100): {set_of_stacks.push(100)}")
print(f"set_of_stacks: {set_of_stacks}")


