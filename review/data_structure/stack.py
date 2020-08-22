"""
    STACK

    The stack data structure is a 'first in last out' (FILO) ordered, linear, data structure.  Push/Pop operations are
    O(1), where Get/Search operations are O(n).

    NOTE: Stacks are very useful when implementing a recursive algorithm iteratively.
"""


class _Node:
    def __init__(self, value=None, next=None):
        """Initialize self.  See help(type(self)) for accurate signature."""
        self.value = value
        self.next = next

    def __repr__(self):
        """Return repr(self)."""
        return repr(self.value)

    def __str__(self):
        """Return str(self)."""
        return str(self.value)


class Stack:
    def __init__(self, *args):
        """Initialize self.  See help(type(self)) for accurate signature."""
        self._top = None
        self._len = 0
        if len(args):
            for i in args:
                self._top = _Node(i, self._top)
                self._len += 1
        
    def __len__(self):
        """Return len(self)."""
        return self._len

    def __iter__(self):
        """Implement iter(self)."""
        n = self._top
        while n:
            yield n
            n = n.next

    def __repr__(self):
        """Return repr(self)."""
        return f"[{', '.join(map(repr, self))}]"

    def clear(self):
        """Remove all items from stack."""
        self._top = None
        self._len = 0

    def push(self, value):
        """Push, or add, value to the top of the stack."""
        self._top = _Node(value, self._top)
        self._len += 1
    
    def pop(self):
        """Pop, or remove and return, the value at the top of stack.
        Raises IndexError if stack is empty."""
        if self._top:
            value = self._top.value
            self._top = self._top.next
            self._len -= 1
            return value
        raise IndexError("pop from empty stack")
    
    def peek(self):
        """Peek at, or return, the value at the top of stack.
        Raises IndexError if stack is empty."""
        if self._top:
            return self._top.value
        raise IndexError("peek from empty stack")
    
    def empty(self):
        """Return True if stack is empty, False otherwise."""
        return self._len == 0


s = Stack(0, 1, 2, 3, 4, 5)
print(f"s: {s}")

my_stack = Stack()

print(f"my_stack: {my_stack}")
print("my_stack.empty():", my_stack.empty())
print("my_stack.size():", len(my_stack), "\n")

try:
    print("my_stack.peek():", my_stack.peek())
except IndexError as e:
    print("IndexError:", e.args)

print(f"my_stack: {my_stack}")
print("my_stack.size():", len(my_stack), "\n")

try:
    print("my_stack.pop():", my_stack.pop())
except IndexError as e:
    print("IndexError:", e.args)

print(f"my_stack: {my_stack}")
print("my_stack.size():", len(my_stack), "\n")

print("my_stack.push(\"A\")"); my_stack.push("A")
print("my_stack.push(\"B\")"); my_stack.push("B")
print("my_stack.push(\"C\")"); my_stack.push("C")
print("my_stack.push(\"D\")"); my_stack.push("D")
print("my_stack.push(\"E\")"); my_stack.push("E")
print(f"my_stack: {my_stack}")
print("my_stack.empty():", my_stack.empty())
print("my_stack.size():", len(my_stack), "\n")

print("my_stack.peek():", my_stack.peek())
print(f"my_stack: {my_stack}")
print("my_stack.size():", len(my_stack), "\n")

print("my_stack.pop():", my_stack.pop())
print(f"my_stack: {my_stack}")
print("my_stack.size():", len(my_stack), "\n")

print("my_stack.push(\"F\")"); my_stack.push("F")
print(f"my_stack: {my_stack}")
print("my_stack.size():", len(my_stack), "\n")



