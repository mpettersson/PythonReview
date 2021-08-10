"""
    REVERSE STACK (50CIQ 20: REVERSE STACK)

    Write a function to reverse the values in a stack WITHOUT any additional data structures.

    Example:
                stack = Stack([1, 2, 3, 4, 5])  # Stacks Order (if it was printed): 1 → 2 → 3 → 4 → 5
        Input = stack
        Output = None                           # Stacks Order (if it was printed): 5 → 4 → 3 → 2 → 1
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What is meant by "data structures"?
#   - What is valid input?
#   - Can a list be used as a stack?
#   - Do you want me to also make a Stack class (or should I use yours)?
#   - What type(s) will the stack hold (this doesn't really affect Python, might with other languages)?


# APPROACH:  Via Recursion Stack (Using A List As A Stack)
#
# This approach makes use of the recursion stacks to get around the data structure limitation.  First, a function is
# needed to be able to push a single value to the bottom of a stack (again, this is done via the recursion stack).  Once
# a value is able to be inserted in the bottom, an additional recursive function is needed to strip off the values
# recurse on the smaller stack, then push the stripped value to the bottom of the (resulting) stack.
#
# NOTE: The KEY to this problem is to FIRST make the push_to_bottom function!!!
#
# Time Complexity: O(n**2), where n is the size of the stack (list).
# Space Complexity: O(n), where n is the size of the stack (list).
def reverse_list_as_stack(l):

    def _push_to_bottom_of_list_as_stack(l, value):
        if len(l) == 0:
            l.append(value)
        else:
            temp = l.pop()
            _push_to_bottom_of_list_as_stack(l, value)
            l.append(temp)

    def _rec(l):
        if len(l) >= 1:
            temp = l.pop()
            _rec(l)
            _push_to_bottom_of_list_as_stack(l, temp)

    if isinstance(l, list):
        _rec(l)


# APPROACH:  Via Recursion Stack (Using Stack & Node Class)
#
# This approach makes use of the recursion stacks to get around the data structure limitation.  First, a function is
# needed to be able to push a single value to the bottom of a stack (again, this is done via the recursion stack).  Once
# a value is able to be inserted in the bottom, an additional recursive function is needed to strip off the values
# recurse on the smaller stack, then push the stripped value to the bottom of the (resulting) stack.
#
# NOTE: The KEY to this problem is to FIRST make the push_to_bottom function!!!
#
# Time Complexity: O(n**2), where n is the size of the stack.
# Space Complexity: O(n), where n is the size of the stack.
def reverse_stack(s):

    def _push_to_bottom_of_stack(s, value):
        if s.is_empty():
            s.push(value)
        else:
            temp = s.pop()
            _push_to_bottom_of_stack(s, value)
            s.push(temp)

    if not s.is_empty():
        temp = s.pop()
        reverse_stack(s)
        _push_to_bottom_of_stack(s, temp)


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        result = f"{self.value}"
        n = self.next
        while n:
            result += f" ⟶ {n.value}"
            n = n.next
        return result


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
        raise IndexError("Stack is empty.")

    def peek(self):
        if self.top:
            return self.top.value
        raise IndexError("Stack is empty.")

    def is_empty(self):
        return self.top is None

    def __repr__(self):
        return repr(self.top) if self.top else repr(None)


args = [(reverse_list_as_stack, [1, 2, 3, 4, 5]),
        (reverse_stack, Stack(1, 2, 3, 4, 5))]

for fn, stack in args:
    print(f"\nstack: {stack}")
    print(f"{fn.__name__}(stack): {fn(stack)}")
    print(f"stack: {stack}\n")


