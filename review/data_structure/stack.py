class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return repr(self.value)


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0
        
    def size(self):
        return self._size
    
    def push(self, value):
        self._size += 1
        self.top = Node(value, self.top)            
    
    def pop(self):
        if self.top is None:
            return None
        self._size -= 1
        value = self.top.value
        self.top = self.top.next
        return value
    
    def peek(self):
        return None if self.top is None else self.top.value
    
    def empty(self):
        return True if self._size == 0 else False
    
    def print_stack(self):
        curr = self.top
        print("[", end="")
        while curr is not None:
            print("", curr.value, end="")
            curr = curr.next
        print(" ]")


my_stack = Stack()

print("my_stack.print_stack():", end=""); my_stack.print_stack()
print("my_stack.empty():", my_stack.empty())
print("my_stack.size():", my_stack.size(), "\n")

print("my_stack.peek():", my_stack.peek())
print("my_stack.print_stack():", end=""); my_stack.print_stack()
print("my_stack.size():", my_stack.size(), "\n")

print("my_stack.pop():", my_stack.pop())
print("my_stack.print_stack():", end=""); my_stack.print_stack()
print("my_stack.size():", my_stack.size(), "\n")

print("my_stack.push(\"A\")"); my_stack.push("A")
print("my_stack.push(\"B\")"); my_stack.push("B")
print("my_stack.push(\"C\")"); my_stack.push("C")
print("my_stack.push(\"D\")"); my_stack.push("D")
print("my_stack.push(\"E\")"); my_stack.push("E")
print("my_stack.print_stack():", end=""); my_stack.print_stack()
print("my_stack.empty():", my_stack.empty())
print("my_stack.size():", my_stack.size(), "\n")

print("my_stack.peek():", my_stack.peek())
print("my_stack.print_stack():", end=""); my_stack.print_stack()
print("my_stack.size():", my_stack.size(), "\n")

print("my_stack.pop():", my_stack.pop())
print("my_stack.print_stack():", end=""); my_stack.print_stack()
print("my_stack.size():", my_stack.size(), "\n")

print("my_stack.push(\"F\")"); my_stack.push("F")
print("my_stack.print_stack():", end=""); my_stack.print_stack()
print("my_stack.size():", my_stack.size(), "\n")


    
