"""
    STACK FROM QUEUES (50CIQ 29: STACK FROM QUEUES,
                       leetcode.com/problems/implement-stack-using-queues)

    Write a stack class using only queues to store the data.
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Verify the problem statement: LIFO stack from two FIFO queues?
#   - Implement a node class, or assume one is created (if created what names were used)?
#   - What stack methods should be created (push, pop, size, is_empty, etc.)?
#   - What data types will the stack contain?


# APPROACH: Stack From Two Python Lists As Queues
#
# This approach uses python lists as queues to maintain the FIFO order property by pushing the new element to an empty
# queue, moving ALL the previous values after it, then SWAPPING the references to the queues.
#
# Time Complexity: See method for time.
# Space Complexity: O(n), where n is the number of elements in the stack.
class StackFromListsAsQueues:
    def __init__(self, *args):  # Use 2 Python lists as queues, where: HEAD [0, 1, ..., n-1, n] TAIL
        self.primary = []       # Primary will always contain all values in LIFO order (at end of each method).
        self.secondary = []     # Used only to push, then is empty again (NOTE: primary & secondary are swapped a lot).
        for a in args:
            self.push(a)

    # Time Complexity: O(n), where n is the total number of elements in the stack.
    def push(self, value):
        self.secondary.append(value)                                    # Push new value in empty secondary queue.
        while self.primary:                                             # Move all values from primary to secondary.
            self.secondary.append(self.primary.pop(0))
        self.primary, self.secondary = self.secondary, self.primary     # Swap the (primary/secondary) queues.

    # Time Complexity: O(1).
    def pop(self):
        return self.primary.pop(0)

    def is_empty(self):
        return not self.primary

    def __len__(self):
        return len(self.primary)

    def __repr__(self):
        return repr(self.primary)


# APPROACH: Stack From Two Queue Classes
#
# This approach uses two Queue classes (see below) as queues to maintain the FIFO order property by pushing the new
# element to an empty queue, moving ALL the previous values after it, then SWAPPING the references to the queues.
#
# Time Complexity: See method for time.
# Space Complexity: O(n), where n is the number of elements in the stack.
class StackFromQueues:
    def __init__(self, *args):
        self.primary = Queue()
        self.secondary = Queue()
        for a in args:
            self.push(a)

    # Time Complexity: O(n), where n is the total number of elements in the stack.
    def push(self, value):
        self.secondary.push(value)
        while not self.primary.is_empty():
            self.secondary.push(self.primary.pop())
        self.primary, self.secondary = self.secondary, self.primary

    # Time Complexity: O(1).
    def pop(self):
        if not self.primary.is_empty():
            return self.primary.pop()
        raise IndexError("Queue is empty.")

    def is_empty(self):
        return self.primary.is_empty()

    def __len__(self):
        return len(self.primary)

    def __iter__(self):
        yield from self.primary

    def __repr__(self):
        return repr(self.primary)


class QNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __iter__(self):
        yield self.value
        if self.next:
            yield from self.next

    def __repr__(self):
        return " ⟶  ".join(map(repr, self))


class Queue:
    def __init__(self, *args):
        self.first = None
        self.last = None
        self.size = 0
        for a in args:
            self.push(a)

    def push(self, value):
        node = QNode(value)
        if not self.first:
            self.first = self.last = node
        else:
            self.last.next = node
            self.last = self.last.next
        self.size += 1

    def pop(self):
        if self.first:
            value = self.first.value
            self.first = self.first.next
            self.size -= 1
            return value
        raise IndexError("Empty Queue")

    def is_empty(self):
        return not bool(self.first)

    def __len__(self):
        return self.size

    def __repr__(self):
        return repr(self.first)


classes = [StackFromListsAsQueues,
           StackFromQueues]

for cls in classes:
    print(f"\n{cls.__name__}\n")
    c_name = str.lower(cls.__name__)
    print(f"{c_name} = {cls.__name__}(0, 2, 5)"); c = cls(0, 2, 5)
    print(f"repr({c_name}): {repr(c)}")
    for value in [-1, 5, -42, 42]:
        print(f"{c_name}.push({value})"); c.push(value)
    print(f"repr({c_name}): {repr(c)}")
    for _ in range(len(c) // 2):
        print(f"{c_name}.pop(): {c.pop()}")
    print(f"repr({c_name}): {repr(c)}")
    print(f"{c_name}.is_empty(): {c.is_empty()}")
    while not c.is_empty():
        print(f"{c_name}.pop(): {c.pop()}")
    print(f"repr({c_name}): {repr(c)}")
    print(f"{c_name}.is_empty(): {c.is_empty()}")


