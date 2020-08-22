"""
    STACK MIN (CCI 3.2)

    How would you design a stack which, in addition to push and pop, has a function min which returns the minimum
    element?  Push, pop and min should all operate in O(1) time.
"""

# NOTE: The following solutions use python lists, in a first in last out (FILO) order, as a replacement for node/stack
# classes to cut down on the length/complexity of the code.  In an interview you would want to ask the interviewer if
# this substitution was acceptable.


# Stack (Value, Min) Approach: One (less efficient) solution is for each stack node to contain both value and min. Push
# pop and min operate in O(1), space complexity is O(n) where n is the number of elements in the stack.
# This, however, would be inefficient if; for example, if the first pushed value was the min of the whole stack the min
# value would be duplicated many times.
class OneStackMin:
    def __init__(self, *args):
        self._top = []
        for i in args:
            self.push(i)

    def push(self, value):
        min = value
        if self._top and value > self._top[0][0]:
            min = self._top[0][1]
        self._top.insert(0, (value, min))

    def pop(self):
        if self._top:
            return self._top.pop(0)[0]
        raise IndexError("pop from empty stack")

    def min(self):
        if self._top:
            return self._top[0][1]
        raise IndexError("min from empty stack")

    def __repr__(self):
        return f"\n\ttop:{self._top}"


# Second Stack with Min Approach: Use a second stack to track min.  Push pop and min operate in O(1), space complexity
# is O(n) where n is the number of elements in the stack.
class StackMin:
    def __init__(self, *args):
        self.top = []
        self.mins = []
        for i in args:
            self.push(i)

    def push(self, value):
        if not self.mins or value <= self.mins[0]:
            self.mins.insert(0, value)
        self.top.insert(0, value)

    def pop(self):
        if self.top:
            value = self.top.pop(0)
            if self.mins[0] is value:
                self.mins.pop(0)
            return value
        raise IndexError("pop from empty stack")

    def min(self):
        if self.mins:
            return self.mins[0]
        raise IndexError("min from empty stack")

    def __repr__(self):
        return f"\n\ttop:{self.top}\n\tmin:{self.mins}"


# First (Less Effective) Approach:
one_stack_min = OneStackMin(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"one_stack_min: {one_stack_min}")
print(f"one_stack_min.min(): {one_stack_min.min()}")
print(f"one_stack_min.pop(): {one_stack_min.pop()}")
print(f"one_stack_min.min(): {one_stack_min.min()}")
print(f"one_stack_min.push(-1)"); one_stack_min.push(-1)
print(f"one_stack_min.min(): {one_stack_min.min()}")
print(f"one_stack_min: {one_stack_min}")
print()

# Second Approach (More Efficient):
stack_min = StackMin(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"stack_min: {stack_min}")
print()

stack_min = StackMin(4, 3, 2, 2, 4, 10, 1, 0, 11)
print(f"stack_min: {stack_min}")
print(f"stack_min.min(): {stack_min.min()}")
print(f"stack_min.push(-1)"); stack_min.push(-1)
print(f"stack_min: {stack_min}")
print(f"stack_min.min(): {stack_min.min()}")
print(f"stack_min.pop(): {stack_min.pop()}")
print(f"stack_min.min(): {stack_min.min()}")


