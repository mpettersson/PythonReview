"""
    STACK MIN (CCI 3.2)

    How would you design a stack which, in addition to push and pop, has a function min which returns the minimum
    element?  Push, pop and min should all operate in O(1) time.
"""


# NOTE: TWO of the following three solutions use python lists, in a first in last out (FILO) order, as a replacement for
# node/stack classes to (minimally) cut down on the length/complexity of the code.  In an interview you would want to
# ask the interviewer if this substitution was acceptable.


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

    def __len__(self):
        return len(self._top)


# Second Stack W/ Min Approach: Use a second stack to track min, although the space complexity is the same as above
# (O(n)), there doesn't need to be two values stored at each level of the stack.  If the lowest value was the first item
# placed on the stack, and no duplicate values were added, then there would only be one item in that stack for any
# number of n items in the 'top' stack.
# Time Complexity: SEE Below.
# Space Complexity: O(n), where n is the number of elements in the stack.
class TwoStackMin:
    # Time Complexity: O(n), where n is the number of arguments.
    def __init__(self, *args):
        self._top = []   # End of list is the top of the stack.
        self._min = []  # End of list is the top of the stack.
        for i in args:
            self.push(i)

    # Time Complexity: O(1).
    def push(self, value):
        if not self._min or value <= self._min[-1]:
            self._min.append(value)
        self._top.append(value)

    # Time Complexity: O(1).
    def pop(self):
        if self._top:
            if self._min[-1] == self._top[-1]:
                self._min.pop()
            return self._top.pop()
        raise IndexError("pop from empty stack")

    # Time Complexity: O(1).
    def min(self):
        if self._min:
            return self._min[-1]
        raise IndexError("min from empty stack")

    def __repr__(self):
        return f"\n\ttop:{self._top}\n\tmin:{self._min}"

    def __len__(self):
        return len(self._top)


# Linked List W/  Approach: Use a second stack to track min, although the space complexity is the same as above
# (O(n)), there doesn't need to be two values stored at each level of the stack.  If the lowest value was the first item
# placed on the stack, and no duplicate values were added, then there would only be one item in that stack for any
# number of n items in the 'top' stack.
# Time Complexity: SEE Below.
# Space Complexity: O(n), where n is the number of elements in the stack.
class Node:
    def __init__(self, value, next=None, my_min=None):
        self.value = value
        self.next = next
        self.my_min = my_min

    def __iter__(self):
        yield self.value
        if self.next:
            yield from self.next

    def __repr__(self):
        return " ⟵ ".join(map(repr, self))


class MinLinkedListStack:
    def __init__(self, *args):
        self.top = None
        for e in args:
            self.push(e)

    def push(self, value):
        node = Node(value, self.top)
        node.my_min = node if self.top is None or value < self.top.my_min.value else self.top.my_min.my_min
        self.top = node

    def pop(self):
        if self.top:
            result = self.top.value
            self.top = self.top.next
            return result
        raise IndexError

    def min(self):
        if self.top:
            return self.top.my_min.value
        raise IndexError

    def __len__(self):
        node = self.top
        counter = 0
        while node:
            node = node.next
            counter += 1
        return counter

    def __repr__(self):
        return repr(self.top)


classes = [OneStackMin,
           TwoStackMin,
           MinLinkedListStack]

for cls in classes:
    print(f"\n{cls.__name__}\n")
    c_name = str.lower(cls.__name__)
    print(f"{c_name} = {cls.__name__}(0, 2, 5)"); c = cls(0, 2, 5)
    print(f"repr({c_name}): {repr(c)}")
    for value in [-1, 5, -42, 42]:
        print(f"{c_name}.min(): {c.min()}")
        print(f"{c_name}.push({value})"); c.push(value)
    print(f"repr({c_name}): {repr(c)}")
    for _ in range(len(c) // 2):
        print(f"{c_name}.pop(): {c.pop()}")
    print(f"len({c_name}): {len(c)}")
    print(f"repr({c_name}): {repr(c)}")
    print(f"{c_name}.min(): {c.min()}")


