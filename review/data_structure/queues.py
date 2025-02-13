class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return repr(self.value)


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __len__(self):
        return self.length

    def enqueue(self, value):
        new_node = Node(value)
        self.length += 1
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def dequeue(self):
        if self.first is None:
            return None
        else:
            value = self.first.value
            self.first = self.first.next
            self.length -= 1
        return value

    def peek(self):
        if self.first is None:
            return None
        else:
            return self.first.value

    def empty(self):
        return True if self.length == 0 else False

    def print_queue(self):
        curr = self.first
        print("[", end="")
        while curr is not None:
            print("", curr.value, end="")
            curr = curr.next
        print(" ]")


my_queue = Queue()

print("my_queue.print_queue():", end=""); my_queue.print_queue()
print("my_queue.length:", my_queue.length, "\n")

print("my_queue.peek():", my_queue.peek())
print("my_queue.print_queue():", end=""); my_queue.print_queue()
print("my_queue.length:", my_queue.length, "\n")

print("my_queue.dequeue():", my_queue.dequeue())
print("my_queue.print_queue():", end=""); my_queue.print_queue()
print("my_queue.length:", my_queue.length, "\n")

print("my_queue.enqueue(\"A\")"); my_queue.enqueue("A")
print("my_queue.enqueue(\"B\")"); my_queue.enqueue("B")
print("my_queue.enqueue(\"C\")"); my_queue.enqueue("C")
print("my_queue.enqueue(\"D\")"); my_queue.enqueue("D")
print("my_queue.enqueue(\"E\")"); my_queue.enqueue("E")
print("my_queue.print_queue():", end=""); my_queue.print_queue()
print("my_queue.length:", my_queue.length, "\n")

print("my_queue.peek():", my_queue.peek())
print("my_queue.print_queue():", end=""); my_queue.print_queue()
print("my_queue.length:", my_queue.length, "\n")

print("my_queue.dequeue():", my_queue.dequeue())
print("my_queue.print_queue():", end=""); my_queue.print_queue()
print("my_queue.length:", my_queue.length, "\n")

print("my_queue.enqueue(\"F\")"); my_queue.enqueue("F")
print("my_queue.print_queue():", end=""); my_queue.print_queue()
print("my_queue.length:", my_queue.length, "\n")

