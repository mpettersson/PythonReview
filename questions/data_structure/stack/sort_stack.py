"""
    SORT STACK (CCI 3.5: SORT STACK,
                50CIQ 21: SORT STACKS)

    Write a function, which accepts a stack, and sorts the stack.  An additional temporary stack is allowed, however,
    the elements may not be put into any other data structure (such as a list).

    Variations:
        - Same question, however, temporary stacks are NO longer allowed.
"""
import random


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What data types will the stack contain?
#   - Implement a node class, or assume one is created (if created what names were used)?
#   - What is the sorted order (smallest or largest on top)?
#   - Verify assumption that a temporary variable be used.


# APPROACH: Sort Via 2nd Stack (List As Stack)
#
# Use a temporary variable and a second stack, which maintains the property that all values are in reverse sorted order,
# to sort the provided stack.
#
# Time Complexity: O(n**2), where n is the number of elements in the stack.
# Space Complexity: O(n), where n is the number of elements in the stack.
def sort_list_as_stack(s):
    if s:
        temp_s = []
        while True:
            while s and (not temp_s or temp_s[-1] < s[-1]):
                temp_s.append(s.pop())
            if s:
                temp_value = s.pop()
                while temp_s and temp_s[-1] > temp_value:
                    s.append(temp_s.pop())
                temp_s.append(temp_value)
            else:
                while temp_s:
                    s.append(temp_s.pop())
                return


# APPROACH: Sort Via 2nd Stack (Stack Class)
#
# Use a temporary variable and a second stack, which maintains the property that all values are in reverse sorted order,
# to sort the provided stack.
#
# Time Complexity: See method for time.
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
        return f"(Bottom)[{', '.join(reversed(list(map(repr, self))))}](Top)"


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return repr(self.value)


values = [random.randrange(-10, 10) for _ in range(11)]

list_as_stack = values[:]
print(f"\nlist_as_stack: {list_as_stack}")
print(f"sort_list_as_stack(list_as_stack): {sort_list_as_stack(list_as_stack)}")
print(f"list_as_stack: {list_as_stack}")

stack = Stack(*values)
print(f"\nstack: {stack}")
print(f"stack.sort(): {stack.sort()}")
print(f"stack: {stack}")


